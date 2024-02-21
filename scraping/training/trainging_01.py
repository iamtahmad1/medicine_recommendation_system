import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

# Load data from CSV file into a pandas DataFrame
df = pd.read_csv('output.csv')

# Combine symptom columns into a single text field
df['Symptoms'] = df[['Head', 'Stomach', 'Abdomen']].apply(lambda x: ' '.join(x.dropna()), axis=1)

# Split the DataFrame into features (X) and labels (y)
X = df['Symptoms']
y = df.drop(columns=['Medicine Name'])  # Exclude symptom columns, keep only medicine columns as labels

# Initialize TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Initialize Random Forest classifier
rf_classifier = RandomForestClassifier()

# Initialize MultiOutputClassifier with Random Forest classifier
multi_output_classifier = MultiOutputClassifier(estimator=rf_classifier, n_jobs=-1)

# Create a pipeline with TF-IDF vectorizer and MultiOutputClassifier
pipeline = Pipeline([
    ('tfidf', tfidf_vectorizer),
    ('clf', multi_output_classifier)
])

# Train the pipeline on the data
pipeline.fit(X, y)

# Now you can use the trained pipeline to predict medicines based on symptoms
predicted_medicines = pipeline.predict(["list of symptoms"])
print("Predicted Medicines:", predicted_medicines)
