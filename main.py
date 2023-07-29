# from flask import Flask, jsonify, request
from websiteApi import create_app

# app = Flask(__name__)

# A dictionary to store user data (replace with your own user data storage mechanism)

app=create_app()



if __name__ == '__main__':
    app.run(debug=True)
