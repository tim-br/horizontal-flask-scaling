from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

@app.route('/multiply/<int:number>', methods=['GET'])
def multiply(number):
    # Simulate processing time
    time.sleep(random.uniform(2, 5))
    return jsonify({"result": number * 2})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
