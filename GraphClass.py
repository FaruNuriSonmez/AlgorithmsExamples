class GraphClass:
    def __init__(self, dictionary=None):
        if dictionary == None:
            dictionary = {}
        self.dictionary = dictionary
    #Breadth-First Search
    def BFS(self, starting):
        visited = {}
        output = []
        engueue = []

        engueue.append(starting)
        if starting not in visited:
            visited[starting] = True
        while engueue:
            x = engueue.pop(0)
            output.append(x)
            for i in self.dictionary[x]:
                if i not in visited:
                    engueue.append(i)
                    visited[i] = True
        return output
    #Breadth-First Search Shortest Path
    def BFS_ShortestPath(self, first, end):
       visited = []
       engueue = [[first]]

       if first == end:
           return
       while engueue:
           path = engueue.pop(0)
           node = path[-1]

           if node not in visited:
               neighbors = self.dictionary[node]

               for neighbor in neighbors:
                   newPath = list(path)
                   newPath.append(neighbor)
                   engueue.append(newPath)
                   if neighbor == end:
                       return newPath
                   visited.append(node)