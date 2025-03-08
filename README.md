# 🫡 Lung Cancer Detection using Deep Learning

This is a **Flask-based web application** that detects **lung cancer** using deep learning. The model is trained on **chest X-ray images** and predicts whether a patient has lung cancer. The app allows users to **upload an X-ray image** and get a diagnosis with an accuracy percentage.

![Lung Cancer Detection](https://your-image-link-here.png)

---

## 🚀 Features
- **Upload X-ray images** for detection
- **Deep Learning Model (Keras/TensorFlow)**
- **Flask Web App** with a user-friendly UI
- **Animated UI** with smooth effects
- **Cancer Detection Alert with GIF**
- **Deployed on Render**

---

## 🛠️ Installation

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Amanyadav-07/Lung_Cancer_Detection.git
cd Lung_Cancer_Detection
```

### 2️⃣ Create a Virtual Environment  
```bash
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# OR
.venv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4️⃣ Download the Model (300MB)  
Since the model is too large for GitHub, **download it manually** and place it in the project directory:  

👉 **[Download Model from Google Drive](https://drive.google.com/uc?id=YOUR_FILE_ID)**  
```bash
mv lung_cancer_model.keras ./  # Move it to the project root
```

### 5️⃣ Run the Flask App  
```bash
python app.py
```
Now open **http://127.0.0.1:5000/** in your browser! 🎉

---

## 🎨 UI & Screenshots
| **Home Page** | **Result Page** |
|--------------|--------------|
| ![Home](https://your-image-link-home.png) | ![Result](https://your-image-link-result.png) |

---

## 🚀 Deploy on Render  
1. Push your code to **GitHub**  
2. Go to [Render](https://dashboard.render.com)  
3. Create a **new Web Service**  
4. Select **your repository**  
5. **Set Build Command:**
   ```bash
   pip install -r requirements.txt
   ```
6. **Set Start Command:**
   ```bash
   gunicorn app:app
   ```
7. Deploy & Get your **Live URL** 🎉

---

## 💡 Technologies Used
- **Python, Flask** (Backend)
- **TensorFlow, Keras** (Deep Learning Model)
- **HTML, CSS, JavaScript** (Frontend)
- **Bootstrap & Animations** (UI Enhancements)

---

## 📌 Contributing  
Want to improve this project?  
1. Fork the repo  
2. Create a new branch  
3. Make changes & test  
4. Submit a Pull Request  

---

## 🐟 License  
This project is **MIT Licensed**. Feel free to use & modify. 🚀  

---

## 📞 Contact  
📧 **Email:** amanyadav32327@gmail.com  
🌐 **GitHub:** [Amanyadav-07](https://github.com/Amanyadav-07)  

---
**⭐ If you found this project helpful, please give it a star! ⭐**  

