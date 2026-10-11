
from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

@app.route("/")
def home():
    return """
    <h1>RetailVision AI</h1>
    <p>Upload a shelf image to test the API.</p>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="image" accept="image/*" required>
        <button type="submit">Upload Image</button>
    </form>
    """

@app.route("/upload", methods=["POST"])
def upload():
    if "image" not in request.files:
        return jsonify({"error": "Please select an image"}), 400

    image = request.files["image"]

    if not image.filename:
        return jsonify({"error": "No image selected"}), 400

    filename = secure_filename(image.filename)
    if not filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
        return jsonify({"error": "Use JPG, JPEG, PNG or WEBP"}), 400

    return jsonify({
        "project": "RetailVision AI",
        "filename": filename,
        "message": "Image uploaded successfully. Detection will be added next."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
