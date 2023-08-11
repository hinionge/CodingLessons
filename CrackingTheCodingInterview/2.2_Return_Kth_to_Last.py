# 11.8.2023
# CTCI Chapter 2 Q2.2

####### QUESTION: Implement an algorithm to find the kth to last element of a singly linked list.

    # NB this code written without actually implementing a linked list


                            # Function takes in k
def is_node_K_from_end(node,k):
                            # Boolean to trip when node checked is K back from tail node
    is_K_from_end = False
    fwd = null
                            # Count K forward from current node
    for j in range (k):
        fwd = list[node].next
        node = fwd

                            # if the node k ahead points to 'null', it's the end
    if fwd = null:
                            # .... so switch the boolean
        is_K_from_end = True

    return is_K_from_end


def Kth_to_Last(k):
    node = 0

                            # Go through list until the node K away from the end is reached
    while is_node_K_from_end(node,k) = False:
                            # And then read its value
        node = list[node].next

    return list[node].value


if __main__ == "__name__":

    k = 5

    print(Kth_to_Last(k))