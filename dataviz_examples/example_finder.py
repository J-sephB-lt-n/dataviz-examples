"""Defines the base ExampleFinder class"""

import importlib
import os
import re
from typing import Any


class ExampleFinder:
    """
    example_finder = ExampleFinder()
    for example in example_finder.all_examples:
        print(example)
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

    def search(self) -> list[Any]:
        """docstring TODO"""
        return ["still", "to", "do"]
