original_list = [1,2,3,4,5,5,66,66,66,3,4,5]
standard_list =[]
for new_list in original_list:
    if new_list != original_list:
        standard_list.append(new_list)
print(standard_list)