# Snowflake Streamlit Advisor App

## 🚀 Overview

This project is a simple interactive application built using **Streamlit inside Snowflake**.
It allows users to explore client-related data in a user-friendly way.

The app enables:

* Selecting a client
* Viewing their associated questions
* Clicking a question to see the corresponding answer

---

## 🧩 Features

* Interactive dropdown for client selection
* Dynamic retrieval of questions based on selected client
* Display of answers on user interaction
* Clean and simple UI using Streamlit

---

## 🛠️ Tech Stack

* Python
* Streamlit (Snowflake Native)
* Snowflake (Snowpark)
* SQL

---

## ⚙️ How It Works

1. The app runs inside Snowflake using Streamlit
2. A Snowpark session is used to connect to Snowflake
3. SQL queries fetch data from tables
4. Data is converted into Pandas DataFrames
5. Streamlit displays the data interactively

---

## 📊 Application Flow

User selects a client →
App fetches related questions →
User selects a question →
App displays the answer

---

## 📌 Key Learnings

Through this project, I learned:

* How to build UI using Streamlit (`selectbox`, display components)
* How to connect and interact with Snowflake using Snowpark
* How SQL, Python, and UI work together in real applications
* How to fetch, filter, and display data dynamically
* Basics of building data-driven applications

---

## ⚠️ Note

This application is built using **Streamlit in Snowflake**, so it runs within the Snowflake environment and uses an active Snowflake session.

---

## ▶️ Running the App

This app is designed to run inside Snowflake (Snowsight UI).
To run:

* Open Snowflake
* Navigate to Streamlit Apps
* Run the application

---

## 📌 Future Improvements

* Add search functionality
* Improve UI/UX design
* Handle multiple answers
* Add authentication and user roles

---
