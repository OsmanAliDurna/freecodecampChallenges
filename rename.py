text = """Testing Objects for Properties"""

print(text.title().replace(" ", "").replace("(", "").replace(")", "").replace('"', "").replace("?", "").replace(".", "").replace("-", "").replace("!", "").replace("'", "").replace(",", "").replace(":", "") +
      ".js")
