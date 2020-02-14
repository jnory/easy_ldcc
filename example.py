from collections import defaultdict

from easy_ldcc import download


def print_stat(data):
    count = defaultdict(lambda: 0)
    for d in data:
        count[d["category"]] += 1
    count = dict(count)
    print(count)


def main():
    data = download()
    train = data["train"]
    dev = data["dev"]
    test = data["test"]
    vocab = data["vocab"]
    categories = data["cat_id"]

    print("# of training =", len(train))
    print("# of dev =", len(dev))
    print("# of test =", len(test))
    print("# of vocab =", len(vocab))
    print("# of categories =", len(categories))
    print_stat(train)
    print_stat(dev)
    print_stat(test)


if __name__ == "__main__":
    main()
