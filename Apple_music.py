import requests
from bs4 import BeautifulSoup

def scrape_apple_music_trending_songs():
    # Example URL for a trending songs playlist (you can replace this with an actual playlist URL)
    playlist_url = "https://music.apple.com/ua/playlist/techno-essentials/pl.de1ac365ed3549698bcd6e099db5171d"

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
    scrape_apple_music_trending_songs()
