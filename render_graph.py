from graphviz import Digraph

from scg_dependency_graph.constants.item_category import Category
from scg_dependency_graph.constants.item_type import Type

def get_shape(item):
    return {
        Type.COMMERCIAL: 'diamond',
        Type.INDUSTRIAL: 'box'
    }.get(item.type, 'ellipse')

def get_color(item):
    return {
        Category.FACTORY_MADE: 'red',
        Category.BUILDING_SUPPLIES: 'blue',
        Category.HARDWARE_STORE: 'green',
        Category.GARDENING_SUPPLIES: 'yellow',
        Category.FARMERS_MARKET: 'purple',
    }.get(item.category, 'grey')

def render_di_graph(items):
    dot = Digraph()
    dot.attr(rankdir='BT')
    dot.attr(layout='dot')

    subgraphs = dict()

    for item in items:
        # dot.subgraph(item.category.name)
        # dot.node(item.name, item.name, shape=get_shape(item), color=get_color(item))
        if item.category.name not in subgraphs:
            subgraphs[item.category.name] = Digraph(name=item.category.name)
            subgraphs[item.category.name].attr(label=item.category.name)

        subgraphs[item.category.name].node(item.name, item.name, shape=get_shape(item), color=get_color(item))

    for subgraph in subgraphs.values():
        dot.subgraph(subgraph)

    for item in items:
        if item.dependencies:
            for key, value in item.dependencies.items():
                dot.edge(key.name, item.name, str(value))

    dot.render('graph', format='png', view=True)