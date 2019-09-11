import sys
import os
import urllib.request
from urllib.error import HTTPError
import shutil

BASE = "https://tower-streaming.la.utexas.edu/vod/_definst_/gov312lusfp/2019/Fall/2019-09-09_gov312l.mp4/media_{}.ts"

MAX = 2000


def download():
    try:
        for i in range(MAX):
            urllib.request.urlretrieve(BASE.format(i), f"vid_{i}.ts")
            print(f"Downloaded clip {i}")
    except HTTPError:
        stitch(i)


def stitch(index):
    ts_filenames = [f"vid_{x}.ts" for x in range(index)]
    # open one ts_file from the list after another and append them to merged.ts
    with open("merged.ts", "wb") as merged:
        for ts_file in ts_filenames:
            with open(ts_file, "rb") as mergefile:
                shutil.copyfileobj(mergefile, merged)

    # delete files
    for i in range(index):
        filename = f"{os.getcwd()}/vid_{index}.ts"
        if os.path.exists(filename):
            print(f"Removing {filename}")
            os.remove(filename)


if __name__ == "__main__":
    download()
