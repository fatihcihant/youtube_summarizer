from graphviz import Digraph
import matplotlib.pyplot as plt
import re

def generate_diagram(description, output_file='diagram.png'):
    """Generate a diagram based on the description."""
    # Simple heuristic to decide diagram type
    if 'flowchart' in description.lower():
        return generate_flowchart(description, output_file)
    else:
        return generate_concept_map(description, output_file)

def generate_flowchart(description, output_file):
    """Generate a flowchart using graphviz."""
    dot = Digraph(comment='Flowchart')
    # Parse description for nodes and edges (simplified)
    nodes = re.findall(r'Node: (\w+)', description) or ['Step1', 'Step2', 'Step3']
    edges = re.findall(r'Edge: (\w+) -> (\w+)', description) or [('Step1', 'Step2'), ('Step2', 'Step3')]
    
    for node in nodes:
        dot.node(node, node)
    for start, end in edges:
        dot.edge(start, end)
    
    dot.render(output_file, format='png', cleanup=True)
    return output_file

def generate_concept_map(description, output_file):
    """Generate a concept map using matplotlib (placeholder)."""
    plt.figure(figsize=(8, 6))
    plt.text(0.5, 0.5, "Concept Map\n(Based on description)", ha='center', va='center')
    plt.axis('off')
    plt.savefig(output_file, bbox_inches='tight')
    plt.close()
    return output_file