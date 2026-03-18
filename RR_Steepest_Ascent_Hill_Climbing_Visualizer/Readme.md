# Steepest Ascent Hill Climbing Visualization

This project demonstrates the **Steepest Ascent Hill Climbing algorithm with Random Restart** using a graphical interface in Python.

The algorithm searches for the maximum value of a mathematical function and visualizes each step on a graph.

---

## 📌 Features

- Steepest Ascent Hill Climbing
- Random Restart mechanism
- Graphical visualization using matplotlib
- Interactive Start and Exit buttons
- Displays best solution found after all restarts

---

## 🧠 Problem Description

We are maximizing the function:

f(x) = -(x - 3)^2 + 9

This is a parabola with a global maximum at:
- **x = 3**
- **f(x) = 9**

The algorithm tries to reach this maximum starting from random points.

---

## 📂 Project Structure


project-folder/
│
├── main.py # Main algorithm + GUI control
├── gui.py # Graph plotting and interface
├── Function.py # Function definition
└── README.md


---

## ▶️ How to Run

1. Make sure Python is installed
2. Install required libraries:


pip install matplotlib numpy


3. Run the program:


python main.py


---

## 🎮 How It Works

- Click **Start** → Runs one restart of hill climbing
- Each restart:
  - Picks a random starting point
  - Moves step-by-step toward better values
  - Stops when no better neighbor is found

- Graph shows:
  - Blue curve → Function
  - Red line → Path taken by algorithm

- After all restarts:
  - Best solution is printed in console

---

## 🔁 Random Restart

- Total restarts: 10
- Helps avoid getting stuck in local maxima
- Keeps track of the best overall solution

---

## ⚙️ Parameters

- Step size: `0.1`
- Range: `-10 to 10`
- Restarts: `10`

---

## 📊 Output Example


Start: -4.23 Final: 2.98 Value: 8.99
Start: 6.12 Final: 3.01 Value: 9.00


---

## 🎯 Learning Purpose

This project helps understand:
- Local Search Algorithms
- Hill Climbing behavior
- Importance of Random Restart
- Visualization of optimization

---

## 👤 Author

GhulamMohyuddin