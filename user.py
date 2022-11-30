import json

import games.controller_game as cg


class User:
    DEFAULT_BAlANCE = 100

    def __init__(self, user_name: str, is_new_person: bool, balance: int):
        self.user_name = user_name
        self.is_new_person = is_new_person
        self.balance = balance

    @classmethod
    def creating_user(cls):
        user_name = cls.set_user_name()
        is_new_person = cls.checking_is_new_person(user_name)
        balance = cls.get_balance(user_name, is_new_person)
        return cls(user_name, is_new_person, balance)

    @classmethod
    def get_balance(cls, user_name: str, is_new_person: bool, path_to_json_file: str = 'users_data.json') -> int:
        # если пользователь новый, то присваивается дефолтное значение, иначе достается из json
        if is_new_person:
            return cls.DEFAULT_BAlANCE
        else:
            with open(path_to_json_file, 'r', encoding='utf-8') as file:
                users = json.load(file)
                return int(users[user_name]['balance'])

    @staticmethod
    def checking_is_new_person(user_name: str, path_to_json_file: str = 'users_data.json') -> bool:
        # проверка на нового пользователя
        with open(path_to_json_file, 'r', encoding="utf-8") as file:
            # если json пустой, значит пользователь новый
            try:
                users = json.load(file)
            except BaseException:
                return True
            for k, v in users.items():
                if user_name == k:
                    return False
            return True

    def greetings(self):
        if self.is_new_person:
            self.welcome()
        else:
            self.welcome_back()

    def welcome(self):
        self.user_name_to_DB()
        print(f'Выбирайте автомат, проходите, {self.user_name}!!!')

    def welcome_back(self):
        print(f'С возвращением, {self.user_name}! Желаем сегодня вам отыграться!')

    @staticmethod
    def set_user_name() -> str:
        return input(
            'Добрый вечер, я диспетчер. Мы рады вас приветствовать в нашем заведении. Пожалуйста, представьтесь : ')

    def user_name_to_DB(self):
        # записывает пользователя в БД
        with open('users_data.json', 'r', encoding='utf-8') as file:
            try:
                users = json.load(file)
            except BaseException:
                users = {}
        with open('users_data.json', 'w', encoding='utf-8') as file:
            users[self.user_name] = {'balance': self.DEFAULT_BAlANCE}
            json.dump(users, file, indent=4, ensure_ascii=False)

    def start_game(self):
        if self.is_new_person:
            print(f'Вы начинаете игру с начальным балансом {self.balance}$')
        else:
            self.continue_or_restart_game()
        num_of_game = cg.GameController.choice_mini_game()
        cg.GameController.start_selected_game(num_of_game, self.balance, self.user_name)

    def continue_or_restart_game(self):
        print(f'Продолжить игру с прошлым балансом ({self.balance}$) или начать по новой с 100$. Введите 1 или 2')
        answer = int(input())
        if answer == 1:
            return
        elif answer == 2:
            self.balance = self.DEFAULT_BAlANCE

        else:
            print('Некорректный ввод.')
            self.continue_or_restart_game()
