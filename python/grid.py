import numpy as np

def grid(*args):
    """grid returns a parameter mesh for an arbitrary number of inputs.

    Given N lists of input parameters, grid returns a 2D list
    giving all possible combinations of the parameters, in a logical
    order (ie, x, y, z, ... for all x in args[0] for all y in args[1] ...)

    Args:
    * An arbitrary-length iterable of lists of values

    Returns:
    * A 2D numpy.ndarray giving all combinations of input values

    Assumes numpy as imported as np
    """
    if len(args) == 0:
        return np.array([])
    elif len(args)==1:
        return args[0]
    else:
        return np.concatenate([[np.insert(r, 0, k) for k in args[0]]
                                                    for r in grid(*args[1:])])

if __name__ == '__main__':
    print(grid())
    print grid([1, 2, 3])
    print grid([1, 2, 3], [4, 5, 6])
    X = grid(range(3), range(4), range(3), range(3), range(2))
    print(X.shape)
    print(3*4*3*3*2)
