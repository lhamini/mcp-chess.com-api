import requests  #type: ignore

CHESS_API_URL = "https://api.chess.com/pub"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

def get_player_profile(username):
    """Fetches the profile of a chess player from the Chess.com API."""
    response = requests.get(f"{CHESS_API_URL}/player/{username}", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    

def get_player_stats(username):
    """Fetches the statistics of a chess player from the Chess.com API."""
    response = requests.get(f"{CHESS_API_URL}/player/{username}/stats", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
