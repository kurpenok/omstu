from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error

from boosting import GradientBoostingRegressor

# Загрузка набора данных
diabetes = load_diabetes()

# Разделение на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target, test_size=0.2, random_state=42)

# Инициализация и обучение модели бустинга
gb = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3)
gb.fit(X_train, y_train)

# Прогнозирование на тестовой выборке
y_pred = gb.predict(X_test)

# Вычисление MSE
mse = mean_squared_error(y_test, y_pred)
print("MSE: {:.2f}".format(mse))
print("MAPE: {:.2f}".format(mean_absolute_percentage_error(y_test, y_pred)))
