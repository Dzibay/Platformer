tile = 50
level_map_ = ['@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',
              '@...............................................@',
              '@...............................................@',
              '@..................@@@@@......................@@@',
              '@..........@@@@@@@@@@@@@........................@',
              '@.................................@@@@@.........@',
              '@...............................................@',
              '@@@@@@@@@.......................................@',
              '@........................................@@@....@',
              '@...............................................@',
              '@...........@@@@@@@@@...........................@',
              '@..................................@@@..........@',
              '@...............................................@',
              '@....@@@................................@@......@',
              '@....@@@................................@@......@',
              '@....@@@@@@@@@@@@@@@....................@@......@',
              '@.................@@...............@@@@@@@......@',
              '@.................@@............................@',
              '@@@...............@@@@@@@@@.....................@',
              '@...............................................@',
              '@.......@@@@@@@................@@@..............@',
              '@..............................@@@..............@',
              '@..............................@@@..............@',
              '@.......................@@@@@@@.................@',
              '@....................@@@........................@',
              '@...............................................@',
              '@...............................................@',
              '@..@@...........@...............................@',
              '@..@@...........@@@@............................@',
              '@..@@...........@@@@@@@.........................@',
              '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@']

level_map = {y: [x for x in range(len(level_map_[y])) if level_map_[y][x] != '.'] for y in range(len(level_map_))}
print(level_map)
