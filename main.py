import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from field import generate_field


def run_animation():
    x = np.linspace(-9, 9, 420)
    y = np.linspace(-9, 9, 420)
    X, Y = np.meshgrid(x, y)

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_axis_off()

    image = ax.imshow(
        generate_field(X, Y, 0),
        extent=[-9, 9, -9, 9],
        origin="lower",
    )

    title = ax.text(
        0.5,
        1.02,
        "Ob() Field Orbit — Wave → Pattern → Structure",
        transform=ax.transAxes,
        ha="center",
        va="bottom",
        fontsize=12,
    )

    for radius in [2.5, 4.7, 6.8]:
        circle = plt.Circle((0, 0), radius, fill=False, linewidth=0.8, alpha=0.35)
        ax.add_patch(circle)

    ax.scatter([0], [0], s=18)

    def update(frame):
        phase = 2 * np.pi * frame / 72
        image.set_data(generate_field(X, Y, phase))
        title.set_text(f"Ob() Field Orbit — phase {frame:02d}/72")
        return [image, title]

    FuncAnimation(fig, update, frames=72, interval=70, blit=False)
    plt.show()


if __name__ == "__main__":
    run_animation()
