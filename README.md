# 🧠 AI-Based Image Classification Web App

This project is a full-stack AI web application that classifies uploaded images (e.g., cat vs dog) using a trained Convolutional Neural Network (CNN). It includes:

- A **Flask web app** for image uploads and result display.
- An **API backend** for serving model predictions.
- A trained model (`model.pkl`) with preprocessing logic.
- Large datasets handled via **Google Drive**.

---

## 📂 Project Structure

```
AI-Based-Project/
│
├── app.py                  # Flask app
├── api.py                  # (Optional) FastAPI backend
├── model.pkl               # Trained model (downloaded via gdown)
├── requirements.txt        # Python dependencies
├── templates/              # HTML files
│   ├── index.html
│   └── result.html
├── data/                   # Dataset (downloaded from Drive)
├── download_dataset.py     # Script to download large files from Drive
└── README.md
```

---

## ⚙️ Setup Instructions
### 📁 Dataset & Model Files

The large files required for this project (such as datasets and pre-trained models) are hosted on Google Drive due to GitHub's file size limitations.

🔗 **Google Drive Folder:**  
[Click here to access the files](https://drive.google.com/drive/u/0/folders/1dZvL1gi5QLwOGrfdn9XEsi4EnXx535bD)

---

### 📥 How to Download Files Using Python

We recommend using the `gdown` Python library to download files directly from Google Drive into your project.

#### ✅ Step 1: Install `gdown`

```bash
pip install gdown

### 1. Clone the repository

```bash
git clone https://github.com/srikanthyeli/AI-Based-Project.git
cd AI-Based-Project
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

### 3. Install required packages

```bash
pip install -r requirements.txt
```

### 4. Download dataset and model

```bash
python download_dataset.py
```

---

## 🚀 Running the App

### Run the Flask Web App:

```bash
python app.py
```

Then open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### (Optional) Run the FastAPI Backend:

```bash
uvicorn api:app --reload
```

Then open: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🖼️ How to Use

1. Launch the Flask app.
2. Open the home page in your browser.
3. Upload an image (JPG/PNG).
4. Click "Predict".
5. The result (label + confidence score) will be displayed.

---

## 🧾 Dataset Description

- **Source**: Custom dataset of cats and dogs.
- **Train Size**: ~1.4 GB (`input.csv`, `labels.csv`)
- **Test Size**: ~300 MB (`input_test.csv`, `labels_test.csv`)
- **Format**: Flattened image arrays stored in CSV format.
- **Access**: Files are hosted on [Google Drive](https://drive.google.com) and downloaded via `gdown`.

---

## 🧠 Model Details

- **Type**: CNN (Convolutional Neural Network)
- **Input**: RGB image resized to 244×244
- **Output**: Binary classification (`cat` or `dog`)
- **Framework**: TensorFlow / Keras
- **Performance**:
  - Accuracy: **96.2%** on test set
  - Loss: **0.12**
- **File**: `model.pkl` (saved via `model.save()` or `pickle`)

---

## 📌 Notes

- Avoid pushing large files to GitHub. Files over 100 MB are downloaded via Google Drive.
- If you face `TemplateNotFound`, ensure `templates/` directory is correctly named and placed.
- This app is for educational and demo purposes.

---

## 📧 Contact

Created by [Srikanth Yelisetty](https://github.com/srikanthyeli)  
Feel free to reach out via GitHub Issues or Pull Requests.
