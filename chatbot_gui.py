import tkinter as tk
from tkinter import scrolledtext

class ChatbotApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple Chatbot")

        self.chat_history = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=50, height=20)
        self.chat_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.chat_history.config(state=tk.DISABLED)

        self.user_input = tk.Entry(master, width=40)
        self.user_input.grid(row=1, column=0, padx=10, pady=10)
        self.user_input.bind("<Return>", self.send_message)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

        self.append_message("Chatbot: Hello! I am a simple chatbot. Type 'bye' to exit.")

    def append_message(self, message):
        self.chat_history.config(state=tk.NORMAL)
        self.chat_history.insert(tk.END, message + "\n")
        self.chat_history.config(state=tk.DISABLED)
        self.chat_history.see(tk.END)

    def send_message(self, event=None):
        user_message = self.user_input.get()
        self.user_input.delete(0, tk.END)

        if user_message.strip() == "":
            return

        self.append_message(f"You: {user_message}")
        self.get_chatbot_response(user_message.lower())

    def get_chatbot_response(self, message):
        if message == "hello":
            response = "Hi!"
        elif message == "how are you":
            response = "I'm fine, thanks!"
        elif message == "bye":
            response = "Goodbye!"
            self.master.after(500, self.master.destroy) # Close window after a short delay
        else:
            response = "I don't understand that. Please try 'hello', 'how are you', or 'bye'."
        
        self.append_message(f"Chatbot: {response}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()

