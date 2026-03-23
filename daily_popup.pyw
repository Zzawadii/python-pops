import tkinter as tk
from tkinter import font
from pathlib import Path
from datetime import date
import random

# ==========================
# 1. Quotes / Bible Verses
# ==========================
quotes = [
    "🔹Don't strive to be superior to others; strive to be better than you were yesterday",
    "✨NEVER allow failure to be an option",
    "🔹you can't change how ppl feel aobut u, so don't try just to be as they wish , justlive ur life and be HAPPY!",
    "✨The only true wisdom is in knowing you know nothing",
    "🔹One day you will sit and be glad you didn't give up",
    "✨Believe in yourself and all that you are",
    "🔹Mistakes are proof that you are trying",
    "✨The greatest weapon against stress in ur ability to choose one thought over another",

    "🔹Many of life’s failures are people who did not realize how close they were to success when they gave up."
]

# ==========================
# 2. Check if popup already shown today
# ==========================
log_file = Path.home() / "daily_popup_log.txt"
today_str = str(date.today())

if log_file.exists():
    with open(log_file, "r") as f:
        last_date = f.read().strip()
    if last_date == today_str:
        exit()  # Exit if already shown today

with open(log_file, "w") as f:
    f.write(today_str)

# ==========================
# 3. Pick quote of the day
# ==========================
index = date.today().toordinal() % len(quotes)
quote_of_the_day = quotes[index]

# ==========================
# 4. Create Tkinter popup
# ==========================
root = tk.Tk()
root.title("🌞 Daily Motivation")
root.geometry("600x350")  # Slightly wider for long quotes
root.resizable(False, False)

# ==========================
# 4a. Layout Frames
# ==========================
main_frame = tk.Frame(root, bg="#FFCCCC", bd=5, relief="ridge")
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

title_frame = tk.Frame(main_frame, bg="#FFCCCC")
title_frame.pack(fill="x", pady=(10, 5))

quote_frame = tk.Frame(main_frame, bg="#FFCCCC")
quote_frame.pack(fill="both", expand=True, pady=10)

btn_frame = tk.Frame(main_frame, bg="#FFCCCC")
btn_frame.pack(fill="x", pady=(0, 10), anchor="e")

# ==========================
# 4b. Create Widgets
# ==========================
# Title
title_label = tk.Label(title_frame, text="💡 Daily Wisdom 💡",
                       font=("Comic Sans MS", 18, "bold"), fg="white", bg="#FFCCCC")
title_label.pack()

# Quote
quote_label = tk.Label(quote_frame, text=quote_of_the_day,
                       font=("Georgia", 14), fg="black", bg="#FFCCCC",
                       wraplength=550, justify="center")
quote_label.pack(expand=True, padx=20, pady=10)

# Close Button
btn = tk.Button(btn_frame, text="Close ✖", command=root.destroy,
                bg="#FF4500", fg="white", font=("Helvetica", 12, "bold"),
                activebackground="#FF6347", activeforeground="white")
btn.pack(side="right", padx=20)

# ==========================
# 4c. Animated background
# ==========================
bg_colors = ["#FFB6C1", "#87CEFA", "#90EE90",
             "#FFFACD", "#FFA07A", "#E6E6FA", "#FFD700"]


def animate_bg():
    color = random.choice(bg_colors)
    main_frame.configure(bg=color)
    title_frame.configure(bg=color)
    quote_frame.configure(bg=color)
    btn_frame.configure(bg=color)
    title_label.configure(bg=color)
    quote_label.configure(bg=color)
    root.after(1000, animate_bg)


animate_bg()

# ==========================
# 5. Run popup
# ==========================
root.mainloop()
