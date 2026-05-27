import re

print("===============================")
print("NOTE: CREATE A 'logs' folder first")
print("=============================== \n")


file = input("File to monitor: " )
search = input("Filter log: ").lower()
num = 0
match = 0
found = False

ip_num = {}

with open(f"logs/{file}","r") as logs:
    print("\nResults: ")
    for filtered in logs:
        num += 1
        if search in filtered.lower():
            match += 1
            found = True
            print(f"{match}. {filtered.strip()}")

            #IP Counter

            ip = re.search(r"\d+\.\d+\.\d+\.\d+", filtered)

            if ip:
                
                ip_add = ip.group()

                if ip_add in ip_num:
                    ip_num[ip_add] += 1
                else:
                    ip_num[ip_add] = 1

    if not found:   
         print("No matched ")

#Summary
print("\n===============================\n------------SUMMARY------------\n===============================\n")
print(f"Total Matches for {search.capitalize()}: {match}")
print(f"Total events scanned: {num}")
if num > 0 :
    percent = (match / num) * 100
    print(f"Match rate: {percent:.2f}%")

print("\n------------Extracted IP------------\n")

for ip, count in ip_num.items():
    print(f"{ip} -> {count}")

print("\n--------------------Done Executing--------------------")