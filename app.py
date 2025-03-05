import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


model_pickle = open('classifier.pkl', 'rb')
clf = pickle.load(model_pickle)


@app.route("/predict", methods=['POST'])
def predictions():
    loan_req = request.get_json()
    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1

    if loan_req['Married'] == "Unmarried":
        Married = 0
    else:
        Married = 1

    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount']
    Credit_History = loan_req['Credit_History']

    prediction = clf.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

    if prediction == 1:
        pred = 'Approved'
    else:
        pred = 'Rejected'
    return {"loan_approval_status ": pred}
