graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["tom", "jhonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["tom"] = []
graph["jhonny"] = []

from collections import deque

def person_is_seller(name):
    return name[-1] == 'm' #random way to decide who is a seller

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search("you")