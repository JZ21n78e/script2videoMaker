import os
from pathlib import Path
from moviepy.editor import VideoFileClip, concatenate_videoclips

# directory to scan for MP4 files
directory = Path.cwd()/f"vid_ai/video_asset"

# create a list of all MP4 file paths in the directory
videos = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.mp4')]
print(videos)

# create a list of VideoFileClip objects
clips = [VideoFileClip(video) for video in videos]

# concatenate the clips
final_clip = concatenate_videoclips(clips, method='compose')

filename = str(directory)+"/output.mp4"
# save the output to a file
# final_clip.write_videofile()

final_clip.write_videofile(
        filename,
        threads=5,
        bitrate="2000k",
        audio_codec="aac",
        codec="h264_nvenc",
    )