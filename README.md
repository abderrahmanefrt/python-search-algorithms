# Graph Algorithms in Python

This repository contains implementations of common **graph algorithms** in Python.  
Each algorithm includes example graphs and step-by-step output to illustrate how it works.

## 📌 Implemented Algorithms
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- (More coming soon: Dijkstra, A*, Topological Sort, etc.)

## 🚀 Example (BFS)

```python
from bfs import Bfs

graph = {
    'A': ['B', 'D'],
    'B': ['C', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': ['J'],
    'J': ['K'],
    'K': []
}

def successor(node):
    return graph.get(node, [])

Bfs('A', successor, 'K')
✅ Output
yaml
Copier le code
Visite: A
Visite: B
Visite: D
Visite: C
Visite: E
Visite: F
Visite: J
Visite: K
Goal found: K
📂 Structure
sql
Copier le code
graph-algorithms-python/
│
├── bfs.py      # Breadth-First Search
├── dfs.py      # Depth-First Search
├── README.md   # Documentation
🛠 Requirements
Python 3.x

📖 Usage
Clone the repo:

bash
Copier le code
git clone https://github.com/your-username/graph-algorithms-python.git
cd graph-algorithms-python
Run an algorithm:

bash
Copier le code
python bfs.py
yaml
Copier le code

---

👉 Do you want me to **prepare the repo structure with `bfs.py`, `dfs.py`, and README.md` as actual files** so
