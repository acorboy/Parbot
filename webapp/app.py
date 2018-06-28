from flask import Flask, jsonify, render_template, request, json
from parse_data import parse_data
app = Flask(__name__)

@app.route('/')
def index_view():
  return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    print("RECEIVED POST")
    # get file
    str_data = request.data
    # return parse_data(str_data)
    return "received data!"


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=1111)