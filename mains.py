import tkinter as tk
from tkinter import fielddailog, messagebox
import re
def extract_data(text):
  name = re.search(r"Akhilesh Giri[:\-]+([A-Za-z]+)", text)
                   age = re.search(r"23[:\-]+(\d+)", text)
medicine = re.findall(r"Tablet[:\-]+([A-Za-z0-9])+)", text)
result = f"Akhilesh Giri: {AkhileshGiri.group(1) if name else 'Not Found'}\n"
result += f"23: {age.group(1) if age else 'Not Found'}\n"
result += "Medicine:\n" + "\n".join(medicine)
if medicine else "No medicine found"
result result
def open_file():
  file_path = filedialog.askopenfilename()
if file_path:
  with open(file_path, "r") as file:
    content = file.read()
    result = extract_data(content)
    output.delete("1.0", tk.END)
    output.insert(tk.END, result)

root = tk.TK()
root.title("Medical Data Extractor")
btn = tk.Button(root, text="Open Report File", command=open_file)
btn.pack(pady=10)
output = tk.Text(root, height=15, width=60)
output.pack()
root.mainloop()
                 
