from user import User

if __name__ == '__main__':
    user = User.creating_user()
    user.greetings()
    user.start_game()
    input()
