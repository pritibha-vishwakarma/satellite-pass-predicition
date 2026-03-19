import subprocess
import time

print("🚀 Starting Project...")

# Step 1: Run main.py
print("📡 Running main.py (data processing)...")
subprocess.run(["python", "main.py"])

# Small delay
time.sleep(2)

# Step 2: Start API
print("🌐 Starting API server...")
subprocess.run(["uvicorn", "api:app", "--reload"])