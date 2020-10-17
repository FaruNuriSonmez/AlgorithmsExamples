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
graphNesnesi = GraphClass.GraphClass(graph)
output = graphNesnesi.BFS("A")
print(output)