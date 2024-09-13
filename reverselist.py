def reverse_list(lst):
    return lst[::-1]

def switch_positions(lst, pos1, pos2):
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    return lst

# Take list as input
lst = list(map(int, input("Enter the list elements separated by space: ").split()))

print("Original List: ", lst)

# Reverse the list
reversed_lst = reverse_list(lst)
print("Reversed List: ", reversed_lst)

# Switch positions
pos1 = int(input("Enter the first position to switch: "))
pos2 = int(input("Enter the second position to switch: "))

switched_lst = switch_positions(lst, pos1, pos2)
print("List after switching positions: ", switched_lst)