from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
from utils import predict
import os

app = Flask(__name__)
CORS(app)

# Define the upload directory
UPLOAD_DIR = "upload"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "This is a garbage classification API",
                    "help": "Use /predict to get the output for classification"}), 200

@app.route("/predict", methods=["POST"])
def predict_endpoint():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_DIR, filename))

        predicted_value, predicted_accuracy = predict(os.path.join(UPLOAD_DIR, filename))
        return jsonify({
            "predicted_value": predicted_value,
            "predicted_accuracy": predicted_accuracy
        }), 200
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)