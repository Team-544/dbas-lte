import matplotlib.pyplot as plt


class Visualization:
    @staticmethod
    def showPlot(x, y, x_name, y_name, title):
        plt.figure()
        plt.plot(x, y)
        plt.xlabel(x_name)
        plt.ylabel(y_name)
        plt.title(title)
        plt.show()


if __name__ == '__main__':
    Visualization.showPlot([0, 1, 2], [1, 2, 3], 'x', 'y', 'Hello plot')