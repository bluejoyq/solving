
from collections import Counter
s = list(map(str.upper, input()))
counter = Counter(s)
max_count = -1
max_val = []
for letter in counter:
    if counter[letter] > max_count:
        max_val = [letter]
        max_count = counter[letter] 
    elif counter[letter] == max_count:
        max_val.append(letter)
if len(max_val) > 1:
    print("?")
else:
    print(max_val[0])