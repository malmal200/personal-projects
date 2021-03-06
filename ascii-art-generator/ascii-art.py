char_map = {'a': ['  ___  ', ' / _ \\ ', '/ /_\\ \\', '|  _  |', '| | | |', '\\_| |_/', '       ', '       '],
            'b': ['______ ', '| ___ \\', '| |_/ /', '| ___ \\', '| |_/ /', '\\____/ ', '       ', '       '],
            'c': [' _____ ', '/  __ \\', '| /  \\/', '| |    ', '| \\__/\\', ' \\____/', '       ', '       '],
            'd': ['______ ', '|  _  \\', '| | | |', '| | | |', '| |/ / ', '|___/  ', '       ', '       '],
            'e': [' _____ ', '|  ___|', '| |__  ', '|  __| ', '| |___ ', '\\____/ ', '       ', '       '],
            'f': ['______ ', '|  ___|', '| |_   ', '|  _|  ', '| |    ', '\\_|    ', '       ', '       '],
            'g': [' _____ ', '|  __ \\', '| |  \\/', '| | __ ', '| |_\\ \\', ' \\____/', '       ', '       '],
            'h': [' _   _ ', '| | | |', '| |_| |', '|  _  |', '| | | |', '| | | |', '       ', '       '],
            'i': [' _____ ', '|_   _|', '  | |  ', '  | |  ', ' _| |_ ', ' \\___/ ', '       ', '       '],
            'j': ['   ___ ', '  |_  |', '    | |', '    | |', '/\\__/ /', '\\____/ ', '       ', '       '],
            'k': [' _   __', '| | / /', '| |/ / ', '|    \\ ', '| |\\  \\', '\\_| \\_/', '       ', '       '],
            'l': [' _     ', '| |    ', '| |    ', '| |    ', '| |____', '\\_____/', '       ', '       '],
            'm': ['___  ___', '|  \\/  |', '| .  . |', '| |\\/| |', '| |  | |', '\\_|  |_/', '        ', '        '],
            'n': [' _   _ ', '| \\ | |', '|  \\| |', '| . ` |', '| |\\  |', '\\_| \\_/', '       ', '       '],
            'o': [' _____ ', '|  _  |', '| | | |', '| | | |', '\\ \\_/ /', ' \\___/ ', '       ', '       '],
            'p': ['______ ', '| ___ \\', '| |_/ /', '|  __/ ', '| |    ', '\\_|    ', '       ', '       '],
            'q': [' _____ ', '|  _  |', '| | | |', '| | | |', '\\ \\/` /', ' \\_/\\_\\', '       ', '       '],
            'r': ['______ ', '| ___ \\', '| |_/ /', '|    / ', '| |\\ \\ ', '\\_| \\_|', '       ', '       '],
            's': [' _____ ', '/  ___|', '\\ `--. ', ' `--. \\', '/\\__/ /', '\\____/ ', '       ', '       '],
            't': [' _____ ', '|_   _|', '  | |  ', '  | |  ', '  | |  ', '  \\_/  ', '       ', '       '],
            'u': [' _   _ ', '| | | |', '| | | |', '| | | |', '| |_| |', '\\_____/', '       ', '       '],
            'v': [' _   _ ', '| | | |', '| | | |', '| | | |', '\\ \\_/ /', ' \\___/ ', '       ', '       '],
            'w': [' _    _ ', '| |  | |', '| |  | |', '| |/\\| |', '\\  /\\  /', ' \\/  \\/ ', '        ', '        '],
            'x': ['__   __', '\\ \\ / /', ' \\ V / ', ' /   \\ ', '/ /^\\ \\', '\\/   \\/', '       ', '       '],
            'y': ['__   __', '\\ \\ / /', ' \\ V / ', '  \\ /  ', '  | |  ', '  \\_/  ', '       ', '       '],
            'z': [' ______', '|___  /', '   / / ', '  / /  ', './ /___', '\\_____/', '       ', '       '],
            ' ': ['        ', '        ', '        ', '        ', '        ', '        ', '        ', '        ']}

text = input('Input text:').lower().strip()

while 1:
    for char_part in range(8):
        line = ''
        for char in text:
            if char.isalpha() or char == ' ':
                line += char_map[char][char_part]
        print(line)
    text = input('Input text:').lower()
