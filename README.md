# Product Keyword Extractor for Pet Retail

This is a Flask-based web application that extracts keywords for product names using a combination of NLP models: KeyBERT, YAKE, and HuggingFace Transformers (`zero-shot-classification`). The output is an Excel file with the original product names and their associated keywords.

---

## 🚀 Features

- Upload Excel file with product names
- Extract top keywords using:
  - **KeyBERT**
  - **YAKE**
  - **Zero-Shot Classification** from HuggingFace
- Download enriched Excel file with extracted keywords
- Designed specifically for **pet product domain**

---

## 📦 Installation

1. **Clone the repository**
```bash
git clone (https://github.com/mehtadigisha/Automate-Keywords)
cd Automate Keywords
````

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Download model (optional)**
   On first run, `transformers` and `keybert` models will be downloaded automatically.

---

## 📁 Folder Structure

```
.
├── app.py                  # Main Flask app
├── templates/
│   └── form.html           # Upload form for web interface
├── outputs/                # Generated Excel files
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## 🛠️ Usage

1. **Run the Flask app**

```bash
python app.py
```

2. **Open browser**
   Visit: [http://localhost:5000](http://localhost:5000)

3. **Upload your Excel file**

* Must contain a column named `Product Name`
* Click **Submit** to process
* Download the resulting file with keywords

---

## 📚 Dependencies

* `Flask`
* `pandas`
* `keybert`
* `yake`
* `transformers`
* `scikit-learn`
* `sentence-transformers`

Install all with:

```bash
pip install -r requirements.txt
```

---

## ✅ To-Do

* Add API support (optional)
* Add interface for direct keyword input
* Add support for CSV upload

---
