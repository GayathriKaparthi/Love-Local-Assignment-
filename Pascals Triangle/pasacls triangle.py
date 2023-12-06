def generate_pascals_triangle(num_rows):
    triangle=[]
    for i in range(num_rows):
        row=[1]*(i+1)
        if i>=2:
            for j in range(1,i):
                row[j]=triangle[i-1][j-1]+triangle[i-1][j]
        triangle.append(row)
    return triangle
def print_pascals_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str,row)).center(len(triangle[-1])*3))
num_rows=int(input())
pascals_triangle=generate_pascals_triangle(num_rows)
print("Pascal's Triangle:")
print_pascals_triangle(pascals_triangle)