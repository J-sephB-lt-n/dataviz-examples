"""Example Stacked Vertical Barplot using Matplotlib"""

from typing import Any

metadata: dict[str, Any] = {
    "plot_name": "Bar Plot (Vertical)",
    "plot_aliases": {"Bar Chart (Vertical)"},
    "description": """Chart showing the relationship between a categorical and 
    numeric variable using stacked vertical bars""",
    "tags": {
        "bar",
        "stack",
        "stacked",
        "vertical",
    },
    "frameworks": {"matplotlib"},
}


if __name__ == "__main__":
    # if not installed: "pip install matplotlib"
    from matplotlib import pyplot as plt

    x_axis_labels = ["A", "B", "C", "D"]
    stack1 = [10, 20, 10, 30]
    stack2 = [20, 25, 15, 25]
    stack3 = [5, 10, 15, 20]
    stack_labels = ["cat1", "cat2", "cat3"]

    fig, ax = plt.subplots(figsize=(8, 6))
    # colour reference:
    #   import matplotlib.colors
    #   print(matplotlib.colors.CSS4_COLORS)
    stack_colours = ["red", "green", "blue"]
    bottom = [0] * len(stack1)

    # build the stacked bars #
    for stack_idx, stack_values in enumerate((stack1, stack2, stack3)):
        ax.bar(
            x_axis_labels,
            stack_values,
            bottom=bottom,
            color=stack_colours[stack_idx],
            label=stack_labels[stack_idx],
        )
        for idx, val in enumerate(stack_values):
            bottom[idx] += val

    # label each stack (central label) #
    for bar in ax.patches:
        ax.text(
            bar.get_x() + bar.get_width() / 2,  # x position
            bar.get_y() + bar.get_height() / 2,  # y position
            round(bar.get_height()),  # actual value shown
            ha="center",  # horizontal alignment
            va="center",  # vertical alignment
            color="white",
            weight="bold",
            size=8,
        )
    ax.set_xlabel("This is the X axis")
    ax.set_ylabel("This is the Y axis")
    ax.set_title("This is the Plot Title")
    ax.legend()
    plt.show()
