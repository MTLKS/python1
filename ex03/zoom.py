import numpy as np
from matplotlib import pyplot as plt
from load_image import ft_load


def rgb2gray(rgb: np.array) -> np.array:
    """Convert an RGB image to grayscale.

    Args:
        rgb: The RGB image to convert.

    Returns:
        The grayscale image.
    """
    return np.mean(rgb, axis=2)[:, :, np.newaxis].astype(np.uint8)


def main():
    """Main function."""
    arr = ft_load("aanimal.jpeg")
    if arr is None:
        return
    print(arr)

    arr = rgb2gray(arr)[100:500, 450:850]
    print("New shape after slicing:", arr.shape)
    print(arr)

    _, ax = plt.subplots()
    ax.imshow(arr, cmap="gray")
    plt.savefig("animal_gray_plot.jpeg")


if __name__ == '__main__':
    main()
