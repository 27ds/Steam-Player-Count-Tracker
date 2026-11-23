from flask import Flask, jsonify, request

from db_client import DBClient
from steam_client import SteamClient


class APIApp:
    """Flask API application."""

    def __init__(self, db_client=None) -> None:
        self.app = Flask(__name__)

        self.db_client = db_client if db_client is not None else DBClient()
        self.steam_client = SteamClient()

        self.app.add_url_rule(
            "/api/games/<int:game_id>",
            "get_game",
            self.get_game,
            methods=["GET"],
        )

        self.app.add_url_rule(
            "/api/games",
            "add_game",
            self.add_game,
            methods=["POST"],
        )

        self.app.add_url_rule(
            "/api/games/<int:game_id>",
            "remove_game",
            self.remove_game,
            methods=["DELETE"],
        )

        self.app.add_url_rule(
            "/api/games/<int:game_id>/count",
            "get_count",
            self.get_count,
            methods=["GET"],
        )

        self.app.add_url_rule(
            "/api/health",
            "health",
            self.health,
            methods=["GET"],
        )

    def health(self):
        """Health check endpoint."""
        return jsonify(
            {
                "status": "success",
                "message": "API is healthy",
            }
        )

    def get_game(self, game_id: int):
        """Return game information."""
        game_name = SteamClient.get_game_name(game_id)

        if game_name == "":
            return jsonify(
                {
                    "status": "error",
                    "message": "Game not found",
                    "game_id": game_id,
                }
            ), 404

        return jsonify(
            {
                "status": "success",
                "data": {
                    "game_id": game_id,
                    "game_name": game_name,
                },
            }
        )

    def get_count(self, game_id: int):
        """Return player count."""
        player_count = SteamClient.get_current_player(game_id)

        if player_count == -1:
            return jsonify(
                {
                    "status": "error",
                    "message": "Game not found",
                    "game_id": game_id,
                }
            ), 404

        return jsonify(
            {
                "status": "success",
                "data": {
                    "game_id": game_id,
                    "player_count": player_count,
                },
            }
        )

    def add_game(self):
        """Placeholder for adding a game."""
        return jsonify(
            {
                "status": "success",
                "message": "add_game endpoint",
            }
        )

    def remove_game(self, game_id: int):
        """Placeholder for removing a game."""
        return jsonify(
            {
                "status": "success",
                "message": f"remove_game endpoint for {game_id}",
            }
        )


if __name__ == "__main__":
    api = APIApp()
    api.app.run(host="0.0.0.0", port=5000, debug=True)