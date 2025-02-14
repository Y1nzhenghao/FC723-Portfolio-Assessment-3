
# main.(first draft)
"""
Scientific Calculator - First Draft
This first draft introduced tkinter and the Arithmetic module (Arithmetic, Trigonometry, PowerRoot).
Build a basic CalculatorApp class without implementing buttons or calculation logic for now
"""

import tkinter as tk   # Import GUI framework.
from arithmetic import Arithmetic   # Import the plus,minus,times,and divide module.
from triangle_function import Trigonometry   # Import the Trigonometric module.
from power_root import PowerRoot   # Import the Squares and square roots module.

class CalculatorApp:
    """
    A basic framework for the calculator GUI.
    """
    
    def __init__(self,root):
        """
        Initialize the application window.
        :param root: Tkinter root window object
        """
        self.root = root
        self.root.title("Scientific Calculator")   # Set the title of the window.
        self.root.geometry("400x600")   # Set the first size of window(I need to test).
        
        # Initialize the mathematic operate module.
        self.arithmetic = Arithmetic()
        self.triangle_function = Trigonometry()
        self.power_root = PowerRoot()
        
def main():
    """
    Main function to initialize the calculator application.
    """
    root = tk.Tk()   # Create the tkinter window.
    app = CalculatorApp(root)   # Create a calculator application instance.
    root.mainloop()   # Run the Tkinter main loop.
    
if __name__ == "__main__":
    main()