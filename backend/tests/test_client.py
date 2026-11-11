import unittest
from unittest.mock import MagicMock, patch

from src.client import SteamClient


class TestSteamClient(unittest.TestCase):
    @patch("src.client.requests.get")
    def test_get_current_player_success(self, mock_get):
        """normal request"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "response": {"player_count": 5000, "result": 1}
        }
        mock_get.return_value = mock_response

        player_count = SteamClient.get_current_player(730)
        self.assertEqual(player_count, 5000)

    @patch("src.client.requests.get")
    def test_get_current_player_api_error_404(self, mock_get):
        """error 404 server not reachable"""
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        player_count = SteamClient.get_current_player(999999)
        self.assertEqual(player_count, -1)

    @patch("src.client.requests.get")
    def test_get_current_player_api_error_respons(self, mock_get):
        """invalid response"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "response": {"player_count": 5000, "result": 0}
        }
        mock_get.return_value = mock_response

        player_count = SteamClient.get_current_player(730)
        self.assertEqual(player_count, -1)

    @patch("src.client.requests.get")
    def test_get_game_name_success(self, mock_get):
        """get name from game ID"""
        game_id = 730
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            str(game_id): {"success": True, "data": {"name": "Counter-Strike 2"}}
        }
        mock_get.return_value = mock_response

        game_name = SteamClient.get_game_name(game_id)
        self.assertEqual(game_name, "Counter-Strike 2")


if __name__ == "__main__":
    unittest.main()
