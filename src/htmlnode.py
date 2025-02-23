from typing import Self

class HTMLNode():
    def __init__(
            self, 
            tag: str | None = None,
            value: str | None = None,
            children: list[Self] | None = None,
            props: dict | None = None
        ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"{self.__class__.__name__}({self.tag}, {self.value}, children: {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props is None:
            return ""
        s = ""
        for prop in self.props:
            s += f" {prop}=\"{self.props[prop]}\""
        return s
    
class LeafNode(HTMLNode):
    def __init__(
            self,
            tag: str | None,
            value: str,
            props: dict | None = None
        ):
        if value is None:
            raise ValueError("LeafNode must have a value")
        
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if not self.value:
            raise ValueError("invalid HTML: no value")
        
        if self.tag == None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(
            self,
            tag: str,
            children: list[HTMLNode],
            props: dict | None = None
        ):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("invalid Parent: no tag")
        
        if self.children is None:
            raise ValueError("invalid Parent: no children")
        
        s = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            s += child.to_html()
        s += f"</{self.tag}>"

        return s