#Break statement- Exits the entire loop

num = 20
while num <= 25:
    print(num)
    if num == 23:
        break
    num += 1

#Continue statement- skips a loop
devices = ["laptop","phone", "tablet"]
for x in devices:
    if x =="phone":
        continue
    print(x)


