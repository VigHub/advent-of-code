import sympy as sp

with open('2023/24/ex.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
hailstones = []
for line in lines:
    p, v = line.split(' @ ')
    hailstone = (*(map(int, p.split(', '))),
                 *(map(int, v.split(', '))))
    hailstones.append(hailstone)


def part2():
    first_three_hailstones = hailstones[:3]
    uknw = 'x y z dx dy dz t1 t2 t3'.split()
    unknowns = sp.symbols('x y z dx dy dz t1 t2 t3')
    x, y, z, dx, dy, dz, *time = unknowns

    equations = []  # build system of 9 equations with 9 unknowns
    for t, h in zip(time, first_three_hailstones):
        equations.append(sp.Eq(x + t*dx, h[0] + t*h[3]))
        equations.append(sp.Eq(y + t*dy, h[1] + t*h[4]))
        equations.append(sp.Eq(z + t*dz, h[2] + t*h[5]))

    solution = sp.solve(equations, unknowns).pop()
    for i, u, v in zip(range(9), uknw, solution):
        end = '\n' if i % 3 == 2 else '\t'
        print(f'{u}: {v}', end=end)
    return sum(solution[:3])


print(part2())
