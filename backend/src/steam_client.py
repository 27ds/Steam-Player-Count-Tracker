import requests


class SteamClient:
    """Steam client witch interacts with the Steam API."""

    @staticmethod
    def _request_data(url: str) -> dict:
        try:
            response: requests.models.Response = requests.get(url)
            if response.status_code == 200:
                data: dict = response.json()
                return data

            return {}
        except requests.exceptions.Timeout:
            print("Error: The request took too long (timeout).")
        except requests.exceptions.ConnectionError:
            print("Error: Unable to connect to the server (network error/DNS).")
        except requests.exceptions.HTTPError as e:
            print(f"An HTTP error occurred: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Another unexpected request error has occurred: {e}")
        return {}

    @staticmethod
    def get_current_player(game_id: int) -> int:
        """Get the current player count from the Steam API.

        Args:
            game_id: The ID of the Steam game.

        Returns:
            int: The player count if the request is valid, otherwise -1.
        """
        url: str = f"https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid={game_id}"
        requests: dict = SteamClient._request_data(url)
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
        url: str = f"https://store.steampowered.com/api/appdetails?appids={game_id}"
        requests: dict = SteamClient._request_data(url)
        if requests == {}:
            return ""
        game_name: str = requests[str(game_id)]["data"]["name"]
        return game_name


if __name__ == "__main__":
    # local test
    app_id = 526870  # Satisfactory
    current_player: int = SteamClient.get_current_player(app_id)
    game_name: str = SteamClient.get_game_name(app_id)
    print(f"Game: {game_name}, current player: {current_player}")
