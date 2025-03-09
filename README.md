# Calculator Application

## Overview
This is a simple calculator application built using Python and PyQt. It follows the Model-View-Controller (MVC) design pattern to separate concerns between the user interface (View), business logic (Model), and application control (Controller).

## Features
- Perform basic arithmetic operations: addition (+), subtraction (-), multiplication (*), and division (/)
- User-friendly graphical interface using PyQt
- Displays input and results in a QLineEdit field
- Reset functionality (C button) to clear the input
- Error handling for invalid expressions and division by zero

## Technologies Used
- Python
- PyQt for GUI development
- MVC architecture

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/bbzet/Calculator.git
   cd Calculator
   ```
2. Install dependencies:
   ```bash
   pip install PyQt6
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Usage
- Click the number buttons to enter digits.
- Click the operator buttons (+, -, *, /) to perform operations.
- Press the `=` button to calculate the result.
- Press `AC` to clear the input field.

## Project Structure
```
calculator-app/
│── main.py              # Entry point for the application
│── calculator.py        # Model: Handles the arithmetic logic
│── controller.py        # Controller: Manages input and user interactions
│── view.py              # View: Handles UI using PyQt
│── README.md            # Documentation
```

## Sample Input/Output
### Example 1:
**Input:** `4 + 10 =`
**Output:** `14`

### Example 2:
**Input:** `9 / 0 =`
**Output:** `Error`

## Screenshots
![](https://raw.githubusercontent.com/bbzet/Calculator/refs/heads/main/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-03-09%20141311.png)
![](https://raw.githubusercontent.com/bbzet/Calculator/refs/heads/main/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-03-09%20141317.png)
![](https://raw.githubusercontent.com/bbzet/Calculator/refs/heads/main/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-03-09%20141502.png)
![](https://raw.githubusercontent.com/bbzet/Calculator/refs/heads/main/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-03-09%20141507.png)




