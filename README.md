# Satellite Pass Prediction System

## About Project
This project is about tracking satellites and finding when they pass over a location.

I fetch satellite data from Celestrak website. Then I use SGP4 algorithm to calculate where the satellite will be in future. After that, I check when the satellite comes close to a location (pass detection).

Finally, I store this data in a database and show it using an API.

---

## Features
- Fetch satellite data (TLE)
- Calculate satellite position
- Detect passes
- Store data in database
- Show data using API

---

## Technologies Used
- Python
- SGP4
- SQLite
- FastAPI

---

## How to Run

1. Install required libraries:
pip install sgp4 requests fastapi uvicorn

2. Run main file:
python main.py

3. Run API:
uvicorn api:app --reload

4. Open in browser:
http://127.0.0.1:8000/passes

---

## Output
The API shows satellite name, start time, and end time of pass.

---

## Note
This is a basic implementation. Logic can be improved for more accurate results.
