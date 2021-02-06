data = []
count = 0
with open("reviews.txt", "r") as f:
    for line in f:
        data.append((line))
        count += 1
        if count % 1000 == 0:
            print(len(data))
print("Finish read, there are: ", len(data), "data in file")

sum_len = 0
#d is string type, data is list type
for d in data:
    sum_len = sum_len + len(d)
print("The avg length is ", sum_len/len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print("Filter there are", len(new), "comments under 100 length")
print(new[0])
print("---------------------")
print(new[1])

good = []
for d in data:
    if "good" in d:
        good.append(d)
print(len(good))
print("There are", len(good),"good comments in reviews.txt")
print(good[0])
print("---------------------")
print(good[1])

bad = []
for d in data:
    if "bad" in d:
        bad.append(d)
print("There are", len(bad),"bad comments in reviews.txt")
print()
print(bad[0])
print("---------------------")
print(bad[1])