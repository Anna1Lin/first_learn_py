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
print(new[1])