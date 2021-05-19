text = """Updating Object Properties"""

print(text.title().replace(" ", "").replace("(", "").replace(")", "").replace('"', "").replace("?", "").replace(".", "").replace("-", "").replace("!", "").replace("'", "").replace(",", "").replace(":", "") +
      ".js")
