class TrainingDataSet(object):
    def __init__(self, train):
        self.vocab = {
            "<unk>": 0,
            "<s>": 1,
            "</s>": 2,
        }
        self.categories = {}
        self.data = []
        for _, doc, category in train:
            if category not in self.categories:
                self.categories[category] = len(self.categories)
            category_id = self.categories[category]

            word_ids = []
            sentences = []
            for sentence in doc:
                for word in sentence:
                    if word not in self.vocab:
                        self.vocab[word] = len(self.vocab)
                    word_ids.append(self.vocab[word])
                sentences.append(" ".join(sentence))
            self.data.append(
                dict(
                    text=" ".join(sentences),
                    category=category,
                    word_ids=word_ids,
                    category_id=category_id,
                )
            )


class EvalDataSet(object):
    def __init__(self, data, train: TrainingDataSet):
        self.data = []
        unk_id = train.vocab["<unk>"]
        for _, doc, category in data:
            assert category in train.categories
            category_id = train.categories[category]

            word_ids = []
            sentences = []
            for sentence in doc:
                for word in sentence:
                    word_ids.append(train.vocab.get(word, unk_id))
                sentences.append(" ".join(sentence))
            self.data.append(
                dict(
                    text=" ".join(sentences),
                    category=category,
                    word_ids=word_ids,
                    category_id=category_id,
                )
            )
