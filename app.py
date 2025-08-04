from flask import Flask, request, jsonify, render_template
from transformers import DistilBertTokenizerFast, TFDistilBertForSequenceClassification
import tensorflow as tf
import os

app = Flask(__name__)

# Load model from Google Drive download
MODEL_PATH = './model'  # You'll place your model here

try:
    tokenizer = DistilBertTokenizerFast.from_pretrained(MODEL_PATH)
    model = TFDistilBertForSequenceClassification.from_pretrained(MODEL_PATH)
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Model loading failed: {e}")
    tokenizer = None
    model = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not model or not tokenizer:
        return jsonify({"error": "Model not loaded"}), 500
        
    text = request.form.get('text', '')
    if not text:
        return jsonify({"error": "No text provided"}), 400
        
    try:
        inputs = tokenizer(text, return_tensors='tf', truncation=True, max_length=128)
        outputs = model(inputs)
        probs = tf.nn.softmax(outputs.logits, axis=1)
        
        return jsonify({
            "real_prob": float(probs[0][0]),
            "fake_prob": float(probs[0][1]),
            "verdict": "REAL NEWS" if probs[0][0] > 0.5 else "FAKE NEWS"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)