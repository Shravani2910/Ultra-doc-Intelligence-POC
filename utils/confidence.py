def compute_confidence(retrieved_docs):
    scores = [1 - doc[1] for doc in retrieved_docs]  # convert distance → similarity
    avg_score = sum(scores) / len(scores)

    # scale to %
    return round(avg_score * 100, 2)