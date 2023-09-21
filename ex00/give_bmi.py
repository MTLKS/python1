import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """Return the BMI for each person.

    Args:
        heigh: A list of heights.
        weight: A list of weights.

    Returns:
        A list of BMIs.
    """
    try:
        assert len(height) == len(weight), \
            "The length of height and weight must be the same."
        assert all(isinstance(h, (int, float)) for h in height), \
            "The height must be a list of numbers."
        assert all(isinstance(w, (int, float)) for w in weight), \
            "The weight must be a list of numbers."
        assert len(height) > 0, "The height must not be empty."
        assert len(weight) > 0, "The weight must not be empty."
        assert all(h > 0 for h in height), "The height must be positive."

        return list(np.array(weight) / np.array(height) ** 2)
    except AssertionError as e:
        print(e)
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return a list of booleans indicating whether the BMI is above the limit.

    Args:
        bmi: A list of BMIs.
        limit: The limit to check against.

    Returns:
        A list of booleans.
    """
    try:
        assert type(limit) in [int, float], "The limit must be a number."
        assert len(bmi) > 0, "The BMI must not be empty."

        assert all(isinstance(b, (int, float)) for b in bmi), \
            "The BMI must be a list of numbers."

        return [b > limit for b in bmi]
    except AssertionError as e:
        print(e)
        return []
