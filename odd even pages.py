from datetime import datetime
from json import load, dump
from math import ceil
from os import path
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from sys import argv, exit
from forms.odd_even_form import Ui_MergeWindow
from requests import post
from PyPDF2 import PdfFileReader, PdfFileWriter

# =============================== !SECTION ===============================
# ========================= SECTION OCR Functions ========================
# ========================================================================

_settings_dt = {}


def createDirs():
    if not path.exists('settings.json'):
        _settings_dt = {'count': 0}
        with open('settings.json', 'w') as file:
            dump(_settings_dt, file)


def sendTelegram(text: str):

    chat_id = 547571285
    token = "5562840901:AAFhiQQuPjH7cn21gZ-dOELSUE686yJNgSM"

    response = post(
        url=f'https://api.telegram.org/bot{token}/sendMessage',
        data={
            'chat_id': chat_id,
            'text': f'odd even pages:\n Files Count: {text} 📕'
        }
    )


def startMerging():
    ui.progressBar.setValue(1)

    pdf_writer = PdfFileWriter()

    oddPDF = PdfFileReader(ui.odd_tx.text())
    evenPDF = PdfFileReader(ui.even_tx.text())
    for i in range(min(oddPDF.getNumPages(), evenPDF.getNumPages())):
        # Add each page to the writer object
        ui.progressBar.setValue(ceil(i/oddPDF.getNumPages() * 100) -1)
        pdf_writer.addPage(oddPDF.getPage(i))
        pdf_writer.addPage(evenPDF.getPage(i))

    if not (oddPDF.getNumPages() == evenPDF.getNumPages()):
        ui.progressBar.setValue(ceil(i/oddPDF.getNumPages() * 100) -1)
        pdf_writer.addPage(oddPDF.getPage(i))

    # Write out the merged PDF
    with open(ui.out_tx.text(), 'wb') as out:
        pdf_writer.write(out)
        ui.progressBar.setValue(100)

    _settings_dt = load(open('settings.json', 'r'))
    _settings_dt['count'] = _settings_dt['count'] + 1
    with open('settings.json', 'w') as file:
        sendTelegram(_settings_dt['count'])
        dump(_settings_dt, file)
        ui.count_lbl(_settings_dt['count'])


# =============================== !SECTION ===============================
# ========================= SECTION Main Program =========================
# ========================================================================
app = QApplication(argv)
MainWindow = QMainWindow()
ui = Ui_MergeWindow()
ui.setupUi(MainWindow)

createDirs()


def browsePDF(fileClass):
    if (fileClass == 'odd'):
        fileName = ui.odd_tx.text()
        file, check = QFileDialog.getOpenFileName(
            directory=fileName, filter="PDF File (*.pdf)")
        if check:
            ui.odd_tx.setText(file)
    else:
        fileName = ui.even_tx.text()
        file, check = QFileDialog.getOpenFileName(
            directory=fileName, filter="PDF File (*.pdf)")
        if check:
            ui.even_tx.setText(file)


def savePDF():
    fileName = ui.out_tx.text()
    if fileName == '':
        fileName = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    file, check = QFileDialog.getSaveFileName(
        directory=fileName, filter="PDF File (*.pdf)")
    if check:
        if not file.endswith('.pdf'):
            file = file + '.pdf'
        ui.out_tx.setText(file)


ui.merge_btn.clicked.connect(startMerging)
ui.odd_btn.clicked.connect(lambda: browsePDF('odd'))
ui.even_btn.clicked.connect(lambda: browsePDF('even'))
ui.out_btn.clicked.connect(lambda: savePDF())


MainWindow.show()

exit(app.exec_())


# =============================== !SECTION ===============================
