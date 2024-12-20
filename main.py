l = input("Введи строку для поиска: ")
count = 0

with open("text.txt") as file:
    for i in file:
        if l in i:
            print(i.strip())
            count += 1

print(f"Количество строк, содержащих '{l}': {count}")