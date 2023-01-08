#Задание №1
import pprint

cook_book = {}

def read_file():
    dish_list = []
    with open('recipes.txt', 'rt', encoding='utf8') as file:
        for dish in file:
            name_dish = dish.strip()
            ingredients_list = []
            dish = {name_dish: ingredients_list}
            ingredient_count = file.readline()
            for i in range(int(ingredient_count)):
                number = file.readline()
                ingredient_name, quantity, measure = number.strip().split(' | ')
                ingredients_list.append({'ingredient_name': ingredient_name,
                                         'quantity': int(quantity),
                                         'measure': measure})
                dish_list.append(dish)
            empty_string = file.readline()
            cook_book.update(dish)
    pprint.pprint(cook_book, width=150, sort_dicts=False)

#Задание №2

def get_shop_list_by_dishes(name_dish, person_count):
    result = {}
    for val in name_dish:
        for elem in cook_book[val]:
            if elem['ingredient_name'] not in result.keys():
                result[elem['ingredient_name']] = \
                    {"measure": elem['measure'], "quantity": elem['quantity'] * person_count}
            else:
                summa = result[elem['ingredient_name']]['quantity'] + (elem['quantity'] * person_count)
                result[elem['ingredient_name']].update({"quantity": summa})

    for key, val in result.items():
        print(key, val)

if __name__ == "__main__":
    read_file()
    print("\n")
    get_shop_list_by_dishes(["Омлет", 'Запеченный картофель', 'Фахитос'], 2)

print("\n")
# Задание №3

outputfile = 'output.txt'
file1 = '1.txt'
file2 = '2.txt'
file3 = '3.txt'
myfile = open(outputfile, mode='w', encoding='utf-8')
def num_of_lines(*files):
    count = {}
    for file in files:
        with open(file, mode='r', encoding='utf-8') as f:
            count.update({file[-5:] : (len(f.readlines()))})
    files2 = {}
    for i in sorted(count, key=count.get, reverse=True):
        files2[i] = count[i]
    print(files2)
    for key, value in files2.items():
        myfile.write(f'Даны файлы: {key} \n')
        myfile.write(f'Количество строк: {value}, файл номер: {key}\n')
    return files2
num_of_lines(file1, file2, file3)