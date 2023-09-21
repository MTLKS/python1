import numpy as np
from matplotlib import pyplot as plt
from load_image import ft_load


def main():
    """Main function."""
    arr = ft_load("animal_gray.jpeg")
    if arr is None:
        return
    print(arr)

    rows = len(arr)
    cols = len(arr[0])

    transposed = [[arr[j][i] for j in range(rows)] for i in range(cols)]
    arr = np.array(transposed)

    print("New shape after Transpose:", arr.shape)
    print(arr)

    _, ax = plt.subplots()
    ax.imshow(arr, cmap="gray")
    plt.savefig("animal_gray_plot.jpeg")


if __name__ == '__main__':
    main()
