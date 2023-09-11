from pytube import Playlist
import os
from tqdm import tqdm

# Prompt the user to enter the playlist URL
playlist_url = input("Enter Playlist URL: ")

# Create a Playlist object
playlist = Playlist(playlist_url)

# Set the download folder path to "Downloaded/PlaylistAudio"
download_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Downloaded/PlaylistAudio")

# Create the download folder if it doesn't exist
os.makedirs(download_folder, exist_ok=True)

# Iterate over each video in the playlist
for video in tqdm(playlist.videos, desc="Downloading"):
    # Get the audio stream
    audio_stream = video.streams.filter(only_audio=True).first()

    # Download the audio
    print(f"Downloading audio: {video.title}")
    audio_file = audio_stream.download(output_path=download_folder, filename_prefix='temp_')

    # Rename the downloaded file to have the .mp3 extension
    new_file_name = os.path.splitext(audio_file)[0] + '.mp3'
    os.rename(audio_file, new_file_name)

print("Download completed!")
