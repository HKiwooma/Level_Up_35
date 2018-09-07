from flask import Flask, jsonify

from api.users import Users, users_api

app = Flask(__name__)
app.register_blueprint(users_api)

DEBUG =True
HOST = '127.0.0.1'
PORT = 5050

@app.route('/')
def api():
    return 'This is the first route' 

if __name__ == '__main__':
    app.run(debug = DEBUG, host = HOST, port = PORT)
