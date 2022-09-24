import matplotlib
import matplotlib.pyplot as plt
import platform
if platform.system() == 'Darwin':
    matplotlib.use('MacOSX')
else:
    matplotlib.use("TkAgg")



# given a list of y values, this function plots it using matplotlib in a visualizable way
class Plotter:
    def __init__(self):
        pass

    def plot(self, y: list, title='', x_title='', y_title=''):
        plt.plot(y)
        plt.ylabel(y_title)
        plt.suptitle(title)
        plt.xlabel(x_title)
        plt.show()

    def bar(self, kpi, traversed, result: dict):
        fig, ax = plt.subplots(len(result.keys()), sharex=True, sharey=True)
        all = []
        for values in result.values():
            all += values
        print(all)
        scope = []
        counter = round(min(all), 1) - 0.2
        ceiling = round(max(all), 1) + 0.2
        #define scope
        while counter <= ceiling:
            scope.append(format(counter, '.1f'))
            counter += 0.1
        print(scope)
        vals = {}
        points = []
        y = []
        counter = 0
        for algo in result.keys():
            # initialize all values in the scope as 0
            for i in scope:
                vals[i] = 0
            # count all results and increment values accordingly (for algo)
            for point in result[algo]:
                temp = format(round(point, 1), '.1f')
                vals[temp] += 1
            # val dict to points list
            for val in vals.items():
                points.append([val[0], val[1]])
            points.sort()
            for point in points:
                y.append(point[1])
            ax[counter].bar(scope, y, color='blue', width=0.2)
            print(algo)
            print("scope ", scope)
            print("incidents ", y)
            vals.clear()
            points.clear()
            y.clear()
            counter += 1
        print("Benchmarking " + kpi + ", Stations Traversed = " + str(traversed))
        plt.suptitle("Benchmarking " + kpi + ", Stations Traversed = " + str(traversed))
        names = ", ".join(result.keys())
        plt.xlabel(kpi + " for " + names + " in ms")
        print(kpi + " for " + names + " in ms")
        plt.show()
        # 'Dijkstra': [26.857852935791016, 27.530193328857422, 26.99136734008789, 34.22975540161133, 32.55128860473633, 29.19912338256836, 30.8990478515625, 36.711692810058594, 29.900074005126953, 27.69947052001953]
        # 'A_star': [31.039714813232422, 29.821395874023438, 30.868053436279297, 31.409263610839844, 29.478073120117188, 31.280517578125, 27.30846405029297, 28.061866760253906, 27.170181274414062, 26.731491088867188]

    def line(self, kpi, result: dict):
        points = []
        x = []
        y = []
        for algo in result.keys():
            for point in result[algo]:
                points.append([point['traversed'], point['value']])
            points.sort()
            for p in points:
                x.append(p[0])
                y.append(p[1])
            print(x)
            print(y)
            plt.plot(x, y, label=algo)
            points.clear()
            x.clear()
            y.clear()
        plt.xlabel('Stations Traversed')
        plt.ylabel(kpi)
        plt.title('Benchmarking ' + kpi)
        plt.legend()
        plt.show()
