file_name = "score.txt"

with open(file_name, 'r') as f:
    r = f.read()

l = r.split(" ")
print(l)

# total = sum([int(e) for e in l])

# print(total)