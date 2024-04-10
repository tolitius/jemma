import os, json
import jemma.prompt.tester.test as test
from jemma.tools import say, color

class Tester:
    def __init__(self, role, testing_approach=""):
        self.role = role
        self.testing_approach = testing_approach

    def read_prototype(self, path):
        prototype = {}

        # Read the CSS file
        css_file_path = os.path.join(path, "app.css")
        with open(css_file_path, "r") as css_file:
            prototype["css"] = css_file.read()

        # Read the JavaScript file
        js_file_path = os.path.join(path, "app.js")
        with open(js_file_path, "r") as js_file:
            prototype["js"] = js_file.read()

        # Read the HTML file
        html_file_path = os.path.join(path, "index.html")

        with open(html_file_path, "r") as html_file:
            prototype["html"] = html_file.read()

        return prototype

    def review_prototype(self,
                         thinker,
                         requirements,
                         prototype):
        say("Tester",
            f"reviewing a prototype based on the requirements",
            message_color=color.DARKCYAN)

        review = thinker.think(test.review_code(# self.testing_approach,
                                                self.role,
                                                requirements,
                                                prototype["html"],
                                                prototype["css"],
                                                prototype["js"]),
                                       "Tester")
        return review
