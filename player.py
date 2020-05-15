class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Player:
    def __init__(self, start):
        self.current_room = start
        self.visited = set()
        self.path = list()
        
    def travel(self, d):
        """print("TRAVERSE")"""
        n = self.current_room = self.current_room.get_room_in_direction(d)
        if n:
            self.visited.add(self.current_room.id)
            self.path.append(d)
            
        else:
            print("You cannot move in that direction.")
            
            
    def bfs(self):
        """print("BFS")"""
        q = Queue()
        q.enqueue([self.current_room, list()])
        
        searched = set()

        while q.size() > 0:
            room, path = q.dequeue()
  
            if room.id not in searched:
                searched.add(room.id)      
                for d in room.get_exits():
                    copy = list(path)
                    copy.append(d)
                    n = room.get_room_in_direction(d)
                    q.enqueue([n, copy])
                        
            if room.id not in self.visited:
                return path
        
        
    def traverse(self, n):
        self.visited.add(self.current_room.id)
        while len(self.visited) < n :
            path = self.bfs()
            for d in path:
                self.travel(d)
