
def hello(name="Hong Gil Dong", age='10'):
    print("Hello! " + name)
    print(age + " years old!\n")

# typing = input("What is your name: ")
# hello(typing)

name = input("Your Name : ")
age = input("How old are you? ")
hello(name, age)
hello(name) # error 발생. argument가 1개 밖에 사용하지 않아 발생.
hello()     # 매개변수에 초기값을 설정하면 에러를 방지할 수 있다.

hello(age='30', name = 'Chang')

