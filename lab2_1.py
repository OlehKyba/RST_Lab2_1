import numpy as np
import matplotlib.pyplot as plt

from random import random
from math import sin, cos, pi


N = 256 #number of discrete
n = 8 #number of harmonic
w = 2000 #cutoff frequency

x = np.arange(0, N, 1)


def generate_random_signals(max_a=5):
    def generate_random_signal(t):
        sum_res = 0
        wp = w / n

        for i in range(n):
            a = max_a * random()
            fi = 2 * pi * random()
            sum_res += a * sin(wp * t + fi)
            wp += w / n

        return sum_res

    x_array = np.array([generate_random_signal(i) for i in range(N)])
    return x_array


def dft(signal):
    def factor(pk, n):
        angle = -2 * pi / n * pk
        return cos(angle), sin(angle)

    length = len(signal)
    real = np.zeros(length)
    image = np.zeros(length)

    for p in range(length):
        for k in range(length):
            cos_factor, sin_factor = factor(p * k, length)
            real[p] += cos_factor * signal[k]
            image[p] += sin_factor * signal[k]

    return real, image


def main():
    random_signal = generate_random_signals()
    real_spectrum, image_spectrum = dft(random_signal)

    fig, axes = plt.subplots(3, sharex=True, figsize=(15, 15))
    axes[0].set_title("Signal")
    axes[0].plot(x, random_signal)

    axes[1].set_title("DFT: Real part")
    axes[1].bar(x, real_spectrum)

    axes[2].set_title("DFT: Imaginary part")
    axes[2].bar(x, image_spectrum)

    plt.savefig("lab_2_1.png")
    plt.show()


if __name__ == '__main__':
    main()
