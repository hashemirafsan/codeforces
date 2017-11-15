n = int(input())
n_arr = ['Tetrahedron', 'Cube', 'Octahedron', 'Dodecahedron', 'Icosahedron']
v_arr = [4, 6, 8, 12, 20]
count = 0
while n:
    a = str(input())
    index = n_arr.index(a)
    count += v_arr[index]
    n -= 1
print(count)