class Splitter(object):
    def __init__(self, data):
        n_data = len(data)
        n_test = int(n_data * 0.1)
        n_dev = int(n_data * 0.1)
        n_train = n_data - (n_test + n_dev)

        self.train = data[:n_train]
        self.dev = data[n_train:n_train+n_dev]
        self.test = data[n_train+n_dev:]
