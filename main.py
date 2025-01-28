import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_filename):
    """Merge multiple PDFs into a single PDF."""
    merger = PdfMerger()

    for pdf in pdf_list:
        if os.path.exists(pdf):
            merger.append(pdf)
        else:
            print(f"Warning: File '{pdf}' not found and will be skipped.")

    # Write the merged PDF to the specified output file
    merger.write(output_filename)
    merger.close()

    print(f"Merged PDF saved as '{output_filename}'.")

def add_files():
    """Open file dialog to select PDFs and add them to the list."""
    files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    for file in files:
        if file not in pdf_files:
            pdf_files.append(file)
            listbox.insert(tk.END, file)

def merge_and_save():
    """Merge the selected PDFs and save the output."""
    if not pdf_files:
        messagebox.showwarning("No PDFs", "Please add PDF files to merge.")
        return

    output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if not output_file:
        return

    merge_pdfs(pdf_files, output_file)
    messagebox.showinfo("Success", f"Merged PDF saved as '{output_file}'.")

# Initialize GUI
app = tk.Tk()
app.title("PDF Merger")
app.geometry("600x400")

pdf_files = []

# Add UI Elements
frame = tk.Frame(app)
frame.pack(pady=10)

add_button = tk.Button(frame, text="Add PDFs", command=add_files)
add_button.pack(side=tk.LEFT, padx=5)

merge_button = tk.Button(frame, text="Merge PDFs", command=merge_and_save)
merge_button.pack(side=tk.LEFT, padx=5)

listbox = tk.Listbox(app, selectmode=tk.SINGLE, width=80, height=15)
listbox.pack(pady=10)

# Run the application
app.mainloop()