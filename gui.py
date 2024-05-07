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
initial_cmap = 'magma'

# Setup the plot
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(left=0.1, bottom=0.25, right=0.8, top=0.9)

# Initial plot with a lower resolution for live updates
c = complex(initial_r, initial_i)
iterations = julia.julia_plot_set(1000, 1000, c)
img = plt.imshow(iterations, extent=[-2, 2, -2, 2], cmap='magma')
ax.margins(x=0)

# Add colorbar
cbar = plt.colorbar(img)
cbar.set_label('Iterations')

# Slider axes
axcolor = 'lightgoldenrodyellow'
ax_r = plt.axes([0.1, 0.1, 0.5, 0.03], facecolor=axcolor)
ax_i = plt.axes([0.1, 0.05, 0.5, 0.03], facecolor=axcolor)
ax_cmap = plt.axes([0.1, 0.00, 0.5, 0.03], facecolor=axcolor)

# Sliders
s_r = Slider(ax_r, 'Real', -2.0, 2.0, valinit=initial_r)
s_i = Slider(ax_i, 'Imaginary', -2.0, 2.0, valinit=initial_i)

# Cmap Selection
cmap_list = ['viridis', 'plasma', 'inferno', 'magma', 'cividis','twilight_shifted','gist_earth','ocean','pink','prism','tab10','cubehelix','jet','coolwarm','brg']
initial_cmap_index = cmap_list.index(initial_cmap)
s_cmap = Slider(ax_cmap, 'Colormap', 0, len(cmap_list) - 1, valinit=initial_cmap_index, valfmt='%d')

# Cache to store pre-calculated results
cache = {}

def update(val):
  r = s_r.val
  i = s_i.val
  cmap_index = int(s_cmap.val)
  cmap_name = cmap_list[cmap_index]

  c = complex(r,i)
  if set_type.get() == 'Mandelbrot':
    iterations = mandelbrot_plot_set(1000, 1000, c=c)
    ax.set_title('Mandelbrot Set', fontsize=16, pad=20)
  else:
    iterations = julia.julia_plot_set(1000, 1000, c=c)
    ax.set_title('Julia Set', fontsize=16, pad=20)
    
  img.set_data(iterations)
  img.set_cmap(cmap_name)
  fig.canvas.draw_idle()

update_button_ax = plt.axes([0.8, 0.0, 0.1, 0.04])
update_button = Button(update_button_ax, 'Update', color=axcolor, hovercolor='0.975')
update_button.on_clicked(update)

# Reset button
resetax = plt.axes([0.8, 0.05, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
  s_r.reset()
  s_i.reset()
  cache.clear()  # Clear cache on reset

button.on_clicked(reset)

# Set type button
set_type = tk.StringVar(value='Julia')
ax.set_title('Julia Set', fontsize=16, pad=20)
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