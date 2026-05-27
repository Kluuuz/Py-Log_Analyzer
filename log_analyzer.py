import re
import sys

print("===============================")
print("NOTE: CREATE A 'logs' folder first")
print("=============================== \n")

file = input("File to monitor: ")
search = input("Filter log: ").lower()
num = 0
match = 0
found = False
ip_num = {}

try:
    with open(f"logs/{file}", "r") as logs:
        print("\nResults: ")
        for filtered in logs:
            num += 1
            if search in filtered.lower():
                match += 1
                found = True
                print(f"{match}. {filtered.strip()}")

                # IP Counter
                ip = re.search(r"\d+\.\d+\.\d+\.\d+", filtered)
                if ip:
                    ip_add = ip.group()
                    if ip_add in ip_num:
                        ip_num[ip_add] += 1
                    else:
                        ip_num[ip_add] = 1

        if not found:
            print("No matched")

except FileNotFoundError:
    print(f"Error: '{file}' not found in logs/ folder.")
    sys.exit(1)  # stop the program cleanly
except PermissionError:
    print(f"Error: No permission to read '{file}'.")
    sys.exit(1)
except IsADirectoryError:
    print(f"Error: '{file}' is a folder, not a log file.")
    sys.exit(1)

# Summary
print("\n===============================\n------------SUMMARY------------\n===============================\n")
print(f"Total Matches for {search.capitalize()}: {match}")
print(f"Total events scanned: {num}")
if num > 0:
    percent = (match / num) * 100
    print(f"Match rate: {percent:.2f}%")

print("\n------------Extracted IP------------\n")
for ip in ip_num:
    print(f"{ip} -> {ip_num[ip]}")

print("\n--------------------Done Executing--------------------")