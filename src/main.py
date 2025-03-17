import time
import threading
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb  # Modern UI Library
from pynput import mouse, keyboard
import os
import platform

# Cross-platform sound support
if platform.system() == "Windows":
    import winsound
    def play_sound(file):
        winsound.PlaySound(file, winsound.SND_FILENAME)
else:
    from playsound import playsound
    def play_sound(file):
        playsound(file)

# Constants
WORK_DURATION = 20 * 60  # 20 minutes in seconds
BREAK_DURATION = 20  # 20 seconds

# Sound files (Replace with actual sound paths if needed)
ALERT_SOUND = "./assets/game-bonus-2-294436.wav"  # Plays after 20 min
BREAK_DONE_SOUND = "./assets/computer-startup-sound-effect-312870.wav"  # Plays after 20 sec

# Icon file (Provide your .ico file here)
ICON_PATH = "./assets/icon.ico"

class TwentyTwentyTwentyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("20-20-20 Reminder")
        self.root.geometry("400x250")
        self.root.resizable(False, False)
        self.style = tb.Style(theme="darkly")  # Modern dark theme

        # Set icon for Windows
        if os.path.exists(ICON_PATH):
            self.root.iconbitmap(ICON_PATH)

        # Labels
        self.label = tb.Label(root, text="Monitoring activities...", font=("Arial", 14, "bold"))
        self.label.pack(pady=15)

        # Progress Bar
        self.progress = tb.Progressbar(root, length=300, mode="determinate")
        self.progress.pack(pady=10)

        # Timer Variables
        self.time_left = WORK_DURATION  # Start with 20 minutes countdown
        self.break_time_left = 0
        self.on_break = False  # Flag to track if break is active

        # Start countdown automatically
        self.update_timer()

    def update_timer(self):
        """Updates the 20-minute countdown timer with progress bar."""
        if self.time_left > 0:
            minutes = self.time_left // 60
            seconds = self.time_left % 60
            self.label.config(text=f"Time left: {minutes:02d}:{seconds:02d}", foreground="white")

            self.progress["value"] = ((WORK_DURATION - self.time_left) / WORK_DURATION) * 100
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            play_sound(ALERT_SOUND)  # Play sound when 20 min is up
            self.start_break()

    def start_break(self):
        """Starts the 20-second break and monitors activity."""
        self.on_break = True
        self.label.config(text="🔔 Look 20 feet away for 20 sec!", foreground="yellow")
        self.break_time_left = BREAK_DURATION
        self.progress["value"] = 0

        def reset_if_active(*args):
            """Resets the 20-second timer if activity is detected."""
            if self.on_break:
                self.break_time_left = BREAK_DURATION
                self.label.config(text="🔴 Detected activity! Restarting 20 sec", foreground="red")

        # Start monitoring keyboard & mouse only for the break time
        self.mouse_listener = mouse.Listener(on_move=reset_if_active, on_click=reset_if_active)
        self.keyboard_listener = keyboard.Listener(on_press=reset_if_active)
        self.mouse_listener.start()
        self.keyboard_listener.start()

        self.break_countdown()

    def break_countdown(self):
        """Counts down for 20 seconds, resetting if activity is detected."""
        if self.break_time_left > 0:
            self.label.config(text=f"🔔 Look away! {self.break_time_left} sec left", foreground="yellow")
            self.progress["value"] = ((BREAK_DURATION - self.break_time_left) / BREAK_DURATION) * 100
            self.break_time_left -= 1
            self.root.after(1000, self.break_countdown)
        else:
            # End break and restart 20-minute countdown
            play_sound(BREAK_DONE_SOUND)  # Play sound when 20-sec break is done
            self.on_break = False
            self.time_left = WORK_DURATION
            self.label.config(text="Monitoring activities...", foreground="white")
            self.progress["value"] = 0
            self.update_timer()

# Run the GUI
root = tb.Window(themename="darkly")  # Modern UI
app = TwentyTwentyTwentyApp(root)
root.mainloop()
