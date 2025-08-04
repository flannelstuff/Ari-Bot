Ari-Bot: Offline LLM Chatbot
A Python-based chatbot using Phi-3-mini-4K-instruct, running offline to answer questions in science, education, history, general knowledge, and practical scenarios.
Features

Offline AI for diverse topics (knowledge up to early 2023).
Lightweight: Runs on laptops with 8GB+ RAM, ~2.2GB disk space.
"Thinking" indicator for user-friendly interaction.
Great for learning AI deployment and Python.

Requirements

Python 3.8+ (Download)
llama-cpp-python library
Phi-3-mini model file (~2.2GB)

Setup

Install Python 3 from python.org.
Install the library:pip3 install llama-cpp-python


Download the model: Phi-3-mini-4k-instruct-q4.
Place Phi-3-mini-4k-instruct-q4.gguf in the project folder.

How to Run

Navigate to the project folder:cd path/to/Chatbot


Run the chatbot:python3 chatbot.py


Ask questions (e.g., “What causes the aurora borealis?”); type “quit” to exit.

Example Questions

“How do I splint a broken finger in the woods?”
“What causes the aurora borealis?”
“List 5 whole foods.”

Notes

Knowledge is limited to early 2023; verify recent events (e.g., current president) with current sources.
Niche topics (e.g., specific brands) may have inaccuracies; rephrase for better results.
Tested on macOS with Apple M1 Max; adjust n_threads in chatbot.py for performance.
Debug logs (ggml_metal_init) may appear but are harmless.
