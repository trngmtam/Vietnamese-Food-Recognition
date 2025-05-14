import tkinter as tk
from tkinter import messagebox
from database_setup import get_full_dish_data, get_total_calories

def open_calorie_panel(parent_window, dish_name, size_factor):
    parent_window.destroy()

    data = get_full_dish_data(dish_name)
    if not data:
        messagebox.showerror("Error", f"No data found for {dish_name}")
        return

    total_calories = get_total_calories(dish_name)
    total_calories = int(total_calories * size_factor)

    window = tk.Tk()
    window.title("Calorie Table")
    window.geometry("1100x500")  # adjusted width to fit the wider 'Notes' column

    tk.Label(window, text=f"Dish: {dish_name} ({'Small' if size_factor==0.5 else 'Large' if size_factor==2 else 'Medium'})", font=("Arial", 16)).pack(pady=10)

    frame = tk.Frame(window)
    frame.pack(pady=10)

    headers = ["Ingredient", "Weight (g)", "Calories", "Notes"]
    for col, text in enumerate(headers):
        width = 40 if col == 3 else 20
        tk.Label(frame, text=text, borderwidth=1, relief="solid", width=width).grid(row=0, column=col)

    for i, row in enumerate(data):
        ingredient = row[1]
        weight  = int(row[2] * size_factor)
        cal     = int(row[3] * size_factor)
        notes   = row[4] or "-"

        tk.Label(frame, text=ingredient, borderwidth=1, relief="solid", width=20).grid(row=i+1, column=0)
        tk.Label(frame, text=weight,     borderwidth=1, relief="solid", width=20).grid(row=i+1, column=1)
        tk.Label(frame, text=cal,        borderwidth=1, relief="solid", width=20).grid(row=i+1, column=2)
        tk.Label(frame, text=notes,      borderwidth=1, relief="solid", width=40).grid(row=i+1, column=3)

    tk.Label(window, text=f"Total Calories: {total_calories} kcal", font=("Arial", 14)).pack(pady=20)

    def back_to_menu():
        window.destroy()
        import main_panel
        main_panel.open_main_panel()

    tk.Button(window,
              text="Back to Menu",
              command=back_to_menu,
              width=20,
              height=2
    ).pack(pady=10)

    window.mainloop()
