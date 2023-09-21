import numpy as np
from matplotlib import image


def ft_load(path: str) -> np.array:
    """Load an image from a file.

    Args:
        path: The path to the image file.

    Returns:
        The image as a numpy array.
    """

    try:
        img = image.imread(path)
        arr = np.array(img)
        print("The shape of image is:", arr.shape)
        return arr
    except Exception as e:
        print(e.__class__.__name__ + ": " + str(e))
        return None
