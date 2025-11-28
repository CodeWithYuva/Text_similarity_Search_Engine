
## 📌 Project Title

**AI Text Similarity Search Engine (Vector-Based)**

## 📌 Internship Task Requirements

* Build a **Text Similarity Search Engine**
* Take user input from frontend
* Compare the user’s text with a dataset (100+ lines)
* Use **TF-IDF** for text vectorization
* Use **Cosine Similarity** to calculate similarity scores
* Return **Top 3 most similar sentences** from the dataset
* Build a simple **frontend UI** for input + results
* Build backend using **Flask**
* Dataset provided in `.txt` or `.json` format
* **NO external AI APIs** (OpenAI / Gemini / Claude not allowed)

---

## 📌 Tech Stack Used

* **Flask (Python)** for backend
* **HTML + CSS + JavaScript** for frontend
* **Scikit-learn** for TF-IDF and cosine similarity
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
(line no 12 and 13 you can uncomment in first time execution)

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
<img width="1919" height="945" alt="Screenshot 2025-11-28 184219" src="https://github.com/user-attachments/assets/2107c48e-e179-4a33-9526-6223e5d56a19" />
<img width="1917" height="868" alt="Screenshot 2025-11-28 184310" src="https://github.com/user-attachments/assets/f8d8ef29-4657-4039-955e-33042843bf25" />



---
# Features #

### ⭐ ** Dataset Upload Feature**

Users can upload **their own custom dataset (.txt file)**.

* Automatically rebuilds TF-IDF model
* Makes the search engine usable for any domain (sports, news, finance, etc.)

---


### 🔍 Synonym Expansion (Internal Semantic Boost)

To make the search engine more intelligent, the backend uses NLTK WordNet to expand the user’s query with relevant synonyms. This helps the model find more meaningful matches even if the exact words do not appear in the dataset.

✔ Example

User input:

India won the match


Expanded internally to include:

win, victory, triumph, succeed, achieve
match, game, contest

✔ Why this improves accuracy

TF-IDF normally matches exact words only.
With synonym expansion:

“win” also matches “victory”

“match” also matches “game”

“succeed” also matches “come through”

This makes the search semantic, not just keyword-based. 


