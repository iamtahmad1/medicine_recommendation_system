import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load data from CSV file into a pandas DataFrame
df = pd.read_csv('output_10.csv')

# Assuming 'Symptoms' is the column containing symptoms and 'Medicine' is the column containing corresponding medicines
X = df['Symptoms']
y = df['Medicine']

# Split data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Initialize Support Vector Machine classifier
svm_classifier = SVC()

# Create a pipeline with TF-IDF vectorizer and SVM classifier
pipeline = Pipeline([
    ('tfidf', tfidf_vectorizer),
    ('clf', svm_classifier)
])

# Train the pipeline on the training data
pipeline.fit(X , y)

# Predict labels for the testing data
y_pred = pipeline.predict(X_test)

# Evaluate model performance
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
