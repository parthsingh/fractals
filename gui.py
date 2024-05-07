import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from mandelbrot import mandelbrot_plot_set
import julia

# Initial parameters
initial_r = -0.7
initial_i = 0.27015

# Setup the plot
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(left=0.1, bottom=0.25, right=0.8, top=0.9)

# Initial plot with a lower resolution for live updates
iterations = mandelbrot_plot_set(500, 500)
img = plt.imshow(iterations, extent=[-2, 2, -2, 2], cmap='magma')
ax.margins(x=0)

# Add colorbar
cbar = plt.colorbar(img)
cbar.set_label('Iterations')

# Slider axes
axcolor = 'lightgoldenrodyellow'
ax_r = plt.axes([0.1, 0.1, 0.5, 0.03], facecolor=axcolor)
ax_i = plt.axes([0.1, 0.05, 0.5, 0.03], facecolor=axcolor)

# Sliders
s_r = Slider(ax_r, 'Real', -2.0, 2.0, valinit=initial_r)
s_i = Slider(ax_i, 'Imaginary', -2.0, 2.0, valinit=initial_i)

# Cache to store pre-calculated results
cache = {}

def update(val):
  r = s_r.val
  i = s_i.val
  key = (round(r, 4), round(i, 4))  # Round values for cache key

  # Check if data for this range is already cached
  if key in cache:
    iterations = cache[key]
  else:
    # If not cached, calculate for higher resolution and store in cache
    iterations = mandelbrot_plot_set(1000, 1000, c=complex(r, i))
    cache[key] = iterations

  if set_type.get() == 'Mandelbrot':
    ax.set_title('Mandelbrot Set', fontsize=16, pad=20)
  else:
    c = complex(r, i)
    iterations = julia.julia_plot_set(1000, 1000, c=complex(r, i))
    ax.set_title('Julia Set', fontsize=16, pad=20)
  img.set_data(iterations)
  fig.canvas.draw_idle()

s_r.on_changed(update)
s_i.on_changed(update)

# Reset button
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
  s_r.reset()
  s_i.reset()
  cache.clear()  # Clear cache on reset

button.on_clicked(reset)

# Set type button
set_type = tk.StringVar(value='Mandelbrot')
ax.set_title('Mandelbrot Set', fontsize=16, pad=20)
set_typeax = plt.axes([0.8, 0.1, 0.1, 0.04])
set_type_button = Button(set_typeax, 'Change Set', color=axcolor, hovercolor='0.975')

def change_set(event):
    if set_type.get() == 'Mandelbrot':
        set_type.set('Julia')
    else:
        set_type.set('Mandelbrot')
    update(None)

set_type_button.on_clicked(change_set)

# Create GUI window
root = tk.Tk()
root.title("Fractal Sets")

# Create canvas
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Run the GUI
root.mainloop()