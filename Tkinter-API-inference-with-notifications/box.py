import tkinter as tk
from tkinter import messagebox
import json
import requests
from plyer import notification

PORT = 1234

class OverlayApp:
    def __init__(self, root):
        self.root = root
        root.geometry('300x50+100+0')
        root.resizable(False, False)
        root.overrideredirect(True)
        
        self.keep_on_top()
        root.update_idletasks()
        self.history = []
        self.history_index = -1
        self.current_text = ""

        def quit_app(event=None):
            confirm = messagebox.askyesno("Confirmation", "Are you sure you want to quit?")
            if confirm:
                root.quit()
        
        root.bind('<Escape>', quit_app)

        self.wordbox = tk.Entry(root)
        self.wordbox.pack(pady=5, padx=5, fill=tk.BOTH, expand=True)
        self.wordbox.bind('<Return>', self.generate)
        self.wordbox.bind('<Up>', self.scroll_up)
        self.wordbox.bind('<Down>', self.scroll_down)        

        def start_move(event):
            root.x = event.x
            root.y = event.y

        def stop_move(event):
            root.x = None
            root.y = None

        def do_move(event):
            x = (event.x_root - root.x)
            y = (event.y_root - root.y)
            root.geometry(f"+{x}+{y}")

        root.bind("<Button-1>", start_move)
        root.bind("<ButtonRelease-1>", stop_move)
        root.bind("<B1-Motion>", do_move)

    def scroll_up(self, event=None):
        if len(self.history) > 0 and self.history_index < len(self.history) - 1:
            if self.history_index == -1:
                self.current_text = self.wordbox.get()
            self.history_index += 1
            self.wordbox.delete(0, tk.END)
            self.wordbox.insert(0, self.history[self.history_index])

    def scroll_down(self, event=None):
        if self.history_index > -1:
            self.history_index -= 1
            self.wordbox.delete(0, tk.END)
            if self.history_index == -1:
                self.wordbox.insert(0, self.current_text)
            else:
                self.wordbox.insert(0, self.history[self.history_index])


    def generate(self, event=None):
        user_input = self.wordbox.get()
        self.history.append(user_input)  # Updating history
        self.history = self.history[-10:]  # Keep only last 10 entries
        self.history_index = -1  # Resetting history index
        self.current_text = ""  # Clearing current text
        try:
            response = self.send_request(user_input)
            send_notification(f"Response: {response}")
        except requests.RequestException as e:
            send_notification(f"Request Exception: {str(e)}")
        self.wordbox.delete(0, tk.END)


    def send_request(self, user_input):
        url = f"http://localhost:{PORT}/v1/chat/completions"
        headers = {"Content-Type": "application/json"}
        data = {
            "messages": [
                {"role": "user", "content": f"### Instruction: {user_input}\n###Response: "}
            ],
            "stop": ["### Instruction:"],
            "temperature": 0.7,
            "max_tokens": -1,
            "stream": False
        }
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']

    def keep_on_top(self):
        self.root.attributes('-topmost', True)
        self.root.after(1000, self.keep_on_top)

def send_notification(message):
    max_length = 240
    while len(message) > 0:
        if len(message) <= max_length:
            notification.notify(
                message=message
            )
            break

        split_index = message.rfind('.', 0, max_length)
        if split_index == -1:
            split_index = message.rfind(' ', 0, max_length)
        if split_index == -1:
            split_index = max_length

        chunk = message[:split_index]
        notification.notify(
            message=chunk,
            timeout=0
        )

        message = message[split_index + 1:].strip()

if __name__ == "__main__":
    root = tk.Tk()
    app = OverlayApp(root)
    root.mainloop()
