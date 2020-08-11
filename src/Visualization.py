import matplotlib.pyplot as plt
import _thread


class Visualization:
    @staticmethod
    def showPlot(x, y, x_name, y_name, title):
        v = Visualization()
        _thread.start_new_thread(v.__show, (x, y, x_name, y_name, title,))

    def __show(self,x, y, x_name, y_name, title):
        plt.figure()
        plt.plot(x, y)
        plt.xlabel(x_name)
        plt.ylabel(y_name)
        plt.title(title)
        plt.show()

if __name__ == '__main__':
    Visualization.showPlot(['2016-07-17 00:00:00', '2016-07-18 00:00:00', '2016-07-19 00:00:00'], [0.001, 0.002, 0.004], 'x', 'y', 'Hello pl范戳色')