# pybilibangumi

This is a tool for getting bangumi info on [bilibili](https://www.bilibili.com).

## Usage

### Windows

1. Install `python 3` (skip if already done)
2. Open cmd and switch to that direction through `cd $dir$`(your work direction instead of the dollar signs) and type `py3 main.py` or `python3 main.py` or `python main.py`(if no other versions of python exists).

### Linux and MacOS

Refer to above.

## Results

Results will be put in a `.csv` file.

## Tutorial

### 1. `main.py`

Original one writes:
```python
brating.startOver()
```

Function list in `pybilirating.PyBiliRating`:

| Function | Params | Usage | 
| - | - | - | 
| `__init__()` or `PyBiliRating()` | `csv_file_path=None, mode='w', basicInfo=True, show_rating=True, progress=True` | Construct a PyBiliRating object for getting data. |
| `continueOnCsv()` | `start=None, end=None`| Continue writing on an existing csv file. If start or end not specified, continue writing 100 data. **<font color=red>Open the file in `append` mode!!</font>** | 
| `startOver()` | `start=1, end=7000` | Rewrite the file with bangumi data from `start` to `end`. **<font color=red>Open the file in `write` mode!!</font>** | 
| `close()` |  | Closes the file stream. |

### 2. `cmlineutil.progbar`

No API available.