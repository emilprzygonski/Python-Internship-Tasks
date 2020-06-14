import numpy as np
import matplotlib.pyplot as plt

squares = 7
side_len = 100
channels = 3

if squares == 0:
    print("Użyj mózgu")
    exit(1)

def reverse_row(row):
    reversed_row = []
    for j in range(len(row)):
        if row[j] == 0:
            reversed_row.append(1)
        else:
            reversed_row.append(0)
    return reversed_row

def make_checkboard(squares, side_len, channels):
    row = [int(i % 2) for i in range(squares)]
    checkerboard = []
    for i in range(squares):
        if i % 2 == 0:
            checkerboard.append(row)
        else:
            checkerboard.append(reverse_row(row))
    checkerboard = (np.kron(checkerboard, np.ones((side_len, side_len))))
    checkerboard = np.stack((checkerboard,) * channels, axis=-1)
    return checkerboard

checkerboard = make_checkboard(8, 100, 3)
checkerboard[:, :, 0].fill(0)
plt.imshow(checkerboard)
plt.show()


