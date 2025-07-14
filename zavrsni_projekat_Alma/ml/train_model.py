from ml import model

def run_training(connection_string, table_name):
    df = model.load_data_sql(connection_string, table_name)
    print(f"Učitano {len(df)} redova i {len(df.columns)} kolona iz baze.")
    X_train, X_test, y_train, y_test = model.split_data(df)
    clf = model.train_model(X_train, y_train)
    model.evaluate_model(clf, X_test, y_test)
    model.plot_feature_importance(clf, X_train.columns)