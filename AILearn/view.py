
import os
from tkinter.font import BOLD
from PyQt6.QtWidgets import QMainWindow, QFileDialog
from PyQt6.QtGui import QAction,QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from configuration import config
from Linear_Matplot import*


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.theta0_Qline.setReadOnly(True)
        self.ui.theta1_Qline.setReadOnly(True)
        self.ui.Cost_QLine.setReadOnly(True)
        self.ui.Value_predicted.setReadOnly(True)
        self.ui.Graph_cboBox.addItems(["Scatter", "Line"])

        self.ui.theta_0.setPlaceholderText('Enter a integer')
        self.ui.theta_1.setPlaceholderText('Enter a integer')
        self.ui.value_iterations.setPlaceholderText('Enter a integer')
        self.ui.Alpha.setPlaceholderText('from 0.001 to 0.02')
        self.ui.axe_x_Qline.setPlaceholderText('Name "X" axe')
        self.ui.axe_y_Qline.setPlaceholderText('Name "Y" axe')
        self.ui.PValue_lineEdit.setPlaceholderText('Enter a float')
        self.__create_menu()

    def __create_menu(self):
        fileMenu = self.ui.menuFile

        self.openAction = QAction(QIcon(os.path.join(*config.get_instance().data["Btn_Open_file_icon"])),"Open", self)
        self.openAction.setShortcut("Ctrl+O")
        fileMenu.addAction(self.openAction)
        fileMenu.addSeparator()
        self.exitAction = QAction(QIcon(os.path.join(*config.get_instance().data["exit_icon"])),"Exit", self)
        self.exitAction.setShortcut("Ctrl+X")
        fileMenu.addAction(self.exitAction)


    def show_dialog(self):
        file_filter = 'Data File (*.txt)'
        self.path_file_txt = QFileDialog.getOpenFileName(parent=self, caption='Select data file',directory=os.getcwd(),
        filter=file_filter) 
        return self.path_file_txt[0]
        

    def call_canvas_scatter(self,X,y,x_graph_label,y_graph_label):
        self.scatter = Canvas_scatter(X,y,x_graph_label,y_graph_label)
        self.ui.scatter_VLayout.addWidget(self.scatter)
        self.ui.stackedWidget.setCurrentIndex(0)
      

    def call_canvas_Linear(self,X,y,X1,theta_m,x_graph_label,y_graph_label):
        self.Linear = Canvas_Linear(X,y,X1,theta_m,x_graph_label,y_graph_label)
        self.ui.line_VLayout.addWidget(self.Linear)
        self.ui.stackedWidget.setCurrentIndex(1)
        


    def clear_canvas(self):
        self.ui.scatter_VLayout.takeAt(0)
        self.ui.line_VLayout.takeAt(0)
        

    def Change_Widget(self):
        widget = self.ui.Graph_cboBox.currentIndex()
        self.ui.stackedWidget.setCurrentIndex(widget)

    def status_bar(self):
        sender = self.sender()
        message_toolbar = f'Event: "{sender.text()}" has been selected'
        self.statusBar().showMessage(message_toolbar)

    def close_window(self):
        self.close() 
       
class Canvas_scatter(FigureCanvas):
    
    def __init__(self, X , y,x_graph_label,y_graph_label): 
        plt.close('all')
        figure , ax = plt.subplots(1, dpi=100, figsize=(5, 5), 
            sharey=True, facecolor='white')
        super().__init__(figure)
        
        ax.plot(X,y,'o',color = 'tab:blue', markersize=7)

        ax.set_xlabel(x_graph_label, fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})
        ax.set_ylabel(y_graph_label)
        ax.set_xlim([4,25])
        ax.grid(axis = 'y', color = 'gray', linestyle = 'dashed')
        ax.grid(axis = 'x', color = 'gray', linestyle = 'dashed')
        figure.suptitle('Scatter Plot', size=12, fontweight=BOLD)
        

class Canvas_Linear(FigureCanvas):
    
    def __init__(self, X,y,X1,theta_m,x_graph_label,y_graph_label):
        plt.close('all')     
        self.fig , self.ax = plt.subplots(1,dpi=100, figsize=(5, 5), 
            sharey=True, facecolor='white')
        super().__init__(self.fig) 
        self.ax.plot(X,y,'o',color = 'tab:gray', markersize=7)
        self.ax.plot(X,X1 @ theta_m, ':r')
        self.ax.set_xlabel(x_graph_label, fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_ylabel(y_graph_label)
        self.ax.set_xlim([4,25])
        self.ax.grid(axis = 'y', color = 'gray', linestyle = 'dashed')
        self.ax.grid(axis = 'x', color = 'gray', linestyle = 'dashed')
        self.fig.suptitle(' Adjusted Line',size=12, fontweight=BOLD)
        

