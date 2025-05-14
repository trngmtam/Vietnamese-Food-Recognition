import tkinter as tk
from database_setup import get_dish_data

def open_calorie_panel(parent_window, dish_name, size_factor):
    parent_window.destroy()

    data = get_dish_data(dish_name)
    if not data:
        tk.messagebox.showerror("Error", f"No data found for {dish_name}")
        return

    ingredients = data[1].split(",")
    calories = int(data[2] * size_factor)
    weights = [int(float(w) * size_factor) for w in data[3].split(",")]

    window = tk.Tk()
    window.title("Calorie Table")
    window.geometry("500x400")

    tk.Label(window, text=f"Dish: {dish_name} ({'Small' if size_factor==0.5 else 'Large' if size_factor==2 else 'Medium'})", font=("Arial", 16)).pack(pady=10)

    frame = tk.Frame(window)
    frame.pack(pady=10)

    headers = ["Ingredient", "Weight (g)"]
    for col, text in enumerate(headers):
        tk.Label(frame, text=text, borderwidth=1, relief="solid", width=20).grid(row=0, column=col)

    for i, (ingredient, weight) in enumerate(zip(ingredients, weights)):
        tk.Label(frame, text=ingredient, borderwidth=1, relief="solid", width=20).grid(row=i+1, column=0)
        tk.Label(frame, text=weight, borderwidth=1, relief="solid", width=20).grid(row=i+1, column=1)

    tk.Label(window, text=f"Total Calories: {calories} kcal", font=("Arial", 14)).pack(pady=20)

    window.mainloop()
