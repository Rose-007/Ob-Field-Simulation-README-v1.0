from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

from field import generate_field


def export_gif(output_path="assets/ob_field_orbit_animation.gif"):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    x = np.linspace(-9, 9, 360)
    y = np.linspace(-9, 9, 360)
    X, Y = np.meshgrid(x, y)

    fig, ax = plt.subplots(figsize=(7, 7), dpi=120)
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

    animation = FuncAnimation(fig, update, frames=72, interval=70, blit=False)
    animation.save(output_path, writer=PillowWriter(fps=14))
    plt.close(fig)
    return output_path


if __name__ == "__main__":
    path = export_gif()
    print(f"Exported: {path}")
