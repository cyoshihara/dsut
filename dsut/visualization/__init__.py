"""
Visualization functions of dsut
====================================

This module implements vizualization utility functions for data science.
If this module grows, some functions may be moved in another module.

"""
# Author: SoftBank Corp.
# License: MIT

import matplotlib.pyplot as plt
from enum import IntEnum


class Font:
    """
    attributes for font used for vizualization
    ...
    Attributes
    ----------
    family
    size
    __family : str
        font families. eg.) Arial, Meiryo, MS Gothic...
    __size: int
        font size.
    """

    def __init__(
        self,
        family: str = "Meiryo",  # 日本語を許容し、MacOS/Windows双方にプリインストールのフォントとしてメイリオを選択
        size: int = 14
    ):
        """
        Constructor
        ...
        Parameters
        ----------
        family : str
            font family.
        size : int
            font size
        """
        self.__family = family
        self.__size = size

    @property
    def family(self):
        return self.__family

    @property
    def size(self):
        return self.__size


class Tick:
    """
    TODO: Construnting...
    """

    def __init__(self):
        # direction =
        pass


class Legend:
    """
    TODO: Construnting...
    """
    class LocationEnum(IntEnum):
        """
        TODO: Construnting...
        """
        Best = 0
        RightTop = 1
        LeftTop = 2
        LeftBottom = 3
        RightBottom = 4
        RightModdle = 5
        LeftMiddle = 6
        # 7は5と同じ
        CenterMiddle = 8
        CenterTop = 9

    def __init__(
        self,
        location: LocationEnum = LocationEnum.Best
    ):
        """
        TODO: Construnting...
        """
        self.__location = location

    @property
    def location(self):
        return self.__location


def show_graph(
    x,
    y: list,

    xlabel: str = "",
    ylabel: str = "",
    xtick: Tick = Tick(),
    ytick: Tick = Tick(),

    legend: Legend = Legend(),
    legend_label: str = "",

    font: Font = Font()
) -> list:
    """
    TODO: Construnting...
    """
    plt.rcParams["font.family"] = font.family
    plt.rcParams["font.size"] = font.size

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y, label=legend_label)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # legend
    if legend.location == Legend.LocationEnum.Best:
        plt.legend(loc='best')
    else:
        plt.legend(loc=legend.location)

    plt.show()

    return ax
