from os import O_CREAT
import queue
cache = []
queue = queue.Queue()

def init_cache():
    try:
        with open('../files/userlist.txt', "r") as f:
            l = f.read().splitlines()
            for line in l:
                cache.append(line)
    except:
        print('file not exists')

def usercheck():
    while True:
        user = queue.get()
        if user not in cache:
            cache.append(user)
            with open('../files/userlist.txt', "a") as f:
                f.write(user + '\n')


