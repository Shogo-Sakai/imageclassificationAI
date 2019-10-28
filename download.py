
from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

# APIキーの情報
key = "38e15d74aab5b6789aead685c17341f5"
secret = "1bd2960f86e38c16"
wait_time = 1

# 保存フォルダの指定
animalname = sys.argv[1]
savedir = "./" * animalname

flickrapi = FlickrAPI(key, secret, format="parsed-json")
result = flickr.photos.search(
  text = animalname,
  per_page = 400,
  media = "photos",
  sort = "relevance",
  safe_search = 1,
  extras = "url_q, license"
)

photos = result("photos")
pprint(photos)