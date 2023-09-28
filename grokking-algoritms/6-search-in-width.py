from collections import deque

graph = {
    "you":["alice","bob", "claire"],
    "bob": ["anuj","peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jhonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jhonny": [],
}

def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print('the best seller of mango -> ', person)
                return True
            else:
                search_queue += graph[person]
                searched.append(person)

    return False
    


search_result = search("you")
print(search_result)