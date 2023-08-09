from flask import Flask, requests,jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    data = requests.json
    num1 = data.get('first')
    num2 = data.get('second')
    
    if num1 is None or num2 is None:
        return jsonify({'error': 'Both numbers are required'}), 400
    
    result = num1+num2
    return jsonify({'result': result})

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = requests.json
    num1 = data.get('first')
    num2 = data.get('second')
    
    if num1 is None or num2 is None:
        return jsonify({'error': 'Both numbers are required'}), 400
    
    result = num1-num2
    return jsonify({'result': result})
    

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = requests.json
    first = data.get("first")
    second =data.get("second")
    sum=int(first)-int(second)
    return jsonify({"result":sum})

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
