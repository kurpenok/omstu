import os
import gzip
import urllib.request
import numpy as np


def download_mnist():
    base_url = "http://yann.lecun.com/exdb/mnist/"
    files = [
        "train-images-idx3-ubyte.gz",
        "train-labels-idx1-ubyte.gz",
        "t10k-images-idx3-ubyte.gz",
        "t10k-labels-idx1-ubyte.gz",
    ]

    if not os.path.exists("data"):
        os.makedirs("data")

    for file in files:
        if not os.path.exists(f"data/{file}"):
            print(f"Downloading {file}...")
            urllib.request.urlretrieve(base_url + file, f"data/{file}")
        else:
            print(f"{file} already exists.")


def load_images(filename):
    with gzip.open(filename, "rb") as f:
        _ = int.from_bytes(f.read(4), byteorder="big")
        num_images = int.from_bytes(f.read(4), byteorder="big")
        rows = int.from_bytes(f.read(4), byteorder="big")
        cols = int.from_bytes(f.read(4), byteorder="big")

        data = np.frombuffer(f.read(), dtype=np.uint8)
        data = data.reshape(num_images, rows * cols)
        return data.astype(np.float32) / 255.0


def load_labels(filename):
    with gzip.open(filename, "rb") as f:
        _ = int.from_bytes(f.read(4), byteorder="big")
        _ = int.from_bytes(f.read(4), byteorder="big")

        data = np.frombuffer(f.read(), dtype=np.uint8)
        return data


def load_mnist():
    # download_mnist()
    X_train = load_images("data/train-images-idx3-ubyte.gz")
    y_train = load_labels("data/train-labels-idx1-ubyte.gz")
    X_test = load_images("data/t10k-images-idx3-ubyte.gz")
    y_test = load_labels("data/t10k-labels-idx1-ubyte.gz")
    return (X_train, y_train), (X_test, y_test)
