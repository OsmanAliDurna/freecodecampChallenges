text = """Shopping List"""

print(text.title().replace(" ", "").replace("(", "").replace(")", "").replace('"', "").replace("?", "").replace("-", "").replace("!", "").replace("'", "").replace(",", "").replace(":", "") +
      ".js")
