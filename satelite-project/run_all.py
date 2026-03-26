import subprocess
import time

print(" Starting Project...")

print(" Running main.py (data processing)...")
subprocess.run(["python", "main.py"])

time.sleep(2)

print(" Starting API server...")
subprocess.run(["uvicorn", "api:app", "--reload"])
