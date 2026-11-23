import unittest
from unittest.mock import MagicMock, patch

from src.api import APIApp


class TestAPIApp(unittest.TestCase):
    def setUp(self) -> None:
        self.db_adapter = MagicMock()
        self.client = APIApp(self.db_adapter).app.test_client()

    def test_get_game_returns_tracked_game(self) -> None:
        self.db_adapter.get_game.return_value = {
            "game_id": 730,
            "game_name": "Counter-Strike 2",
        }

        response = self.client.get("/api/get_game/730")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json()["data"]["game_name"],
            "Counter-Strike 2",
        )

    @patch("src.api.SteamClient.get_game_name", return_value="Counter-Strike 2")
    def test_add_game_stores_valid_game(self, _get_game_name: MagicMock) -> None:
        self.db_adapter.add_game.return_value = True

        response = self.client.post("/api/add_game", json={"game_id": 730})

        self.assertEqual(response.status_code, 201)
        self.db_adapter.add_game.assert_called_once_with(730, "Counter-Strike 2")

    @patch("src.api.SteamClient.get_game_name", return_value="Counter-Strike 2")
    def test_add_game_rejects_duplicate(self, _get_game_name: MagicMock) -> None:
        self.db_adapter.add_game.return_value = False

        response = self.client.post("/api/add_game", json={"game_id": 730})

        self.assertEqual(response.status_code, 409)

    def test_add_game_requires_positive_integer_id(self) -> None:
        response = self.client.post("/api/add_game", json={"game_id": True})

        self.assertEqual(response.status_code, 400)
        self.db_adapter.add_game.assert_not_called()

    def test_remove_game_reports_missing_game(self) -> None:
        self.db_adapter.remove_game.return_value = False

        response = self.client.delete("/api/remove_game/730")

        self.assertEqual(response.status_code, 404)

    @patch("src.api.SteamClient.get_current_player", return_value=5000)
    def test_get_count_returns_live_player_count(self, _get_current_player: MagicMock):
        self.db_adapter.get_game.return_value = {
            "game_id": 730,
            "game_name": "Counter-Strike 2",
        }

        response = self.client.get("/api/get_count/730")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["data"]["player_count"], 5000)


if __name__ == "__main__":
    unittest.main()
