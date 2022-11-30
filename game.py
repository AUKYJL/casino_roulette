import json
import time, random, os
from colorama import init
from colorama import Fore, Back, Style
from game_controller import GameController

init()


class Roulette:
    SYMBOLS = ('☺', '♥', '♦', '♣', '☼', '♀', '♂')

    def __init__(self, balance, player):
        self.balance = balance
        self.player = player

    def draw_roof_or_bottom_machine(self):
        LiGHTYELLOWANDDIM = Fore.LIGHTYELLOW_EX + Style.DIM
        print(f'{Fore.YELLOW}{Style.BRIGHT}<-------------------------------->\n'
              f'{LiGHTYELLOWANDDIM}[ --- {{{Fore.RED}7 7 7{LiGHTYELLOWANDDIM}}} {Fore.GREEN}CASINO {LiGHTYELLOWANDDIM}{{{Fore.RED}7 7 7{LiGHTYELLOWANDDIM}}} --- ]\n'
              f'{Fore.YELLOW}{Style.BRIGHT}<-------------------------------->{Style.RESET_ALL}')

    def draw_cursor(self):
        indent = '\t       '
        print(Fore.RED + f'{indent} ^')
        print(f'{indent} |' + Style.RESET_ALL)

    def draw_machine(self, slots, symbol, bet):
        print(f'Ваш символ : {symbol}, ваша ставка : {bet}$')
        self.draw_roof_or_bottom_machine()
        print('')
        print(Fore.LIGHTMAGENTA_EX + '   '.join(slots))
        print('' + Style.RESET_ALL)
        self.draw_cursor()
        self.draw_roof_or_bottom_machine()

    def get_win_slot(self, symbol, bet):
        game_symbols = self.get_game_symbols()
        win_slot = ''
        for i in range(len(game_symbols) - 9):
            slots = game_symbols[i:i + 9]
            os.system('cls')
            self.draw_machine(slots, symbol, bet)
            time.sleep(0.1)
            win_slot = slots[len(slots) // 2]
        return win_slot

    def get_game_symbols(self):
        return [self.SYMBOLS[random.randint(0, len(self.SYMBOLS) - 1)] for i in range(30)]

    def set_bet(self):
        self.bet = input('Ваша ставка : ')
        if not (0 < int(self.bet) <= self.balance):
            print('Неверное число!')
            self.set_bet()

    def set_symbol(self):

        print(f'Выберите символ из представленных, введя его индекс (счет с 1)\n {self.SYMBOLS}')
        try:
            index = int(input())
            if 1 <= index <= len(self.SYMBOLS):
                self.symbol = self.SYMBOLS[index - 1]
            else:
                print('Вы указали число в неверном диапазоне')
                self.set_symbol()
        except BaseException:
            print('Вы ввели неверный индекс!')
            self.set_symbol()

    def congrats(self):
        win_balance = int(self.bet) * GameController.games_win_balance_multiply[0]
        print(f'Хорош, бро\nТекущий баланс увеличен на {win_balance}$!')
        self.balance += win_balance

    def lose(self):
        print(f'В следующий раз повезет!\nБаланс уменьшен на {self.bet}$')
        self.balance -= int(self.bet)

    def not_enough_money(self):
        print('На вашем счету нет денежек!')
        self.bye_bye()

    def start_game(self):
        self.balance = self.get_balance()
        if self.balance <= 0:
            self.not_enough_money()
            return

        self.set_bet()
        self.set_symbol()
        if self.symbol == self.get_win_slot(self.symbol, self.bet):
            self.congrats()
        else:
            self.lose()
        if self.balance > 0:
            self.restart()
        else:
            self.not_enough_money()

    def get_balance(self):
        print(f'Ваш баланс : {self.balance}$')
        return int(self.balance)

    def bye_bye(self):
        print('Приходите к нам играть еще!')

        with open('users_data.json', 'r', encoding='utf-8') as file:
            try:
                users = json.load(file)
            except BaseException:
                users = {}
        with open('users_data.json', 'w', encoding='utf-8') as file:
            users[self.player] = {'balance': self.balance}
            json.dump(users, file, indent=4, ensure_ascii=False)

    def restart(self):
        print('Хотите сыграть еще? y/n')
        answ = input()
        if answ.lower() == 'y':
            self.start_game()
        elif answ.lower() == 'n':
            self.bye_bye()
        else:
            print('Введите еще раз')
            self.restart()

