
import os
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

class VectorStore:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings()
        self.index_path = "faiss_index"

        if os.path.exists(self.index_path):
            self.store = FAISS.load_local(self.index_path, self.embeddings)
        else:
            self.store = None

    def add(self, texts):
        if self.store is None:
            self.store = FAISS.from_texts(texts, self.embeddings)
        else:
            self.store.add_texts(texts)

        self.store.save_local(self.index_path)

    def search(self, query):
        if self.store:
            return self.store.similarity_search(query, k=3)
        return [] 
    
    
