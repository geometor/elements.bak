import os

def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def create_file_with_docstring(file_path, docstring):
    with open(file_path, 'w') as f:
        f.write('\'\'\'\n')
        f.write(docstring)
        f.write('\n\'\'\'')

elements_base_path = 'elements'
elements_pkg_path = os.path.join(elements_base_path, 'elements_pkg')

directories = [
    os.path.join(elements_pkg_path, 'data', 'json_data'),
    os.path.join(elements_pkg_path, 'data', 'raw_data'),
    os.path.join(elements_pkg_path, 'data', 'processed_data'),
    os.path.join(elements_pkg_path, 'embeddings'),
    os.path.join(elements_pkg_path, 'embeddings', 'embeddings_models'),
    os.path.join(elements_pkg_path, 'fine_tuning'),
    os.path.join(elements_pkg_path, 'fine_tuning', 'fine_tuned_models'),
    os.path.join(elements_pkg_path, 'graph_db'),
    os.path.join(elements_pkg_path, 'milvus_db'),
    os.path.join(elements_pkg_path, 'visualization'),
    os.path.join(elements_pkg_path, 'euclid_bot'),
    os.path.join(elements_pkg_path, 'utils')
]

for directory in directories:
    create_directory(directory)

files_with_docstrings = {
    os.path.join(elements_base_path, 'main.py'): 'Main script for the Elements project.',
    os.path.join(elements_pkg_path, 'data', '__init__.py'): '',
    os.path.join(elements_pkg_path, 'embeddings', 'embeddings_generation.py'): 'Embeddings generation module.',
    os.path.join(elements_pkg_path, 'embeddings', '__init__.py'): '',
    os.path.join(elements_pkg_path, 'fine_tuning', 'fine_tuning.py'): 'Fine-tuning module.',
    os.path.join(elements_pkg_path, 'fine_tuning', '__init__.py'): '',
    os.path.join(elements_pkg_path, 'graph_db', 'neo4j_connection.py'): 'Neo4j connection module.',
    os.path.join(elements_pkg_path, 'graph_db', 'neo4j_queries.py'): 'Neo4j queries module.',
    os.path.join(elements_pkg_path, 'graph_db', 'neo4j_setup.py'): 'Neo4j setup module.',
    os.path.join(elements_pkg_path, 'graph_db', '__init__.py'): '',
    os.path.join(elements_pkg_path, 'milvus_db', 'milvus_connection.py'): 'Milvus connection module.',
    os.path.join(elements_pkg_path, 'milvus_db', 'milvus_queries.py'): 'Milvus queries module.',
    os.path.join(elements_pkg_path, 'milvus_db', '__init__.py'): '',
    os.path.join(elements_pkg_path, 'visualization', 'network_visualization.py'): 'Network visualization module.',
    os.path.join(elements_pkg_path, 'visualization', 'embedding_visualization.py'): 'Embedding visualization module.',
    os.path.join(elements_pkg_path, 'visualization', '__init__.py'): '',
    os.path.join(elements_pkg_path, 'euclid_bot', 'bot_main.py'): 'EuclidBot main module.',
    os.path.join(elements_pkg_path, 'euclid_bot', 'bot_nlp.py'): 'EuclidBot NLP module.',
    os.path.join(elements_pkg_path, 'euclid_bot', 'bot_responses.py'): 'EuclidBot responses module.',
    os.path.join(elements_pkg_path, 'euclid_bot', 'bot_utils.py'): 'EuclidBot utilities module.',
    os.path.join(elements_pkg_path, 'euclid_bot', '__init__.py'): '',
    os.path.join(elements_pkg_path, 'utils', 'data_preparation.py'): 'Data preparation utilities module.',
    os.path.join(elements_pkg_path, 'utils', 'pattern_discovery.py'): 'Pattern discovery utilities module.',
    os.path.join(elements_pkg_path, 'utils', '__init__.py'): ''
}

for file_path, docstring in files_with_docstrings.items():
    create_file_with_docstring(file_path, docstring)

