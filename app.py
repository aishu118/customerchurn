from flask import Flask,render_template,request,redirect
import pickle
import numpy as np

model=pickle.load(open("churn.pkl","rb"))

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("churn.html")

@app.route("/predictwo",methods=["POST"])
def predict():
    accountlength=float(request.form.get("accountlength"))
    internationalplan=float(request.form.get("internationalplan"))
    #voicemailplan=float(request.form.get("voicemailplan"))
    numbervmailmessages=float(request.form.get("numbervmailmessages"))
    totaldayminutes=float(request.form.get("totaldayminutes"))
    totaldaycalls=float(request.form.get("totaldaycalls"))
    totaldaycharge=float(request.form.get("totaldaycharge"))
    totaleveminutes=float(request.form.get("totaleveminutes"))
    totalevecalls=float(request.form.get("totalevecalls"))
    totalevecharge=float(request.form.get("totalevecharge"))
    totalnightminutes=float(request.form.get("totalnightminutes"))
    totalnightcalls=float(request.form.get("totalnightcalls"))
    totalnightcharge=float(request.form.get("totalnightcharge"))
    totalintlminutes=float(request.form.get("totalintlminutes"))
    totalintlcalls=float(request.form.get("totalintlcalls"))
    totalintlcharge=float(request.form.get("totalintlcharge"))
    numbercustomerservicecalls=float(request.form.get("numbercustomerservicecalls"))
    
    
    result=model.predict(np.array([[accountlength,internationalplan,numbervmailmessages,totaldayminutes,totaldaycalls,totaldaycharge,totaleveminutes,totalevecalls,totalevecharge,totalnightminutes,totalnightcalls,totalnightcharge,totalintlminutes,totalintlcalls,totalintlcharge,numbercustomerservicecalls]]))
    
    if result[0]==1:
        return render_template("churned.html")
    else:
        return render_template("notchurned.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)