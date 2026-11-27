import joblib


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


from housing_data import load_data


# Load dataset
df = load_data()


# Separate input and output
X = df[["area", "bedrooms", "age"]]
y = df["price"]


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Create and train model
model = LinearRegression()


model.fit(X_train, y_train)


# Evaluate model
predictions = model.predict(X_test)


rmse = mean_squared_error(y_test, predictions) ** 0.5


r2 = r2_score(y_test, predictions)


print("RMSE:", round(rmse, 2))
print("R2 Score:", round(r2, 4))


# Save model
joblib.dump(model, "model.pkl")


print("Model saved successfully.")
