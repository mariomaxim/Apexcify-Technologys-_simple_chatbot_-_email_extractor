import tkinter as tk
from tkinter import filedialog, messagebox
import re

def extract_emails_logic(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            text = f.read()
        
        emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)
        
        with open(output_file, 'w') as f:
            for email in emails:
                f.write(email + '\n')
        
        return f"Successfully extracted {len(emails)} emails to {output_file}"
    except FileNotFoundError:
        return f"Error: The file {input_file} was not found."
    except Exception as e:
        return f"An error occurred: {e}"

class EmailExtractorApp:
    def __init__(self, master):
        self.master = master
        master.title("Email Extractor")

        self.input_file_path = tk.StringVar()
        self.output_file_name = tk.StringVar(value="extracted_emails.txt")

        # Input File Selection
        tk.Label(master, text="Input File:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        tk.Entry(master, textvariable=self.input_file_path, width=50).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(master, text="Browse", command=self.browse_input_file).grid(row=0, column=2, padx=5, pady=5)

        # Output File Name
        tk.Label(master, text="Output File Name:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        tk.Entry(master, textvariable=self.output_file_name, width=50).grid(row=1, column=1, padx=5, pady=5)

        # Extract Button
        tk.Button(master, text="Extract Emails", command=self.extract_emails).grid(row=2, column=1, pady=10)

    def browse_input_file(self):
        file_path = filedialog.askopenfilename(
            title="Select Input Text File",
            filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
        )
        if file_path:
            self.input_file_path.set(file_path)

    def extract_emails(self):
        input_file = self.input_file_path.get()
        output_file = self.output_file_name.get()

        if not input_file:
            messagebox.showwarning("Warning", "Please select an input file.")
            return
        
        if not output_file:
            messagebox.showwarning("Warning", "Please enter an output file name.")
            return

        result_message = extract_emails_logic(input_file, output_file)
        messagebox.showinfo("Extraction Result", result_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = EmailExtractorApp(root)
    root.mainloop()

