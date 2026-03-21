with open('bayeselo.txt', 'r', encoding='utf-8') as f, open('standings.md', 'a', encoding='utf-8') as out:
    out.writelines(['|' + '|'.join(f.readline().split()) + '|\n', '|-' * 9 + '|\n'])
    for line in f:
        out.write('|' + '|'.join(line.split()) + '|\n')