import turtle

MINIMUM_BRANCH_LENGTH = 5

def build_tree(t, branch_length, shorten_by, angle):
  if branch_length > MINIMUM_BRANCH_LENGTH:
    new_length = branch_length / 2

    t.left(angle)
    t.forward(branch_length)
    build_tree(t, new_length, shorten_by, angle)

    t.left(angle)
    t.forward(branch_length)
    build_tree(t, new_length, shorten_by, angle)

    t.left(angle)
    t.forward(branch_length)
    build_tree(t, new_length, shorten_by, angle)

tree = turtle.Turtle()
tree.speed(0)
tree.hideturtle()
tree.setheading(0)
tree.color('green')
build_tree(tree, 100, 20, 120)
turtle.mainloop()
