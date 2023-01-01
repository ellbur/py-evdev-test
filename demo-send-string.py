
from evdev import UInput, ecodes as e
from time import sleep

char_mappings = {
    '`': [e.KEY_GRAVE],
    '~': [e.KEY_LEFTSHIFT, e.KEY_GRAVE],
    '1': [e.KEY_1],
    '!': [e.KEY_LEFTSHIFT, e.KEY_1],
    '2': [e.KEY_2],
    '@': [e.KEY_LEFTSHIFT, e.KEY_2],
    '3': [e.KEY_3],
    '#': [e.KEY_LEFTSHIFT, e.KEY_3],
    '4': [e.KEY_4],
    '$': [e.KEY_LEFTSHIFT, e.KEY_4],
    '5': [e.KEY_5],
    '%': [e.KEY_LEFTSHIFT, e.KEY_5],
    '6': [e.KEY_6],
    '^': [e.KEY_LEFTSHIFT, e.KEY_6],
    '7': [e.KEY_7],
    '&': [e.KEY_LEFTSHIFT, e.KEY_7],
    '8': [e.KEY_8],
    '*': [e.KEY_LEFTSHIFT, e.KEY_8],
    '9': [e.KEY_9],
    '(': [e.KEY_LEFTSHIFT, e.KEY_9],
    '0': [e.KEY_0],
    ')': [e.KEY_LEFTSHIFT, e.KEY_0],
    '-': [e.KEY_MINUS],
    '_': [e.KEY_LEFTSHIFT, e.KEY_MINUS],
    '=': [e.KEY_EQUAL],
    '+': [e.KEY_LEFTSHIFT, e.KEY_EQUAL],
    'q': [e.KEY_Q],
    'Q': [e.KEY_LEFTSHIFT, e.KEY_Q],
    'w': [e.KEY_W],
    'W': [e.KEY_LEFTSHIFT, e.KEY_W],
    'e': [e.KEY_E],
    'E': [e.KEY_LEFTSHIFT, e.KEY_E],
    'r': [e.KEY_R],
    'R': [e.KEY_LEFTSHIFT, e.KEY_R],
    't': [e.KEY_T],
    'T': [e.KEY_LEFTSHIFT, e.KEY_T],
    'y': [e.KEY_Y],
    'Y': [e.KEY_LEFTSHIFT, e.KEY_Y],
    'u': [e.KEY_U],
    'U': [e.KEY_LEFTSHIFT, e.KEY_U],
    'i': [e.KEY_I],
    'I': [e.KEY_LEFTSHIFT, e.KEY_I],
    'o': [e.KEY_O],
    'O': [e.KEY_LEFTSHIFT, e.KEY_O],
    'p': [e.KEY_P],
    'P': [e.KEY_LEFTSHIFT, e.KEY_P],
    '[': [e.KEY_LEFTBRACE],
    '{': [e.KEY_LEFTSHIFT, e.KEY_LEFTBRACE],
    ']': [e.KEY_RIGHTBRACE],
    '}': [e.KEY_LEFTSHIFT, e.KEY_RIGHTBRACE],
    '\\': [e.KEY_BACKSLASH],
    '|': [e.KEY_LEFTSHIFT, e.KEY_BACKSLASH],
    'a': [e.KEY_A],
    'A': [e.KEY_LEFTSHIFT, e.KEY_A],
    's': [e.KEY_S],
    'S': [e.KEY_LEFTSHIFT, e.KEY_S],
    'd': [e.KEY_D],
    'D': [e.KEY_LEFTSHIFT, e.KEY_D],
    'f': [e.KEY_F],
    'F': [e.KEY_LEFTSHIFT, e.KEY_F],
    'g': [e.KEY_G],
    'G': [e.KEY_LEFTSHIFT, e.KEY_G],
    'h': [e.KEY_H],
    'H': [e.KEY_LEFTSHIFT, e.KEY_H],
    'j': [e.KEY_J],
    'J': [e.KEY_LEFTSHIFT, e.KEY_J],
    'k': [e.KEY_K],
    'K': [e.KEY_LEFTSHIFT, e.KEY_K],
    'l': [e.KEY_L],
    'L': [e.KEY_LEFTSHIFT, e.KEY_L],
    ';': [e.KEY_SEMICOLON],
    ':': [e.KEY_LEFTSHIFT, e.KEY_SEMICOLON],
    "'": [e.KEY_APOSTROPHE],
    '"': [e.KEY_LEFTSHIFT, e.KEY_APOSTROPHE],
    'z': [e.KEY_Z],
    'Z': [e.KEY_LEFTSHIFT, e.KEY_Z],
    'x': [e.KEY_X],
    'X': [e.KEY_LEFTSHIFT, e.KEY_X],
    'c': [e.KEY_C],
    'C': [e.KEY_LEFTSHIFT, e.KEY_C],
    'v': [e.KEY_V],
    'V': [e.KEY_LEFTSHIFT, e.KEY_V],
    'b': [e.KEY_B],
    'B': [e.KEY_LEFTSHIFT, e.KEY_B],
    'n': [e.KEY_N],
    'N': [e.KEY_LEFTSHIFT, e.KEY_N],
    'm': [e.KEY_M],
    'M': [e.KEY_LEFTSHIFT, e.KEY_M],
    ',': [e.KEY_COMMA],
    '<': [e.KEY_LEFTSHIFT, e.KEY_COMMA],
    '.': [e.KEY_DOT],
    '>': [e.KEY_LEFTSHIFT, e.KEY_DOT],
    '/': [e.KEY_SLASH],
    '?': [e.KEY_LEFTSHIFT, e.KEY_SLASH],
    ' ': [e.KEY_SPACE],
    '\n': [e.KEY_ENTER]
}

def send_string(ui, s):
    for ch in s:
        keys = char_mappings.get(ch, [])
        for k in keys:
            ui.write(e.EV_KEY, k, 1)
        for k in reversed(keys):
            ui.write(e.EV_KEY, k, 0)
    ui.syn()

with UInput(
    {
        e.EV_KEY: [
            e.KEY_GRAVE, e.KEY_1, e.KEY_2, e.KEY_3, e.KEY_4, e.KEY_5,
                e.KEY_6, e.KEY_7, e.KEY_8, e.KEY_9, e.KEY_0, e.KEY_MINUS, e.KEY_EQUAL, e.KEY_BACKSPACE,
            e.KEY_TAB, e.KEY_Q, e.KEY_W, e.KEY_E, e.KEY_R, e.KEY_T,
                e.KEY_Y, e.KEY_U, e.KEY_I, e.KEY_O, e.KEY_P, e.KEY_LEFTBRACE, e.KEY_RIGHTBRACE, e.KEY_BACKSLASH,
            e.KEY_A, e.KEY_S, e.KEY_D, e.KEY_F, e.KEY_G, e.KEY_H,
                e.KEY_J, e.KEY_K, e.KEY_L, e.KEY_SEMICOLON, e.KEY_APOSTROPHE, e.KEY_ENTER,
            e.KEY_LEFTSHIFT, e.KEY_Z, e.KEY_X, e.KEY_C, e.KEY_V, e.KEY_B,
                e.KEY_N, e.KEY_M, e.KEY_COMMA, e.KEY_DOT, e.KEY_SLASH,
            e.KEY_LEFTCTRL, e.KEY_SPACE,
        ]
    },
    name='py-evdev-test',
    vendor=1,
    product=1,
    version=1,
    bustype=3,
) as ui:
    print(ui.capabilities())
    
    while True:
        send_string(ui, 'Howdy?\n')
        sleep(0.25)

