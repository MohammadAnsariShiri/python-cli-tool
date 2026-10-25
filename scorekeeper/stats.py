def average(rows):
    if not rows:
        return 0.0
    return sum([score for name, score in rows]) / len(rows)


def best(rows):
    if not rows:
        return None
    top = rows[0]
    for row in rows:
        if row[1] > top[1]:
            top = row
    return top