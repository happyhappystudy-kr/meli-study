s = input()

count_dict = {}
for i in range(ord("a"), ord("z")+1):
    count_dict[chr(i)] = 0

for char in s:
    count_dict[char] += 1

count_list = [str(v) for _, v in count_dict.items()]
print(" ".join(count_list))