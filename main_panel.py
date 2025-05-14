import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
import os
from picture_panel import open_picture_panel

selected_file = None

def upload_image():
    global selected_file
    selected_file = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png *.pdf")])

def take_picture():
    import cv2
    cam = cv2.VideoCapture(1)
    ret, frame = cam.read()
    if ret:
        cv2.imwrite("captured_image.jpg", frame)
    cam.release()
    global selected_file
    selected_file = "captured_image.jpg"

def on_enter_key(event, root):
    if not selected_file:
        messagebox.showerror("No File Selected", "Please upload or capture a dish image first.")
        return
    open_picture_panel(selected_file, root)

def open_main_panel():
    root = tk.Tk()
    root.title("Food Detection - Calories Calculation")
    root.geometry("500x400")

    title = tk.Label(root, text="Food Detection - Calories Calculation", font=("Arial", 18))
    title.pack(pady=20)

    upload_btn = tk.Button(root, text="Upload Image", command=upload_image)
    upload_btn.pack(pady=10)

    capture_btn = tk.Button(root, text="Take a picture", command=take_picture)
    capture_btn.pack(pady=10)

    root.bind('<Return>', lambda event: on_enter_key(event, root))
    root.mainloop()

if __name__ == "__main__":
    open_main_panel()
