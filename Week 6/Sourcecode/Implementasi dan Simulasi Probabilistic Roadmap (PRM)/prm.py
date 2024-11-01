#!/usr/bin/env python3
import yaml
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from scipy.spatial import KDTree
import os

def load_params(file_path='/home/young/ros2_ws/src/prm_simulation/params.yaml'):
    print(f"Mencoba memuat file: {file_path}")
    print(f"Direktori kerja saat ini: {os.getcwd()}")
    try:
        with open(file_path, 'r') as file:
            params = yaml.safe_load(file)
        return params
    except FileNotFoundError:
        print(f"File tidak ditemukan: {file_path}")
        raise
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        raise

def generate_random_nodes(num_nodes, x_max, y_max):
    nodes = np.random.rand(num_nodes, 2) * [x_max, y_max]
    return nodes

def build_graph(nodes, connection_radius):
    graph = nx.Graph()
    kdtree = KDTree(nodes)
    for i, node in enumerate(nodes):
        neighbors = kdtree.query_ball_point(node, r=connection_radius)
        for neighbor in neighbors:
            if neighbor != i:
                distance = np.linalg.norm(nodes[i] - nodes[neighbor])
                graph.add_edge(i, neighbor, weight=distance)
    return graph

def find_shortest_path(graph, nodes, start, goal):
    start_idx = np.argmin(np.linalg.norm(nodes - start, axis=1))
    goal_idx = np.argmin(np.linalg.norm(nodes - goal, axis=1))
    path = nx.dijkstra_path(graph, start_idx, goal_idx)
    return path

def visualize(nodes, graph, path, start, goal):
    plt.figure()
    plt.title("Probabilistic Roadmap (PRM) dengan Jalur Terpendek")
    for (i, j) in graph.edges:
        plt.plot([nodes[i][0], nodes[j][0]], [nodes[i][1], nodes[j][1]], 'r-', linewidth=0.5)
    plt.plot(nodes[:, 0], nodes[:, 1], 'bo')
    path_coords = nodes[path]
    plt.plot(path_coords[:, 0], path_coords[:, 1], 'y-', linewidth=2)
    plt.plot(start[0], start[1], 'go', markersize=10, label="Start")
    plt.plot(goal[0], goal[1], 'ro', markersize=10, label="Goal")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()

def main():
    params = load_params('params.yaml')
    nodes = generate_random_nodes(params['num_nodes'], params['x_max'], params['y_max'])
    graph = build_graph(nodes, params['connection_radius'])
    path = find_shortest_path(graph, nodes, np.array(params['start']), np.array(params['goal']))
    visualize(nodes, graph, path, params['start'], params['goal'])
    
if __name__ == "__main__":
    main()
