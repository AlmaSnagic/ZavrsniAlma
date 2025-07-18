from ml import model
from sqlalchemy import create_engine
import pandas as pd

def load_data_sql(connection_string, table_name):
    engine = create_engine(connection_string)
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, engine)
    return df

def run_training(connection_string, table_name):
    print("✅ Učitavanje podataka iz baze...")
    df = load_data_sql(connection_string, table_name)

    print(f"✅ Učitano {len(df)} redova i {len(df.columns)} kolona.\n")

    X_train, X_test, y_train, y_test = model.split_data(df)

    print("✅ Trening modela sa GridSearchCV pipeline-om...")
    clf = model.train_model(X_train, y_train)

    print("\n✅ Evaluacija modela na test skupu:")
    model.evaluate_model(clf, X_test, y_test)

    print("\n✅ SHAP analiza (ako je primjenjiva):")
    model.explain_model_shap(clf, X_train)

    print("\n✅ Feature importance (ako je primjenjivo):")
    model.plot_feature_importance(clf, X_train)

    print("\n🎉 Trening i analiza modela završeni.")