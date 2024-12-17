from PyQt6.QtWidgets import *
from gpohi import *
import requests

def ckicugrohi(uani, grivnu):
    windows2 = QDialog()
    windows2.setWindowTitle('Your money:')
    windows2.resize(200, 200)
    windows2.move(700, 300)

    dsfsdf = QLabel("Гроші в юанях")
    ghohicny = QLineEdit(uani)
    fsdfsdf = QLabel("Гроші в гривнях")
    grohigrn = QLineEdit(grivnu)

    windows2.setStyleSheet("""
    QDialog { 
        background-color : #FFDAB9;
        color: 	#CD3333;

    }

    QLineEdit { 
        background-color : #FFF5EE;
        color: 	#CD3333;
        
    }
    """)

    mine_line45 = QVBoxLayout()
    mine_line45.addWidget(dsfsdf)
    mine_line45.addWidget(ghohicny)
    mine_line45.addWidget(fsdfsdf)
    mine_line45.addWidget(grohigrn)


    windows2.setLayout(mine_line45)

    windows2.show()
    windows2.exec()
