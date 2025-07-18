import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
import shap
import matplotlib.pyplot as plt

def split_data(df, target='quality', test_size=0.2, random_state=42):
    X = df.drop(target, axis=1)
    y = df[target]
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def train_model(X_train, y_train):
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('clf', RandomForestClassifier(random_state=42))
    ])

    param_grid = [
        {
            'clf': [RandomForestClassifier(random_state=42)],
            'clf__n_estimators': [100, 200],
            'clf__max_depth': [5, 10, None],
        },
        {
            'clf': [KNeighborsClassifier()],
            'clf__n_neighbors': [3, 5, 7],
            'clf__weights': ['uniform', 'distance']
        }
    ]

    grid_search = GridSearchCV(pipeline, param_grid, cv=3, scoring='accuracy', n_jobs=-1)
    grid_search.fit(X_train, y_train)

    print("Najbolji parametri:", grid_search.best_params_)
    print("Najbolji model:", grid_search.best_estimator_)
    return grid_search.best_estimator_

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    print("\nKlasifikacijski izvještaj:\n")
    print(classification_report(y_test, y_pred))

def explain_model_shap(model, X_train):
    clf = model.named_steps['clf']
    if isinstance(clf, RandomForestClassifier):
        explainer = shap.TreeExplainer(clf)
        shap_values = explainer.shap_values(X_train)
        shap.summary_plot(shap_values, X_train, plot_type="bar")
    else:
        print("SHAP analiza dostupna samo za RandomForestClassifier - preskačem vizualizaciju.")

def plot_feature_importance(model, X_train):
    clf = model.named_steps['clf']
    if isinstance(clf, RandomForestClassifier):
        importances = clf.feature_importances_
        indices = importances.argsort()[::-1]
        feature_names = X_train.columns

        plt.figure(figsize=(10, 6))
        plt.bar(range(len(feature_names)), importances[indices])
        plt.xticks(range(len(feature_names)), feature_names[indices], rotation=90)
        plt.title("Feature Importances - RandomForestClassifier")
        plt.tight_layout()
        plt.show()
    else:
        print("Feature importance nije dostupna za KNeighborsClassifier.")

