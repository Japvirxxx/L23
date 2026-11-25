s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}
s3 = list(zip(s1, s2))
print(s3, "\n")

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2):
    print(f"Sum of {x} and {y} is: {x + y}")

stocks = ['AAPL', 'MSFT', 'GOOGL']
prices = [150, 250, 2800]

new_dict = dict(zip(stocks, prices))
print(f"\nThe new dictionary created by zipping stocks and prices is: {new_dict}")
