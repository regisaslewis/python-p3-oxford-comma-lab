def oxford_comma(items):
    if len(items) > 2:
        items.insert(-1, "and")
        string = ", ".join(items)
        return string.replace("and,", "and")
    elif len(items) == 2:
        items.insert(-1, "and")
        string = " ".join(items)
        return string
    else:
        return "".join(items)
