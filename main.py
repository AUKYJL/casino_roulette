from game import *
import json


class User():
    def __init__(self):
        self.get_user_name()
        if self.is_new_person():
            self.welcome()

    def is_new_person(self):
        # если это не новый игрок, то его приветствуют
        # иначе is_new_person = True
        with open('users_data.json', 'r', encoding="utf-8") as file:
            # если json пустой, значит пользователь новый
            try:
                users = json.load(file)
            except BaseException:
                return True
            for k, v in users.items():
                if self.user_name == k:
                    self.welcome_back()
                    return False
            return True

    def welcome(self):
        self.user_name_to_json()
        print(f'Выбирайте автомат, проходите, {self.user_name}!!!')

    def welcome_back(self):
        print(f'С возвращением, {self.user_name}! Желаем сегодня вам отыграться!')

    def get_user_name(self):
        self.user_name = input(
            'Добрый вечер, я диспетчер. Мы рады вас приветствовать в нашем заведении. Пожалуйста, представьтесь : ')
        # создаем в json новое поле

    def user_name_to_json(self):
        with open('users_data.json', 'r', encoding='utf-8') as file:
            try:
                users = json.load(file)
            except BaseException:
                users = {}
        with open('users_data.json', 'w', encoding='utf-8') as file:
            users[self.user_name] = {'balance': 100}
            json.dump(users, file, indent=4, ensure_ascii=False)

    # def greetings(cls):
    #     user_name = get_user_name()


def choice_game(user_name):
    choice = input('Продолжить игру или получить только 100 бабок с небес?!?  (1 или 2) : ')
    user_name = user_name
    if int(choice) == 1:
        continue_game(user_name)
    else:
        start_game(user_name)


def start_game(user_name, balance=100):
    rl = Roulette(balance, user_name)
    rl.start_game()


def continue_game(user_name):
    with open('users_data.json', 'r', encoding='utf-8') as file:
        users = json.load(file)
        balance = users[user_name]['balance']
        start_game(user_name, int(balance))


if __name__ == '__main__':
    user = User()
    choice_game(user.user_name)
    input()



