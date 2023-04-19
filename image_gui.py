from image import generate_image, download_image, get_fname_from_prompt
import os
import threading
import tkinter as tk

class MyApplication(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        parent.title("OpenAI Image Generator")
        
        # create the text box
        self.textbox = tk.Text(self, width=50, height=5)
        self.textbox.pack(padx=5, pady=5)

        # create the button
        self.button = tk.Button(self, text="Create Image", command=self.button_callback, pady=10)
        self.button.pack(pady=10)

        self.progress = tk.Label(self, text="", font=("Helvetica", 12), wraplength=self.winfo_width())
        self.progress.pack(pady=10)

    def button_callback(self):
        user_input = self.textbox.get("1.0", "end-1c")
        self.progress.config(text="Please wait.", wraplength=self.winfo_width())
        self.button.config(state="disabled")
        threading.Thread(target=self.create_image, args=(user_input,)).start()
        
    
    def create_image(self, prompt):
        desktop = os.path.expanduser("~/Desktop/OpenAI")
        os.makedirs(desktop, exist_ok=True)
        fname = get_fname_from_prompt(prompt)
        fpath = os.path.join(desktop, fname)
        url = generate_image(prompt)
        download_image(url, fpath)
        self.button.config(state="normal")
        self.progress.config(text=f"Image saved to {fpath}", wraplength=self.winfo_width())




if __name__ == "__main__":
    root = tk.Tk()
    app = MyApplication(root)
    app.pack()
    root.mainloop()