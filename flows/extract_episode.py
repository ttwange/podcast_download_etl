import feedparser
import requests
from prefect import Flow, task

# Define the RSS feed URL
RSS_FEED_URL = "https://www.marketplace.org/feed/podcast/marketplace/"

# Define the directory where you want to save the podcast episodes
DOWNLOAD_DIR = "./episodes"

@task
def fetch_podcast_episodes(feed_url):
    # Parse the RSS feed
    feed = feedparser.parse(feed_url)

    # Extract episode information
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

# Create a Prefect flow
with Flow("DownloadMarketplacePodcastEpisodes") as flow:
    episodes = fetch_podcast_episodes(RSS_FEED_URL)
    download_episode.map(episodes, DOWNLOAD_DIR)

# Run the Prefect flow
if __name__ == "__main__":
    flow.run()
