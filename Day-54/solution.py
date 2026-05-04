import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("dataset.csv")

print("Distribution of sensitive attribute (gender):")
print(df['gender'].value_counts(normalize=True))

print("\nCorrelation with target label:")
print(df.select_dtypes(include=['number']).corr()['hired'])

df['gender_encoded'] = df['gender'].map({'male': 0, 'female': 1})

X = df.drop(columns=['hired', 'gender'])  # drop original text column
X['gender_encoded'] = df['gender_encoded']
y = df['hired']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print("\nFairness Evaluation:")
for group in df['gender'].unique():
    group_idx = (X_test['gender_encoded'] == (0 if group == 'male' else 1))
    acc = accuracy_score(y_test[group_idx], model.predict(X_test[group_idx]))
    print(f"Accuracy for {group}: {acc:.2f}")
