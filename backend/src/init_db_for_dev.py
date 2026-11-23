import time
from db_client import DBClient
from steam_client import SteamClient

game_id_list: list[int] = [
    730,  # Counter-Strike 2
    1172470,  # Apex Legends
    3419430,  # Bongo Cat
    1808500,  # ARC Raiders
    526870,  # Satisfactory
    2300320,  # Farming Simulator 25
    227300,  # Euro Truck Simulator 2
    2060160,  # The Farmer Was Replaced
    960090,  # Bloons TD 6
    1325200,  # Nioh 2
    1222670,  # The Sims 4
    5160800,  # Find The Needle
    570,  # Dota 2
    2357570,  # Overwatch
    105600,  # Terraria
    2483190,  # Forza Horizon 6
    5266240,  # Potato Please
]


if __name__ == "__main__":
    db_client = DBClient()
    for game_id in game_id_list:
        game_name: str = SteamClient.get_game_name(game_id)
        db_client.add_game(game_id, game_name)
        print(f"add {game_id}\t{game_name}")
        time.sleep(2)
