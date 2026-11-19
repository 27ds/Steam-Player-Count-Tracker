import os
from datetime import datetime

import psycopg
from psycopg.rows import dict_row


class DBClient:
    """Database client which interacts with the PostgreSQL Database."""

    def __init__(self) -> None:
        dsn = os.environ.get("DATABASE_URL")
        if not dsn:
            raise RuntimeError("Environment variable DATABASE_URL is not set.")
        self._dsn: str = dsn
        self._create_tables()

    def _db_connect(self) -> psycopg.Connection:
        return psycopg.connect(self._dsn)

    def _create_tables(self) -> None:
        """
        create the two tables

        games table: game_id and game_name

        game_infos table: game_id, time and player_count

        """

        with self._db_connect() as conn, conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS games (
                    game_id   INTEGER PRIMARY KEY,
                    game_name TEXT    NOT NULL
                )
                """
            )

            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS game_infos (
                    game_id      INTEGER     NOT NULL
                                REFERENCES games (game_id) ON DELETE CASCADE,
                    time        TIMESTAMPTZ NOT NULL DEFAULT now(),
                    player_count INTEGER     NOT NULL,
                    PRIMARY KEY (game_id, time)
                )
                """
            )

    def add_game(self, game_id: int, game_name: str) -> None:
        """
        add game to game table

        Args:
            game_id: The ID of the Steam game.
            game_name: The name of the Steam game.

        """
        with self._db_connect() as conn, conn.cursor() as cur:
            cur.execute(
                t"INSERT INTO games (game_id, game_name) VALUES ({game_id}, {game_name})"
            )

    def get_games(self) -> list[dict[str, int | str]]:
        """
        Get all games from the games table.

        Returns:
        A list of games, e.g. [{"game_id": 526870, "game_name": "Satisfactory"}].
        """
        with self._db_connect() as conn, conn.cursor(row_factory=dict_row) as cur:
            cur.execute(t"SELECT game_id, game_name FROM games ORDER BY game_name")
            return cur.fetchall()

    def add_data(self, game_id: int, player_count: int) -> None:
        """
        Add game data ex. a player count for a game, to the game_infos table.

        Args:
            game_id: The ID of the Steam game.
            player_count: The current player count. Negative values
                (failed Steam requests) are ignored.
        """

        if player_count < 0:
            return

        with self._db_connect() as conn, conn.cursor() as cur:
            cur.execute(
                t"INSERT INTO game_infos (game_id, player_count) "
                t"VALUES ({game_id}, {player_count})"
            )

    def get_data(self, game_id: int) -> list[dict[str, datetime | int]]:
        """
        Get game data ex. a player count for a game, from the game_infos table.

        Args:
            game_id: The ID of the Steam game.
            player_count: The current player count. Negative values
                (failed Steam requests) are ignored.
        """
        with self._db_connect() as conn, conn.cursor(row_factory=dict_row) as cur:
            cur.execute(
                t"SELECT time, player_count FROM game_infos "
                t"WHERE game_id = {game_id} ORDER BY time"
            )
            return cur.fetchall()

    def remove_game(self, game_id: int) -> None:
        """
        Remove a game and all its game infos ex. player count.

        Args:
            game_id: The ID of the Steam game.

        It is enough to just delete it from the games table because it
        was created with ON DELETE CASCADE so it deletes the game infos ex. player count
        automatically
        """
        with self._db_connect() as conn, conn.cursor() as cur:
            cur.execute(t"DELETE FROM games WHERE game_id = {game_id}")
