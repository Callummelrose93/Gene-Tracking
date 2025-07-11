import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression   
import numpy as np  

# Load the dataset
df = pd.read_csv('weight_to_body_fat_percentage.csv')


# Preprocess the data
X = df['Weight'].values.reshape(-1, 1)
y = df['BodyFatPercentage'].values

# Train the model
model = LinearRegression()
model.fit(X, y)

# Make predictions
predictions = model.predict(X)

# Visualize the results
plt.scatter(X, y, color='blue', label='Actual')
plt.plot(X, predictions, color='red', label='Predicted')
plt.xlabel('Weight')
plt.ylabel('Body Fat Percentage')
plt.title('Weight vs Body Fat Percentage')
plt.legend()
plt.show()