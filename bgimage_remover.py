import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from rembg import remove
from tkinter import messagebox
import os

def open_image():
    global input_path
    input_path = filedialog.askopenfilename()
    if input_path:
        try:
            # Open and display the original image
            img = Image.open(input_path)
            img.thumbnail((300, 300))  # Resize for display
            photo = ImageTk.PhotoImage(img)
            original_label.config(image=photo)
            original_label.image = photo
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open image: {e}")

def remove_background():
    global input_path, output_image
    if input_path:
        try:
            # Remove background
            with open(input_path, 'rb') as i:
                with Image.open(i) as input:
                    output_image = remove(input)

            # Display the processed image
            output_image.thumbnail((500, 500))
            photo = ImageTk.PhotoImage(output_image)
            processed_label.config(image=photo)
            processed_label.image = photo
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process image: {e}")

def download_image():
    global output_image
    if output_image:
        try:
            save_path = filedialog.asksaveasfilename(defaultextension=".png")
            if save_path:
                output_image.save(save_path)
                messagebox.showinfo("Success", "Image downloaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to download image: {e}")

# Create main window
window = tk.Tk()
window.title("Background Remover")

# Buttons
open_button = tk.Button(window, text="Open Image", command=open_image)
open_button.pack(pady=10)

remove_button = tk.Button(window, text="Remove Background", command=remove_background)
remove_button.pack(pady=10)

download_button = tk.Button(window, text="Download Image", command=download_image)
download_button.pack(pady=10)

# Labels for images
original_label = tk.Label(window)
original_label.pack(side=tk.LEFT, padx=10)

processed_label = tk.Label(window)
processed_label.pack(side=tk.RIGHT, padx=10)

# Initialize output_image
output_image = None

window.mainloop()