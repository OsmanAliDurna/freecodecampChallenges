text = """Global Scope and Functions"""

print(text.title().replace(" ", "").replace("(", "").replace(")", "").replace('"', "").replace("?", "").replace("-", "").replace("!", "").replace("'", "").replace(",", "").replace(":", "") +
      ".js")
