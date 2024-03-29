import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi

class FinestraPrincipal(QMainWindow):
  
    def __init__(self):
        super(FinestraPrincipal, self).__init__()
        self.setWindowIcon(QIcon('calc.ico'))
        loadUi('calcper_gui.ui',self)

        self.btnCost.clicked.connect(self.calcCost)
        self.btnAugPer.clicked.connect(self.augmentPer)
        self.btnMenysDte.clicked.connect(self.ferDte)
        self.btnMesIva.clicked.connect(self.posarIva)
        self.btnMenysIva.clicked.connect(self.treureIva)
        self.btnPosarZero.clicked.connect(self.posarAzero)
        self.btnCopia.clicked.connect(self.copiaResult)

        self.iPreu.setText("0") 
        self.iPreuDte.setText("0")

    def calcCost(self):
        valor1 = float(self.iPreu.text().replace(",","."))
        valor2 = float(self.iPreuDte.text().replace(",","."))
        if valor1 == 0 and valor2 == 0:
            self.missatge()
        else:
            self.etiSortRes.setText(str(round((valor1 - valor2)/valor2*100,2))+ "%")
        
    def augmentPer(self):
        valor1 = float(self.iPreu.text().replace(",","."))
        valor2 = float(self.iPreuDte.text().replace(",","."))
        self.etiSortRes.setText(str(round(valor1/(1-(valor2/100)),2))+ "€")
    
    def ferDte(self):
        valor1 = float(self.iPreu.text().replace(",","."))
        valor2 = float(self.iPreuDte.text().replace(",","."))
        dte = valor1*(valor2/100)
        self.etiSortRes.setText(str(round(valor1-dte,2))+ "€")

    def posarIva(self):
        valor1 = float(self.iPreu.text().replace(",","."))
        valor2 = float(self.iPreuDte.text().replace(",","."))
        if valor2 == 0:
            self.etiSortRes.setText(str(round(valor1*0.21+valor1,2))+ "€")
        else:
            self.etiSortRes.setText(str(round(valor1*(valor2/100)+valor1,2))+ "€")

    def treureIva(self):
        valor1 = float(self.iPreu.text().replace(",","."))
        self.etiSortRes.setText(str(round(valor1/1.21,2))+ "€")

    def missatge(self):
        msg = QMessageBox()
        msg.setIcon(1)
        msg.setWindowTitle("Atenció!")
        msg.setText("Falta algun valor")
        msg.exec_()
    
    def posarAzero(self):
        self.iPreu.setText("0")
        self.iPreuDte.setText("0")
        self.etiSortRes.setText("0")

    def copiaResult(self):
        temp = len(self.etiSortRes.text())
        resolt = self.etiSortRes.text()[:temp-1]
        self.iPreu.setText(resolt)
        self.iPreuDte.setText("0")
    
app = QApplication(sys.argv)
finestra = FinestraPrincipal()
finestra.show()
app.exec_()

