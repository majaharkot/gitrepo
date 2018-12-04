#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget
from gui import Ui_Widget, LoginDialog
from PyQt5.QtWidgets import QMessageBox, QInputDialog
import baza
from tbmodel import TbModel, pola


class Zadania(QWidget, Ui_Widget):

    def __init__(self, parent=None):
        super(Zadania, self).__init__(parent)
        self.setupUi(self)
        
        self.logujBtn.clicked.connect(self.loguj)
        self.koniecBtn.clicked.connect(self.koniec)
        self.dodajBtn.clicked.connect(self.dodaj)
        self.zapiszBtn.clicked.connect(self.zapisz)

    def zapisz(self):
        baza.zapiszDane(baza.sesja, model.tabela)
        model.layoutChanged.emit()

    def dodaj(self):
        """ Dodawanie nowego zadania """
        zadanie, ok = QInputDialog.getMultiLineText(self,
                                                    'Zadanie',
                                                    'Co jest do zrobienia?')
        if not ok or not zadanie.strip():
            QMessageBox.critical(self,
                                 'Błąd',
                                 'Zadanie nie może być puste.',
                                 QMessageBox.Ok)
            return

        zadanie = baza.dodajZadanie(baza.sesja, self.osoba, zadanie)
        model.tabela.append(zadanie)
        model.layoutChanged.emit()  # wyemituj sygnał: zaszła zmiana!
        if len(model.tabela) == 1:  # jeżeli to pierwsze zadanie
            self.odswiezWidok()     # trzeba przekazać model do widoku
    def koniec(self):
        self.close()

    def loguj(self):
        login, haslo, ok = LoginDialog.getLoginHaslo(self)
        if not ok:
            return
            
        if not login or not haslo:
            QMessageBox.warning(
                                self, 'Błąd', 'Pusty login lub hasło!',
                                QMessageBox.Ok)
            return
        self.osoba = baza.loguj(baza.sesja, login, haslo)
        if self.osoba is None:
            QMessageBox.critical(self, 'Błąd', 'Błędne dane!', QMessageBox.Ok)
            return

        # ~QMessageBox.information(
                    # ~self, 'Dane logowania',
                    # ~'Podano: ' + login + ' ' + haslo, QMessageBox.Ok)

        zadania = baza.pobierzDane(baza.sesja, self.osoba)
        model.aktualizuj(zadania)
        model.layoutChanged.emit()
        self.odswiezWidok()
        self.dodajBtn.setEnabled(True)
        self.zapiszBtn.setEnabled(True)

    def odswiezWidok(self):
        self.widok.setModel(model)  # przekazanie modelu do widoku
        self.widok.hideColumn(0)  # ukrywamy kolumnę id
        # ograniczenie szerokości ostatniej kolumny
        self.widok.horizontalHeader().setStretchLastSection(True)
        # dopasowanie szerokości kolumn do zawartości
        self.widok.resizeColumnsToContents()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    model = TbModel(pola)
    okno = Zadania()
    okno.show()
    okno.move(350, 200)
    sys.exit(app.exec_())
