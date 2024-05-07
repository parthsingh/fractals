import numpy as np
import matplotlib.pyplot as plot
import turtle

def julia_plot_set(width, height, c, max = 100, theshold = 2):
    x = np.linspace(-2, 2, width)
    y = np.linspace(-2, 2, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j* Y

    iterations = np.zeros(Z.shape, dtype=int)

    for i in range(max):
        Z = Z**2 + c
        mask = np.abs(Z) < theshold
        iterations += mask
        Z[~mask] = np.nan
    return iterations

def julia_plot(color = 'magma', r = -.7, i = 0.27015):
    width, height = 1000, 1000

    # Define the constant c for the Julia set
    # (r, i), r is real number which influences horizontal shift
    # i is imaginary numer which influences vertical shift
    c = complex(r, i)

    # Generate the Julia set
    iterations = julia_plot_set(width, height, c)

    # Plot the Julia set
    plot.figure(figsize=(10, 10))
    # Different cmaps will provide different color schemes to fractals
    # Good examples: magma, viridis, plasma, inferno, cividis, hot
    plot.imshow(iterations, cmap=color, extent=(-2, 2, -2, 2))
    plot.colorbar(label='Iterations')
    plot.title(f'Julia Set')
    plot.show()

def julia_turtle_set(r = -.7, i = 0.27015, width = 400, height = 400, max = 100, threshold = 2):
    turtle.speed(0)
    turtle.hideturtle()

    turtle.setup(width + 100, height + 100)
    screen = turtle.Screen()
    screen.setworldcoordinates(-2, -2, 2, 2)
    screen.tracer(0, 0)
    turtle.colormode(255)
    for y in range(-height // 2, height // 2):
        for x in range(-width //2, width // 2):
            zx = x / (width / 4)
            zy = y / (height / 4)
            c = complex(r, i)
            z = complex(zx, zy)

            iteration = 0
            while abs(z) <= threshold and iteration < max:
                z = z ** 2 + c
                iteration == 1
            
            color = (iteration % 255, 255 - iteration % 255, (iteration * 10) % 255)

            turtle.penup()
            turtle.goto(x / (width / 2), y / (height / 2))
            turtle.pendown()
            turtle.dot(1,color)
    screen.update()
    turtle.done()

def main():
    #julia_turtle_set()
    julia_plot()

# main()