# create_main_file.py

chatbot_code = """
import tkinter as tk
from tkinter import scrolledtext
import random
import time
import threading
import datetime

# -----------------------------
# Memory to store user info
# -----------------------------
memory = {
    "name": None,
    "favorite_color": None,
    "previous_topics": []
}

# -----------------------------
# Response templates
# -----------------------------
def generate_response(user_input):
    user_input = user_input.lower()
    
    # Limit memory to last 10 topics
    memory["previous_topics"].append(user_input)
    if len(memory["previous_topics"]) > 10:
        memory["previous_topics"].pop(0)
    
    # Greetings
    if any(greet in user_input for greet in ["hello", "hi", "hey", "hola"]):
        if memory["name"]:
            return f"Hello {memory['name']}! How are you today?"
        else:
            return random.choice([
                "Hello! What's your name?",
                "Hi there! How are you doing?",
                "Hey! Nice to meet you."
            ])
    
    # Capture name
    if "my name is" in user_input:
        name = user_input.split("my name is")[-1].strip().capitalize()
        memory["name"] = name
        return f"Nice to meet you, {name}! How can I help you today?"
    elif "i am" in user_input and not memory["name"]:
        name = user_input.split("i am")[-1].strip().capitalize()
        memory["name"] = name
        return f"Nice to meet you, {name}! How can I help you today?"
    
    # Farewell
    if any(farewell in user_input for farewell in ["bye", "goodbye", "see you"]):
        return random.choice([
            f"Goodbye {memory.get('name','friend')}! Take care!",
            "See you later! Have a great day!",
            "Bye! It was nice chatting with you!"
        ])
    
    # How are you
    if "how are you" in user_input:
        return random.choice([
            "I'm just a bot, but feeling great!",
            "Doing well! How about you?",
            "All systems operational!"
        ])
    
    # Favorite color
    if "favorite color" in user_input:
        if memory["favorite_color"]:
            return f"My favorite color is {memory['favorite_color']}. What's yours?"
        else:
            return "I like green! What's your favorite color?"
    
    if "is my favorite color" in user_input:
        color = user_input.split()[-1].capitalize()
        memory["favorite_color"] = color
        return f"Got it! I'll remember that your favorite color is {color}."
    
    # Date and time
    if "time" in user_input and "date" not in user_input:
        return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"
    if "date" in user_input:
        return f"Today is {datetime.datetime.now().strftime('%A, %d %B %Y')}"
    
    # Jokes
    if "joke" in user_input:
        return random.choice([
            "Why did the computer go to the doctor? It caught a virus!",
            "Why was the math book sad? Too many problems.",
            "Why do programmers prefer dark mode? Because light attracts bugs."
        ])
    
    # Quotes
    if "quote" in user_input or "motivation" in user_input:
        return random.choice([
            "Believe in yourself!",
            "Stay positive and work hard!",
            "Dream big and dare to fail!",
            "Mistakes are lessons in disguise!"
        ])
    
    # Default response
    return random.choice([
        "Interesting! Tell me more.",
        "Hmm, I can't answer that yet.",
        "Can you explain it differently?",
        "I see! Let's talk more about it.",
        "That's interesting! What else would you like to talk about?"
    ])

# -----------------------------
# Typing animation
# -----------------------------
def type_bot_message(message):
    chat_window.configure(state='normal')
    chat_window.insert(tk.END, "Bot: ", "bot")
    for char in message:
        chat_window.insert(tk.END, char, "bot")
        chat_window.update()
        time.sleep(0.02)
    chat_window.insert(tk.END, "\\n\\n")
    chat_window.configure(state='disabled')
    chat_window.yview(tk.END)

def send_message(event=None):
    user_input = user_entry.get().strip()
    if user_input == "":
        return
    chat_window.configure(state='normal')
    chat_window.insert(tk.END, f"You: {user_input}\\n\\n", "user")
    chat_window.configure(state='disabled')
    chat_window.yview(tk.END)
    user_entry.delete(0, tk.END)
    threading.Thread(target=type_bot_message, args=(generate_response(user_input),), daemon=True).start()

# -----------------------------
# GUI Setup
# -----------------------------
def main():
    global chat_window, user_entry
    root = tk.Tk()
    root.title("ChatGPT-like PyBot")
    root.geometry("650x700")
    root.configure(bg="#f0f0f0")
    chat_window = scrolledtext.ScrolledText(root, width=75, height=35, font=("Arial", 11), bg="#ffffff", padx=10, pady=10, wrap=tk.WORD)
    chat_window.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
    chat_window.tag_configure("user", foreground="white", background="#4a90e2", justify="right", spacing3=5)
    chat_window.tag_configure("bot", foreground="black", background="#d3f8d3", justify="left", spacing3=5)
    chat_window.configure(state='disabled')
    input_frame = tk.Frame(root, bg="#f0f0f0")
    input_frame.pack(pady=10, padx=10, fill=tk.X)
    user_entry = tk.Entry(input_frame, width=60, font=("Arial", 12))
    user_entry.pack(side=tk.LEFT, padx=(0, 10), fill=tk.X, expand=True)
    user_entry.bind("<Return>", send_message)
    user_entry.focus()
    send_button = tk.Button(input_frame, text="Send", command=send_message, font=("Arial", 12), bg="#4a90e2", fg="white", width=8)
    send_button.pack(side=tk.RIGHT)
    chat_window.configure(state='normal')
    chat_window.insert(tk.END, "Bot: Welcome to PyBot! How can I help you today?\\n\\n", "bot")
    chat_window.configure(state='disabled')
    root.mainloop()

if __name__ == "__main__":
    main()
"""

# Write to main.py
with open("main.py", "w", encoding="utf-8") as f:
    f.write(chatbot_code)

print("main.py has been created successfully! You can upload this to GitHub.")
