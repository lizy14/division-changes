from bs4 import BeautifulSoup
import os

for root, dirs, files in os.walk('.'):
    for filename in files:
        if not filename.endswith('.html'):
            continue
        out_filename = filename.replace('.html', '.csv')
        with open(out_filename, 'w') as of:
            with open(filename) as f:
                soup = BeautifulSoup(f)
            for tr in soup.find_all('tr'):
                cells = []
                for td in tr.find_all('td'):
                    text = td.text.strip()
                    if text:
                        cells.append(text)
                print(','.join(cells), file=of)
        