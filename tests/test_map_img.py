import matplotlib.pyplot as plt
import sys


ws_id = (48.999192, -117.032352)
ws_pix = (130, 18)

miss = (31.000673, -85.001672)
miss_pix = (575, 347)

miami = (25.769568, -80.197209)


class electionPlot:

    def __init__(self):
        self.mercator = plt.imread("../data/US_Mercator.png")
        self.fig, self.ax = plt.subplots()
        self.ax.imshow(self.mercator)

    def test_point(self, lat, long):
        pix = self.ll2pix(lat, long)
        self.ax.scatter(pix[0], pix[1], s=15, c='r')

    def ll2pix(self, lat, long):

        # x_b = 13.869760376296599
        # y_b = -17.735005053227518
        #
        # x_a = 1753.4308496643794
        # y_a = 903.176795769178

        x_b = 13.899769576026893
        y_b = -17.649876726373186

        x_a = 1756.7227257404702
        y_a = 882.8296984918912

        return (x_b * long + x_a, y_b * lat + y_a)

    def show(self):
        # self.ax.axis('off')
        plt.show()


if __name__ == "__main__":
    lat = float(sys.argv[1])
    print("lat: ", lat)
    long = float(sys.argv[2])
    print("long: ", long)
    ep = electionPlot()
    ep.test_point(lat, long)
    ep.show()