from game import Roulette

class GameController:
    # множитель записывается в порядке игр
    games_win_balance_multiply = [5]
    # название:описание игры
    games = {0:
                 {'name': "Классическая рулетка",
                  'class': Roulette,
                  'desc': f'Вам предстоит выбрать символ и крутануть рулетку, если'
                          f' выпадает ваш символ, то вы получаете x{games_win_balance_multiply[0]}'
                  }
             }

    @classmethod
    def choice_mini_game(cls) -> int:
        """"Предоставляет пользователю выбор игры"""
        print('Выберите игру из представленных :\n')
        cls.show_list_of_games()
        answer = input()
        if cls.checking_for_correctness_selected_game(answer):
            return int(answer)
        else:
            cls.choice_mini_game()

    @classmethod
    def checking_for_correctness_selected_game(cls, num):
        """Проверяет введено ли верное число, не превышающее колво игр"""
        try:
            num = int(num)
            if 1 <= num <= len(cls.games):
                return True
        except BaseException:
            print('Введите число')
        return False

    @classmethod
    def show_list_of_games(cls):
        """Показывает список доступных игр"""
        for i in range(len(cls.games)):
            name = cls.games[i]["name"]
            desc = cls.games[i]["desc"]
            print(f'{i + 1}) {name} : {desc}')

    @classmethod
    def start_selected_game(cls, num_of_game: int, user_balance: int, user_name: str):
        """Из списка games получает класс игры и запускается"""
        game_name = cls.games[num_of_game]['class']
        game_name(user_balance, user_name).start_game()
