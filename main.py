# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt
import numpy as np

def get_next(x, r):
    return r * x * (1 - x)


def main():
    k=100
    for r in np.linspace(1,4,1000):
        x = [.5]
        for i in range(1000):
            x.append(get_next(x[i], r))
        ys = x[-k:]
        xs = r*np.ones_like(ys)
        plt.plot(xs,ys,"b,")
    plt.show()


main()
