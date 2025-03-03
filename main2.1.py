number = int(input("Enter a number: "))

n1 = number // 1000          # Перша цифра (тисячі)
n2 = (number // 100) % 10   # Друга цифра (сотні)
n3 = (number // 10) % 10    # Третя цифра (десятки)
n4 = number % 10            # Четверта цифра (одиниці)

print(n1)
print(n2)
print(n3)
print(n4)