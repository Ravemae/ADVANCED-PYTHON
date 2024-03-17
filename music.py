import requests
from bs4 import BeautifulSoup

def scrape_apple_music_dance_playlist():
    # Example URL for the dance and entertainment playlist
    playlist_url = "https://music.apple.com/us/playlist/dance-pop-hits/pl.02b98f9d97e54709be8272fc297636a4"

    try:
        response = requests.get(playlist_url)
        response.raise_for_status()  # Check for successful response

        soup = BeautifulSoup(response.content, "html.parser")

        # Find all song titles (adjust the CSS selector based on the actual page structure)
        song_titles = soup.find_all("meta", attrs={"property": "music:song"})
        for title in song_titles:
            print(title.get("content"))

    except requests.RequestException as e:
        print(f"Error fetching playlist: {e}")

if __name__ == "__main__":
    scrape_apple_music_dance_playlist()
