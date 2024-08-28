# Williams Villalba _ January,12th 2022
import sys
from PyQt6.QtWidgets import QApplication


from view import View
from model import Model
from controller import Controller

def main():
  
  ML = QApplication(sys.argv)

  view = View()
  view.show()

  model = Model()

  
  controller = Controller(view, model)

  sys.exit(ML.exec())

if __name__ == '__main__':
  main()