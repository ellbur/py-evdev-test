
row_codes = [
    ['e.KEY_GRAVE', 'e.KEY_1', 'e.KEY_2', 'e.KEY_3', 'e.KEY_4', 'e.KEY_5',
        'e.KEY_6', 'e.KEY_7', 'e.KEY_8', 'e.KEY_9', 'e.KEY_0', 'e.KEY_MINUS', 'e.KEY_EQUAL' ],
    ['e.KEY_Q', 'e.KEY_W', 'e.KEY_E', 'e.KEY_R', 'e.KEY_T',
        'e.KEY_Y', 'e.KEY_U', 'e.KEY_I', 'e.KEY_O', 'e.KEY_P', 'e.KEY_LEFTBRACE', 'e.KEY_RIGHTBRACE', 'e.KEY_BACKSLASH'],
    ['e.KEY_A', 'e.KEY_S', 'e.KEY_D', 'e.KEY_F', 'e.KEY_G', 'e.KEY_H',
        'e.KEY_J', 'e.KEY_K', 'e.KEY_L', 'e.KEY_SEMICOLON', 'e.KEY_APOSTROPHE'],
    ['e.KEY_Z', 'e.KEY_X', 'e.KEY_C', 'e.KEY_V', 'e.KEY_B',
        'e.KEY_N', 'e.KEY_M', 'e.KEY_COMMA', 'e.KEY_DOT', 'e.KEY_SLASH'],
]

unshifted_chars = [
    '`1234567890-=',
    'qwertyuiop[]\\',
    'asdfghjkl;\'',
    'zxcvbnm,./',
]

shifted_chars = [
    '~!@#$%^&*()_+',
    'QWERTYUIOP{}|',
    'ASDFGHJKL:"',
    'ZXCVBNM<>?',
]

for unshifted_row, shifted_row, key_row in zip(unshifted_chars, shifted_chars, row_codes):
    for unshifted_char, shifted_char, key in zip(unshifted_row, shifted_row, key_row):
        print('%s: [%s],' % (repr(unshifted_char), key))
        print('%s: [e.KEY_LEFTSHIFT, %s],' % (repr(shifted_char), key))
        

