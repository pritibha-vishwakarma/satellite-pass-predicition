import requests

def fetch():
    url = "https://celestrak.org/NORAD/elements/stations.txt"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching data")
        return []

    lines = response.text.strip().split("\n")

    satellites = []

    for i in range(0, len(lines)-2, 3):
        name = lines[i].strip()
        line1 = lines[i+1].strip()
        line2 = lines[i+2].strip()

        satellites.append({
            "name": name,
            "line1": line1,
            "line2": line2
        })

    return satellites


# TEST CODE (IMPORTANT)
if __name__ == "__main__":
    data = fetch()
    print("Total satellites:", len(data))
    print("First satellite:", data[0])