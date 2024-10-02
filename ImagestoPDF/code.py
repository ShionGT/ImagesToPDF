import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

def download_pdf():
    images_path = images_path_entry.get()
    download_path = pdf_path_entry.get()

    if not images_path:
        messagebox.showerror("Error", "Please select the images path")
        return
    if not download_path:
        messagebox.showerror("Error", "Please select a download path.")
        return

    # Convert images to PDF
    images = []

    for file in sorted(os.listdir(images_path)):
        if file.split('.')[-1] in ('png', 'jpg', 'jpeg'):
            image = Image.open(os.path.join(images_path, file))
            image_converted = image.convert('RGB')
            images.append(image_converted)
    if len(images) == 0:
        messagebox.showerror("Error", "No images found.")
        return

    images[0].save(download_path + "/merged.pdf", save_all=True, append_images=images)

def browse_images_path():
    selected_path = filedialog.askdirectory()
    if selected_path:
        images_path_entry.delete(0, tk.END)
        images_path_entry.insert(0, selected_path)

def browse_pdf_path():
    selected_path = filedialog.askdirectory()
    if selected_path:
        pdf_path_entry.delete(0, tk.END)
        pdf_path_entry.insert(0, selected_path)

app = tk.Tk()
app.title("Images to PDF Converter")

# IMPORT
tk.Label(app, text="Images Path:").grid(row=0, column=0, padx=10, pady=10)
images_path_entry = tk.Entry(app, width=50)
images_path_entry.grid(row=0, column=1, padx=10, pady=10)

browse_button = tk.Button(app, text="Browse", command=browse_images_path)
browse_button.grid(row=0, column=2, padx=10, pady=10)

# DOWNLOAD
tk.Label(app, text="Download Path:").grid(row=1, column=0, padx=10, pady=10)
pdf_path_entry = tk.Entry(app, width=50)
pdf_path_entry.grid(row=1, column=1, padx=10, pady=10)

browse_button = tk.Button(app, text="Browse", command=browse_pdf_path)
browse_button.grid(row=1, column=2, padx=10, pady=10)

download_button = tk.Button(app, text="Convert", command=download_pdf, bg="green", fg="white")
download_button.grid(row=2, column=1, padx=10, pady=20)

app.mainloop()
