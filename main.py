import os
import sklearn
import prediciton
from flask import Flask, render_template, request, flash, jsonify
from werkzeug.utils import secure_filename

# print('The scikit-learn version is {}.'.format(sklearn.__version__))
app = Flask(__name__)
@app.route('/prediction/<age>/<Kidney>/<Glucose>/<Gender>/<Hepatic>/<pulse>')
def success(age,	Kidney, Glucose,	Gender, Hepatic, pulse):
    pred = prediciton.predict(int(age),	int(Kidney), int(Glucose),	int(Gender), int(Hepatic), int(pulse))
    return jsonify(pred)

@app.route('/')
def home():
  return 'Covid Server'
if __name__ == '__main__':
    app.run(host="0.0.0.0")
