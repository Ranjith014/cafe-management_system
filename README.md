Simple CLI Restaurant Ordering System
A basic command-line restaurant ordering system built with Python. This project allows users to select items from a predefined menu and calculates the total cost of their order.

Overview
This script is a straightforward demonstration of fundamental Python concepts.It's designed for beginners to understand how to work with dictionaries, handle user input, and use conditional logic (if/else statements) to build a simple interactive application.

Features
Menu Display: Greets the user and clearly displays the available menu items and their prices.
Sequential Ordering: Allows the user to order multiple items one after another.
Input Validation: Checks if the ordered item exists in the menu and provides feedback to the user if it doesn't.
Dynamic Bill Calculation: Keeps a running total of the order and displays the final amount to the user.

Getting Started
To run this project, you will need to have Python installed on your computer.

Prerequisites
Make sure you have Python 3 installed. You can check your Python version by running:

code
Sh
python --version

 Installation & Execution
Clone the repository or download the hotelmenu.py file to your local machine.
code
Sh
git clone <your-repository-url>
Or simply save the hotelmenu.py file.

Navigate to the project directory in your terminal.
code
Sh
cd path/to/your/project
Run the script.
code
Sh
python hotelmenu.py
The program will then start, display the menu, and prompt you for your order.
💻 Usage Example
Here is an example of a user interacting with the application:
code
Code
Welcome to our restaurant
Burger:Rs20
Pizza:Rs100
Pasta:Rs50
Salad:Rs70
Fries:Rs60
Drink:Rs40

Enter your 1st item:Pizza
your Pizza is added to your order
Do you want to order another item? (yes/no):yes
Enter your 2nd item:Drink
your Drink is added to your order
Do you want to order another item? (yes/no):no
the total amount of items to pay is 140
Thank you,visit again
🛠️ Technologies Used
Python: The core language used for the script.
