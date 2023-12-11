# import matplotlib.pyplot as plt

import numpy as np


def numpy_lib():

    print("quiz:")
    X = np.array([[1, 0], [0, 1]])
    Y = np.array([[2, 1], [1, 2]])
    Z = np.dot(X, Y)
    print(Z)

    X = np.array([[1, 0, 1], [2, 2, 2]])
    out = X[0:2, 2]
    print(out)

    a = np.array([-1, 1])
    b = np.array([1, 1])
    c = np.dot(a, b)
    print(c)

    # x = np.linspace(0, 2*np.pi, 100)
    # y = np.sin(x)
    # # %matplotlib inline
    # plt.plt(x, y)

    a = ["0", 1, "two", "3", 4]
    n = 0
    for i in a:
        print("a[", n, "]:", i)
        n += 1
    else:
        print("Standard array looped")

    anp = np.array([0, 1, 2, 3, 4])
    n = 0
    for i in anp:
        print("anp[", n, "]:", anp[n])
        n += 1
    print("NUMericPYthon version", np.__version__)
    print("type of anp:", type(anp))
    print("type of values stored in numpy array:", anp.dtype)
    print(anp[1:5])
    # assign two values
    anp[3:5] = 300, 400
    print(anp[1:5])

    b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
    print("type of b array:", type(b), "type of values stored in b array:", b.dtype)

    # Print the even elements in the given array.
    arr = np.array([1, 2, 3, 4, 5, 6, 7])
    print(arr[1:8:2])

    # Similarly, we can use a list to select more than one specific index
    select = [0, 2, 3, 4]
    arr[select] = 100000

    a = np.array([0, 1, 2, 3, 4])
    print(a.size)

    # Get the number of dimensions of numpy array
    print(a.ndim)

    # Get the shape/size of numpy array
    print(a.shape)

    # We can add the two arrays and assign it to z:
    z = np.add(arr, a)
    print("z:", z)

    a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
    A = np.array(a)
    if A[1, 2] == A[1][2]:
        print("As are equal")

    # Access the element on the first row and first and second columns
    if A[0][0:2] == (11, 12):
        print("slicing numpy array horizontally to tuple")

    # Access the element on the first and second rows and third column
    if A[0:2, 2] == (13, 23):
        print("slicing numpy array horizontally to tuple")

    X = [[1, 0], [0, 1]]
    Y = [[2, 1], [1, 2]]
    SumXnY = [[3, 1], [1, 3]]
    # Adding arrays
    if np.array(X) * np.array(Y) == np.array(SumXnY):
        print("Adding arrays check")

    Y = np.array([[2, 1], [1, 2]])
    X = np.array([[1, 0], [0, 1]])

    # Multiply X with Y
    Z = X * Y
    Z

    # Calculate the dot product
    Z = np.dot(X, Y)
    Z

    # Calculate the sine of matrix Z
    C = np.sin(Z)

    # Get the transposed of C
    C.T


