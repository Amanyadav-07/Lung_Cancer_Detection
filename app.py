import os
import numpy as np
from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

# Load trained lung cancer model
MODEL_PATH = "Lung_Cancer_model.keras"
model = load_model(MODEL_PATH)

# Ensure the upload folder exists
UPLOAD_FOLDER = "static/uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
def preprocess_image(img_path):
    """Preprocesses the image to match the model input shape."""
    img = image.load_img(img_path, target_size=(150, 150))  # Resize image to match model
    img_array = image.img_to_array(img)  # Convert to array
    img_array = img_array / 255.0  # Normalize pixel values
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension (1, 150, 150, 3)
    return img_array

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Check if the file was uploaded
        if "file" not in request.files:
            return "No file uploaded", 400

        file = request.files["file"]
        if file.filename == "":
            return "No selected file", 400

        # Save uploaded file
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        # Preprocess and predict
        img_array = preprocess_image(filepath)
        prediction = model.predict(img_array)[0][0]  # Extract probability

        # Calculate confidence percentage
        confidence = prediction * 100 if prediction > 0.5 else (1 - prediction) * 100
        result = "Lung Cancer Detected" if prediction < 0.5 else "No Lung Cancer"

        return render_template("result.html", prediction=result, confidence=confidence, image_path=filepath)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
