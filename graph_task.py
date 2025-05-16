import argparse
import networkx as nx
import matplotlib.pyplot as plt


def get_adj_matrix(graph):
    adj_matrix = nx.to_numpy_array(graph)
    print("Adjacency Matrix:")
    print(adj_matrix)

    return adj_matrix


def visualize_graph(graph, layout="shell"):
    layout_functions = {
        "circular": nx.circular_layout,
        "spring": nx.spring_layout,
        "spiral": nx.spiral_layout,
        "spectral": nx.spectral_layout,
        "shell": nx.shell_layout,
        "kamada_kawai": nx.kamada_kawai_layout,
    }

    if layout not in layout_functions:
        print(
            f"Warning: Layout '{layout}' not recognized. Using 'shell' layout instead."
        )
        layout = "shell"

    pos = layout_functions[layout](graph)
    nx.draw(graph, pos, with_labels=True, node_color="lightblue", edge_color="gray")
    plt.show()


def creat_graph(a, b, c, visualize=True, layout="shell"):
    if not 0 < a <= b <= c:
        print("Invalid Input!")
        return

    left = nx.complete_graph(c + 1)
    right = nx.complete_graph(c + 1)

    combined_graph = nx.disjoint_union(left, right)

    for i in range(a):
        combined_graph.add_edge(i, c + 1 + i)

    diff = b - a
    for j in range(1, diff + 1):
        combined_graph.add_edge(i, c + 1 + i + j)

    # Get Adjacency Matrix
    get_adj_matrix(combined_graph)

    # Visualize the graph
    if visualize:
        visualize_graph(combined_graph, layout)


def main():
    parser = argparse.ArgumentParser(description="Create and analyze graph structures with specific properties.")
    
    parser.add_argument("a", type=int, help="Number of direct connections between corresponding nodes")
    parser.add_argument("b", type=int, help="Total number of connections from first node (includes a)")
    parser.add_argument("c", type=int, help="Size of each complete graph (c+1 nodes in each)")
    parser.add_argument("--no-viz", action="store_true", help="Skip graph visualization")
    parser.add_argument(
        "--layout",
        type=str,
        default="shell",
        choices=["circular", "spring", "spiral", "spectral", "shell", "kamada_kawai"],
        help="Layout algorithm for graph visualization",
    )

    args = parser.parse_args()

    creat_graph(
        args.a,
        args.b,
        args.c,
        visualize=not args.no_viz,
        layout=args.layout,
    )

if __name__ == "__main__":
    main()