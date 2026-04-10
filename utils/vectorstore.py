from langchain_community.vectorstores import Chroma

def create_vector_store(chunks, embedding):
    return Chroma.from_documents(
        chunks,
        embedding,
        persist_directory="db/"
    )