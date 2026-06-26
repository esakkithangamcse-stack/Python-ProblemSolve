num = [ 2,8,4,5,10,9]
max_element = max(num)
sorted_numlist= sorted(num)
print(sorted_numlist)
missing_num = [n  for n in range(0, max(num)) if n not in sorted(num)]
print(f"Missing number in the list: {missing_num}")