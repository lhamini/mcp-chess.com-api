from mcp.server.fastmcp import FastMCP #type: ignore

mcp = FastMCP("chess.com")

from .chess_api import get_player_profile, get_player_stats

@mcp.tool()
def get_chess_player_profile(username: str):
    """Fetches and returns chess player profile and stats from Chess.com."""
    return get_player_profile(username)


@mcp.tool()
def get_chess_player_stats(username: str):
    """Fetches and returns chess player statistics from Chess.com."""
    return get_player_stats(username)   

def main():
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
