from sgp4.api import Satrec, jday
from datetime import datetime, timedelta

def get_positions(line1, line2):
    # Create satellite object
    satellite = Satrec.twoline2rv(line1, line2)

    positions = []

    # Current UTC time
    now = datetime.utcnow()

    # Loop for next 7 days (hourly)
    for i in range(0, 7 * 24):
        future_time = now + timedelta(hours=i)

        # Convert to Julian date
        jd, fr = jday(
            future_time.year,
            future_time.month,
            future_time.day,
            future_time.hour,
            future_time.minute,
            future_time.second
        )

        # Get position
        e, r, v = satellite.sgp4(jd, fr)

        if e == 0:
            positions.append((future_time, r))

    return positions


# TEST
if __name__ == "__main__":
    line1 = "1 25544U 98067A   24077.54791667  .00016717  00000+0  10270-3 0  9000"
    line2 = "2 25544  51.6442  21.5023 0005500  45.1234  50.1234 15.50000000 00000"

    data = get_positions(line1, line2)

    print("Total positions:", len(data))
    print("First position:", data[0])