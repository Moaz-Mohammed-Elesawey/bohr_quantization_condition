try:
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtWidgets import *
    print('[INFO] using PyQt5 backend')

except ImportError as e:
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
    print('[INFO] using PySide2 backend')


import numpy as np
import matplotlib as mpl
mpl.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg,
        NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

from ui_main import Ui_MainWindow


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = self.fig.add_subplot(111, projection='polar')
        super(MplCanvas, self).__init__(self.fig)


class MainWindow(QMainWindow):
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)

        self.initUi()

    def initUi(self):

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui_components()

        self.ui.plot_btn.clicked.connect(lambda e: self.plot_callback(move=False))
        self.ui.n_slider.sliderMoved.connect(lambda e: self.plot_callback(move=True))
        self.ui.R_slider.sliderMoved.connect(lambda e: self.plot_callback(move=True))
        self.ui.A_slider.sliderMoved.connect(lambda e: self.plot_callback(move=True))

        self.ui.n_slider.valueChanged.connect(self.slider_n_callback)
        self.ui.R_slider.valueChanged.connect(self.slider_R_callback)
        self.ui.A_slider.valueChanged.connect(self.slider_A_callback)

        self.setWindowIcon(QIcon('./icons/icon.png'))


        self.show()

    def ui_components(self):
        
        self.sc = MplCanvas()
        toolbar = NavigationToolbar(self.sc, None)

        self.ui.verticalLayout_2.addWidget(self.sc)
        self.ui.verticalLayout_2.addWidget(toolbar)
        

    def plot_callback(self, move=False):


        self.n = self.ui.n_inp.value()
        if move: self.n += .1

        self.A = self.ui.A_inp.value()
        self.R = self.ui.R_inp.value()

        if self.n and self.A and self.R:

            _remainder = round(self.n - int(self.n), 1)
            _factor = 2

            if _remainder in (.1, .3, .7, .9):
                _factor = 12
            elif _remainder in (.2, .4, .6, .8):
                _factor = 10
            elif _remainder == .5:
                _factor = 4

            self.sc.ax.clear()

            theta = np.linspace(0, _factor*np.pi, 1000)
            r = self.R + self.A * np.sin(self.n * theta)
            r_ = np.repeat(self.R, r.shape[0])

            self.sc.ax.plot(theta, r, color='r', label=r'$r = R + Asin(n\theta)$', alpha=.6)
            self.sc.ax.plot(theta, r_, color='b', label=r'$r = R$', alpha=.8)

            self.sc.ax.axes.set_rmax(np.max(r) + (np.mean(r)/2))
            # self.sc.ax.axes.set_rticks(np.arange(np.min(r), np.max(r), .2))  # Less radial ticks
            self.sc.ax.axes.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
            self.sc.ax.axes.grid(True)

            self.sc.ax.legend(fontsize=11, loc='upper right')

            self.sc.draw()

    def slider_n_callback(self, value):
        self.ui.n_inp.setValue((value / 10))

    def slider_R_callback(self, value):
        self.ui.R_inp.setValue((value / 10))

    def slider_A_callback(self, value):
        self.ui.A_inp.setValue((value / 10))



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())

