import sklearn.ensemble
import joblib



filename =  "mom.sav"
loaded_model = joblib.load(filename)
def predict(age,	Kidney, Glucose,	gender, Hepatic, pulse):
    final = loaded_model.predict([[age,	Kidney, Glucose,	gender, Hepatic, pulse]])
    # final = loaded_model.evaluate([[age,	Kidney, Glucose,	gender, Hepatic, pulse]])

    if final == 1:
        final = "Prediction: deceased. Recommended to visit the hospital."
    elif final == 0:
        final = "Prediction: discharged. Recommended to stay at home."
    return final
#     print(final)
# print(predict(82,	0,	148,	0,	1,	1))

