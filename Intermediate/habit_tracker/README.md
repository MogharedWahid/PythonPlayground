# 📈 Python Practice Tracker using Pixela API
![Habit Tracker App](https://github.com/MogharedWahid/PythonPlayground/blob/main/Intermediate/habit_tracker/moghared_graph.jpg)
This project is a **Python-based habit tracker** that logs and visualizes how many hours you practice Python each day using the [Pixela API](https://pixe.la/).

It's a great mini-project for Python learners who want to explore real-world API interaction, JSON handling, HTTP methods, and data visualization.

---

## 🚀 Project Purpose

The goal of this project is to:

- **Track daily practice time** using a simple command-line interface.
- **Send data to an online graph** via Pixela API.
- **Visualize progress over time**, which is great for building and maintaining study habits.

---

## 🧰 Tools & Technologies Used

| Tool/Library | Purpose |
|--------------|---------|
| `Python` | Core programming language used |
| `datetime` | To generate the current date in required format |
| `requests` | For making HTTP requests to the Pixela API |
| `Pixela API` | Free service for tracking and visualizing daily activities as a graph |

---

## 📦 Features

- ✅ Create a Pixela user account (only needs to be done once)
- ✅ Create a visual graph to track progress (only needs to be done once)
- ✅ Input and log daily Python practice time
- ✅ Automatically formats the date and sends a "pixel" to Pixela
- ✅ Graph is updated in real-time and viewable in your browser

---

## 📝 How It Works

1. The script uses the `requests` module to send data to Pixela.
2. You are prompted to enter how many hours you practiced Python today.
3. The input is sent as a "pixel" to the graph with the current date.
4. You can view your graph online at:  
   `https://pixe.la/v1/users/YOUR_USERNAME/graphs/YOUR_GRAPH_ID.html`

---

## 📚 Lessons Learned

Working on this project helped me:

- Understand how REST APIs work (GET, POST, PUT).
- Practice using Python modules like `requests` and `datetime`.
- Learn how to format and send JSON data.
- Discover how to interact with external services and APIs.
- Build better project structure and readable code.

---
## 🔒 Disclaimer

Do not share your Pixela `TOKEN` publicly — it acts like a password for your account.

---

## 📌 Future Improvements

- Automate daily logging via a scheduled script
- Add options to update or delete pixels
- Track multiple habits or topics
- Create a GUI version using Tkinter or web frameworks
