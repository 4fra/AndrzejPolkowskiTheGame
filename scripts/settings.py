# left = L, right = R, top = T, bottom = B, main = X, topleft = W, topright = D, bottomleft = A, bottomright = S, insidetopleft = Q, insidetopright = E, insidebottomright = Y, insidebottomleft = U, grass = M, e = enemy, s = kebab, P = character, d = door
level1 = {'level_map': [
    '                              ',
    '              e               ',
    '                              ',
    '  s                           ',
    ' WTTD      WTTD               ',
    ' LXXETD                WD     ',
    ' LYBBBS        s  WTD       d ',
    ' AS           WTTTQXR      WTT',
    '              ABBBBBS         ',
    '         WTD            WD    ',
    ' P    WTTQXR          WTQR    ',
    '                    WTQYBS    ',
    'TTTD                ABBS      ',
    '          s  WTTD             ',
    '       WTTTTTQXXR             ',
    '       LXXXXXXXXR             ',
    '       LXXXXXXXXR             ',
    '       LXXXXXXXXR             ',
    '       LXXXXXXXXR             ',
], 'enemy_speed': 3, 'enemy_dist': 250}

level2 = {'level_map': [
    'XXXXR                         ',
    'XXXYS             e           ',
    'XYBS                          ',
    'BS               s            ',
    '          WTTTTTTTTTTTTD      ',
    '                              ',
    '     WD      e             WTT',
    '    WQR                   WQXX',
    '                              ',
    'TD                   WD       ',
    '                  s         d ',
    '    WTD          WD       WTTT',
    '   P                          ',
    '          WTTD        WD      ',
    'TTTTD                       s ',
    'XXXXETD                   WTTT',
    'XXXXXXR                WTTQXXX',
    'XXXXXXR                LXXXXXX',
    'XXXXXXR                LXXXXXX',
], 'enemy_speed': 2, 'enemy_dist': 125}

level3 = {'level_map': [
    '                              ',
    '                    e         ',
    '                              ',
    '                              ',
    '  P    s                    s ',
    'TTD    T              WTTTTTTT',
    '                      ABBUXXXX',
    '           WTTTTTD       ABBBB',
    '                              ',
    '    WTD                       ',
    '    AUR                       ',
    'D    AS                       ',
    'ED                            ',
    'XR s                   WD     ',
    'XETD    s              LR   d ',
    'XXXR   WD      e       LETTTTT',
    'XXXR   LR              LXXXXXX',
    'XXXR   LR              LXXXXXX',
    'XXXR   LR              LXXXXXX',
], 'enemy_speed': 4, 'enemy_dist': 125}

level4 = {'level_map': [
    '                              ',
    '         e                    ',
    '                              ',
    ' P              s        T    ',
    'WTD        T    T   WD        ',
    'ABS   WTD                  WD ',
    '                              ',
    '                              ',
    '                       s      ',
    '              T   T    WD     ',
    '                              ',
    '                              ',
    '        WD           e        ',
    '                              ',
    '            s                 ',
    '            WD             d  ',
    '            AS  WD    T   WTD ',
    '                   sD         ',
    '                   AS         ',
    '                              ',
], 'enemy_speed': 4, 'enemy_dist': 250}

level5 = {'level_map': ['                              ',
     '                              ', '             e                ', '                              ', '                         e    ', 's                             ', 'W                             ', 'LX                     s      ', 'ABS                   WTD     ', '            sWD   WD  ABS     ', '     WD     WXR   AS          ', '          WTBBS               ', 'TTD                           ', ' P              e             ', 'TTTD                          ', '                              ', '      WTTTD                 d ', '      LXXXR  WD   s        WTT', '      ABBBS  AS  WTD       ABB', '                              ']
, 'enemy_speed': 7, 'enemy_dist': 250}

level6 = {'level_map': ['                              ', '             e                ', '         e                    ', '           W d D              ', '           ABBBS              ', '       WD         WD          ', '      AS           AS s       ', '  s                   T       ', ' WTD                          ', '                         TD   ', '    e D      e          ABS   ', '     TR                       ', '    ABS            WTD        ', '                   ABS  WD    ', 'WTD                          W', 'ABBD           P            WR', '     s   WD   WTTTD   s    WXR', '     WD  AS   ABBBS  WTD  WXXR', '                          ABBS', '                              ']
, 'enemy_speed': 8, 'enemy_dist': 400}

level7 = {'level_map': ['                              ', '                 e            ', 'd                 e           ', 'TD                            ', 'BBS                           ', '                              ', '     WD   WTTTD               ', '   sLBS   ABBBS               ', '   AS            T   WTTTDs   ', '                     BBBBBS   ', '          e                  W', '               e            WR', '                           WXR', '          WD              WXXR', ' P        AS     s      WBBBBS', 'TTD   WD        WTTD   AS     ', 'XXR   AS        ABBS          ', 'BBS                           ', '            e                 ', '                              ']
, 'enemy_speed': 6, 'enemy_dist': 400}

level8 = {'level_map': ['        e                     ', '             e                ', '                         e    ', '    s          e              ', '   WTD                        ', '   ABS                        ', '         WD                   ', '         AS                   ', '              TTD   WD        ', 'd                   AXD       ', 'WD                   AS    s  ', 'AS          e            WTD  ', '         e              WBS   ', '                              ', '         TTD   WT   WD        ', ' P        sXD  Ls             ', 'WTD   WTTTTXXTTXTD            ', 'ABS   ABBBBBBBBBBS            ', '                     e        ', '                              ']
, 'enemy_speed': 8, 'enemy_dist': 300}

tile_size = 48

win_width, win_height = 1400, 800