📌 Project Overview

This project implements and visualizes different auction mechanisms using Python and a Flask-based web interface. Users can add bidders dynamically, choose an auction type, and observe the results in real time.

🧠 Implemented Auction Mechanisms

The simulator currently supports three standard auction formats:
English Auction (Open Ascending Bid)
Price increases step-by-step
Bidders drop out when price exceeds their valuation
Last remaining bidder wins
First-Price Sealed Bid Auction
Each bidder submits one sealed bid
Highest bidder wins and pays their own bid
Second-Price (Vickrey) Auction
Highest bidder wins
Winner pays the second-highest bid

🛠️ Tech Stack

Backend: Python, Flask

Frontend: HTML, Bootstrap, JavaScript

Version Control: Git & GitHub

📂 Project Structure
auction-simulator/
│
├── app.py                   # Flask web application
├── auction_simulator.py     # Core auction logic
├── templates/
│   └── index.html          # Frontend UI
└── README.md               # Project documentation

▶️ How to Run the Project
Step 1 — Install dependencies

Run in terminal:

pip install flask

Step 2 — Start the server
python app.py

Step 3 — Open in browser

Go to:

http://127.0.0.1:5000/

🎯 Features

Add multiple bidders dynamically
Choose auction type from dropdown
View formatted auction results in UI
Clean and responsive web interface
