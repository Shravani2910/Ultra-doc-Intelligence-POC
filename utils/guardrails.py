SIMILARITY_THRESHOLD = 0.75

def apply_guardrails(retrieved_docs):
    if not retrieved_docs:
        return False, "No relevant content found"

    top_score = retrieved_docs[0][1]

    if top_score < SIMILARITY_THRESHOLD:
        return False, "Low confidence retrieval"

    return True, None