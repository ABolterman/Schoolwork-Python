from Trains import Train
from Planes import Plane
from GenericQueue import Queue
from GenericStack import Stack


# https://stackoverflow.com/questions/434287/how-to-iterate-over-a-list-in-chunks
def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


def get_load_times():
    trains = []
    planes = []
    t_p_nt_np = str(
        input("Separated by a space, enter the number of: trains, planes, train items, plane items")).split()

    # Gets item numbers for trains/planes & splits into a list. Creates trains/planes
    number_of_items_per_train = str(input("Separated by a space, enter the amount of items per train")).split()
    for train_number in range(int(t_p_nt_np[0])):
        trains.append(Train(number_of_items_per_train[train_number], train_number+1))

    number_of_items_per_plane = str(input("Separated by a space, enter the amount of items per plane")).split()
    for plane_number in range(int(t_p_nt_np[1])):
        planes.append(Plane(number_of_items_per_plane[plane_number], plane_number+1))

    # Creates stacks of 5 train destinations, enters stacks into queue
    queue_of_train_destination_stacks = Queue()
    train_destinations = str(input("Separated by a space, enter which train each item goes to")).split()
    for chunk in chunker(train_destinations, 5):
        chunk_stack = Stack()
        for destination in chunk:
            chunk_stack.push(destination)
        queue_of_train_destination_stacks.enqueue(chunk_stack)

    # Creates queue of plane destinations
    plane_destinations = str(input("Separated by a space, enter which plane each item goes to")).split()
    queue_of_plane_destinations = Queue()
    for destination in plane_destinations:
        queue_of_plane_destinations.enqueue(destination)

    # Iterates through queue of stacks, iterates through each stack, adds item to train
    train_time = 0
    while queue_of_train_destination_stacks.get_storage_length() != 0:
        current_stack = queue_of_train_destination_stacks.dequeue()
        while current_stack.get_storage_length() != 0:
            destination = int(current_stack.pop())
            train_time = trains[destination-1].add_item(train_time)

    print("Train Times:")
    for train in trains:
        print(train.get_time_departed(), end=" ")

    # Goes through queue to get destinations, adds to correct plane
    plane_time = 0
    while queue_of_plane_destinations.get_storage_length() != 0:
        destination = int(queue_of_plane_destinations.dequeue())
        plane_time = planes[destination-1].add_item(plane_time)

    print()
    print("Plane Times:")
    for plane in planes:
        print(plane.get_time_departed(), end=" ")


get_load_times()
