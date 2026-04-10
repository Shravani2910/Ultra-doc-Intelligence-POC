def retrieve_docs(vector_db, query, k=4):
    docs = vector_db.similarity_search_with_score(query, k=k)
    return docs