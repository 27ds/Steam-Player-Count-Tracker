#!/usr/bin/env python3

# import threading - not used yet, but will be used in the future
import logging
import time
# from datetime import datetime

# import api - not used yet, but will be used in the future for the provider class
import db_client
import steam_client


logger = logging.getLogger(__name__)
INTERVAL_SECONDS: int = 300


class DataGetter:  # Thread 1 -> SteamClient -> DBClient (or PlayerCountCollector)
    # fetches player counts all 5 minutes

    def __init__(
        self,
        steam: steam_client.SteamClient,
        db: db_client.DBClient,
        interval_seconds: int,
    ) -> None:
        self.steam = steam  # info: passed in from main to be handed from both classes
        self.db = db
        self.interval_seconds = interval_seconds

    def fetch_count_and_time_once(self) -> None:  # Data all 5 minutes
        # timestamp = datetime.now() - missed in db
        for game in self.db.get_games():
            game_id = int(game["game_id"])
            player_count = self.steam.get_current_player(game_id)
            if player_count == -1:
                continue
            self.db.add_data(game_id, player_count)
            # self.db.timestamp = timestamp - missed in db

    def load_game_names(self) -> None:
        for game in self.db.get_games():
            game_id = int(game["game_id"])
            self.db.add_game(game_id, self.steam.get_game_name(game_id))

    def run(self) -> None:  # info: 5 min cycle
        while True:
            start = time.monotonic()
            try:
                self.fetch_count_and_time_once()
            except Exception:
                logger.exception("Error while fetching player counts")
            duration = time.monotonic() - start
            time.sleep(max(0, self.interval_seconds - duration))  # TODO write error


def main() -> None:
    logging.basicConfig(level=logging.INFO)

    steam = steam_client.SteamClient()
    db = db_client.DBClient()

    getter = DataGetter(steam, db, INTERVAL_SECONDS)
    # provider = ...#TODO - not implemented yet, but will be used in the future for the provider class

    getter.load_game_names()

    # threading


if __name__ == "__main__":
    main()
