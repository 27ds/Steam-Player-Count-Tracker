import os
from contextlib import contextmanager
from typing import Iterator

from mysql.connector import MySQLConnection, connect
from mysql.connector.cursor import MySQLCursorDict


class DBAdapter:
    """Access the externally hosted MySQL database."""

    def __init__(self) -> None:
        required_variables = ("MYSQL_HOST", "MYSQL_USER", "MYSQL_PASSWORD", "MYSQL_DATABASE")
        missing_variables = [
            variable for variable in required_variables if variable not in os.environ
        ]
        if missing_variables:
            raise ValueError(
                "Missing required database environment variables: "
                + ", ".join(missing_variables)
            )

        self._config = {
            "host": os.environ["MYSQL_HOST"],
            "port": int(os.getenv("MYSQL_PORT", "3306")),
            "user": os.environ["MYSQL_USER"],
            "password": os.environ["MYSQL_PASSWORD"],
            "database": os.environ["MYSQL_DATABASE"],
        }

    @contextmanager
    def _cursor(self) -> Iterator[tuple[MySQLConnection, MySQLCursorDict]]:
        connection = connect(**self._config)
        try:
            cursor = connection.cursor(dictionary=True)
            try:
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS tracked_games (
                        game_id BIGINT UNSIGNED PRIMARY KEY,
                        game_name VARCHAR(255) NOT NULL
                    )
                    """
                )
                yield connection, cursor
            finally:
                cursor.close()
        finally:
            connection.close()

    def get_game(self, game_id: int) -> dict[str, int | str] | None:
        with self._cursor() as (_, cursor):
            cursor.execute(
                "SELECT game_id, game_name FROM tracked_games WHERE game_id = %s",
                (game_id,),
            )
            game = cursor.fetchone()
            return game

    def add_game(self, game_id: int, game_name: str) -> bool:
        with self._cursor() as (connection, cursor):
            cursor.execute(
                "SELECT game_id FROM tracked_games WHERE game_id = %s",
                (game_id,),
            )
            if cursor.fetchone() is not None:
                return False

            cursor.execute(
                "INSERT INTO tracked_games (game_id, game_name) VALUES (%s, %s)",
                (game_id, game_name),
            )
            connection.commit()
            return True

    def remove_game(self, game_id: int) -> bool:
        with self._cursor() as (connection, cursor):
            cursor.execute(
                "DELETE FROM tracked_games WHERE game_id = %s",
                (game_id,),
            )
            removed = cursor.rowcount > 0
            if removed:
                connection.commit()
            return removed
