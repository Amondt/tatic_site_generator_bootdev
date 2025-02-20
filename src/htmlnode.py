from typing import Self

class HTMLNode():
    def __init__(
            self, tag: str | None = None,
            value: str | None = None,
            children: list[Self] | None = None,
            props: dict | None = None
        ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"{self.__class__.__name__}({self.tag}, {self.value}, children:{self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        s = ""
        for prop in self.props:
            s += f" {prop}=\"{self.props[prop]}\""
        return s