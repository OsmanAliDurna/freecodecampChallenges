text = """Escaping Literal Quotes in Strings"""

print(text.title().replace(" ", "").replace('"', "").replace("?", "").replace("!", "").replace("'", "").replace(",", "").replace(":", "") +
      ".js")
