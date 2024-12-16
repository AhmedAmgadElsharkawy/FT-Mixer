import sys
from PyQt5.QtWidgets import QApplication
from view.main_window import MainWindow
import logging
logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO, filemode="w", 
                        format="%(asctime)s - %(levelname)s - %(message)s")
    logger.info("Started")
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()