import matplotlib.pyplot as plt


class electionPlot:
    
    def __init__(self, formatted_data):
        self.mercator = plt.imread("../data/US_Mercator.png")
        self.fig, self.ax = plt.subplots()
        self.ax.imshow(self.mercator)
        self.election_data = formatted_data


    def populate(self):
        ii_count = 0
        print()
        print("Populating Map")
        print("--------------")
        for ii, datum in enumerate(self.election_data):

            if datum[0] == 10000:
                continue

            pix = self.ll2pix(datum[0], datum[1])

            if datum[2] == "R":
                self.ax.scatter(pix[0], pix[1], s=(15*datum[3]/3434308), c='r')
            else:
                self.ax.scatter(pix[0], pix[1], s=(15*datum[3]/3434308), c='b')

            if 100 * ii / len(self.election_data) > ii_count:
                ii_count = ii_count + 10
                print("% " + str(ii_count))


    def ll2pix(self, lat, long):

        x_b = 13.869760376296599
        y_b = -17.735005053227518

        x_a = 1753.4308496643794
        y_a = 903.176795769178

        return (x_b*long + x_a, y_b*lat + y_a)


    def show(self):
        self.ax.axis('off')
        plt.show()


if __name__ == "__main__":
    ep = electionPlot()
    ep.show()