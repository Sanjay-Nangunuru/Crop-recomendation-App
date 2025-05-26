import tkinter as tk
from tkinter import messagebox
from crop_predictor import recommend_crop

def on_submit():
    try:
        temp = float(entry_temp.get())
        humidity = float(entry_humidity.get())
        soil = entry_soil.get()
        crop = recommend_crop(temp, humidity, soil)
        messagebox.showinfo("Recommended Crop", f"Suggested Crop: {crop}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Crop Recommendation System")

tk.Label(root, text="Temperature (°C)").pack()
entry_temp = tk.Entry(root)
entry_temp.pack()

tk.Label(root, text="Humidity (%)").pack()
entry_humidity = tk.Entry(root)
entry_humidity.pack()

tk.Label(root, text="Soil Type (e.g., loamy)").pack()
entry_soil = tk.Entry(root)
entry_soil.pack()

tk.Button(root, text="Recommend Crop", command=on_submit).pack(pady=10)

root.mainloop()
