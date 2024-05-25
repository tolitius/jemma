# CONTEXT
- Company documentation is stored on an internally hosted Confluence wiki
- Each team has their own space for documentation
- Documents contain text, links, images, tables, presentations, etc.
- The wiki contains hundreds of thousands of documents

# PROBLEM
- Searching for information on the wiki is difficult due to:
  - Information being scattered across different spaces and pages
  - Many documents being abandoned and not updated
- Onboarding new employees is challenging as they need to read through extensive documentation
- Understanding integration points between systems is difficult due to scattered information
- Comprehending how things work is not easy, despite most information being available

# SOLUTION
- Build a RAG (Retrieval Augmented Generation) system that allows users to interact with and retrieve information from the wiki through natural language queries
- Ensure data privacy by:
  - Running the RAG system on internal company servers
  - Using local embeddings and language models (e.g., Ollama or llama.cpp)
- Host the RAG system using an open-source UI (e.g., open-webui, oobabooga) for user interaction
- Implement document indexing to keep the RAG system up-to-date:
  - Index new documents as they are created
  - Periodically re-index old documents
- Utilize ColBERT (v2) for document retrieval and RAGatouille for reranking to provide relevant search results
- Implement a fallback search mechanism using LLM function calling/tooling to directly search the wiki when the RAG system fails to find relevant information
- Develop user authentication, authorization, and access control to ensure data security
- Implement monitoring, logging, and reporting features to track system performance and usage
