from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# Create a dictionary containing the opposite direction for us to backtrack
reversed_directions = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}

# Add a reverse path to keep track for backtracking
reversal_path = []

# room_dict = {}
# for x in range(0, len(room_graph)):
#    room_dict[x] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}

# Create a set containing the ROOMS that we've visited
visited = set()

# While the amount of room we've visited is less than the total amount of rooms
while len(visited) < 500:

    # Initializing, we'll use this variable to dictate where we WANT to travel next
    next_move = None

    # Go through the exits in the current room
    for exit in player.current_room.get_exits():
        # If we haven't visited one of the room connected yet
        if player.current_room.get_room_in_direction(exit) not in visited:
            # Set that as the destination to travel
            next_move = exit
            break

    # If we have a direction that we can go to (not dead end)
    if next_move is not None:
        # Add the movement to our traversal path
        traversal_path.append(next_move)
        # We also want to add the opposite direction of where we're going for backtracking later
        reversal_path.append(reversed_directions[next_move])
        # We finally move the player to the room
        player.travel(next_move)
        # Add the new room that we are in now to the set of visited room
        visited.add(player.current_room)

    # If there's no more exit that we have not visited (dead end)
    else:
        # We will set the destination for the next move to be the previous path we've taken
        next_move = reversal_path.pop()
        # Add the backtracking step to the traversal path
        traversal_path.append(next_move)
        # Finally, move the PLAYER to the previous room
        player.travel(next_move)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
