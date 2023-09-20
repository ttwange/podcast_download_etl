import os
import requests
import xmltodict
from prefect import flow, task

@task
def fetch_podcast_episodes(feed_url):
    feed = requests.get(feed_url)
    data = xmltodict.parse(feed.text)
    episodes = data["rss"]["channel"]["item"]
    print(f"Found {len(episodes)} episodes.")
    print(episodes)
    return episodes

@task()
def download_episodes(episodes):
    for episode in episodes:
        filename = f"{episode['link'].split('/')[-1]}.mp3"
        audio_path = os.path.join("episodes",filename)
        if not os.path.exists(audio_path):
            print(f"Downloading {filename}")
            audio = requests.get(episodes["enclosure"]["@url"])
            with open(audio_path, "wb+") as f:
                f.write(audio.content)
                
@flow()
def get_episodes() -> None:
    RSS_FEED_URL = "https://www.marketplace.org/feed/podcast/marketplace/"
    DOWNLOAD_DIR = "./episodes"
    episodes = fetch_podcast_episodes(RSS_FEED_URL)
    download_episodes(episodes)

if __name__ == "__main__":
    get_episodes()