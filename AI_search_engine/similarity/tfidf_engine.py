from sklearn.feature_extraction.text import TfidfVectorizer

class TFIDFEngine:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.corpus = []
        self.matrix = None

    def fit(self, corpus):
        self.corpus = corpus
        self.matrix = self.vectorizer.fit_transform(corpus)

    def transform(self, text):
        return self.vectorizer.transform([text])
