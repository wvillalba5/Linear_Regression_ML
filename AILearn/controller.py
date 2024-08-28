# Williams Villalba _ January,12th 2022
import os
class Controller:

    def __init__(self, view, model):
        self.__view = view
        self.__model = model
        self.__connect_signals()

    def __connect_signals(self):
        
        self.__view.ui.Graph_cboBox.activated.connect(self.__view.Change_Widget)
        self.__view.ui.Calculate_btn.clicked.connect(self.__inicial_values)
        self.__view.ui.Calculate_btn.clicked.connect(self.__view.status_bar)
        self.__view.ui.Btn_predictvalue.clicked.connect(self.__predict_value)
        self.__view.ui.Btn_predictvalue.clicked.connect(self.__view.status_bar)
        self.__view.ui.Btn_Delete_graph.clicked.connect(self.__view.clear_canvas)
        self.__view.ui.Btn_Open_file.clicked.connect(self.__getPath)
        self.__view.ui.Btn_Open_file.clicked.connect(self.__view.status_bar)
        self.__view.exitAction.triggered.connect(self.__view.close_window)
        self.__view.openAction.triggered.connect(self.__getPath)

    def __getPath(self):

            path_file = self.__view.show_dialog()
            if os.path.splitext(str(path_file))[1].lower() == '.txt':
                self.__model.read_file(str(path_file))
                self.__read_scatter()

    def __read_scatter(self):
        X = self.__model.X
        y = self.__model.y
        x_graph_label = self.__view.ui.axe_x_Qline.text()
        y_graph_label = self.__view.ui.axe_y_Qline.text()
        self.__view.call_canvas_scatter(X,y,x_graph_label,y_graph_label)
        

    def __inicial_values(self):
        try:
            theta0 = float(self.__view.ui.theta_0.text())
            theta1 = float(self.__view.ui.theta_1.text())
            iter_num = int(self.__view.ui.value_iterations.text())
            Alpha = float(self.__view.ui.Alpha.text())
        except ValueError:
            theta0 = 0
            theta1 = 0
            iter_num = 1500
            Alpha = 0.01
        if Alpha>=0.001 and Alpha <= 0.02:
            self.__model.calling_Cost_Function(theta0, theta1,iter_num,Alpha)
            self.__print_data()

    def __print_data(self):
        self.__view.ui.theta0_Qline.setText(str(self.__model.theta_m[0]))
        self.__view.ui.theta1_Qline.setText(str(self.__model.theta_m[1]))
        self.__view.ui.Cost_QLine.setText(str(self.__model.J))            
        self.__scatter_line_Data()
        
        
    def __scatter_line_Data(self):
        X = self.__model.X
        y = self.__model.y
        X1 = self.__model.X1
        theta_m = self.__model.theta_m
        x_graph_label = self.__view.ui.axe_x_Qline.text()
        y_graph_label = self.__view.ui.axe_y_Qline.text()

        self.__view.call_canvas_Linear(X,y,X1,theta_m,x_graph_label,y_graph_label)

    def __predict_value(self):
        Value_predicted = self.__view.ui.PValue_lineEdit.text()
        self.__model.predictions(Value_predicted)
        self.__view.ui.Value_predicted.setText(str(self.__model.predict1)) 
