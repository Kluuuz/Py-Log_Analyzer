print("===============================")
print("NOTE: CREATE A 'logs' folder first")
print("=============================== \n")


file = input("File to monitor: " )
search = input("Filter log: ").lower()
num = 0
match = 0
found = False

with open(f"logs/{file}","r") as logs:
    print("\nResults: ")
    for filtered in logs:
        num += 1
        if search in filtered.lower():
            match += 1
            found = True
            print(f"{match}. {filtered.strip()}")
    if not found:   
         print("No matched ")

#Summary
print("\n===============================\n============SUMMARY============\n===============================\n")
print(f"Number of {search.capitalize()}: {match}")
if num > 0 :
    percent = (match / num) * 100
    print(f"Match rate: {percent:.2f}%")