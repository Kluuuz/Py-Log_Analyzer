search = input("Search Query: ").lower()
num = 0

with open("logs/sample_logs.txt","r") as logs:
    for filter in logs:
        num += 1
        if search in filter.lower():
            print(f"{num}. {filter.strip()}")

