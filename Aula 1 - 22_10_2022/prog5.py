import turtle

cores = ['red', 'green', 'orange', 'white', 'gray', 'pink']
turtle.bgcolor('black')

voltas = int(turtle.numinput('Voltas', 'Número de voltas:'))
lados = int(turtle.numinput('Lados', 'Número de lados:'))

for x in range(voltas):
    resto = x % len(cores)
    cor = cores[resto]
    turtle.pencolor(cor)
    turtle.forward(x*5)
    turtle.left(360 / lados )
