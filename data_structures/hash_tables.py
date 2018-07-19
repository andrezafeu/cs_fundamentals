voted = {}

def check_voter(name):
    if voted.get(name):
        print("{} has already voted!".format(name))
    else:
        voted[name] = True
        print("{} has not voted!".format(name))

check_voter("tom")
check_voter("mike")
check_voter("mike")



cache = {}

def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data