#!/usr/bin/python

codepoints = [
    (2, 0x25b6),  # BLACK MEDIUM RIGHT-POINTING TRIANGLE
    (3, 0x25c0),  # BLACK LEFT-POINTING TRIANGLE
    (7, 0x2407),  # SYMBOL FOR BELL
    (32, 32),  # SPACE
    (33, 33),  # EXCLAMATION MARK
    (34, 34),  # QUOTATION MARK
    (35, 35),  # NUMBER SIGN
    (36, 36),  # DOLLAR SIGN
    (37, 37),  # PERCENT SIGN
    (38, 38),  # AMPERSAND
    (39, 39),  # APOSTROPHE
    (40, 40),  # LEFT PARENTHESIS
    (41, 41),  # RIGHT PARENTHESIS
    (42, 42),  # ASTERISK
    (43, 43),  # PLUS SIGN
    (44, 44),  # COMMA
    (45, 45),  # HYPHEN-MINUS
    (46, 46),  # FULL STOP
    (47, 47),  # SOLIDUS
    (48, 48),  # DIGIT ZERO
    (49, 49),  # DIGIT ONE
    (50, 50),  # DIGIT TWO
    (51, 51),  # DIGIT THREE
    (52, 52),  # DIGIT FOUR
    (53, 53),  # DIGIT FIVE
    (54, 54),  # DIGIT SIX
    (55, 55),  # DIGIT SEVEN
    (56, 56),  # DIGIT EIGHT
    (57, 57),  # DIGIT NINE
    (58, 58),  # COLON
    (59, 59),  # SEMICOLON
    (60, 60),  # LESS-THAN SIGN
    (61, 61),  # EQUALS SIGN
    (62, 62),  # GREATER-THAN SIGN
    (63, 63),  # QUESTION MARK
    (64, 64),  # COMMERCIAL AT
    (65, 65),  # LATIN CAPITAL LETTER A
    (66, 66),  # LATIN CAPITAL LETTER B
    (67, 67),  # LATIN CAPITAL LETTER C
    (68, 68),  # LATIN CAPITAL LETTER D
    (69, 69),  # LATIN CAPITAL LETTER E
    (70, 70),  # LATIN CAPITAL LETTER F
    (71, 71),  # LATIN CAPITAL LETTER G
    (72, 72),  # LATIN CAPITAL LETTER H
    (73, 73),  # LATIN CAPITAL LETTER I
    (74, 74),  # LATIN CAPITAL LETTER J
    (75, 75),  # LATIN CAPITAL LETTER K
    (76, 76),  # LATIN CAPITAL LETTER L
    (77, 77),  # LATIN CAPITAL LETTER M
    (78, 78),  # LATIN CAPITAL LETTER N
    (79, 79),  # LATIN CAPITAL LETTER O
    (80, 80),  # LATIN CAPITAL LETTER P
    (81, 81),  # LATIN CAPITAL LETTER Q
    (82, 82),  # LATIN CAPITAL LETTER R
    (83, 83),  # LATIN CAPITAL LETTER S
    (84, 84),  # LATIN CAPITAL LETTER T
    (85, 85),  # LATIN CAPITAL LETTER U
    (86, 86),  # LATIN CAPITAL LETTER V
    (87, 87),  # LATIN CAPITAL LETTER W
    (88, 88),  # LATIN CAPITAL LETTER X
    (89, 89),  # LATIN CAPITAL LETTER Y
    (90, 90),  # LATIN CAPITAL LETTER Z
    (91, 91),  # LEFT SQUARE BRACKET
    (92, 92),  # REVERSE SOLIDUS
    (93, 93),  # RIGHT SQUARE BRACKET
    (94, 94),  # CIRCUMFLEX ACCENT
    (95, 95),  # LOW LINE
    (96, 96),  # GRAVE ACCENT
    (97, 97),  # LATIN SMALL LETTER A
    (98, 98),  # LATIN SMALL LETTER B
    (99, 99),  # LATIN SMALL LETTER C
    (100, 100),  # LATIN SMALL LETTER D
    (101, 101),  # LATIN SMALL LETTER E
    (102, 102),  # LATIN SMALL LETTER F
    (103, 103),  # LATIN SMALL LETTER G
    (104, 104),  # LATIN SMALL LETTER H
    (105, 105),  # LATIN SMALL LETTER I
    (106, 106),  # LATIN SMALL LETTER J
    (107, 107),  # LATIN SMALL LETTER K
    (108, 108),  # LATIN SMALL LETTER L
    (109, 109),  # LATIN SMALL LETTER M
    (110, 110),  # LATIN SMALL LETTER N
    (111, 111),  # LATIN SMALL LETTER O
    (112, 112),  # LATIN SMALL LETTER P
    (113, 113),  # LATIN SMALL LETTER Q
    (114, 114),  # LATIN SMALL LETTER R
    (115, 115),  # LATIN SMALL LETTER S
    (116, 116),  # LATIN SMALL LETTER T
    (117, 117),  # LATIN SMALL LETTER U
    (118, 118),  # LATIN SMALL LETTER V
    (119, 119),  # LATIN SMALL LETTER W
    (120, 120),  # LATIN SMALL LETTER X
    (121, 121),  # LATIN SMALL LETTER Y
    (122, 122),  # LATIN SMALL LETTER Z
    (123, 123),  # LEFT CURLY BRACKET
    (124, 124),  # VERTICAL LINE
    (125, 125),  # RIGHT CURLY BRACKET
    (126, 126),  # TILDE
    (219, 224),  # LATIN SMALL LETTER A WITH GRAVE
    (220, 233),  # LATIN SMALL LETTER E WITH ACUTE
    (221, 234),  # LATIN SMALL LETTER E WITH CIRCUMFLEX
    (222, 232),  # LATIN SMALL LETTER E WITH GRAVE
    (224, 244),  # LATIN SMALL LETTER O WITH CIRCUMFLEX
    (251, 231),  # LATIN SMALL LETTER C WITH CEDILLA
    (252, 239),  # LATIN SMALL LETTER I WITH DIAERESIS
    (253, 251),  # LATIN SMALL LETTER U WITH CIRCUMFLEX
    (254, 249),  # LATIN SMALL LETTER U WITH GRAVE
]

if __name__ == '__main__':
    import unicodedata

    for offs, unicodechar in codepoints:
        c = chr(unicodechar)
        name = unicodedata.name(c)
        print(f'{offs:3d}: U+{unicodechar:04x} {c} {name}')
