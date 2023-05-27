from pydub import AudioSegment
import os

def convert_to_mp3(file):
    # Load the MP4 file
    audio = AudioSegment.from_file(file, format="mp4")
    
    # Get the file name without the extension
    file_name = os.path.splitext(os.path.basename(file))[0]
    
    # Specify the directory where the MP3 files will be saved
    export_dir = "mp3_files"
    
    # Create the directory if it doesn't exist
    if not os.path.exists(export_dir):
        os.makedirs(export_dir)
    
    # Save the MP3 file
    audio.export(f"{export_dir}/{file_name}.mp3", format="mp3")

# Specify the subdirectory where MP4 files are located
subdir = "mp4_files"

# Get all MP4 files in the specified subdirectory
mp4_files = [f"{subdir}/{file}" for file in os.listdir(subdir) if file.endswith(".mp4")]

# Convert all MP4 files to MP3
for file in mp4_files:
    convert_to_mp3(file)

print("All MP4 files in the subdirectory have been converted to MP3 and saved in the mp3_files folder.")
