import pandas as pd
import numpy as np
from reconcile_data import create_formatted_data
from map import electionPlot


if __name__ == "__main__":
    ep = electionPlot(create_formatted_data())
    ep.populate()
    ep.show()
