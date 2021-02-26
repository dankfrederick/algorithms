from collections import deque

# Breadth-First Search Example
# Complexity: O(V+E) (V for number of vertices, E for number of edges)
# Trees are special cases of graphs that have no edges that point back towards previous vertices
# Breadth-First Search is completed using Queues which are First-In, First-Out (FIFO) data structures

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []



def search(name):
	search_queue = deque()
	search_queue += graph[name]
	searched = []
	while search_queue:
		person = search_queue.popleft()
		if not person in searched:
			if person_is_seller(person):
				print(person + " is a mango seller!")
				return True
			else:
				search_queue += graph[person]
	return False

def person_is_seller(name):
	return name[-1] == 'm'

search("you")