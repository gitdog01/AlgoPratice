import sys


def dividi(post_order, in_order, p, i):
    p_start, p_end = p
    i_start, i_end = i

    root = post_order[p_end]
    left_post = []
    left_in = []

    return [root]


N = int(sys.stdin.readline().replace("\n", ""))
in_order = list(sys.stdin.readline().replace("\n", "").split())
post_order = list(sys.stdin.readline().replace("\n", "").split())

print(*dividi(post_order, in_order,
              [0, len(post_order)-1], [0, len(in_order)-1]))
