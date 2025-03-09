import os
import numpy as np
from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import gdown
import warnings

warnings.filterwarnings("ignore")
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # Disable GPU
app = Flask(__name__)

# Google Drive file ID
file_id = "1VPollmB85-K4jYdBtobQLZ0T02Jv8txG"
url = f"https://drive.google.com/uc?id={file_id}&export=download"
model_path = "Lung_Cancer_model.keras"

# ✅ Only download the model if it doesn't already exist
if not os.path.exists(model_path):
    print("Downloading model...")
    gdown.download(url, model_path, quiet=False)
    print("Download Complete!")
else:
    print("Model already exists. Skipping download.")

# ✅ Load the model once
print("Loading model...")
model = load_model(model_path)
print("Model loaded successfully!")

# Ensure the upload folder exists
UPLOAD_FOLDER = "static/uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def preprocess_image(img_path):
    """Preprocess the image to match the model input shape."""
    img = image.load_img(img_path, target_size=(150, 150))  # Resize image
    img_array = image.img_to_array(img) / 255.0  # Convert and normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
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

        # Calculate confidence
        confidence = prediction * 100 if prediction > 0.5 else (1 - prediction) * 100
        result = "Lung Cancer Detected" if prediction < 0.5 else "No Lung Cancer"

        return render_template("result.html", prediction=result, confidence=confidence, image_path=filepath)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
