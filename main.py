# main.(Second draft)
"""
Scientific Calculator - Second Draft
This version adds a Tkinter entry field for user input and 
basic button layout.
"""


import tkinter as tk   # Import GUI framework.
from arithmetic import Arithmetic   # Import the plus,minus,times,and divide module.
from triangle_function import Trigonometry   # Import the Trigonometric module.
from power_root import PowerRoot   # Import the Squares and square roots module.

class CalculatorApp:
    """
    A calculator GUI application with an input field and button layout.
    """
    def __init__(self,root):
       """
       Initializes the application window with an input field and buttons.
       :param root: Tkinter root window object
       """
       self.root = root
       self.root.title("Scientific Calculator")   # Set the title of the window.
       self.root.geometry("500x300")   # Set the first size of window(I need to test).
       # Initialize the mathematic operate module.
       self.arithmetic = Arithmetic()
       self.triangle_function = Trigonometry()
       self.power_root = PowerRoot()
       
       # Create the input.
       self.entry = tk.Entry(root,width=20,font=("Arial",24),borderwidth=2,relief="solid")
       self.entry.grid(row=0,columnspan=4,pady=10)
        
       # Create buttons.
       self.create_buttons()
        
    def create_buttons(self):
        """
        Creates buttons for numbers and operations, but does not yet implement functionality.
        """
        buttons = [
            ("7",1,0),("8",1,1),("9",1,2),("+",1,3),
            ("4",2,0),("5",2,1),("6",2,2),("-",2,3),
            ("1",3,0),("2",3,1),("3",3,2),("*",3,3,),
            ("0",4,0),(".",4,1),("=",4,2),("/",4,3)
            ]
        for (text,row,col) in buttons:
            button = tk.Button(self.root,text=text,width=10,height=2,font=("Arial",14))
            button.grid(row=row,column=col,padx=5,pady=5)
            
def main():
    """
    Main function to initialize the calculator application.
    """
    root = tk.Tk()   # Create the tkinter window.
    app = CalculatorApp(root)   # Create a calculator application instance.
    root.mainloop()   # Run the Tkinter main loop.
    
if __name__ == "__main__":
    main()