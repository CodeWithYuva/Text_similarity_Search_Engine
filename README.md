# Text Similarity Search Engine (Flask) — README

## 📌 Project Title

**AI Text Similarity Search Engine (Vector-Based)**

## 📌 Internship Task Requirements

This project was built as part of an internship assignment with the following mandatory requirements:

### ✅ **Task Requirements Given by Company**

* Build a **Text Similarity Search Engine**
* Take user input from frontend
* Compare the user’s text with a dataset (100+ lines)
* Use **TF-IDF** for text vectorization
* Use **Cosine Similarity** to calculate similarity scores
* Return **Top 3 most similar sentences** from the dataset
* Build a simple **frontend UI** for input + results
* Build backend using **Flask / Node.js** (Flask chosen)
* Dataset provided in `.txt` or `.json` format
* **NO external AI APIs** (OpenAI / Gemini / Claude not allowed)

---

## 📌 Tech Stack Used

* **Flask (Python)** for backend
* **HTML + CSS + JavaScript** for frontend
* **Scikit-learn** for TF-IDF and cosine similarity
* **NLTK (optional earlier)** — later removed as per final requirement
* **LocalStorage** for storing search history

---

## 📌 Features Implemented (Beyond the Basic Requirement)

I enhanced the project significantly to make it more professional and interview‑ready.

### ⭐ **1. Modular Architecture (Professional Code Structure)**

Backend logic was divided into reusable modules:

* `tfidf_engine.py` → Handles TF-IDF vectorization
* `similarity_engine.py` → Handles Cosine similarity
* `app.py` → Flask routes + integration

This makes the project scalable and clean.

---

### ⭐ **2. Highlighting Matching Words (Google-like UI)**

Search results highlight matched words using `<mark>` tag so users can visually see relevance.

Example:

```
Query: cricket match
Result: India won the <mark>cricket</mark> <mark>match</mark> yesterday.
```

---

### ⭐ **3. Dataset Upload Feature**

Users can upload **their own custom dataset (.txt file)**.

* Automatically rebuilds TF-IDF model
* Makes the search engine usable for any domain (sports, news, finance, etc.)

---

### ⭐ **4. Search History Panel (LocalStorage)**

Every search is saved locally and shown in a history sidebar.

* Helps test functionality quickly
* Improves UI/UX

---

### ⭐ **5. Clean, Responsive Frontend UI**

Includes:

* Input box
* Search button
* Dataset upload section
* Search results
* History panel

Simple, intuitive, and user-friendly.

---

## 📌 Features Removed (Based on Your Requirement)

Initially, the project had *synonym expansion* using WordNet.
You requested removal of **Expanded Query** feature.

So the final version uses:
✔ Pure TF‑IDF
✔ Pure cosine similarity
❌ No synonyms
❌ No query expansion

This returns only exact TF-IDF based similarity.

---

## 📌 How It Works (Simple Explanation)

1. User enters a sentence in the frontend.
2. Backend converts the text to a TF-IDF vector.
3. Compares it with dataset vectors using cosine similarity.
4. Finds top 3 most similar sentences.
5. Highlights matched words.
6. Displays them with similarity scores.

---

## 📌 Project Structure

```
text-similarity-flask/
├── app.py
├── dataset.txt
├── requirements.txt
├── similarity/
│     ├── tfidf_engine.py
│     └── similarity_engine.py
├── templates/
│     └── index.html
└── static/
      └── script.js
```

---

## 📌 Requirements

Install dependencies:

```
pip install -r requirements.txt
```

Run once:

```
python -m nltk.downloader wordnet
python -m nltk.downloader omw-1.4
```

*(Only if synonyms were needed earlier; now optional.)*

---

## 📌 Run Instructions

Start the Flask server:

```
python app.py
```

Open in browser:

```
http://127.0.0.1:5000/
```

---

## 📌 Why This Project Is Impressive for an Internship

When explaining to interviewers, say:

> “I didn’t just complete the basic requirement.
> I added modular architecture, dataset upload, search history, and highlighted results.
> The project is scalable, easy to maintain, and built with clean separation of logic.”

This shows:

* Strong Python & Flask skills
* Understanding of text vectorization
* Good UI/UX sense
* Code organization & real‑world structure
* Ability to go beyond requirements

---

## 📌 Want me to add anything else?

I can also include:

* UML diagram
* Flowchart
* Architecture diagram
* Deployment (Render / PythonAnywhere)

Just tell me!
