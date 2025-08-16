### KNN Workflow

1. Import and initialize model
knn = KNeighborsClassifier(n_neighbors=3)

2. Fit (learning)
knn.fit(X_train, y_train)

3. Predict (for inspection)
y_pred = knn.predict(X_test)

4. Evaluate
knn.score(X_test, y_test)