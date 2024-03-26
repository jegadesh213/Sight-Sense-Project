import requests
from bs4 import BeautifulSoup
import webbrowser

def play_first_trending_tamil_song():
    # Fetch the YouTube page containing trending Tamil songs
    url = "https://www.youtube.com/results?search_query=trending+tamil+songs"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all video elements on the page
    video_elements = soup.find_all("a", class_="yt-simple-endpoint style-scope ytd-video-renderer")

    # Check if there are any video elements found
    if video_elements:
        # Extract the URL of the first video
        first_video_url = "https://www.youtube.com" + video_elements[0]["href"]
        
        # Open the first video in a web browser
        webbrowser.open(first_video_url)
    else:
        print("No trending Tamil songs found.")

if __name__ == "__main__":
    play_first_trending_tamil_song()
