import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


node_coordinates = [(0, 0), (1, 1), (0, 2), (1, 3)]

adjacency_matrix = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]

for x, y in node_coordinates:
    plt.scatter(x, y, c='b', s=400)

for i in range(len(adjacency_matrix)):
    for j in range(i, len(adjacency_matrix)):
        if adjacency_matrix[i][j] == 1:
            x1, y1 = node_coordinates[i]
            x2, y2 = node_coordinates[j]
            plt.plot([x1, x2], [y1, y2], 'k-')
plt.show()

for i, (x, y) in enumerate(node_coordinates):
    plt.scatter(x, y, c='c', s=400)
    plt.text(x, y, str(i+1), fontsize=10, color='r', ha='left', va='top')

for i in range(len(adjacency_matrix)):
    for j in range(i, len(adjacency_matrix)):
        if adjacency_matrix[i][j] == 1:
            x1, y1 = node_coordinates[i]
            x2, y2 = node_coordinates[j]
            plt.plot([x1, x2], [y1, y2], 'k-')

adjacency_matrix = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]

edges = []
num_nodes = len(adjacency_matrix)
for i in range(num_nodes):
    for j in range(i + 1, num_nodes):
        if adjacency_matrix[i][j] == 1:
            edges.append((i, j))

G = nx.Graph(edges)
nx.draw(G, with_labels=True, node_size=200, node_color='lightblue')
plt.show()

adjacency_matrix = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]

edges = []
num_nodes = len(adjacency_matrix)
for i in range(num_nodes):
    for j in range(i + 1, num_nodes):
        if adjacency_matrix[i][j] == 1:
            edges.append((i, j))

G = nx.Graph(edges)
nx.draw(G, with_labels=True, node_size=200, node_color='lightblue')
plt.show()

import plotly.graph_objs as go

adjacency_matrix = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]

nodes = [str(i) for i in range(len(adjacency_matrix))]

edges = []

for i in range(len(adjacency_matrix)):
    for j in range(i + 1, len(adjacency_matrix)):
        if adjacency_matrix[i][j] == 1:
            edges.append((i, j))

node_x = [0, 1, 0, 1]
node_y = [0, 1, 2, 3]

edge_x = []
edge_y = []

for edge in edges:
    x0, y0 = node_x[edge[0]], node_y[edge[0]]
    x1, y1 = node_x[edge[1]], node_y[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        colorscale='YlGnBu',
        size=10,
        colorbar=dict(
            thickness=15,
            title='Node Connections',
            xanchor='left',
            titleside='right'
        ),
    )
)

node_text = nodes

node_trace.text = node_text

fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=0, l=0, r=0, t=0),
                ))

fig.show()

