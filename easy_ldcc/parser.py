import re
import MeCab
from dateutil.parser import parse

DATETIME_PAT = re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\d.*$")


def remove_meta(sentences):
    data = []
    timestamp = None

    for sentence in sentences:
        sentence = sentence.strip()
        if sentence == "":
            continue
        if sentence.startswith("http"):
            continue
        if DATETIME_PAT.match(sentence):
            timestamp = parse(sentence)
            continue
        data.append(sentence)
    return data, timestamp


class Parser(object):
    def __init__(self):
        self.tagger = MeCab.Tagger("-Owakati")
        self.tagger.parse("")

    def parse(self, text):
        sentences = text.split("\n")
        sentences, timestamp = remove_meta(sentences)
        assert timestamp is not None
        doc = []
        for sentence in sentences:
            tokenized = self.tagger.parse(sentence).strip()
            words = tokenized.split()
            doc.append(["<s>"] + words + ["</s>"])
        return doc, timestamp
