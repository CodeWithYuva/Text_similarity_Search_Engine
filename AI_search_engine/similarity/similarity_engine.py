from sklearn.metrics.pairwise import cosine_similarity

class SimilarityEngine:

    @staticmethod
    def get_top_n(query_vector, corpus_matrix, n=3):
        scores = cosine_similarity(query_vector, corpus_matrix)[0]
        top_idx = scores.argsort()[::-1][:n]
        return top_idx, scores
