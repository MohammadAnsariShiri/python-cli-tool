import logging


def read_scores(file_path):
    rows = []
    bad = 0
    try:
        with open(file_path, 'r') as f:
            for n, line in enumerate(f, start=1):
                try:
                    name, score = line.strip().split(',')
                    rows.append((name, float(score)))
                except ValueError as e:
                    bad += 1
                    logging.warning(f'Line {n} skipped ({line.strip()!r}): {e}')
    except FileNotFoundError:
        logging.error(f'File not found: {file_path}')
        return []
    logging.info(f'Read {len(rows)} valid lines, skipped {bad}')
    return rows