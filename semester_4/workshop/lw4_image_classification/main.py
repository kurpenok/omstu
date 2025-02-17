from mnist_downloader import load_mnist
from neural_network import NeuralNetwork
from gui import DigitDrawer


def main():
    (X_train, y_train), (_, _) = load_mnist()

    nn = NeuralNetwork(784, 128, 10)
    try:
        nn.load_weights("weights.npz")
    except:
        nn.train(X_train, y_train, epochs=10, batch_size=32, lr=0.1)
        nn.save_weights("weights.npz")

    app = DigitDrawer(nn)
    app.run()


if __name__ == "__main__":
    main()
