class GraphClass:
    def __init__(self, dictionary=None): #class içindeki tüm fonksiyonlar self parametresi alırlar. dictionary grap yapımızı tutan dictionary yapımız
        if dictionary == None: #dictionary eger boş geldiyse,
            dictionary = {}
        self.dictionary = dictionary

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

    def BFS_ShortestPath(self):
        print("ss")