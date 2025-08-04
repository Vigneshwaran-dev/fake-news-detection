# 📰 Fake News Detection Web Application

A Flask-based web app that detects whether a given news article is **REAL** or **FAKE**, using a fine-tuned **DistilBERT** NLP model trained on real-world datasets.

---

## 🚀 Features

- 🔍 Paste any news article or headline and get an instant prediction
- 🧠 Uses a fine-tuned **DistilBERT** model trained with TensorFlow
- 📊 Shows prediction results with confidence percentages
- 🖥️ Clean, responsive UI built with HTML, CSS, and jQuery
- 🐍 Backend developed in **Python Flask**
- ☁️ Model was trained in **Google Colab**

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, Bootstrap, JavaScript (jQuery)
- **Backend**: Python, Flask
- **Machine Learning**: TensorFlow, Hugging Face Transformers, DistilBERT
- **Training Environment**: Google Colab

---

## 🧠 Model Info

The model is a fine-tuned version of DistilBERT, trained for binary classification on a dataset of real and fake news articles.

📁 *Model files are excluded from this repository to reduce size.*

📥 You can download the model files [from Google Drive](#) and place them inside a folder named `/model/` in the root directory.

Example folder structure:
/model/
├── config.json
├── pytorch_model.bin
├── tokenizer_config.json
└── vocab.txt

---

## 🖥️ How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/Vigneshwaran-dev/fake-news-detection.git
cd fake-news-detection

