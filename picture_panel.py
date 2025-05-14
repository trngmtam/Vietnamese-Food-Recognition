import tkinter as tk
from PIL import ImageTk, Image
from calorie_panel import open_calorie_panel
from model_handler import predict_dish

def open_picture_panel(image_path, parent_root):
    parent_root.destroy()

    new_window = tk.Tk()
    new_window.title("Preview Image")
    new_window.geometry("800x600")

    img = Image.open(image_path)
    img = img.resize((600, 400))
    photo = ImageTk.PhotoImage(img)

    img_label = tk.Label(new_window, image=photo)
    img_label.image = photo
    img_label.pack(pady=10)

    def on_size_selected(size):
        detected_dish = predict_dish(image_path)
        open_calorie_panel(new_window, detected_dish, size)

    tk.Label(new_window, text="Choose your serving size", font=("Arial", 14)).pack(pady=10)

    sizes = [("Small", 0.5), ("Medium", 1), ("Large", 2)]
    for text, factor in sizes:
        tk.Button(new_window, text=text, command=lambda f=factor: on_size_selected(f)).pack(pady=5)

    new_window.mainloop()
