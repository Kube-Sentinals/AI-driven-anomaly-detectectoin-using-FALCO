from flask import Flask, jsonify

app = Flask(__name__)

patients = [
    {"id": 1, "name": "John Doe", "age": 29},
    {"id": 2, "name": "Jane Smith", "age": 34},
]

@app.route("/", methods=["GET"])
def get_patients():
    return jsonify(patients)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
