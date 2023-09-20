import feedparser
import requests
from prefect import flow, task

@task
def fetch_podcast_episodes(feed_url):
    feed = feedparser.parse(feed_url)

    episodes = []
    for entry in feed.entries:
        episode_title = entry.title
        episode_url = entry.enclosures[0].href  # Assuming the podcast link is in the enclosures
        episodes.append((episode_title, episode_url))

    return episodes

@task
def download_episode(episode_info, download_dir):
    episode_title, episode_url = episode_info
    response = requests.get(episode_url)
    if response.status_code == 200:
        with open(f"{download_dir}/{episode_title}.mp3", "wb") as file:
            file.write(response.content)

@flow()
def get_episodes() -> None:
    RSS_FEED_URL = "https://www.marketplace.org/feed/podcast/marketplace/"

    DOWNLOAD_DIR = "./episodes"
    episodes = fetch_podcast_episodes(RSS_FEED_URL)
    download_episode.map(episodes, DOWNLOAD_DIR)
    
if __name__ == "__main__":
    get_episodes()
