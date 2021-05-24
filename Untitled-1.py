def f(el):
    return [len(el)] + el

el = []

for i in range(4):
    el = f(el)

print(el)