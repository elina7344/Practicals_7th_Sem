import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
# Load your Facebook data into a pandas DataFrame (assuming you have 'text' and 'label' columns)
df = pd.read_csv('FB_data.csv')
#Step 2: Preprocess the Data
# Convert text data into numerical features using CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text'])
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, df['label'], test_size=0.2, random_state=42)
#Step 3: Train a Classifier (Naive Bayes in this example)
# Initialize and train a Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train, y_train)
#Step 4: Make Predictions and Evaluate the Model
# Make predictions on the test set
predictions = classifier.predict(X_test)
# Calculate accuracy and other metrics
accuracy = accuracy_score(y_test, predictions)

report = classification_report(y_test, predictions)
print(f'Accuracy: {accuracy:.2f}')
print('Classification Report:\n', report)

#OUTPUT
'''
Accuracy: 0.97
Classification Report:
                precision    recall  f1-score   support

     business       0.98      0.93      0.95       101
entertainment       1.00      0.93      0.96        81
     politics       0.91      0.99      0.95        83
        sport       1.00      1.00      1.00        98
         tech       0.95      1.00      0.98        82

     accuracy                           0.97       445
    macro avg       0.97      0.97      0.97       445
 weighted avg       0.97      0.97      0.97       445
'''
