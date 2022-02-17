import config
import queue

cache = []
queue = queue.Queue()


# uncomment for username logging make sure you have their consent
def init_cache():
    """
    try:
        with open(config.BOT_TOKEN + 'userlist.txt', "r") as f:
            l = f.read().splitlines()
            for line in l:
                cache.append(line)
    except:
        print('file not exists')
    """


def usercheck():
    """
    while True:
        user = queue.get()
        if user not in cache:
            cache.append(user)
            with open(config.BOT_TOKEN + 'userlist.txt', "a") as f:
                f.write(user + '\n')
    """
