# Python Data and Log Analysis Exercises

A compact, standard-library-only exercise showing practical use of lists, sets, dictionaries and simple string parsing.

`data_types_log_analysis.py` contains four independent examples:

| Example | What it does |
| --- | --- |
| Damage statistics | Computes total, average and maximum, including the empty-list case |
| Visitor groups | Uses set intersection and difference to classify visitors |
| Product filters | Selects dictionaries whose tag sets contain a requested value |
| Log parsing | Splits selected `key:value` fields from a sample application log line |

## Run

```bash
python data_types_log_analysis.py
```

The script prints all four examples. The log line and product catalog are embedded sample data; this is a collection of exercises, not a deployed analytics system.


## Walk through the four examples

The script starts with a list of sample damage values and computes aggregate statistics. It handles an empty input before dividing for the average. Its visitor example uses set intersection and difference to make overlap explicit. The product example stores records as dictionaries and tests membership in each record's tag collection. The final example splits a structured sample log line into selected fields.

All examples execute from the same `data_types_log_analysis.py` entry point and print their results to the terminal. There is no file input, command-line argument parser or external dependency. To experiment, change the sample lists, sets, product dictionaries or log text in the script and rerun it.

## What to evaluate

This is a deliberately small data-structures exercise. It shows choosing a list for ordered measurements, a set for membership/overlap, and dictionaries for named fields. The parser assumes the shape of the embedded example; it is not a general log ingestion pipeline. The code is most useful as evidence of clean basic Python collection use, while the larger repositories on this profile demonstrate system design.
