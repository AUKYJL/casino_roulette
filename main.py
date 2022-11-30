from user import User
import json


# def start_game(user_name, balance=100):
#     rl = Roulette(balance, user_name)
#     rl.start_game()


# def continue_game(user_name):
#     with open('users_data.json', 'r', encoding='utf-8') as file:
#         users = json.load(file)
#         balance = users[user_name]['balance']
#         start_game(user_name, int(balance))


if __name__ == '__main__':
    user = User.creating_user()
    user.greetings()
    user.start_game()
    input()
    # choice_game(user.user_name)
    # input()
