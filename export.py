with open('bayeselo_games.txt', 'r', encoding='utf-8') as f, open('standings_games.md', 'a', encoding='utf-8') as out:
    out.writelines(['|' + '|'.join(f.readline().split()) + '|\n', '|-' * 9 + '|\n'])
    for line in f:
        out.write('|' + '|'.join(line.split()) + '|\n')