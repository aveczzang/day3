def sum(num1, num2):
    print("Sum함수 안 : ", num1, num2)
    return num1 + num2

num1 = 10
num2 = 20
result = sum(num1, num2) + sum(1, 2)
print(result)

print(sum(num1, num2))
print(sum(1, 2))
print("Sum 함수 밖 : ", num1, num2)
