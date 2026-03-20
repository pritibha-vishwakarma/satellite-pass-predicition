#  Satellite Pass Prediction

## About Project
This project is used to predict when a satellite will pass over a particular location.

It uses TLE (Two-Line Element) data to calculate satellite position and check visibility.

---

##  What it does
- Fetch satellite data (TLE)
- Calculate satellite position
- Detect when satellite is visible
- Store pass details like start time, end time and duration

---

##  Technologies Used
- Python
- Basic orbital calculation logic
- Database (SQLite)

---

##  Project Files
- fetch.py → gets satellite data  
- propagator.py → calculates position  
- pass_predictor.py → checks passes  
- database.py → stores data  
- main.py → runs the project  

---

##  How to run
1. Clone the project
git clone https://github.com/pritibha-vishwakarma/satellite-pass-predicition

2. Go to folder
cd satellite-pass-predicition

3. Run file
python main.py

---

##  Use
- Satellite tracking  
- Communication planning  
- Learning purpose  

---

##  Author
Pritibha Vishwakarma
