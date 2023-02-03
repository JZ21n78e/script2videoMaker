import urllib.request

from pathlib import Path
import uuid

# URL of the MP4 file to download
url = r"https://vod-progressive.akamaized.net/exp=1674076899~acl=%2Fvimeo-prod-skyfire-std-us%2F01%2F2836%2F12%2F314181352%2F1212112675.mp4~hmac=465c0afe070822e79868f785fef152308b9c6f473806d41d0826ad7563a8a215/vimeo-prod-skyfire-std-us/01/2836/12/314181352/1212112675.mp4"

# download the fileF:\21NProjects\vid_ai-flask-demo-python\api\vid_ai\video_asset
urllib.request.urlretrieve(url, Path.cwd()/f"vid_ai/video_asset/video_{uuid.uuid1()}.mp4")
