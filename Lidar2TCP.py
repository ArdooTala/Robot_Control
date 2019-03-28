import numpy as np


def tr_to_tcp(rho, degrees):
    array = np.array([rho * np.cos(degrees), rho * np.sin(degrees), 0])
    M = np.array([[-1, 0, 0, 13.5],
                  [0, 1, 0, 0],
                  [0, 0, -1, 9.35],
                  [0, 0, 0, 1]])

    arr1 = np.dot(M, np.append(array, 1))
    homoArr = np.true_divide(arr1, arr1[3])
    return np.delete(homoArr, 3)


if __name__ == '__main__':

    polLid = [0.8, 10]

    tr = tr_to_tcp(polLid[1], polLid[0])

    print(tr)