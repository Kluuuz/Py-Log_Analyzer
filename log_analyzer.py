print("===============================")
print("NOTE: CREATE A 'logs' folder first")
print("=============================== \n")


file = input("File to monitor: " )
search = input("Filter log: ").lower()
num = 0
found = False

with open(f"logs/{file}","r") as logs:
    for filtered in logs:
        num += 1
        if search in filtered.lower():
            found = True
            print(f"{num}. {filtered.strip()}")
    if not found:   
         print("No matched ")

#Summary
print("\n===============================\n============SUMMARY============\n===============================\n")
print(f"Number of {search.capitalize()}: {num}")
