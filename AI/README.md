# AI

Course work for the Artificial Intelligence course. This repo follows the assignment roadmap step by step.

## What's inside

| Folder / file | What it is |
|---|---|
| `Test.py` | First test file made in VS Code to check Python runs |
| `python_course/` | Python practice from basics up to file handling (10 files) |
| `matplotlib_practice/` | Line, bar, scatter, pie, histogram and subplot examples, with saved images in `plots/` |
| `bfs_traversal/BFS_Traversal.ipynb` | Google Colab notebook: input tree/graph → BFS code → traversal output |
| `bfs_traversal/bfs.py` | Same BFS code as a normal Python script |

## Python course order

1. Variables and data types
2. Operators and conditions
3. Loops
4. Strings
5. Lists and tuples
6. Dictionaries and sets
7. Functions
8. Modules and exceptions
9. Classes and objects
10. File handling

## BFS result

Input tree:

```
            A
          /   \
         B     C
        / \   / \
       D   E F   G
      /
     H
```

Output: `A -> B -> C -> D -> E -> F -> G -> H`

Graph from node 0: `0 -> 1 -> 2 -> 3 -> 4 -> 5`

## How to run

Python 3.11 / 3.12 / 3.13 and VS Code.

```bash
pip install -r requirements.txt
python Test.py
python python_course/10_file_handling.py
python matplotlib_practice/matplotlib_basics.py
python bfs_traversal/bfs.py
```

To open the notebook in Colab: go to colab.research.google.com → File → Open notebook → GitHub tab, and paste this repo's link.
