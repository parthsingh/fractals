import numpy as np
import matplotlib.pyplot as plt

def mandelbrot_plot_set(width, height, max_iter=100, threshold=2, c=0):
    x = np.linspace(-2, 2, width)
    y = np.linspace(-2, 2, height)
    X, Y = np.meshgrid(x, y)
    c_broadcast = np.full((height, width), c)
    Z = X + 1j * Y

    iterations = np.zeros(Z.shape, dtype=int)

    for i in range(max_iter):
        Z = Z**2 + X + 1j * Y +c_broadcast
        mask = np.abs(Z) < threshold
        iterations += mask
        Z[~mask] = np.nan
    return iterations

def mandelbrot_plot(color='magma'):
    width, height = 1000, 1000

    # Generate the Mandelbrot set
    iterations = mandelbrot_plot_set(width, height)

    # Plot the Mandelbrot set
    plt.figure(figsize=(10, 10))
    plt.imshow(iterations, cmap=color, extent=(-2, 2, -2, 2))
    plt.colorbar(label='Iterations')
    plt.title('Mandelbrot Set')
    plt.show()

# def main():
#     mandelbrot_plot()


# main()
