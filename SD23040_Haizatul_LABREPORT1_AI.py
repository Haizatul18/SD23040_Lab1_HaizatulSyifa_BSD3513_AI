import streamlit as st
from collections import deque

# --- Page Title ---
st.title("BFS and DFS Traversal Visualizer")
st.subheader("Lab Report #1 — BSD3513: Introduction to Artificial Intelligence")
st.write("### Topic: Search Algorithms (Breadth-First Search & Depth-First Search)")

# Display picture
st.image("LabReport_BSD2513_#1.jpg", caption="Graph Used for BFS and DFS", use_container_width=True)

# --- Define the Graph (from the given image) ---
graph = {
    'A': ['B', 'D'],
    'B': ['C', 'E', 'G'],
    'C': ['A'],
    'D': ['C'],
    'E': ['H'],
    'F': [],
    'G': ['F'],
    'H': ['F', 'G']
    }

# --- BFS Function ---
def bfs(graph, start):
    visited = []
    queue = deque([start])
    steps = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            steps.append(f"Visited: {node}, Queue: {list(queue)}")
            for neighbour in sorted(graph[node]):  # Alphabetical order
                if neighbour not in visited:
                    queue.append(neighbour)
    return visited, steps


# --- DFS Function ---
def dfs(graph, start, visited=None, steps=None):
    if visited is None:
        visited = []
    if steps is None:
        steps = []

    visited.append(start)
    steps.append(f"Visited: {start}")

    for neighbour in sorted(graph[start]):  # Alphabetical order
        if neighbour not in visited:
            dfs(graph, neighbour, visited, steps)

    return visited, steps


# --- Streamlit Input Section ---
st.write("### Choose Starting Node")
start_node = st.selectbox("Select a node to start traversal:", list(graph.keys()), index=0)

# --- BFS Traversal ---
if st.button("Run Breadth-First Search (BFS)"):
    bfs_result, bfs_steps = bfs(graph, start_node)
    st.success(f"BFS Traversal Order: {' → '.join(bfs_result)}")
    st.write("**Step-by-Step Process:**")
    for step in bfs_steps:
        st.text(step)

# --- DFS Traversal ---
if st.button("Run Depth-First Search (DFS)"):
    dfs_result, dfs_steps = dfs(graph, start_node)
    st.success(f"DFS Traversal Order: {' → '.join(dfs_result)}")
    st.write("**Step-by-Step Process:**")
    for step in dfs_steps:
        st.text(step)

# --- Footer ---
st.write("---")
st.caption("Developed by: [Haizatul Syifa] — [SD23040]")
st.caption("Course: BSD3513 — Introduction to Artificial Intelligence")
