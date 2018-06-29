import json
# 如果以前存储了用户名，就加载他；否则，就提示用户输入用户名并储存他
filename = 'username.json'
try:
    with open(filename) as f_oj:
        username = json.load(f_oj)
except FileNotFoundError:
    username = input("what is your name?")
    with open(filename,'w') as f_oj:
        json.dump(username,f_oj)
        print("欢迎你 "+username)
else:
    print("欢迎回来 "+username)