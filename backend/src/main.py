# import threading - not used yet, but will be used in the future
import time
from datetime import datetime

# import api - not used yet, but will be used in the future for the provider class
import db_adapter
import steam_client


INTERVAL_SECONDS: int = 300


class DataGetter:  # Thread 1 -> SteamClient -> DBAdapter (or PlayerCountCollector)
    # fetches player counts all 5 minutes

    def __init__(
        self,
        steam: steam_client.SteamClient,
        db: db_adapter.DbAdapter,
        interval_seconds: int,
    ) -> None:
        self.steam = steam  # info: passed in from main to be handed from both classes
        self.db = db
        self.interval_seconds = interval_seconds

    def fetch_count_and_time_once(self) -> None:  # Data all 5 minutes
        timestamp = datetime.now()
        for game_id in self.db.get_game_ids():
            count = self.steam.get_current_player(game_id)
            if count == -1:
                continue
            timestamp = self.steam.timestamp
            self.db.save_player_count(game_id, timestamp, count)
            self.db.timestamp = timestamp

    def load_game_names(self) -> None:
        for game_id in self.db.get_game_ids():
            self.db.add_game(game_id, self.steam.get_game_name(game_id))

    def run(self) -> None:  # info: 5 min cycle
        while True:
            start = time.monotonic()
            try:
                self.fetch_count_and_time_once()
            except:
                print(f"Error while fetching player count: {e}")
            duration = time.monotonic() - start
            time.sleep(max(0, self.interval_seconds - duration))  # TODO write error


def main() -> None:
    steam = steam_client.SteamClient()
    db = db_adapter.DbAdapter()

    db.creat_tables()

    getter = DataGetter(steam, db, INTERVAL_SECONDS)
    #provider = ...#TODO - not implemented yet, but will be used in the future for the provider class

    getter.load_game_names()

    # threading


if __name__ == "__main__":
    main()
