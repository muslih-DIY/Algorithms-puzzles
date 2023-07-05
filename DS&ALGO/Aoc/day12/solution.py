
import input
import pprint
from typing import List
from collections import deque

def create_grid(row_grid:str):
    grid = []
    for i,rows in enumerate(row_grid.split('\n'),start=0):
        grid.append([])
        for cell_value in rows:
            grid[i].append(cell_value)
    return grid

def print_grid(grid):
    print('[')
    for row in grid:
        print(row)

    print(']')    


def valid_niegbor(a):
    nieghbor = {a}
    if(a>'a' and a<'z'):
        nieghbor.add(chr(ord(a)+1))
        nieghbor.add(chr(ord(a)-1))
    if(a=='a'):
        nieghbor.add(chr(ord(a)+1))
    if(a=='z'):
        nieghbor.add(chr(ord(a)-1))
    return nieghbor

def create_graph(grid:List[List]):

    graph = {}
    row_length = len(grid)
    column_length = len(grid[0])
    start = end = None
    for i in range(row_length):
        for j in range(column_length):
            # clear
            # print(i,j)
            location_value = grid[i][j]
            if location_value=='S':
                location_value='a'
                start = (i,j)
            if location_value=='E':
                end = (i,j)
                location_value='z'

                
            location = (i,j)
            
            graph[location]:List = []
            
            valid_niegbors_set = valid_niegbor(location_value)
            if i>0 and grid[i-1][j] in valid_niegbors_set:
                graph[location].append(((i-1,j),grid[i-1][j]))

            if j>0 and grid[i][j-1] in valid_niegbors_set:
                graph[location].append(((i,j-1),grid[i][j-1]))

            if j<column_length-1 and grid[i][j+1] in valid_niegbors_set:
                graph[location].append(((i,j+1),grid[i][j+1]))

            if i<row_length-1 and grid[i+1][j] in valid_niegbors_set:
                graph[location].append(((i+1,j),grid[i+1][j]))


    return graph,start,end


def get_shortest_path(graph,start,end):
    
    Queue = deque([(start,[start])])
    visited = set()
    

    while Queue:
        vertex,path= Queue.popleft()
        if vertex==end:
            return path
        visited.add(vertex)

        for niegbor_vertex,value in graph[vertex]:
            if niegbor_vertex in visited:
                
                continue
            Queue.append((niegbor_vertex,path+[niegbor_vertex]))




if __name__=='__main__':

    grid = create_grid(input.row_grid)
    graph,start,end = create_graph(grid)
    print(get_shortest_path( graph,start,end ))
    # pprint.pprint(graph)
