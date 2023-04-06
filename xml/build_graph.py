import os
import json
import glob
import networkx as nx
from networkx.readwrite import json_graph
import pydot
import matplotlib.pyplot as plt

def render_graph_with_matplotlib(graph, output_file='graph.png', k=1.5):
    plt.figure(figsize=(30, 30))
    pos = nx.spring_layout(graph, k=k, seed=42)  # Increasing the k value will place nodes farther apart
    nx.draw(graph, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=12)
    plt.savefig(output_file)


def read_json_files(folder='export'):
    files = glob.glob(os.path.join(folder, '*.json'))
    json_data = []

    for file_path in files:
        with open(file_path, 'r') as file:
            data = json.load(file)
            json_data.append(data)

    return json_data


def build_dependency_graph(json_data):
    graph = nx.DiGraph()

    for element in json_data:
        element_id = element['id']
        graph.add_node(element_id)

        for proof_step in element.get('proof', []):
            refs = proof_step['refs']
            for ref in refs:
                graph.add_edge(element_id, ref)

    return graph


def export_graph_to_dot(graph, output_file='dependency_graph.dot'):
    dot_graph = pydot.Dot(graph_type='digraph')

    for node in graph.nodes():
        dot_graph.add_node(pydot.Node(node))

    for edge in graph.edges():
        dot_graph.add_edge(pydot.Edge(edge[0], edge[1]))

    with open(output_file, 'w') as dot_file:
        dot_file.write(dot_graph.to_string())


def export_graph_to_json(graph, output_file='dependency_graph.json'):
    data = json_graph.node_link_data(graph)
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    json_data = read_json_files('export')
    dependency_graph = build_dependency_graph(json_data)
    export_graph_to_json(dependency_graph)
    export_graph_to_dot(dependency_graph)
    render_graph_with_matplotlib(dependency_graph)

