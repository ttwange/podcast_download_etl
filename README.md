# Podcast Episode Downloader

This Python script is designed to fetch and download podcast episodes from a given RSS feed URL. It uses the [Prefect](https://www.prefect.io/) library for creating data pipelines, making it easy to automate the process of downloading podcast episodes.

## Prerequisites

Before running the script, make sure you have the following prerequisites installed:

- Python 3.x
- `prefect` library (you can install it using `pip install prefect`)
- Other dependencies (`requests`, `xmltodict`) will be installed automatically when you run the script if not already installed.

## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal and navigate to the directory where the script is located.

3. Run the script using the following command:

   ```
   python script_name.py
   ```

   Replace `script_name.py` with the actual name of the script.

4. The script will fetch podcast episodes from the specified RSS feed URL and download them to the `./episodes` directory.

## Configuration

You can customize the script by modifying the following variables in the code:

- `RSS_FEED_URL`: The URL of the RSS feed for the podcast you want to download episodes from. You can replace it with the RSS feed URL of your preferred podcast.

- `DOWNLOAD_DIR`: The directory where downloaded episodes will be saved. By default, it is set to `./episodes`. You can change it to a different directory if desired.

## How It Works

1. The script fetches the podcast episodes from the specified RSS feed URL using the `fetch_podcast_episodes` task. It then parses the XML response to extract episode information.

2. The `download_episode` task is responsible for downloading each episode. It checks if the episode has already been downloaded to avoid duplicates.

3. The `get_episodes` flow orchestrates the entire process. It fetches the episodes and uses the `download_episode.map` method to apply the `download_episode` task to each episode in parallel, improving download efficiency.

## License

This code is provided under the [MIT License](LICENSE). You are free to use, modify, and distribute it as needed.

## Acknowledgments

This script was created for educational purposes and demonstrates how to automate the process of fetching and downloading podcast episodes using Python and Prefect.

If you have any questions or encounter issues, feel free to open an [issue](https://github.com/your-repository-url/issues) in the repository or contact the author.