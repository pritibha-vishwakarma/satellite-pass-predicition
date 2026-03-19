from database import get_all_passes
from tabulate import tabulate

data = get_all_passes()

headers = ["ID", "Satellite", "Start Time", "End Time"]

print(tabulate(data, headers=headers, tablefmt="grid"))