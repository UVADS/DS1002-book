from docutils.parsers.rst.directives.admonitions import Admonition

class Practice(Admonition):
    def run(self):
        # Manually add a "tip" class to style it
        if "class" not in self.options:
            self.options["class"] = ["tip"]
        else:
            self.options["class"].append("tip")
        # Add `Example` to the title so we don't have to type it
        self.arguments[0] = f"Example: {self.arguments[0]}"
        # Now run the Admonition logic so it behaves the same way
        nodes = super().run()
        return nodes

def setup(app):
    app.add_directive("Practice", Practice)
