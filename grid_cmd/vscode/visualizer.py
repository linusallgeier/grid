import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import math
import inverse_kinematics as ik

on_visualize = None
slider_x = None
slider_y = None
l1 = 0
l2 = 0

fig, ax = plt.subplots()

def update_plot(target_x, target_y, angle_elbow, angle_shoulder):
    ax.clear()

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_xticks(range(-10, 11))
    ax.set_yticks(range(-10, 11))
    ax.set_aspect("equal")
    ax.grid()
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    ax.plot(
        target_x,
        target_y,
        color='r',
        marker='x',
        markersize=10
    )

    if angle_elbow is not None and angle_shoulder is not None:
        x0, y0 = 0.0, 0.0
        
        x1 = l1 * math.cos(angle_shoulder)
        y1 = l1 * math.sin(angle_shoulder)
    
        x2 = x1 + l2 * math.cos(angle_shoulder + angle_elbow)
        y2 = y1 + l2 * math.sin(angle_shoulder + angle_elbow)

        ax.plot(
            [x0, x1, x2], 
            [y0, y1, y2], 
            color='k',
            linestyle='-',
            linewidth=3,
            marker='o',
            markersize=8
        )

    fig.canvas.draw_idle()

def update_xy(val=None ):
    global target_x, target_y
    target_x = slider_x.val
    target_y = slider_y.val

    data_elbow = ik.calculate_elbow(target_x, target_y, l1, l2)

    if data_elbow is None:
        update_plot(target_x, target_y, None, None)
        if on_visualize is not None:
            on_visualize(None, None)
        return

    angle_elbow, steps_elbow = data_elbow
    angle_shoulder, steps_shoulder = ik.calculate_shoulder(target_x, target_y, l1, l2, angle_elbow)

    update_plot(target_x, target_y, angle_elbow, angle_shoulder)
    if on_visualize is not None:
        on_visualize(steps_elbow, steps_shoulder)

def setup_slider_x():
    ax_x = plt.axes([0.2, 0.10, 0.65, 0.03])

    return Slider(
        ax=ax_x,
        label="X:",
        valmin=-9.0,
        valmax=9.0,
        valinit=0.0,
        valstep=0.5,
        dragging=True
    )

def setup_slider_y():
    ax_y = plt.axes([0.2, 0.05, 0.65, 0.03])

    return Slider(
        ax=ax_y,
        label="Y:",
        valmin=-9.0,
        valmax=9.0,
        valinit=0.0,
        valstep=0.5,
        dragging=True
    )

def visualize(): 
    global slider_x, slider_y

    plt.subplots_adjust(bottom=0.25)

    slider_x = setup_slider_x();
    slider_x.on_changed(update_xy)

    slider_y = setup_slider_y();
    slider_y.on_changed(update_xy)

    update_xy()

    plt.show()