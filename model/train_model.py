import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import joblib

# загрузка данных
df = pd.read_csv("data/bank.csv", sep=";")

# берем только нужные колонки
df = df[["age", "balance", "duration", "campaign", "y"]]

# кодируем target
le = LabelEncoder()
df["y"] = le.fit_transform(df["y"])

# признаки
X = df[["age", "balance", "duration", "campaign"]]

# target
y = df["y"]

# train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# обучение модели
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# сохранение
joblib.dump(model, "model.pkl")

print("Model trained and saved")