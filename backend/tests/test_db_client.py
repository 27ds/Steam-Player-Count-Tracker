import unittest
from datetime import UTC, datetime
from unittest.mock import MagicMock, patch

from psycopg.rows import dict_row

from src.db_client import DBClient


@patch.dict("os.environ", {"DATABASE_URL": "postgresql://test"})
class TestDBClient(unittest.TestCase):
    def _create_client(self, mock_connect: MagicMock) -> tuple[DBClient, MagicMock]:
        """create a DBClient with a mocked connection and cursor"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor

        db = DBClient()
        mock_cursor.execute.reset_mock()  # ignore CREATE TABLE calls from __init__
        return db, mock_cursor

    @patch("src.db_client.psycopg.connect")
    def test_init_creates_tables(self, mock_connect):
        """both tables are created on init"""
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value.cursor.return_value.__enter__.return_value = mock_cursor

        DBClient()

        sql_calls = [call.args[0] for call in mock_cursor.execute.call_args_list]
        self.assertEqual(len(sql_calls), 2)
        self.assertIn("CREATE TABLE IF NOT EXISTS games", sql_calls[0])
        self.assertIn("CREATE TABLE IF NOT EXISTS game_infos", sql_calls[1])

    @patch("src.db_client.psycopg.connect")
    def test_add_game_success(self, mock_connect):
        """game is inserted into the games table"""
        db, mock_cursor = self._create_client(mock_connect)

        db.add_game(730, "Counter-Strike 2")

        template = mock_cursor.execute.call_args.args[0]
        self.assertIn("INSERT INTO games", "".join(template.strings))
        self.assertEqual(template.values, (730, "Counter-Strike 2"))

    @patch("src.db_client.psycopg.connect")
    def test_get_games_success(self, mock_connect):
        """normal request"""
        db, mock_cursor = self._create_client(mock_connect)
        mock_cursor.fetchall.return_value = [
            {"game_id": 730, "game_name": "Counter-Strike 2"},
            {"game_id": 526870, "game_name": "Satisfactory"},
        ]

        games = db.get_games()

        self.assertEqual(
            games,
            [
                {"game_id": 730, "game_name": "Counter-Strike 2"},
                {"game_id": 526870, "game_name": "Satisfactory"},
            ],
        )

    @patch("src.db_client.psycopg.connect")
    def test_get_games_uses_dict_row(self, mock_connect):
        """rows are returned as dicts"""
        db, _ = self._create_client(mock_connect)
        mock_conn = mock_connect.return_value.__enter__.return_value

        db.get_games()

        mock_conn.cursor.assert_called_with(row_factory=dict_row)

    @patch("src.db_client.psycopg.connect")
    def test_get_games_empty(self, mock_connect):
        """no games in the database"""
        db, mock_cursor = self._create_client(mock_connect)
        mock_cursor.fetchall.return_value = []

        self.assertEqual(db.get_games(), [])

    @patch("src.db_client.psycopg.connect")
    def test_add_data_success(self, mock_connect):
        """player count is inserted into the game_infos table"""
        db, mock_cursor = self._create_client(mock_connect)

        db.add_data(730, 5000)

        sql, params = mock_cursor.execute.call_args.args
        self.assertIn("INSERT INTO game_infos", sql)
        self.assertEqual(params, (730, 5000))

    @patch("src.db_client.psycopg.connect")
    def test_add_data_negative_player_count(self, mock_connect):
        """-1 from a failed steam request is not stored"""
        db, mock_cursor = self._create_client(mock_connect)

        db.add_data(730, -1)

        mock_cursor.execute.assert_not_called()

    @patch("src.db_client.psycopg.connect")
    def test_get_data_success(self, mock_connect):
        """normal request"""
        db, mock_cursor = self._create_client(mock_connect)
        rows = [
            {"time": datetime(2026, 11, 17, 12, 0, tzinfo=UTC), "player_count": 5000},
            {"time": datetime(2026, 11, 17, 12, 5, tzinfo=UTC), "player_count": 5100},
        ]
        mock_cursor.fetchall.return_value = rows

        data = db.get_data(730)

        self.assertEqual(data, rows)
        sql, params = mock_cursor.execute.call_args.args
        self.assertIn("FROM game_infos", sql)
        self.assertIn("ORDER BY time", sql)
        self.assertEqual(params, (730,))

    @patch("src.db_client.psycopg.connect")
    def test_get_data_empty(self, mock_connect):
        """no data for this game"""
        db, mock_cursor = self._create_client(mock_connect)
        mock_cursor.fetchall.return_value = []

        self.assertEqual(db.get_data(730), [])

    @patch("src.db_client.psycopg.connect")
    def test_remove_game_success(self, mock_connect):
        """game is deleted from the games table"""
        db, mock_cursor = self._create_client(mock_connect)

        db.remove_game(730)

        sql, params = mock_cursor.execute.call_args.args
        self.assertIn("DELETE FROM games", sql)
        self.assertEqual(params, (730,))


if __name__ == "__main__":
    unittest.main()