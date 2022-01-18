
import os
import sys


def create_list_1() -> list[str]:
    with open('C:\data\links.csv', 'r', encoding='utf-8') as file:
        list_1 = file.readlines()
    return list_1


def create_list_2() -> list[str]:
    with open(r'C:\data\urls.csv', 'r', encoding='utf-8') as file:
        list_2 = file.readlines()
    return list_2


def create_list_3(list_1: list, list_2: list) -> list[str]:
    return [obj for obj in list_1 if obj not in list_2]



def create_file(list_3: list) -> None:
    with open('C:\data\data.csv', 'a', encoding='utf-8') as file:
        for obj in list_3:
            file.write(obj)


def main():
    list_1 = create_list_1()
    list_2 = create_list_2()
    list_3 = create_list_3(list_1, list_2)
    create_file(list_3)
    sys.exit()


if __name__ == "__main__":
    main()