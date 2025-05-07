from flask import Flask, request, send_file, render_template
import pandas as pd
from transformers import pipeline
from keybert import KeyBERT
import yake
import uuid
import os

app = Flask(__name__)

# Load models once
nlp = pipeline("zero-shot-classification")
kw_model = KeyBERT(model='all-MiniLM-L6-v2')
yake_kw_extractor = yake.KeywordExtractor(lan="en", n=3, dedupLim=0.9, top=20)

CANDIDATE_LABELS = [
    "pet food", "nutrition", "cat food", "dog food", 
    "premium", "kitten", "adult", "large breed"
]

def extract_keywords(text):
    kw_keywords = kw_model.extract_keywords(
        text, keyphrase_ngram_range=(1, 3), stop_words='english', top_n=10)
    yake_keywords = yake_kw_extractor.extract_keywords(text)
    
    combined = {kw for kw, _ in kw_keywords}
    combined.update({kw for kw, _ in yake_keywords})
    
    classification = nlp(text, candidate_labels=CANDIDATE_LABELS)
    combined.update(classification['labels'][:5])
    
    return ", ".join(list(combined)[:20])

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file uploaded", 400

    file = request.files["file"]
    df = pd.read_excel(file)

    if "Product Name" not in df.columns:
        return "Excel file must have a 'Product Name' column.", 400

    results = []
    for product in df["Product Name"].dropna():
        keywords = extract_keywords(product)
        results.append({"Product Name": product, "Keywords": keywords})

    result_df = pd.DataFrame(results)
    output_filename = f"output_keywords_{uuid.uuid4().hex}.xlsx"
    result_path = os.path.join("outputs", output_filename)

    os.makedirs("outputs", exist_ok=True)
    result_df.to_excel(result_path, index=False)

    return send_file(result_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
