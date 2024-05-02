from flask import Flask, request, jsonify
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import precision_score, recall_score, f1_score
import pickle
import os

app = Flask(__name__)

scaler = StandardScaler()
clf = MLPClassifier(hidden_layer_sizes=(50, 100, 150, 200), max_iter=300, activation='relu', solver='adam')


data_path = os.environ.get('data_path', 'wine-quality-white-and-red.csv')
model_path = os.environ.get('model_path', 'wine_model.pkl')

@app.route('/train', methods=['POST'])
def train():
    global clf
    output_column = request.json.get('output_column')

    # Read the dataset
    df = pd.read_csv(data_path)

    # Split features and target variable
    X = df.drop(columns=[output_column]) 
    y = df[output_column]

    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    clf.fit(X_train, y_train)

    # Save the trained model to persistent storage
    with open(model_path, "wb") as f:
        pickle.dump((clf, scaler), f)

    # Make predictions on the test set
    y_pred = clf.predict(X_test)

     # Calculate precision, recall, and F1-score
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')

    return jsonify({'Precision': precision, 'Recall': recall, 'F1-score': f1})

@app.route('/predict', methods=['POST'])
def predict():
    global clf

    # Load the pickled model
    with open(model_path, 'rb') as model_file:
        clf = pickle.load(model_file)
    
    data = request.json.get('data')
    # Perform prediction using the loaded model
    prediction = clf.predict(data)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
