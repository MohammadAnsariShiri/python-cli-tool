import os
import logging

from scorekeeper.reader import read_scores
from scorekeeper.stats import average, best

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

logging.basicConfig(
    filename=os.path.join(BASE_DIR, 'scorekeeper.log'),
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s',
)


def main():
    rows = read_scores(os.path.join(BASE_DIR, 'data', 'scores.txt'))
    print(f'Valid rows: {len(rows)}')
    print(f'Average: {average(rows):.2f}')
    top = best(rows)
    if top:
        print(f'Best: {top[0]} ({top[1]})')


if __name__ == '__main__':
    main()