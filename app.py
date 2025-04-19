from flask import Flask, request, jsonify
import numpy as np
print("Successfully imports!!")
app = Flask(__name__)



@app.route("/", methods=["POST"])
def function():
    data = request.get_json(force=True)
    arr = np.array([data, data, data])
    return jsonify(arr.tolist())



if __name__ == "__main__":
    app.run(port=80, host="0.0.0.0")
