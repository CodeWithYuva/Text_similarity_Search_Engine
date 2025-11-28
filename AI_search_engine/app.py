from flask import Flask, render_template, request, jsonify
import pathlib
import re
import nltk
from nltk.corpus import wordnet

# Import modular engines
from similarity.tfidf_engine import TFIDFEngine
from similarity.similarity_engine import SimilarityEngine

# Uncomment this once (first run only)
#nltk.download('wordnet')
#nltk.download('omw-1.4')

app = Flask(__name__)

# --- Load dataset ---
DATA_PATH = pathlib.Path(__file__).parent / "dataset.txt"
with open(DATA_PATH, encoding="utf-8") as f:
    corpus = [line.strip() for line in f if line.strip()]

# Initialize engines
vector_engine = TFIDFEngine()
vector_engine.fit(corpus)

sim_engine = SimilarityEngine()

# Regex to match words
WORD_RE = re.compile(r"\b([A-Za-z0-9_']+)\b")

def highlight_matches(sentence, query):
    def replace(match):
        word = match.group(0)
        return f"<mark>{word}</mark>" if word.lower() in query_words else word

    global query_words
    query_words = set([w.lower() for w in query.split()])
    return re.sub(WORD_RE, replace, sentence)


# Home page
@app.route('/')
def home():
    return render_template("index.html")

# Main Search API
@app.route('/search', methods=['POST'])
def search():
    data = request.get_json() or {}
    query = data.get('query', '').strip()

    if not query:
        return jsonify({'error': 'Empty query'}), 400

    q_vec = vector_engine.transform(query)


    top_idx, scores = sim_engine.get_top_n(q_vec, vector_engine.matrix)

    # Prepare response
    results = []
    for idx in top_idx:
        sent = vector_engine.corpus[idx]
        sent_html = highlight_matches(sent, query)
        results.append({
            "sentence": sent,
            "sentence_html": sent_html,
            "score": float(round(scores[idx], 4))
        })

    return jsonify({
        "query": query,
        "results": results
    })

# Custom Dataset Upload
@app.route('/upload-dataset', methods=['POST'])
def upload_dataset():
    global corpus, vector_engine

    json_data = request.get_json() or {}
    data = json_data.get('data', '')

    lines = [line.strip() for line in data.split('\n') if line.strip()]

    if len(lines) < 1:
        return jsonify({'error': 'Dataset empty!'}), 400

    corpus = lines
    vector_engine.fit(corpus)

    return jsonify({"message": f"Dataset updated with {len(corpus)} lines"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
