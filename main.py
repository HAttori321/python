# 1
# def main():
#     try:
#         name=input("Введіть ім'я: ")
#         age=int(input("Введіть вік: "))
#         if age<0 or age>130:
#             raise ValueError("Некоректний вік.Будь ласка, введіть ваш вік")
#         print(f"Привіт,{name}.Твій вік:{age}")
#     except ValueError as e:
#         print(f"Помилка: {e}")
# main()
# 2
# def main(name,age):
#     if age<0 or age>130:
#         raise ValueError("Некоректний вік. Будь ласка, введіть вік в межах від 0 до 130.")
#     greeting=f"Привіт,{name}.Твій вік:{age}"
#     return greeting
# def main1():
#     try:
#         name=input("Введіть ваше ім'я:")
#         age=int(input("Введіть ваш вік:"))
#         result=main(name,age)
#         print(result)
#     except ValueError as e:
#         print(f"Помилка:{e}")
# main1()
3
def numbers():
    numbers=[]
    try:
        while True:
            value=float(input("Введіть додатнє число (або enter для завершення): "))
            if value<=0:
                raise ValueError("Число повинно бути більше нуля.")
            numbers.append(value)
    except ValueError as e:
        print(f"Помилка:{e}")
    finally:
        if any(num < 0 for num in numbers):
            print("Від'ємне число у списку.")
        else:
            total=sum(numbers)
            print(f"Сума чисел:{total}")
numbers()
