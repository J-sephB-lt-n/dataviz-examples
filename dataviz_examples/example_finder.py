"""Defines the base ExampleFinder class"""

import importlib
import os
import re
from typing import Any


class ExampleFinder:
    """
    Example Usage
    -------------
    >>> example_finder = ExampleFinder()
    >>> example_finder.print_all_example_names()
    ...
    >>> example_finder.search_by_tags("colour by sign")
    2  Line Plot Coloured by Sign  [python]  {'matplotlib'}
    >>> example_finder.print_example_metadata(2)
    PLOT_NAME      Line Plot Coloured by Sign
    PLOT_ALIASES   {'Line Plot Coloured by Threshold'}
    DESCRIPTION    Line plot which changes colour based on sign
        (also includes transparent bar chart underneath)
    TAGS           {'dynamic', 'sign', 'colour', 'line', 'threshold'}
    FRAMEWORKS     {'matplotlib'}
    LANGUAGE       python
    >>> print( example_finder.get_example_code(2) )
    ...
    >>> exec( example_finder.get_example_code(2) )
    ...
    """

    def __init__(self) -> None:
        """Code run on creation of class instance"""
        self.all_examples: list[dict[str, Any]] = []
        self.fetch_all_examples()

    def fetch_all_examples(self) -> None:
        """Collects all of the example scripts and store their code and metadata in
        master lookup dictionary self.all_examples
        """
        for language in ("python", "R"):
            for script_name in [
                filename
                for filename in os.listdir(language)
                if ".py" in filename or ".r" in filename
            ]:
                module_path: str = language + "." + re.sub(r"\.\w+$", "", script_name)
                module = importlib.import_module(module_path)
                example: dict[str, Any] = getattr(module, "metadata")
                example["language"] = language
                with open(f"{language}/{script_name}", "r", encoding="utf-8") as file:
                    example["code"] = file.read()
                self.all_examples.append(example)

    def print_all_example_names(self) -> None:
        """docstring TODO"""
        for idx, example in enumerate(self.all_examples):
            print(
                f'{idx}  {example["plot_name"]}  [{example["language"]}]  {example["frameworks"]}'
            )

    def search_by_tags(self, search_str: str) -> None:
        """docstring TODO"""
        search_words: set[str] = set(search_str.lower().split())
        matches_found: dict[str, dict[str, Any]] = {}
        for example_idx, example in enumerate(self.all_examples):
            tags_matched: set[str] = example["tags"].intersection(search_words)
            if len(tags_matched) > 0:
                matches_found[example["plot_name"]] = {
                    "index": example_idx,
                    "n_tags_matched": len(tags_matched),
                    "language": example["language"],
                    "frameworks": example["frameworks"],
                }

        # sort search results by number of matched tags #
        matches_found = dict(
            sorted(
                matches_found.items(),
                key=lambda x: x[1]["n_tags_matched"],
                reverse=True,
            )
        )
        if len(matches_found) == 0:
            print("< no examples found >")
        else:
            for example_name, example_info in matches_found.items():
                print(
                    f'{example_info["index"]}  {example_name}  [{example_info["language"]}]  {example_info["frameworks"]}'  # pylint: disable=line-too-long
                )

    def print_example_metadata(self, example_idx: int) -> None:
        """docstring TODO"""
        if example_idx < 0 or example_idx > len(self.all_examples) - 1:
            raise NameError(f"example index {example_idx} does not exist")
        for key, value in self.all_examples[example_idx].items():
            if key != "code":
                print(f"{key.upper():15}{value}")

    def get_example_code(self, example_idx: int) -> str:
        """docstring TODO"""
        if example_idx < 0 or example_idx > len(self.all_examples) - 1:
            raise NameError(f"example index {example_idx} does not exist")
        return self.all_examples[example_idx]["code"]
