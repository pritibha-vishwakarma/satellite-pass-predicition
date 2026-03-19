import os
print(os.listdir())

from fetch import fetch
from propagator import get_positions
from pass_predictor import detect_passes
from database import create_db, insert_pass

def run():
    print("Starting Satellite Pass Detection...")

    # Step 1: Create DB
    create_db()

    # Step 2: Fetch satellites
    satellites = fetch()
    print("Satellites fetched:", len(satellites))

    # Step 3: Process few satellites (for testing)
    for sat in satellites[:3]:
        print("Processing:", sat["name"])

        # Step 4: Get positions
        positions = get_positions(sat["line1"], sat["line2"])

        # Step 5: Detect passes
        passes = detect_passes(positions)

        # Step 6: Store in DB
        for p in passes:
            insert_pass(sat["name"], p["start"], p["end"])

    print("Process completed!")


# RUN
if __name__ == "__main__":
    run()