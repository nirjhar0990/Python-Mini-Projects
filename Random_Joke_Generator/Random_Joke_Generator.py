import tkinter as tk
import os,sys
from tkinter import messagebox
import requests


def get_joke():
    try:
        url = "https://official-joke-api.appspot.com/random_joke"

        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            data = response.json()

            setup = data["setup"]
            punchline = data["punchline"]

            joke_label.config(text=setup)
            answer_label.config(text=punchline)

        else:
            messagebox.showerror(
                "Error",
                "Unable to get a joke from the server."
            )

    except requests.exceptions.RequestException:
        messagebox.showerror(
            "Internet Error",
            "Please check your internet connection."
        )


def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.abspath("."))
    return os.path.join(base_path, relative_path)


# Create window
root = tk.Tk()

root.title("Random Joke Generator")
root.geometry("600x400")
root.resizable(False, False)
root.iconbitmap(resource_path("tongue.ico"))


# Title
title_label = tk.Label(
    root,
    text="😂 Random Joke Generator",
    font=("Arial", 22, "bold")
)

title_label.pack(pady=30)


# Joke
joke_label = tk.Label(
    root,
    text="Click the button to get a random joke!",
    font=("Arial", 14),
    wraplength=500,
    justify="center"
)

joke_label.pack(pady=30)


# Punchline
answer_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "italic"),
    wraplength=500,
    justify="center"
)

answer_label.pack(pady=20)


# Button
joke_button = tk.Button(
    root,
    text="🎲 Get Random Joke",
    font=("Arial", 14, "bold"),
    command=get_joke
)

joke_button.pack(pady=30)


# Start application
root.mainloop()
