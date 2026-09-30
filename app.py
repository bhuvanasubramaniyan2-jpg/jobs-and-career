from flask import Flask,render_template,request,jsonify
from config import RESPONSES
app=Flask(__name__)
@app.route("/")
def home(): return render_template("index.html")
@app.route("/chat",methods=["POST"])
def chat():
    msg=(request.get_json(silent=True) or {}).get("message","").strip().lower()
    if not msg: return jsonify(reply="Please type a jobs or career question.")
    reply=RESPONSES["default"]
    for k,v in RESPONSES.items():
        if k!="default" and k in msg: reply=v; break
    return jsonify(reply=reply)
if __name__=="__main__": app.run(host="0.0.0.0",port=5000,debug=True)
