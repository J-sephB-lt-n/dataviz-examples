# dataviz-examples
    
A searchable database of code examples for common data visualizations in multiple coding languages. 

All of the examples are in the [/dataviz_examples/](./dataviz_examples/) folder.

There are not many examples yet, but I continue to add more every week - please feel free to add to the collection with a pull request and I will add it (any coding language).

I built this package because I like to quickly try different data visualizations without having to leave my IDE, and also because I don't like doing the same task more than once. 

The search functionality (currently very basic) is implemented in python. 

Example usage:

```python
>>> example_finder = ExampleFinder()
>>> example_finder.print_all_example_names()
< prints out names of all available code examples >
>>> example_finder.search_by_tags("colour by sign")
2  Line Plot Coloured by Sign  [python]  {'matplotlib'}
>>> example_finder.print_example_metadata(2)
PLOT_NAME      Line Plot Coloured by Sign
PLOT_ALIASES   {'Line Plot Coloured by Threshold'}
DESCRIPTION    Line plot which changes colour based on which side of 0 the value falls on 
    (also includes transparent bar chart underneath)
TAGS           {'dynamic', 'sign', 'colour', 'line', 'threshold'}
FRAMEWORKS     {'matplotlib'}
LANGUAGE       python
>>> print( example_finder.get_example_code(2) )
< prints out code to generate this plot >
>>> exec( example_finder.get_example_code(2) )
```
![](./docs/line_chart_coloured_by_sign.png)
