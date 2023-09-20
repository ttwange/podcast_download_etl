import requests
import xmltodict
from prefect import flow, task

@task
def fetch_podcast_episodes(feed_url):
    feed = requests.get(feed_url)
    data = xmltodict.parse(feed.text)
    episodes = data["rss"]["channel"]["item"]
    print(f"Found {len(episodes)} episodes.")
    return episodes

@flow()
def get_episodes() -> None:
    RSS_FEED_URL = "https://www.marketplace.org/feed/podcast/marketplace/"
    DOWNLOAD_DIR = "./episodes"
    episodes = fetch_podcast_episodes(RSS_FEED_URL)

if __name__ == "__main__":
    get_episodes()