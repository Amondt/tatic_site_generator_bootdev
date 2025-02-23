from textnode import *
from htmlnode import *

def main():
    my_text_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(my_text_node)

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