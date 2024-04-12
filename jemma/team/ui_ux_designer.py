import json
from jemma.tools import read_file, say, color
import jemma.prompt.ui.designer as prompt

class UiUxDesigner:
    def __init__(self, role, title="UI/UX Designer"):
        self.role = role
        self.title = title

    def idea_with_sketch_to_design(self,
                                   thinker,
                                   requirements,
                                   sketch):
        say(self.title, "🔍 collecting intel about the sketch ...", message_color=color.DARKCYAN)
        return thinker.see(prompt.idea_with_sketch_to_css(requirements),
                           sketch,
                           self.title)

    def design_to_layout(self,
                         thinker,
                         requirements,
                         css,
                         sketch):
        say(self.title, "🎨 designing a layout based on sketch's beauty ...", message_color=color.DARKCYAN)
        return thinker.see(prompt.css_to_html(requirements, css),
                           sketch,
                           self.title)

    def sketch_to_prototype(self,
                            thinker,
                            requirements,
                            sketch):

        css = self.idea_with_sketch_to_design(thinker,
                                              requirements,
                                              sketch)
        print(f"design: {css}")
        html = self.design_to_layout(thinker,
                                     requirements,
                                     css,
                                     sketch)
        print(f"html: {html}")

        return {"css": css, "js": "", "html": html}

    def skech_to_description(self,
                             thinker,
                             sketch,
                             focus):

        say(self.title, "🎨 looking at the sketch very closely now ...", message_color=color.DARKCYAN)
        return thinker.see(prompt.sketch_to_description(focus),
                           sketch,
                           self.title)
