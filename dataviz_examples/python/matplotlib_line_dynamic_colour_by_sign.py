"""Example of Line Plot Dynamically Coloured by Sign, using Matplotlib"""

from typing import Any

metadata: dict[str, Any] = {
    "plot_name": "Line Plot Coloured by Sign",
    "plot_aliases": {"Line Plot Coloured by Threshold"},
    "description": """Line plot which changes colour based on which side of 0 the value falls on 
    (also includes transparent bar chart underneath)""",
    "tags": {"colour", "dynamic", "line", "sign", "threshold"},
    "frameworks": {"matplotlib"},
}

if __name__ == "__main__":
    import random
    import matplotlib.pyplot as plt

    # generate some random data to plot #
    x_values = sorted(random.sample(range(50), k=20))
    y_values = [random.uniform(-100, 100) for _ in range(len(x_values))]

    # initialize plot #
    fig, ax = plt.subplots(figsize=(10, 5))

    # plot the bar charts #
    ax.bar(
        x_values,
        y_values,
        color=["blue" if y >= 0 else "red" for y in y_values],
        alpha=0.2,
    )

    # draw in the line segments #
    for idx, x, y in zip(range(len(x_values[:-1])), x_values[:-1], y_values[:-1]):
        next_x = x_values[idx + 1]
        next_y = y_values[idx + 1]
        if y >= 0 and next_y >= 0:
            ax.plot([x, next_x], [y, next_y], color="blue")
        elif y < 0 and next_y < 0:
            ax.plot([x, next_x], [y, next_y], color="red")
        elif y < 0 <= next_y:
            # line segments change colour on either side of y=0 #
            slope = (next_y - y) / (next_x - x)
            y_intercept = y - slope * x
            x_intercept = -y_intercept / slope  # y = mx + c
            ax.plot([x, x_intercept], [y, 0], color="red")
            ax.plot([x_intercept, next_x], [0, next_y], color="blue")
        else:
            # line segments change colour on either side of y=0 #
            slope = (next_y - y) / (next_x - x)
            y_intercept = y - slope * x
            x_intercept = -y_intercept / slope  # y = mx + c
            ax.plot([x, x_intercept], [y, 0], color="blue")
            ax.plot([x_intercept, next_x], [0, next_y], color="red")

    ax.set_xlabel("This is the X Axis")
    ax.set_ylabel("This is the Y Axis")
    ax.set_title("Line Chart Coloured by Sign")
