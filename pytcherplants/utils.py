from colorsys import hsv_to_rgb, rgb_to_hsv
from typing import Tuple

import matplotlib as mpl
import numpy as np


def hex2rgb(color):
    """
    Converts the given hexadecimal color code to RGB (on 1-256 scale).

    Referenced from https://stackoverflow.com/a/29643643/6514033
    :param color: the hex code
    :return: the RGB values, in a tuple
    """
    return mpl.colors.to_rgb(color)


def rgb2hex(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))


def hex_to_hue_range(color: str, radius: int = 3) -> Tuple[int, int]:
    """
    Converts a hexadecimal color code to a hue range (interval of +/- radius around corresponding hue)

    :param color: The hex color code
    :param radius: The amount to pad the interval around the hue
    :return: The hue range
    """

    r, g, b = hex2rgb(color)
    h, _, _ = rgb_to_hsv(r, g, b)
    h = int(h * 179)
    return h - radius, h + radius


def hue_to_rgb(hue):
    r, g, b = hsv_to_rgb(hue, 0.7, 0.7)
    return float(r), float(g), float(b)


def hue_to_bgr(hue):
    r, g, b = hsv_to_rgb(hue, 0.7, 0.7)
    return float(b), float(g), float(r)


def hue_to_rgb_formatted(k):
    r, g, b = hue_to_rgb(float(k / 360))
    return f"rgb({int(r * 256)},{int(g * 256)},{int(b * 256)})"


def hue_to_bgr_formatted(k):
    b, g, r = hue_to_bgr(float(k / 360))
    return f"bgr({int(b * 256)},{int(g * 256)},{int(r * 256)})"


def row_hsv(row):
    h, s, v = rgb_to_hsv(float(row['R']), float(row['G']), float(row['B']))
    return h, s, v


def row_h(row):
    h, s, v = rgb_to_hsv(float(row['R']), float(row['G']), float(row['B']))
    return h


def row_s(row):
    h, s, v = rgb_to_hsv(float(row['R']), float(row['G']), float(row['B']))
    return s


def row_v(row):
    h, s, v = rgb_to_hsv(float(row['R']), float(row['G']), float(row['B']))
    return v


def row_date(row):
    image = row['Image']
    split = image.rpartition('/')[2].split('.')
    if len(split) < 3:
        print(f"Malformed image name (expected date.treatment.name.ext)")
        return np.NaN  # return NaN to allow use with .apply()
    else:
        date = split[0]
        return date


def row_treatment(row):
    image = row['Image']
    split = image.rpartition('/')[2].split('.')
    if len(split) < 3:
        print(f"Malformed image name (expected date.treatment.name.ext)")
        return np.NaN  # return NaN to allow use with .apply()
    else:
        treatment = split[1]
        return treatment.lower()


def row_name(row):
    image = row['Image']
    split = image.rpartition('/')[2].split('.')
    if len(split) < 3:
        print(f"Malformed image name (expected date.treatment.name.ext)")
        return np.NaN  # return NaN to allow use with .apply()
    else:
        title = split[2]
        return title.lower()
