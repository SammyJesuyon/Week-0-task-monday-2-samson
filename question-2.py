def quadraticSolver(a,b,c):
  if a == 0:
    return "Error: 'a' can't be 0"
  root_1 = (-b + ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
  root_2 = (-b - ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
  return f"{root_1} and {root_2}"

print(quadraticSolver(1,0,-9))