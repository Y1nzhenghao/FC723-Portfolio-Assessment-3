# main.(third draft)
"""
Scientific Calculator - Third Version.
This version implements a fully functional calculator with
basic arithmetic operations and trigonometric functions.
"""


import tkinter as tk   # Import GUI framework.
from tkinter import messagebox
from arithmetic import Arithmetic   # Import the plus,minus,times,and divide module.
from triangle_function import Trigonometry   # Import the Trigonometric module.
from power_root import PowerRoot   # Import the Squares and square roots module.

class CalculatorApp:
    """
    A fully functional scientific calculator with a GUI.
    """
    def __init__(self,root):
       """
       Initialize the calculator application.
       :param root: Tkinter root window object
       """
       self.root = root
       self.root.title("Scientific Calculator")   # Set the title of the window.
       self.root.geometry("500x500")   # Set the first size of window(I need to test).
       # Initialize the mathematic operate module.
       self.arithmetic = Arithmetic()
       self.triangle_function = Trigonometry()
       self.power_root = PowerRoot()
       
       # Create the input.
       self.entry = tk.Entry(root,width=20,font=("Arial",24),borderwidth=2,relief="solid")
       self.entry.grid(row=0,column=0,columnspan=4,pady=10)
        
       # Create buttons.
       self.create_buttons()
        
    def create_buttons(self):
       """Creates all buttons and their functionality."""
       buttons = [
            ("7",1,0),("8",1,1),("9",1,2),("+",1,3),
            ("4",2,0),("5",2,1),("6",2,2),("-",2,3),
            ("1",3,0),("2",3,1),("3",3,2),("*",3,3,),
            ("0",4,0),(".",4,1),("=",4,2),("/",4,3),
           ("c",5,3),("sin",5,0),("cos",5,1),("tan",5,2),
           ("asin",6,0),("acos",6,1),("atan",6,2),("√",6,3),
           ("xˆ2",7,0)
           ]
       for (text,row,col) in buttons:
            button = tk.Button(self.root,text=text,width=10,height=2,font=("Arial",14),
                              command=lambda t=text:self.on_button_click(t))
            button.grid(row=row,column=col,padx=5,pady=5)
            
    def on_button_click(self,button_text):
        """Handles button click events."""
        if button_text == "=":
            self.calculate_result()
        elif button_text == "c":
            self.entry.delete(0,tk.END)
        else:
            self.entry.insert(tk.END,button_text)
            
def main():
    """
    Main function to initialize the calculator application.
    """
    root = tk.Tk()   # Create the tkinter window.
    app = CalculatorApp(root)   # Create a calculator application instance.
    root.mainloop()   # Run the Tkinter main loop.
    
if __name__ == "__main__":
    main()