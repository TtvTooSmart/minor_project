import numpy as np
from sklearn.linear_model import LogisticRegression

# Define the training data
X = np.array([[0, 0, 0, 1, 25, 0, 0],
              [1, 0, 0, 0, 35, 1, 0],
              [1, 1, 0, 0, 45, 1, 1],
              [0, 0, 1, 1, 55, 0, 1],
              [0, 1, 1, 0, 65, 1, 1]])
y_heart_attack = np.array([0, 1, 1, 0, 1])
y_artery_block = np.array([0, 0, 1, 1, 1])

# Train the logistic regression models
heart_attack_model = LogisticRegression().fit(X, y_heart_attack)
artery_block_model = LogisticRegression().fit(X, y_artery_block)

# Define a function to modify the weight values based on the logistic regression models
def modify_weights(smoke, fried_food, alcohol, exercise, age, diabetes, heart_disease, heart_attack_weight, artery_block_weight):
    X_test = np.array([[smoke, fried_food, alcohol, exercise, age, diabetes, heart_disease]])
    heart_attack_weight_mod = heart_attack_weight + heart_attack_model.predict_proba(X_test)[0][1] * 10
    artery_block_weight_mod = artery_block_weight + artery_block_model.predict_proba(X_test)[0][1] * 10
    return heart_attack_weight_mod, artery_block_weight_mod