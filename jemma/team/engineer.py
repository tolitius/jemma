import os, json
from jemma.prompt.engineer.clarify import check_whether_clarification_needed
import jemma.prompt.engineer.code as code
from jemma.tools import say, color

class Engineer:
    def __init__(self, role, implementation_approach=code.default_implementation_approach()):
        self.role = role
        self.implementation_approach = implementation_approach

    def create_prototype(self, thinker, requirements):
        say("Engineer", f"💫 creating a prototype based on the requirements...", message_color=color.DARKCYAN)

        css = thinker.think(code.create_css_file(requirements),
                            "Engineer",
                            mute=True,
                            action="crafting css 🎨 (a.k.a. \"visual beauty\")")

        js = thinker.think(code.create_javascript_file(requirements, css),
                           "Engineer",
                           mute=True,
                           action="cooking javascript 🎮 (a.k.a. \"master of interactions\")")

        html = thinker.think(code.create_html_file(requirements, css, js),
                             "Engineer",
                             mute=True,
                             action="creating html 🕸️ (a.k.a. \"the skeleton of the web\")")

        return {"css": css, "js": js, "html": html}

    def record_prototype(self, path, prototype):
        # Create the directory if it doesn't exist
        os.makedirs(path, exist_ok=True)

        # Write the CSS file
        css_file_path = os.path.join(path, "app.css")
        with open(css_file_path, "w") as css_file:
            css_file.write(prototype["css"])

        # Write the JavaScript file
        js_file_path = os.path.join(path, "app.js")
        with open(js_file_path, "w") as js_file:
            js_file.write(prototype["js"])

        # Write the HTML file
        html_file_path = os.path.join(path, "index.html")
        with open(html_file_path, "w") as html_file:
            html_file.write(prototype["html"])

        print("prototype files created successfully:")
        print(f"- {path}/index.html")
        print(f"- {path}/app.js")
        print(f"- {path}/app.css")

    def refactor_prototype(self,
                           thinker,
                           requirements,
                           prototype,
                           feedback):
        say("Engineer", "💫 refactoring prototype based on the feedback...", message_color=color.DARKCYAN)

        css = thinker.think(code.refactor_css_file(requirements,
                                                   prototype["css"],
                                                   feedback),
                            "Engineer",
                            mute=True,
                            action="♻️  crafting css 🎨 (a.k.a. \"visual beauty\")")

        js = thinker.think(code.refactor_javascript_file(requirements,
                                                         css,
                                                         prototype["js"],
                                                         feedback),
                           "Engineer",
                           mute=True,
                            action="♻️  cooking javascript 🎮 (a.k.a. \"master of interactions\")")

        html = thinker.think(code.refactor_html_file(requirements,
                                                     css,
                                                     js,
                                                     prototype["html"],
                                                     feedback),
                             "Engineer",
                             mute=True,
                             action="♻️  creating html 🕸️ (a.k.a. \"the skeleton of the web\")")

        return {"css": css, "js": js, "html": html}


    def review_user_story(self, thinker, user_story, requirements):
        say("Engineer", f"checking whether clarification is needed for user story: \"{user_story.title}\"",
            message_color=color.DARKCYAN)

        review_result = thinker.think(check_whether_clarification_needed(requirements, user_story), "Engineer")
        return review_result

    def implement_user_story(self,
                             thinker,
                             requirements,
                             user_story = "provide full implementation of this feature",
                             existing_code=""):
        implementation = thinker.think(code.implement_user_story(self.implementation_approach,
                                                                 requirements,
                                                                 user_story,
                                                                 existing_code),
                                       "Engineer")
        return implementation
