import colorsys
import copy


color_keywords = {
        'aliceblue'             : 0xf0f8ff,
        'antiquewhite'          : 0xfaebd7,
        'aqua'                  : 0x00ffff,
        'aquamarine'            : 0x7fffd4,
        'azure'                 : 0xf0ffff,
        'beige'                 : 0xf5f5dc,
        'bisque'                : 0xffe4c4,
        'black'                 : 0x000000,
        'blanchedalmond'        : 0xffebcd,
        'blue'                  : 0x0000ff,
        'blueviolet'            : 0x8a2be2,
        'brown'                 : 0xa52a2a,
        'burlywood'             : 0xdeb887,
        'cadetblue'             : 0x5f9ea0,
        'chartreuse'            : 0x7fff00,
        'chocolate'             : 0xd2691e,
        'coral'                 : 0xff7f50,
        'cornflowerblue'        : 0x6495ed,
        'cornsilk'              : 0xfff8dc,
        'crimson'               : 0xdc143c,
        'cyan'                  : 0x00ffff,
        'darkblue'              : 0x00008b,
        'darkcyan'              : 0x008b8b,
        'darkgoldenrod'         : 0xb8860b,
        'darkgray'              : 0xa9a9a9,
        'darkgreen'             : 0x006400,
        'darkgrey'              : 0xa9a9a9,
        'darkkhaki'             : 0xbdb76b,
        'darkmagenta'           : 0x8b008b,
        'darkolivegreen'        : 0x556b2f,
        'darkorange'            : 0xff8c00,
        'darkorchid'            : 0x9932cc,
        'darkred'               : 0x8b0000,
        'darksalmon'            : 0xe9967a,
        'darkseagreen'          : 0x8fbc8f,
        'darkslateblue'         : 0x483d8b,
        'darkslategray'         : 0x2f4f4f,
        'darkslategrey'         : 0x2f4f4f,
        'darkturquoise'         : 0x00ced1,
        'darkviolet'            : 0x9400d3,
        'deeppink'              : 0xff1493,
        'deepskyblue'           : 0x00bfff,
        'dimgray'               : 0x696969,
        'dimgrey'               : 0x696969,
        'dodgerblue'            : 0x1e90ff,
        'firebrick'             : 0xb22222,
        'floralwhite'           : 0xfffaf0,
        'forestgreen'           : 0x228b22,
        'fuchsia'               : 0xff00ff,
        'gainsboro'             : 0xdcdcdc,
        'ghostwhite'            : 0xf8f8ff,
        'gold'                  : 0xffd700,
        'goldenrod'             : 0xdaa520,
        'gray'                  : 0x808080,
        'green'                 : 0x008000,
        'greenyellow'           : 0xadff2f,
        'grey'                  : 0x808080,
        'honeydew'              : 0xf0fff0,
        'hotpink'               : 0xff69b4,
        'indianred'             : 0xcd5c5c,
        'indigo'                : 0x4b0082,
        'ivory'                 : 0xfffff0,
        'khaki'                 : 0xf0e68c,
        'lavender'              : 0xe6e6fa,
        'lavenderblush'         : 0xfff0f5,
        'lawngreen'             : 0x7cfc00,
        'lemonchiffon'          : 0xfffacd,
        'lightblue'             : 0xadd8e6,
        'lightcoral'            : 0xf08080,
        'lightcyan'             : 0xe0ffff,
        'lightgoldenrodyellow'  : 0xfafad2,
        'lightgray'             : 0xd3d3d3,
        'lightgreen'            : 0x90ee90,
        'lightgrey'             : 0xd3d3d3,
        'lightpink'             : 0xffb6c1,
        'lightsalmon'           : 0xffa07a,
        'lightseagreen'         : 0x20b2aa,
        'lightskyblue'          : 0x87cefa,
        'lightslategray'        : 0x778899,
        'lightslategrey'        : 0x778899,
        'lightsteelblue'        : 0xb0c4de,
        'lightyellow'           : 0xffffe0,
        'lime'                  : 0x00ff00,
        'limegreen'             : 0x32cd32,
        'linen'                 : 0xfaf0e6,
        'magenta'               : 0xff00ff,
        'maroon'                : 0x800000,
        'mediumaquamarine'      : 0x66cdaa,
        'mediumblue'            : 0x0000cd,
        'mediumorchid'          : 0xba55d3,
        'mediumpurple'          : 0x9370db,
        'mediumseagreen'        : 0x3cb371,
        'mediumslateblue'       : 0x7b68ee,
        'mediumspringgreen'     : 0x00fa9a,
        'mediumturquoise'       : 0x48d1cc,
        'mediumvioletred'       : 0xc71585,
        'midnightblue'          : 0x191970,
        'mintcream'             : 0xf5fffa,
        'mistyrose'             : 0xffe4e1,
        'moccasin'              : 0xffe4b5,
        'navajowhite'           : 0xffdead,
        'navy'                  : 0x000080,
        'oldlace'               : 0xfdf5e6,
        'olive'                 : 0x808000,
        'olivedrab'             : 0x6b8e23,
        'orange'                : 0xffa500,
        'orangered'             : 0xff4500,
        'orchid'                : 0xda70d6,
        'palegoldenrod'         : 0xeee8aa,
        'palegreen'             : 0x98fb98,
        'paleturquoise'         : 0xafeeee,
        'palevioletred'         : 0xdb7093,
        'papayawhip'            : 0xffefd5,
        'peachpuff'             : 0xffdab9,
        'peru'                  : 0xcd853f,
        'pink'                  : 0xffc0cb,
        'plum'                  : 0xdda0dd,
        'powderblue'            : 0xb0e0e6,
        'purple'                : 0x800080,
        'red'                   : 0xff0000,
        'rosybrown'             : 0xbc8f8f,
        'royalblue'             : 0x4169e1,
        'saddlebrown'           : 0x8b4513,
        'salmon'                : 0xfa8072,
        'sandybrown'            : 0xf4a460,
        'seagreen'              : 0x2e8b57,
        'seashell'              : 0xfff5ee,
        'sienna'                : 0xa0522d,
        'silver'                : 0xc0c0c0,
        'skyblue'               : 0x87ceeb,
        'slateblue'             : 0x6a5acd,
        'slategray'             : 0x708090,
        'slategrey'             : 0x708090,
        'snow'                  : 0xfffafa,
        'springgreen'           : 0x00ff7f,
        'steelblue'             : 0x4682b4,
        'tan'                   : 0xd2b48c,
        'teal'                  : 0x008080,
        'thistle'               : 0xd8bfd8,
        'tomato'                : 0xff6347,
        'turquoise'             : 0x40e0d0,
        'violet'                : 0xee82ee,
        'wheat'                 : 0xf5deb3,
        'white'                 : 0xffffff,
        'whitesmoke'            : 0xf5f5f5,
        'yellow'                : 0xffff00,
        'yellowgreen'           : 0x9acd32,
}


class ColorValue256:
    def __init__(self, s):
        self.value = int(s)
        if self.value not in range(0, 256):
            raise ValueError(s, 'out of range')

    def __repr__(self):
        return '{}({})'.format(
                self.__class__.__name__,
                self.value,
                )

    def __add__(self, other):
        if isinstance(other, ColorValueEmpty):
            return self

        ret = copy.deepcopy(self)

        if isinstance(other, ColorValueBrighter):
            if ret.value in range(0, 8):
                ret.value = ret.value + 8

            elif ret.value == 8:
                ret.value = 7

            elif ret.value in range(16, 196):
                ret.value += 36

            elif ret.value in range(232, 250):
                ret.value += 6

            elif ret.value in range(250, 256):
                ret.value = 255

            return ret

        elif isinstance(other, ColorValueDarker):
            if ret.value == 7:
                ret.value = 8

            elif ret.value in range(8, 16):
                ret.value -= 8

            elif ret.value in range(52, 232):
                ret.value -= 36

            elif ret.value in range(232, 238):
                ret.value = 232

            elif ret.value in range(238, 250):
                ret.value -= 6

            return ret

        return other

    @property
    def contrast(self):
        c = self.value
        if c in range(0, 16):
            ret = 7 if c == 0 else 0

        elif c in range(16, 232):
            ret = 7 if (((c - 16) % 36) < 18) else 0

        elif c in range(232, 256):
            ret = 7 if ((c - 232) < 12) else 0

        else:
            ret = 0

        return ColorValue256(ret)


class ColorValueRGB:
    def __init__(self, s):
        v = color_keywords.get(s)

        if v is None:
            s = s.lstrip('#')

            if len(s) != 6:
                raise ValueError('Unknown RGB value: ' + s)

            v = int(s, 16)

        self.r = (v & 0xff0000) >> 16
        self.g = (v & 0x00ff00) >> 8
        self.b = (v & 0x0000ff)

    def __repr__(self):
        return '{}({:0>6X})'.format(
                self.__class__.__name__,
                (self.r << 16) | (self.g << 8) | self.b
                )

    def __add__(self, other):
        if isinstance(other, ColorValueEmpty):
            return self

        if isinstance(other, (ColorValueBrighter, ColorValueDarker)):
            return self

        return other

    @property
    def contrast(self):
        if max(self.r, self.g, self.b) > 128:
            return ColorValueRGB('black')

        return ColorValueRGB('lightgrey')


class ColorValueANSI:
    ansi_color_def = {
            'black': '0', 'red': '1', 'green': '2', 'yellow': '3',
            'blue': '4', 'magenta': '5', 'cyan': '6', 'white': '7',
            }

    def __init__(self, s):
        if s.lower() not in self.ansi_color_def:
            raise ValueError('Unknown ANSI color name', s)

        self.name = s.lower()
        self.bright = (s.upper() == s)

    @property
    def value(self):
        return self.ansi_color_def[self.name]

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.name.upper() if self.bright else self.name)

    def __add__(self, other):
        if isinstance(other, ColorValueEmpty):
            return self

        ret = copy.deepcopy(self)

        if isinstance(other, ColorValueBrighter):
            if ret.name == 'black' and ret.bright == 1:
                ret.name = 'white'
                ret.bright = 0
            else:
                ret.bright = min(self.bright + 1, 1)

            return ret

        elif isinstance(other, ColorValueDarker):
            if ret.name == 'white' and ret.bright == 0:
                ret.name = 'black'
                ret.bright = 1
            else:
                ret.bright = max(ret.bright - 1, 0)

            return ret

        return other

    @property
    def contrast(self):
        if self.name == 'blue':
            return ColorValueANSI('white')

        return ColorValueANSI('black')


class ColorValueBrighter:
    def __repr__(self):
        return 'brighter'


class ColorValueDarker:
    def __repr__(self):
        return 'darker'


class ColorValueEmpty:
    def __add__(self, other):
        if isinstance(other, (ColorValueBrighter, ColorValueDarker)):
            return self

        return other

    def __repr__(self):
        return 'empty'


class Color:
    def __init__(self, descriptor):
        self.fg = ColorValueEmpty()
        self.bg = ColorValueEmpty()
        self.italic = False
        self.underline = False
        self.strike = False
        self.reverse = False

        if descriptor == 'italic':
            self.italic = True

        elif descriptor == 'underline':
            self.underline = True

        elif descriptor == 'strike':
            self.strike = True

        elif descriptor in ('reverse', 'invert', 'inverse'):
            self.reverse = True

        else:
            # Parsing
            if ':' not in descriptor:
                fg = descriptor
                bg = None

            else:
                fg, bg = descriptor.split(':')

            def value_normalize(v):
                if not v or (v == 'none'):
                    return ColorValueEmpty()

                if v in ('brighter', 'bright'):
                    return ColorValueBrighter()

                if v in ('darker', 'dim'):
                    return ColorValueDarker()

                try:
                    return ColorValueANSI(v)
                except ValueError:
                    pass

                try:
                    return ColorValue256(v)
                except ValueError:
                    pass

                try:
                    return ColorValueRGB(v)
                except ValueError:
                    pass

                return ColorValueEmpty()

            self.fg = value_normalize(fg)
            self.bg = value_normalize(bg)

    def __add__(self, other):
        ret = copy.deepcopy(self)

        # List[Color]
        if isinstance(other, (list, tuple)) and all(isinstance(o, Color) for o in other):
            # return sum(other, start=ret) # doesnt work in Python3.6
            for o in other:
                ret += o
            return ret

        if not isinstance(other, Color):
            raise ValueError('Cannot add ' + other.__class__.__name__ + ' to Color')

        if other.reverse:
            ret.fg, ret.bg = ret.bg, ret.fg
            return ret

        ret.fg += other.fg
        ret.bg += other.bg

        if other.italic:
            ret.italic = other.italic

        if other.strike:
            ret.strike = other.strike

        if other.underline:
            ret.underline = other.underline

        return ret

    def __call__(self, text):
        code = ''
        text = str(text)

        fg = self.fg
        bg = self.bg

        if isinstance(fg, ColorValueEmpty) and not isinstance(bg, ColorValueEmpty):
            # Special case: none:color => black:color
            # It's because default fg is white
            fg = bg.contrast

            # Special case: black:BLACK => black:white
            # It's because (ansi) black bg is still black
            if isinstance(bg, ColorValueANSI) and bg.name == 'black' and bg.bright:
                bg.name = 'white'
                bg.bright = 0

        if isinstance(self.fg, ColorValueANSI):
            if self.fg.bright >= 1:
                code += ';1'
            else:
                code += ';0'

        if self.italic:
            code += ';3'

        if self.underline:
            code += ';4'

        if self.strike:
            code += ';9'

        # Foreground: ANSI color
        if isinstance(fg, ColorValueANSI):
            code += ';3' + fg.value

        # Foreground: 256 color
        elif isinstance(fg, ColorValue256):
            code += ';38;5;' + str(fg.value)

        # Foreground: true color
        elif isinstance(fg, ColorValueRGB):
            code += ';38;2;' + str(fg.r) + ';' + str(fg.g) + ';' + str(fg.b)

        # Background: ANSI color
        if isinstance(bg, ColorValueANSI):
            code += ';4' + bg.value

        # Background: 256 color
        elif isinstance(bg, ColorValue256):
            code += ';48;5;' + str(bg.value)

        # Background: true color
        elif isinstance(bg, ColorValueRGB):
            code += ';48;2;' + str(bg.r) + ';' + str(bg.g) + ';' + str(bg.b)

        if code:
            return ('\033[' + code.lstrip(';') + 'm') + text + '\033[m'
        else:
            return text


    def __repr__(self):
        return 'Color(' + ', '.join(filter(lambda x: x, [
            '' if not self.fg else 'fg=' + repr(self.fg),
            '' if not self.bg else 'bg=' + repr(self.bg),
            'reverse' if self.reverse else '',
            ])) + ')'
