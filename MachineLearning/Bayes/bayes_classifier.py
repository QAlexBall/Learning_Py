import numpy as np
from sklearn import datasets
from ..utils.dataset_operator import normalize, train_test_split


class NaiveBayes:

    def __init__(self):
        self.parameters = {}

    def fit(self, train_data, train_label):
        classes = np.unique(train_label)
        for category in classes:
            category_images = train_data[np.where(train_label == category)]
            category_images_mean = np.mean(category_images, axis=0, keepdims=True)
            category_images_variance = np.var(category_images, axis=0, keepdims=True)
            parameters = {
                "mean": category_images_mean,
                "variance": category_images_variance,
                "prior": category_images.shape[0] / train_data.shape[0]
            }
            self.parameters["class_" + str(category)] = parameters

    def _gaussian(self, X, classes):
        eps = 1e-3
        mean = self.parameters["class_" + str(classes)]["mean"]
        variance = self.parameters["class_" + str(classes)]["variance"]

        numerator = np.exp(-(X - mean) ** 2 / (2 * variance + eps))
        denominator = np.sqrt(2 * np.pi * variance + eps)

        result = np.sum(np.log(numerator / denominator), axis=1, keepdims=True)
        print(result)
        return result.T


if __name__ == '__main__':
    data = datasets.load_digits()
    X = data.data[30:50]
    X = normalize(X)
    print("train data num:", X.shape[0])
    y = data.target[30:50]
    print("train data labels:", y)
    classifier = NaiveBayes()
    classifier.fit(X, y)
    classifier._gaussian(X, 1)
