from flask import Flask
app = Flask(__name__)
@app.route("/", methods=["GET"])
def root():
	return "Welcome to ITIL exam"

	return "/modules:1.security concept 2.cosa 3.fcn 4.pki 5.ndc 6.itil and devops"

	return "/me:PRN = 230344223005 NAME= Abdulvahid Ansari PHONE NUMBER = 8483825796"
app.run(host="0.0.0.0",port=4000, debug=True)

