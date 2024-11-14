import water as problem
x=int(input("input x[max 3l]:"))
y=int(input("input y[max yl]:"))

print(f"For ({x},{y}):")

for succ,cost in problem.successors((x,y)):
    print(succ,end='')