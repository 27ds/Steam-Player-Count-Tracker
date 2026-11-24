"""Client for fetching game name and player counts from Steam APIs."""

import logging

import requests

logger = logging.getLogger(__name__)


class SteamClient:
    """Steam client witch interacts with the Steam API."""

    @staticmethod
    def _request_data(base_url: str, params: dict[str, int]) -> dict:
        try:
            response: requests.models.Response = requests.get(
                base_url, params=params, timeout=10
            )
            if response.status_code == 200:
                data: dict = response.json()
                return data

            return {}
        except requests.exceptions.Timeout:
            logger.error("Error: The request took too long (timeout).")
        except requests.exceptions.ConnectionError:
            logger.error("Error: Unable to connect to the server (network error/DNS).")
        except requests.exceptions.HTTPError as e:
            logger.error("An HTTP error occurred: %s", e)
        except requests.exceptions.RequestException as e:
            logger.error("Another unexpected request error has occurred: %s", e)
        return {}

    @staticmethod
    def get_current_player_count(game_id: int) -> int:
        """Get the current player count from the Steam API.

        Args:
            game_id: The ID of the Steam game.

        Returns:
            int: The player count if the request is valid, otherwise -1.
        """
        base_url: str = (
            "https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/"
        )
        params = {"appid": game_id}
        requests: dict = SteamClient._request_data(base_url, params)
        # feedback: {'response': {'player_count': 9396, 'result': 1}}
        if requests == {}:
            return -1
        if requests["response"]["result"] != 1:
            return -1

        return requests["response"]["player_count"]

    @staticmethod
    def get_game_name(game_id: int) -> str:
        """Get the game name from the Steam API.

        Args:
            game_id: The ID of the Steam game.

        Returns:
            str: The game name if the request is valid, otherwise "".
        """
        base_url: str = "https://store.steampowered.com/api/appdetails"
        params = {"appids": game_id}
        requests: dict = SteamClient._request_data(base_url, params)
        if requests == {}:
            return ""
        game_name: str = requests[str(game_id)]["data"]["name"]
        return game_name


if __name__ == "__main__":
    # local test
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
    game_id = 526870  # Satisfactory
    current_player_count: int = SteamClient.get_current_player_count(game_id)
    game_name: str = SteamClient.get_game_name(game_id)
    logger.info("Game: %s, current player: %s", game_name, current_player_count)
