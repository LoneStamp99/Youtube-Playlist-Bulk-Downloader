from pytube import Playlist
import os
from tqdm import tqdm
import math

# Prompt the user to enter the playlist URL
playlist_url = input("Enter Playlist URL: ")

# Create a Playlist object
playlist = Playlist(playlist_url)

# Prompt the user to select the video resolution
print("Select Resolution:")
print("(1) Default")
print("(2) 720p")
print("(3) 1080p")
resolution_choice = input("Enter your choice: ")

# Set the download folder path to "Downloaded/PlaylistVideo"
download_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Downloaded/PlaylistVideo")

# Create the download folder if it doesn't exist
os.makedirs(download_folder, exist_ok=True)

# Iterate over each video in the playlist
for video in tqdm(playlist.videos, desc="Downloading"):
    # Download the video based on the user's resolution choice
    if resolution_choice == "1":
        stream = video.streams.first()
    elif resolution_choice == "2":
        stream = video.streams.filter(res="720p").first()
    elif resolution_choice == "3":
        stream = video.streams.filter(res="1080p").first()
    else:
        print("Invalid choice. Skipping video.")
        continue

    # Download the video
    print(f"Downloading: {video.title}")
    video_file = stream.download(output_path=download_folder)

print("Download completed!")
