from flask import Flask, request, jsonify
from flask_cors import CORS
#import train
import pickle


import numpy as np



app = Flask(__name__)
CORS(app, resource = {r"/skins/*" : {"origin" : "*"}})

@app.route("/skins", methods = ["POST"])
def sime():
    p=request.form.getlist('image')
    x=5
    resp = {
	'ans' : x
    }
    return "dxfgjh" 


def main():
	app.run(debug = True)

if __name__ == "__main__":
	main()
