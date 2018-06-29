import json

def get_stored_username():
    '''如果存储了用户名，就获取他'''
    filename = "username.json"
    try:
        with open(filename) as ojbk:
            username = json.load(ojbk)
    except FileNotFoundError:
        return None
    else:
        return username

def get_username():
    '''获取用户的名字'''
    username = input("what is your name?")
    with open(filename, 'w') as f_oj:
        json.dump(username, f_oj)
    return username

def greet_user():
    '''问候用户，并指出他的名字'''
    username = get_stored_username()
    if username:
        print("欢迎回来"+username)
    else:
        username = get_username()
        print("欢迎你 " + username)

greet_user()