numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = list(map(lambda x, y: x + y, numbers1, numbers2))
print(f"in addition to the result, the code will output the sum of corresponding elements from numbers1 and numbers2. The output will be: {result}")
print(list(result))

nums = [1, 2, 3, 4, 5]
def sq(n):
    return n*n
squared = list(map(sq, nums))
print(f"The squared values of the numbers in the list are: {squared}")
print(squared)