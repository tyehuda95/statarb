from src.TickerData import TickerData
import matplotlib.pyplot as plt
from typing import Tuple


class Plotter:

    @staticmethod
    def plot(data: Tuple[TickerData]) -> None:

        f, axes = plt.subplots(nrows=2, ncols=1, figsize=(16, 8))
        ax0, ax1 = axes

        # plot returns
        for ticker_data in data:
            r = ticker_data.returns
            r.plot(label=r.name, ax=ax0)
        ax0.legend(loc=r"best")
        ax0.set_ylabel(r"Returns [%]")
        ax0.set_xlabel(r"Date")
        ax0.grid(b=True, which='major', color='0.65', linestyle='-')

        # plot cumulative returns
        for ticker_data in data:
            cr = ticker_data.cumulative_returns
            cr.plot(label=cr.name, ax=ax1)

        ax1.legend(loc=r"best")
        ax1.set_ylabel(r"Cumulative Returns [%]")
        ax1.set_xlabel(r"Date")
        ax1.grid(b=True, which='major', color='0.65', linestyle='-')

        plt.show()