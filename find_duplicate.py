num_list = [1,4,2,5,2,7,6,7,8,4,2]
#Unique elements in the list
unique_list = list(set(num_list))
print(f"Unique elements in the list: {unique_list}")

# All the duplicate elements in the list
duplicate_list = [num for num in num_list if num_list.count(num)>1]
print(f"All duplicate elements in the list: {duplicate_list}")

#Duplicate elements
duplicate_set = set([num for num in num_list if num_list.count(num)>1])
print(f"Duplicate elements in the list: {duplicate_set}")