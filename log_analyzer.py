print("===============================")
print("NOTE: CREATE A 'logs' folder first")
print("=============================== \n")


file = input("File to monitor: " )
search = input("Search Query: ").lower()
num = 0

with open(f"logs/{file}","r") as logs:
    for filtered in logs:
        num += 1
        if search in filtered.lower():
            print(f"{num}. {filtered.strip()}")

