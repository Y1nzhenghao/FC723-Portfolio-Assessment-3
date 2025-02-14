# main.(final draft)
"""
Scientific Calculator - Final Version.
Added the calculate_result() method: to parse user input and calculate addition, 
subtraction, multiplication and division. calculate_function() method: For calculating
sin, cos, tan, asin, acos, atan, √, x² and other advanced operations and error 
handling: to prevent illegal input resulting in crash.
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
        """Initialize the calculator application."""
        self.root = root
        self.root.title("Scientific Calculator")   # Set the title of the window.
        self.root.geometry("500x600")   # Set the final size of window(after test).
        
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
            ("C",5,3),("sin",5,0),("cos",5,1),("tan",5,2),
            ("asin",6,0),("acos",6,1),("atan",6,2),("√",6,3),
            ("x²",7,0)
            ]
        for (text,row,col) in buttons:
            button = tk.Button(self.root,text=text,width=10,height=2,font=("Arial",14),
                               command=lambda t=text:self.on_button_click(t))
            button.grid(row=row,column=col,padx=5,pady=5)
            
    def on_button_click(self,button_text):
        """Handles button click events."""
        if button_text == "=":
            self.calculate_result()   # Compute the result.
        elif button_text == "C":
            self.entry.delete(0,tk.END)   # Clear the input.
        elif button_text in ["sin","cos","tan","asin","acos","atan","√","x²"]:
            self.calculate_function(button_text)  # Compute advanced math functions.
        else:
            self.entry.insert(tk.END,button_text)   # # Append input to the entry field.
    
    def calculate_result(self):
        """
        Evaluates the mathematical expression entered by the user.
        Uses eval() with a restricted environment to safely compute basic arithmetic operations.
        """
        try:
            expression = self.entry.get()   # Gets the expression entered by the user in the input field.
            
            # I learned that you can use the secure eval() to perform calculations, allowing only certain mathematical operations.
            # eval() is Python's built-in expression evaluation function that converts strings into mathematical operations and executes them.
            # Disable __builtins__ in eval(), making sure it can only execute the functions we define.
            result = eval(expression, {"__builtins__": {}}, {
                "add": self.arithmetic.add, "subtract": self.arithmetic.subtract,
                "multiply": self.arithmetic.multiply, "divide": self.arithmetic.divide
            })
        # Clear the input field and display the result
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)   
        
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")  # Handle invalid input.
            
            
    def calculate_function(self,func_name):
        """
        Computes advanced functions (trigonometric, power, square root).
        """
        try:
            value = float(self.entry.get())   # Convert input to float.
            result = None
            
            # Compute the corresponding math function.
            if func_name == "sin":
                result = self.triangle_function.sine(value)
            elif func_name == "cos":
                result = self.triangle_function.cosine(value)
            elif func_name == "tan":
                result = self.triangle_function.tangent(value)
            elif func_name == "asin":
                result = self.triangle_function.arcsine(value)
            elif func_name == "acos":
                result = self.triangle_function.arccosine(value)
            elif func_name == "atan":
                result = self.triangle_function.arctangent(value)
            elif func_name == "√":
                result = self.power_root.square_root(value)
            elif func_name == "x²":
                result = self.power_root.square(value)   
                
            # Display the result.
            self.entry.delete(0,tk.END)
            self.entry.insert(tk.END,result)
            
        except ValueError:
            messagebox.showerror("Error","Invalid input")   # Handle the error input.
            
def main():
    """
    Main function to initialize the calculator application.
    """
    root = tk.Tk()   # Create the tkinter window.
    app = CalculatorApp(root)   # Create a calculator application instance.
    root.mainloop()   # Run the Tkinter main loop.
    
if __name__ == "__main__":
    main()
