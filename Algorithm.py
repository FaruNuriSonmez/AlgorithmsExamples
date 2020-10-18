import time
import GraphClass
graph = {
    "A" : ["B", "C", "D"],
    "B" : ["A", "C", "E", "D"],
    "C" : ["B", "A", "F"],
    "D" : ["A", "B"],
    "E" : ["B", "H"],
    "F" : ["C"],
    "H" : ["E","G"],
    "G" : ["H"]
}
graphObject = GraphClass.GraphClass(graph)
output = graphObject.BFS("A"), graphObject.BFS_ShortestPath("A", "H")
print(output)