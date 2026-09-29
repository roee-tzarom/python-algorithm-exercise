# Python Data and Log Analysis

A compact Python collection showing how lists, sets and dictionaries solve different data-handling problems. All examples run from a single standard-library script and print their results in the terminal.

## What the code does

| Component | Input | Result |
| --- | --- | --- |
| `analyze_damage` | List of numeric hits | Total, average and maximum; handles an empty list |
| Visitor comparison | Two sets of IDs | Unique visitors, overlap and difference |
| `get_products_with_tag` | Product dictionaries and a tag | Matching products |
| Log parser | One structured sample line | Readable key/value summary |

The examples demonstrate choosing data structures by operation: a list for ordered measurements, sets for membership and overlap, and dictionaries for named product or log fields.

## Run

Python 3 is the only requirement:

```bash
python data_types_log_analysis.py
```

The script executes the log, damage, visitor and product demonstrations in sequence. For example, the product filter selects entries whose `tags` set contains `drink`; the log parser splits selected `key:value` fields from the embedded sample line.

## Code tour

`data_types_log_analysis.py` contains the complete implementation. Each demonstration has its own function, so a reader can inspect one idea at a time. The two reusable functions, `analyze_damage` and `get_products_with_tag`, are separate from the printing examples.

This is intentionally a small, self-contained data-processing sample. It uses embedded input and does not read external logs, accept command-line arguments or implement a general log ingestion pipeline.
