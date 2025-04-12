import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "div",
            "Hi World!",
            None,
            {"class": "greetings", "href": "https://boot.dev"}
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greetings" href="https://boot.dev"'
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "Hello World!"
        )
        self.assertEqual(
            node.tag,
            "div"
        )
        self.assertEqual(
            node.value,
            "Hello World!",
        )
        self.assertEqual(
            node.children,
            None
        )
        self.assertEqual(
            node.props,
            None
        )
    
    def test_repr(self):
        node = HTMLNode(
            "p",
            "Beautiful World!",
            None,
            {"class": "primary"}
        )
        self.assertEqual(
            repr(node),
            "HTMLNode(p, Beautiful World!, None, {'class': 'primary'})"
        )