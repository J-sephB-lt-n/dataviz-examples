"""Creates a grouped and stacked barplot for visualising the relationship 
between 1 numeric and 2 categorical variables (python + matplotlib)"""

from typing import Any, Final

metadata: dict[str, Any] = {
    "plot_name": "Stacked and Grouped Bar Plot (Vertical)",
    "plot_aliases": {"Stacked and Grouped Bar Chart (Vertical)"},
    "description": """Visualizes the relationship between 1 numeric and 2 
categorical variables""",
    "tags": {
        "bar",
        "stack",
        "stacked",
        "facet",
        "faceted",
        "group",
        "grouped",
        "vertical",
    },
    "frameworks": {"matplotlib"},
    "comments": """The plot is built one stacked block at a time, which is a bit anti-pattern for 
    matplotlib, but makes what the code is doing much more clear.
    """,
}

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    DATA_TO_PLOT: Final[dict[str, Any]] = {
        "group_A": {
            "bar1": {"cat1": 12, "cat2": 16, "cat3": 5, "cat4": 35},
            "bar2": {"cat2": 22, "cat3": 15, "cat4": 11, "cat5": 29},
            "bar3": {"cat1": 11, "cat3": 11, "cat5": 11},
        },
        "group_B": {
            "bar1": {"cat1": 12, "cat2": 16, "cat3": 5, "cat4": 35},
            "bar2": {},
            "bar3": {"cat1": 11, "cat3": 11, "cat5": 11},
        },
        "group_C": {
            "bar1": {"cat1": 12, "cat2": 16, "cat3": 5, "cat4": 35},
            "bar2": {"cat2": 22, "cat3": 8, "cat4": 31, "cat5": 29},
            "bar3": {"cat1": 13, "cat3": 9, "cat5": 4},
        },
        "group_D": {
            "bar1": {},
            "bar2": {"cat2": 9, "cat3": 9, "cat4": 10, "cat5": 25},
            "bar3": {"cat1": 11, "cat3": 11, "cat5": 11},
        },
    }

    # initialize the plot #
    fig, ax = plt.subplots(layout="constrained", figsize=(10, 7))
    # fig, ax = plt.subplots()
    cmap = plt.get_cmap("tab10")  # Specify a colour palette

    # some preliminary calculations #
    bar_names_per_grp: list[str] = [
        "|".join(grp.keys()) for grp in DATA_TO_PLOT.values()
    ]
    assert len(set(bar_names_per_grp)) == 1, "each group must have the same bar names"
    bar_names_in_group = tuple(list(DATA_TO_PLOT.values())[0].keys())
    n_bars_per_group: int = len(bar_names_in_group)
    BAR_PAD: Final[float] = 0.01  # this is taken off both sides of each bar
    BAR_WIDTH: Final[float] = 1.0 / (n_bars_per_group + 2) - (2 * BAR_PAD)
    group_labels = tuple(DATA_TO_PLOT.keys())
    group_positions: list[float] = [idx + 0.5 for idx in range(len(group_labels))]
    bar_label_ref_x_axis: list[tuple[float, str]] = []

    # build a category to colour map #
    unique_cat_names: set[str] = set()
    for grp in DATA_TO_PLOT.values():
        for bar in grp.values():
            for cat in bar.keys():
                unique_cat_names.add(cat)
    n_colours: int = len(unique_cat_names)
    colours: list[tuple[float, float, float, float]] = [
        cmap(idx / n_colours) for idx in range(n_colours)
    ]
    colour_map: dict[str, Any] = {
        cat_name: colours[idx] for idx, cat_name in enumerate(unique_cat_names)
    }

    # draw stacked bars #
    for group_idx, group_contents in enumerate(DATA_TO_PLOT.items()):
        group, bars_in_group = group_contents
        bar_start_position: float = group_idx * 1.0 + BAR_PAD
        for bar_name, cats_in_bar in bars_in_group.items():
            bar_start_position += BAR_WIDTH + (2 * BAR_PAD)
            bar_middle = bar_start_position + BAR_WIDTH / 2
            bar_label_ref_x_axis.append((bar_middle, bar_name))
            cat_start_position: float = 0.0
            for cat_name, cat_value in cats_in_bar.items():
                # draw the block #
                ax.bar(
                    x=[bar_start_position],
                    height=cat_value,
                    width=BAR_WIDTH,
                    bottom=cat_start_position,
                    align="edge",
                    label=cat_name,
                    color=colour_map[cat_name],
                )
                # draw text on the block #
                ax.text(
                    x=bar_start_position + BAR_WIDTH / 2,
                    y=cat_start_position + cat_value / 2,
                    s=cat_value,
                    ha="center",
                    va="center",
                    color="white",
                )
                cat_start_position += cat_value

    # add group X axis labels #
    ax.set_xticks(group_positions, [f"\n{lab}" for lab in group_labels])

    # add bar X axis labels #
    for x_pos, lab in bar_label_ref_x_axis:
        ax.text(
            x=x_pos,
            y=0,
            s=f"\n{lab}",
            ha="center",
            va="center",
        )
    # ax.set_xticks(
    #     [entry[0] for entry in bar_label_ref_x_axis],
    #     [entry[1] for entry in bar_label_ref_x_axis],
    # )

    # add axis and title labels #
    ax.set_title("Stacked and Grouped Bar Plot (matplotlib)")
    ax.set_xlabel("This is the X Axis")
    ax.set_ylabel("This is the Y Axis")

    ax_handles, ax_labels = ax.get_legend_handles_labels()
    unique = [
        (h, l)
        for i, (h, l) in enumerate(zip(ax_handles, ax_labels))
        if l not in ax_labels[:i]
    ]
    ax.legend(*zip(*unique))

    fig.show()

# pylint: disable=pointless-string-statement
"""
Here is some code for validating that the methodology is robust.
It generates different random input data for the plotting function.

import random

min_y: int = 10
max_y: int = 100
bar_present_prob: float = 0.8
cat_present_prob: float = 0.5
n_grps: int = random.randint(2, 7)
n_bars: int = random.randint(2, 7)
n_cats: int = random.randint(2, 10)
grp_names: list[str] = [f"grp_{idx}" for idx in range(n_grps)]
bar_names: list[str] = [f"b{idx}" for idx in range(n_bars)]
cat_names: list[str] = [f"cat{idx}" for idx in range(n_cats)]
DATA_TO_PLOT: dict[str, Any] = {}
for grp in grp_names:
    DATA_TO_PLOT[grp] = {}
    for bar in bar_names:
        DATA_TO_PLOT[grp][bar] = {}
        if random.uniform(0, 1) < bar_present_prob:
            for cat_name in cat_names:
                if random.uniform(0, 1) < cat_present_prob:
                    DATA_TO_PLOT[grp][bar][cat_name] = random.randint(min_y, max_y)
"""
