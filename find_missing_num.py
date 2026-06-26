num = [1,2,4,5,6,7,8,9,10]
num_length = len(num)+1
print(f"Length of the list: {num_length}")

expected_seq_sum = num_length*(num_length+1)//2
actual_seq_sum = sum(num)

missing_num =  expected_seq_sum - actual_seq_sum
print(f"Missing number in the list: {missing_num}")