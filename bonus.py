wait_list = ["ben", "sen", "den"]
wait_list.sort()

for index, name in enumerate(wait_list):
    row = f"{index + 1}.{name}"
    print(row)

wait_list.sort(reverse=True)

for index, name in enumerate(wait_list):
    row = f"{index + 1}.{name}"
    print(row)