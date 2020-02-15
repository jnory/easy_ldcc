from easy_ldcc.dataset import TrainingDataSet, EvalDataSet
from easy_ldcc.loader import Downloader
from easy_ldcc.parser import Parser
from easy_ldcc.splitter import Splitter


def download(use_mirror=True):
    downloader = Downloader(use_mirror)
    tokenizer = Parser()
    data = []
    for category, text in zip(downloader.categories, downloader.texts):
        doc, timestamp = tokenizer.parse(text)
        data.append((timestamp, doc, category))

    data = list(sorted(data))
    sp = Splitter(data)
    train = TrainingDataSet(sp.train)
    dev = EvalDataSet(sp.dev, train)
    test = EvalDataSet(sp.test, train)
    return dict(
        train=train.data,
        dev=dev.data,
        test=test.data,
        vocab=train.vocab,
        cat_id=train.categories,
    )
