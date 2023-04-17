from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from svm import SVM


def main() -> None:
    # Загрузка набора данных
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target

    # Преобразование меток классов (-1, 1)
    y[y == 0] = -1
    y[y == 1] = -1
    y[y == 2] = 1

    # Разделение данных на обучающий и тестовый наборы
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    # Создание объекта SVM и обучение модели на обучающем наборе
    clf = SVM()
    clf.fit(X_train, y_train)

    # Получение прогнозов для тестового набора
    y_pred = clf.predict(X_test)

    # Преобразование меток классов обратно (0, 1, 2)
    y_test[y_test == -1] = 0
    y_pred[y_pred == -1] = 0

    # Оценка точности прогнозов
    accuracy = accuracy_score(y_test, y_pred)

    # Вывод результата
    print("[+] Accuracy:", accuracy)


if __name__ == "__main__":
    main()
