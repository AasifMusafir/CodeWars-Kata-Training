def printer_error(s):
    errors = sum(1 for c in s if c < 'a' or c > 'm')
    return f"{errors}/{len(s)}"