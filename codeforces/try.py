"""
 update a char in a string frequently
 cast it to a list first
 then do operations
 finally cast it back to a string
"""
s= 'abcd'
s=list(s)
s[0]='l'
s=''.join(s)
print(s)
print('-----------------------------------')
def custom_sort_rule(x):
    return 8-x

# Example usage:
example_list = [8,9,10]
sorted_list = sorted(example_list, key=custom_sort_rule)

print(sorted_list)  # Output: [9, 7, 6, 5, 5, 4, 3, 2, 1]
