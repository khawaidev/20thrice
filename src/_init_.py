from .main import TwentyTwentyTwentyApp

__version__ = "1.0.0"  # Define the package version
__author__ = "Khawai"  # Replace with your name

# Optional: A function to launch the app
def run():
    import ttkbootstrap as tb
    root = tb.Window(themename="darkly")
    app = TwentyTwentyTwentyApp(root)
    root.mainloop()
