n = input()
VOYELLES = ["a","e","i","o","u","y"]
count = 0
for i in n:
    if i in VOYELLES:
        count += 1
print(count)

