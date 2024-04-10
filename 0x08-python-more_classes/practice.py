def generate_rectangle(width = 10, height = 3):
    if width == 0 or height == 0:
        return ""

    rows = ['#' * width for _ in range(height)]
    return '\n'.join(rows)

print(generate_rectangle())