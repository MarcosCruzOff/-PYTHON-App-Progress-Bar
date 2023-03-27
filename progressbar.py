import tkinter as tk
from tkinter import ttk

def update_progress():
    try:
        value = int(entry_var.get())
        progress["maximum"] = value
        progress["value"] = 0
        root.after(1000, increment_progress)
    except ValueError:
        pass

def increment_progress():
    value = progress["value"]
    maximum = progress["maximum"]
    if value < maximum:
        progress["value"] = value + speed_factor.get()
        root.after(1000 // speed_factor.get(), increment_progress)

def increment_speed():
    global speed_factor
    speed_factor.set(min(speed_factor.get() * 2, 4))

def decrement_speed():
    global speed_factor
    speed_factor.set(max(speed_factor.get() // 2, 1))

root = tk.Tk()
root.title("Barra de Progresso")

entry_var = tk.StringVar()
entry_var.trace_add("write", lambda *args: update_progress())
entry = ttk.Entry(root, textvariable=entry_var)
entry.pack(pady=10)

speed_factor = tk.IntVar(value=1)

progress = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress.pack(pady=10)

increment_button = ttk.Button(root, text="Incrementar", command=increment_speed)
increment_button.pack(side="left", padx=10)

decrement_button = ttk.Button(root, text="Decrementar", command=decrement_speed)
decrement_button.pack(side="right", padx=10)

root.mainloop()
