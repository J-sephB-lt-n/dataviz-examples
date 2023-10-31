"""Example Stacked Vertical Barplot using Matplotlib"""

from typing import Any

metadata: dict[str, Any] = {
    "plot_name": "Stacked Bar Plot (Vertical) with Guide Lines",
    "plot_aliases": {"Stacked Bar Chart (Vertical) with Guide Lines"},
    "description": """Chart showing the relationship between a categorical and 
    numeric variable using stacked vertical bars, with lines joining
    the same category between bars""",
    "tags": {
        "bar",
        "guide",
        "guideline",
        "guidelines",
        "join",
        "joined",
        "joining",
        "line",
        "lines",
        "stack",
        "stacked",
        "vertical",
    },
    "frameworks": {"matplotlib"},
    "comments": """When showing this to people, the guiding lines are too
often interpreted as line charts, so I wouldn't recommend using this plot.""",
}


if __name__ == "__main__":
    # if not installed: "pip install matplotlib"
    from matplotlib import pyplot as plt

    BAR_WIDTH: float = 0.3
    x_axis_labels = ["bar_A", "bar_B", "bar_C", "bar_D"]
    stacks: dict[str, list[int | float]] = {
        "cat1": [6, 10, 0, 14],
        "cat2": [13, 9, 13, 15],
        "cat3": [11, 4, 1, 17],
        "cat4": [4, 16, 7, 19],
        "cat5": [19, 1, 18, 4],
    }
    assert (
        len({len(stack) for stack in stacks.values()}) == 1
    ), "all stacks must be specified by series of the same length"

    colormap = plt.get_cmap("tab10")
    colours: list[tuple[float, ...]] = [
        colormap(i % colormap.N) for i in range(len(stacks))
    ]
    stacks_colour_ref: dict[str, tuple[float, ...]] = {
        cat: colours[idx] for idx, cat in enumerate(stacks)
    }

    fig, ax = plt.subplots(figsize=(8, 6))
    bottom: list[int | float] = [0] * len(list(stacks.values())[0])

    # build the stacked bars #
    for stack_name, stack_values in stacks.items():
        ax.bar(
            x_axis_labels,
            stack_values,
            bottom=bottom,
            label=stack_name,
            color=stacks_colour_ref[stack_name],
            width=BAR_WIDTH,
        )
        for idx, val in enumerate(stack_values[:-1]):
            ax.plot(
                [idx + BAR_WIDTH / 2, idx + 1 - BAR_WIDTH / 2],
                [bottom[idx] + val / 2, bottom[idx + 1] + stack_values[idx + 1] / 2],
                alpha=0.7,
                color=stacks_colour_ref[stack_name],
                linestyle="dashed",
            )
        for idx, val in enumerate(stack_values):
            bottom[idx] += val

    ax.set_title("Stacked Bar Plot (Vertical) with Guide Lines")
    ax.legend()

    # remove some plot elements #
    for side in ("top", "right", "left"):
        ax.spines[side].set_color("none")
    ax.axhline(0, color="white", alpha=1.0)
    ax.set_yticks([])

    fig.show()
