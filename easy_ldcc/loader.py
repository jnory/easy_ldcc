import tarfile
from io import BytesIO
import os
import requests
import re

ARCHIVE_URL = "https://www.rondhuit.com/download/ldcc-20140209.tar.gz"
MIRROR_URL = "https://github.com/jnory/datasets/raw/master/ldcc/ldcc-20140209.tar.gz"
CACHE_DIR = ".cache"
CACHE_PATH = "{}/ldcc-20140209.tar".format(CACHE_DIR)
CORPUS_PAT = re.compile(r"^text/(.*?)/.*\d\.txt$")


def _get_data(use_mirror=True):
    if not os.path.exists(CACHE_DIR):
        os.mkdir(CACHE_DIR)
    if not os.path.exists(CACHE_PATH):
        url = MIRROR_URL if use_mirror else ARCHIVE_URL
        resp = requests.get(url)
        with open(CACHE_PATH, "wb") as fp:
            fp.write(resp.content)
        content = resp.content
    else:
        with open(CACHE_PATH, "rb") as fp:
            content = fp.read()
    return content


class Downloader(object):
    def __init__(self, use_mirror=True):
        tar = tarfile.open(fileobj=BytesIO(_get_data(use_mirror)))

        self.categories = []
        self.texts = []
        for member in tar.getmembers():
            name = member.name
            if not member.isfile():
                continue
            m = CORPUS_PAT.match(name)
            if m is None:
                continue

            category = m.group(1)
            obj = tar.extractfile(member)
            text = obj.read().decode("utf-8")
            self.categories.append(category)
            self.texts.append(text)
