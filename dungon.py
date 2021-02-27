import random


def add_path_to_maze(direction,shortes_path_nodes,maze):
    if direction != "Not Found":
        shortes_path_nodes.pop(0)
        shortes_path_nodes = list(shortes_path_nodes[:-1])
        for node in shortes_path_nodes:
            vertical = node[0]
            horizontal = node[1]
            maze[vertical] = maze[vertical][:horizontal] + "." + maze[vertical][horizontal + 1:]

        for row in maze:
            print(row)


def add_random_rock(row):
    rock_num = int(len(row)/3) # defines number of rocks per row
    len_row = len(row)

    for rock in range(rock_num):
        p = random.randint(0, len_row)
        row = row[:p] + "#" + row[p + 1:]
    return row


def create_dangon(width,height):
    maze = []
    maze_nodes = []
    for h in range(height):
        row = ""
        row_nodes = []
        for x in range(width):
            row += " "
            row_nodes.append([h,x])

        row = add_random_rock(row)
        maze.append(row)
        maze_nodes.append(row_nodes)


    print()
    return maze, maze_nodes

def add_start_end(x,width, height, maze):

    while True:
        horizontal = random.randint(0,width - 1)
        vertical = random.randint(0, height - 1)
        if maze[vertical][horizontal] not in ["S", "E"]:
            place = [vertical, horizontal]
            # adds start and end to maze
            maze[vertical] = maze[vertical][:horizontal] + x + maze[vertical][horizontal + 1:]

            return place, maze

# vars
width, height = 100, 200
maze, maze_nodes = create_dangon(width,height)
start_node,maze = add_start_end("S",width, height, maze)
end_node,maze = add_start_end("E",width, height, maze)

print()
print("start node: ",start_node)
print("end node: ",end_node)
print()

for row in maze:
    print(row)
print()

def find_neighbours(next_node, width, height):
    neighbours_nodes = []
    neighbours = []

    for i in ["left", "right", "up", "down"]:
        if next_node[1] - 1 >= 0:
            left = [next_node[0], next_node[1] - 1]
            if maze[left[0]][left[1]] != "#":
                neighbours.append("L")
                neighbours_nodes.append(left)
        if next_node[1] + 1 < width:
            right = [next_node[0], next_node[1] + 1]
            if maze[right[0]][right[1]] != "#":
                neighbours.append("R")
                neighbours_nodes.append(right)
        if next_node[0] + 1 < height:
            down = [next_node[0] + 1, next_node[1]]
            if maze[down[0]][down[1]] != "#":
                neighbours.append("D")
                neighbours_nodes.append(down)
        if next_node[0] - 1 >= 0:
            up = [next_node[0] - 1, next_node[1]]
            if maze[up[0]][up[1]] != "#":
                neighbours.append("U")
                neighbours_nodes.append(up)

        return neighbours_nodes, neighbours


def main(start_node,end_node):
    visited = []
    queue_nodes = [[start_node]]
    queue_direcion = [[""]]

    while queue_nodes:
        current_way = queue_nodes.pop(0)
        next_node = current_way[-1]

        current_way_str = queue_direcion.pop(0)

        if next_node not in visited:
            neighbours_nodes, neighbours = find_neighbours(next_node, width, height)
            for index, neighbour in enumerate(neighbours_nodes):
                new_way = list(current_way)
                new_way.append(neighbour)
                new_way_str = list(current_way_str)
                new_way_str.append(neighbours[index])
                queue_nodes.append(new_way)
                queue_direcion.append(new_way_str)

                if neighbour == end_node:
                    new_way_str.pop(0)
                    direction = "".join(new_way_str)
                    return new_way, direction
        visited.append(next_node)

    return "There is no path connecting start and end", "Not Found"



shortes_path_nodes, direction = main(start_node,end_node)

print("Direction: ",direction)
print()

add_path_to_maze(direction,shortes_path_nodes,maze)