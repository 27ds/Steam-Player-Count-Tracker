from flask import Flask, jsonify
from steam_client import SteamClient


class APIApp:
    """Flask API application."""

    def __init__(self) -> None:
        self.app = Flask(__name__)

        self.app.add_url_rule(
            "/game/<int:game_id>",
            "get_game",
            self.get_game,
            methods=["GET"],
        )

    def get_game(self, game_id: int):
        """Return game information as JSON."""

        game_name = SteamClient.get_game_name(game_id)
        player_count = SteamClient.get_current_player(game_id)

        if game_name == "" or player_count == -1:
            return jsonify(
                {
                    "status": "error",
                    "message": "Game not found",
                    "game_id": game_id
                }
            ), 404

        return jsonify(
            {
                "status": "success",
                 "data": {
                    "game_id": game_id,
                    "game_name": game_name,
                    "player_count": player_count
                }
            }
        )


if __name__ == "__main__":
    api = APIApp()
    api.app.run(host="0.0.0.0", port=5000, debug=True)
