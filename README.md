# AI-Chatbot-with-Memory-RAG
A command-line AI chatbot built with Python and Google's Gemini API. It holds real, context-aware conversations and can answer questions grounded in your own notes using Retrieval-Augmented Generation (RAG) — instead of relying only on the model's general training.
# Features
Real back-and-forth conversation (not just one-shot Q&A)
Remembers previous messages within a session
Customizable personality via a system prompt
RAG-powered Q&A — answers questions using your own .txt notes as context
Admits when an answer isn't in the provided notes, instead of guessing
Simple terminal interface — type quit to exit anytime
# Tech Stack
Python 3
Google Gemini API (google-genai) — chat generation + embeddings
python-dotenv — for securely managing the API key
NumPy — for similarity calculations between embeddings
