# # Write a function to implement the Towers of Hanoi puzzle.
# The Towers of Hanoi puzzle is a classic mathematical puzzle that involves moving a stack of disks from one peg to another, with the restriction that only one disk can be moved at a time and no larger disk can be placed on top of a smaller disk.
def towers_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        # Move the top disk from source to target
        print(f"Move disk 1 from {source} to {target}")
        return
    # Move n-1 disks from source to auxiliary peg using target as auxiliary
    towers_of_hanoi(n - 1, source, target, auxiliary)
    # Move the nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")
    # Move the n-1 disks from auxiliary peg to target using source as auxiliary
    towers_of_hanoi(n - 1, auxiliary, source, target)

# Example usage:
towers_of_hanoi(3, 'A', 'B', 'C')


