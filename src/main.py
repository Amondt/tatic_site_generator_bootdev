from textnode import *
from htmlnode import *
from converters import *

def main():
    my_bold_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(my_bold_node)

    my_text_node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
    text_node_to_html_node(my_text_node)

    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    print(new_nodes)

    # Create a test structure with different types of nodes
    test_node = ParentNode("div", [
        LeafNode("span", "Hello"),
        ParentNode("p", []),
        LeafNode("span", "World")
    ])
    
    # Add prints in your ParentNode.to_html() method like:
    # for child in self.children:
    #     print(f"Processing child: {type(child)}")
    #     s += child.to_html()
    
    print("\nTesting to_html output:")
    try:
        result = test_node.to_html()
        print(result)
    except TypeError as e:
        print(f"Error occurred: {e}")

main()