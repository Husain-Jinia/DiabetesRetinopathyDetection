import pickle
loaded_model = pickle.load(open('models/final_heart_basic_model.sav', 'rb'))
# result = loaded_model.score(X_test, Y_test)

y_pred= loaded_model.predict([[0.0, 0.0, 1.0, 45.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 4.0]])
print(y_pred)