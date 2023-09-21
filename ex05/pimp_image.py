import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.array:
    """Invert an image."""
    array = 255 - array
    plt.imsave("landscape_invert.jpg", array)
    return array


def ft_red(array) -> np.array:
    """Keep only the red channel of an image."""
    red = array[:, :, 0]
    array = np.zeros(array.shape, dtype=np.uint8)
    array[:, :, 0] = red
    plt.imsave("landscape_red.jpg", array)
    return array


def ft_green(array) -> np.array:
    """Keep only the green channel of an image."""
    green = array[:, :, 1]
    array = np.zeros(array.shape, dtype=np.uint8)
    array[:, :, 1] = green
    plt.imsave("landscape_green.jpg", array)
    return array


def ft_blue(array) -> np.array:
    """Keep only the blue channel of an image."""
    blue = array[:, :, 2]
    array = np.zeros(array.shape, dtype=np.uint8)
    array[:, :, 2] = blue
    plt.imsave("landscape_blue.jpg", array)
    return array


def ft_grey(array) -> np.array:
    """Convert an RGB image to grayscale."""
    array = np.dot(array[..., :3], [0.299, 0.587, 0.114]).astype(np.uint8)
    array = array[:, :, np.newaxis]
    array = np.repeat(array, 3, axis=2)
    plt.imsave("landscape_grey.jpg", array)
    return array
