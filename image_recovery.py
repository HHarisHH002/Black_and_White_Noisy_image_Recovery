from random import randrange
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
img = Image.open('img.jpg').convert('L')
arr = []
num=5
arr = np.array(img)
arr[arr > 200] = 250  # while
arr[arr < 200] = 0  # black
arr[arr == 0] = 0
arr[arr == 250] = 1
noise_arr = np.array([[[0 for _ in range(img.size[0])]
                     for _ in range(img.size[1])]for _ in range(num)])
corrected_arr = np.array([[0 for _ in range(img.size[0])]
                         for _ in range(img.size[1])])
arr_of_noise = np.array([[[0 for _ in range(img.size[0])]
                        for _ in range(img.size[1])] for _ in range(num)])
spot_count = 10000
for i in range(num):
    noise_arr[i] = arr
    for _ in range(spot_count):
        x = randrange(img.size[1])
        y = randrange(img.size[0])
        if (noise_arr[i][x][y] == 1):
            noise_arr[i][x][y] = 0
        else:
            noise_arr[i][x][y] = 1
    noise_arr[i][noise_arr[i] == 1] = 250
    noise_arr[i][noise_arr[i] == 0] = 0
    plt.imsave(f"noise_image_{i+1}.png", noise_arr[i], cmap=cm.gray)
    arr_of_noise[i] = noise_arr[i]
for i in range(img.size[1]):
    for j in range(img.size[0]):
        cores_ele = [0]*num
        for x in range(num):
            cores_ele[x] = arr_of_noise[x][i][j]
        corrected_arr[i][j] = np.bincount(cores_ele).argmax()
plt.imsave('corrected.png', corrected_arr, cmap=cm.gray)
