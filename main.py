import sys
import urllib.request
import shutil


BASE = "https://tower-streaming.la.utexas.edu/vod/_definst_/gov312lusfp/2019/Fall/2019-09-04_gov312l_inn.mp4/media_{}.ts"

def download():
    for i in range(1500):
        urllib.request.urlretrieve(BASE.format(i), f"vid_{i}.ts")
        print(f"Downloaded clip {i} of 1500")

def stitch():
    ts_filenames = [f"vid_{x}.ts" for x in range(328)]
    # open one ts_file from the list after another and append them to merged.ts
    with open('merged.ts', 'wb') as merged:
        for ts_file in ts_filenames:
            with open(ts_file, 'rb') as mergefile:
                shutil.copyfileobj(mergefile, merged)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("Please provide a link")
    download()
    stitch()
