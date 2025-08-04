import logging
import os
import sys
import threading
import time
from llama_cpp import Llama

# Suppress all logging
logging.getLogger().setLevel(logging.CRITICAL)
os.environ["LLAMA_LOG_LEVEL"] = "CRITICAL"
os.environ["GGML_LOG_LEVEL"] = "CRITICAL"
os.environ["LLAMA_CPP_LOG_LEVEL"] = "CRITICAL"
sys.stderr = open(os.devnull, 'w')  # Redirect stderr to suppress ggml logs

# Load the Phi-3-mini model
model_path = "/Users/homebase/Desktop/Chatbot 7:31:25/Phi-3-mini-4k-instruct-q4.gguf"
llm = Llama(model_path=model_path, n_ctx=4096, n_threads=4, verbose=False, seed=42)

# Define a chat prompt template for maximum robustness
prompt_template = """<|user|>
You are Ari-Bot, an offline AI designed as a comprehensive knowledge resource for science, education, history, general knowledge, and practical scenarios. Provide accurate, concise, and factual answers tailored to the user's question, avoiding repetition, emojis, social media tokens (e.g., @POTUS), dates, or system tokens. For lists, ensure all requested items are provided. For practical or first-aid questions, offer general guidance and advise consulting a professional. For real-time data (e.g., weather, recent events), state that your knowledge is limited to early 2023 and suggest verifying with a current source, but provide general context if possible. If unsure, admit limitations and suggest rephrasing.
{user_input}<|end|>
<|assistant|>"""

# Function for a simple spinning loader
def spinner():
    spinner_chars = "|/-\\"
    i = 0
    while not stop_spinner:
        sys.stdout.write("\rAri-Bot is thinking " + spinner_chars[i % len(spinner_chars)])
        sys.stdout.flush()
        i += 1
        time.sleep(0.2)
    sys.stdout.write("\r" + " " * 30 + "\r")  # Clear the spinner line

# Start the conversation
print("Start chatting with Ari-Bot, your offline knowledge resource (type 'quit' to stop)!")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    
    # Format the prompt
    prompt = prompt_template.format(user_input=user_input)
    
    # Start the spinner in a separate thread
    stop_spinner = False
    spinner_thread = threading.Thread(target=spinner)
    spinner_thread.start()
    
    # Generate response
    response = llm(prompt, max_tokens=400, temperature=0.7, top_p=0.9, repeat_penalty=1.2, stop=["<|end|>", "<|assistant|>", "<|system|>"])
    generated_text = response['choices'][0]['text'].strip()
    
    # Stop the spinner
    stop_spinner = True
    spinner_thread.join()
    sys.stdout.write("\r" + " " * 30 + "\r")  # Clear the spinner line
    
    if not generated_text or len(generated_text) < 5:
        # Retry with higher temperature
        response = llm(prompt, max_tokens=400, temperature=0.8, top_p=0.9, repeat_penalty=1.2, stop=["<|end|>", "<|assistant|>", "<|system|>"])
        generated_text = response['choices'][0]['text'].strip()
        if not generated_text or len(generated_text) < 5:
            print("Ari-Bot: I couldn't provide a detailed answer due to my limited knowledge. Try rephrasing or asking about science, history, education, or practical tips!")
        else:
            print("Ari-Bot:", generated_text)
    else:
        print("Ari-Bot:", generated_text)