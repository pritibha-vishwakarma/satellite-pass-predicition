def is_visible(position):
    x, y, z = position

    # Simple distance logic (learning purpose)
    distance = abs(x) + abs(y) + abs(z)

    if distance < 7000:
        return True
    return False


def detect_passes(positions):
    passes = []
    current_pass = None

    for time, pos in positions:
        if is_visible(pos):
            if current_pass is None:
                current_pass = {"start": time}
        else:
            if current_pass:
                current_pass["end"] = time
                passes.append(current_pass)
                current_pass = None

    return passes


# TEST
if __name__ == "__main__":
    # Dummy test data
    sample_positions = [
        ("10:00", (1000, 1000, 1000)),
        ("10:01", (500, 500, 500)),
        ("10:02", (20000, 20000, 20000)),
        ("10:03", (300, 300, 300)),
        ("10:04", (400, 400, 400)),
        ("10:05", (20000, 20000, 20000)),
    ]

    result = detect_passes(sample_positions)
    print(result)