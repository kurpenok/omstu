import numpy as np


class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.W1 = np.random.randn(input_size, hidden_size) * 0.01
        self.b1 = np.zeros(hidden_size)
        self.W2 = np.random.randn(hidden_size, output_size) * 0.01
        self.b2 = np.zeros(output_size)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def softmax(self, x):
        exps = np.exp(x - np.max(x, axis=1, keepdims=True))
        return exps / exps.sum(axis=1, keepdims=True)

    def forward(self, X):
        self.z1 = X @ self.W1 + self.b1
        self.a1 = self.sigmoid(self.z1)
        self.z2 = self.a1 @ self.W2 + self.b2
        self.a2 = self.softmax(self.z2)
        return self.a2

    def compute_loss(self, y_pred, y_true):
        m = y_true.shape[0]
        return -np.log(y_pred[np.arange(m), y_true]).mean()

    def backward(self, X, y_true, y_pred, lr):
        m = y_true.shape[0]
        dz2 = y_pred
        dz2[np.arange(m), y_true] -= 1
        dz2 /= m

        dW2 = self.a1.T @ dz2
        db2 = dz2.sum(axis=0)
        dz1 = (dz2 @ self.W2.T) * (self.a1 * (1 - self.a1))
        dW1 = X.T @ dz1
        db1 = dz1.sum(axis=0)

        self.W1 -= lr * dW1
        self.b1 -= lr * db1
        self.W2 -= lr * dW2
        self.b2 -= lr * db2

    def train(self, X_train, y_train, epochs, batch_size, lr):
        for _ in range(epochs):
            perm = np.random.permutation(X_train.shape[0])
            X_shuffled = X_train[perm]
            y_shuffled = y_train[perm]

            for i in range(0, X_train.shape[0], batch_size):
                X_batch = X_shuffled[i : i + batch_size]
                y_batch = y_shuffled[i : i + batch_size]

                y_pred = self.forward(X_batch)
                self.backward(X_batch, y_batch, y_pred, lr)

    def predict(self, X):
        return np.argmax(self.forward(X), axis=1)

    def save_weights(self, filename):
        np.savez(filename, W1=self.W1, b1=self.b1, W2=self.W2, b2=self.b2)

    def load_weights(self, filename):
        data = np.load(filename)
        self.W1 = data["W1"]
        self.b1 = data["b1"]
        self.W2 = data["W2"]
        self.b2 = data["b2"]
