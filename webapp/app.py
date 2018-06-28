from flask import Flask, jsonify, render_template, request, json
app = Flask(__name__)

@app.route('/')
def index_view():
  return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # get file
    i = 0

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)