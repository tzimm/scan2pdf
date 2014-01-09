from PySide import QtCore, QtGui
import Scan2Pdf_gui
import converter
import sys
import os #used to get username for filedialog

class _scan_gui():

    def __init__(self, qtgui_mainwindow):       
        self.GUI = Scan2Pdf_gui.Ui_MainWindow()
        self.GUI.setupUi(qtgui_mainwindow)

        self.picturepath = "/home/"+os.getlogin()+"/Pictures"
        #initial values:
        self.Say("Started")
        self.GUI.slider_contrast.setValue(20)
        self.GUI.slider_brightness.setValue(20)
        self.GUI.slider_sharpness.setValue(20)
        self.GUI.checkbx_flip.setChecked(True)
        self.GUI.txt_FileToList.clear()
        self.GUI.txt_FileToList.insertPlainText(self.picturepath+"/input.jpg")
        self.GUI.txt_outputpdf.clear()
        self.GUI.txt_outputpdf.insertPlainText(self.picturepath+"/output.pdf")

        #connect signals
        self.GUI.pb_search.clicked.connect(self.SearchPbClicked)
        self.GUI.pb_add.clicked.connect(self.AddPbClicked)
        self.GUI.pb_join.clicked.connect(self.JoinPbClicked)
        self.GUI.slider_sharpness.sliderMoved.connect(self.SliderSharpnessMoved)
        self.GUI.slider_contrast.sliderMoved.connect(self.SliderContrastMoved)
        self.GUI.slider_brightness.sliderMoved.connect(self.SliderBrightnessMoved)
        self.GUI.list_FilesToJoin.itemDoubleClicked.connect(self.RemoveItem)

        self.pdfconverter = converter.Converter()

    def SliderSharpnessMoved(self):
        value = float(self.GUI.slider_sharpness.value())/10
        self.Say("Sharpness:  " + str(value))

    def SliderContrastMoved(self):
        value = float(self.GUI.slider_contrast.value())/10
        self.Say("Contrast:   " + str(value))

    def SliderBrightnessMoved(self):
        value = float(self.GUI.slider_brightness.value())/10
        self.Say("Brightness: " + str(value))

    def RemoveItem(self, WidgetItem):
        #self.GUI.list_FilesToJoin.removeItemWidget(WidgetItem)
        row = self.GUI.list_FilesToJoin.row(WidgetItem)
        self.GUI.list_FilesToJoin.takeItem(row)        
        self.Say("Item removed")

    def SearchPbClicked(self):
        """
        open file dialog
        insert path into txtbox
        """
        self.Say("search files in "+ self.picturepath)
        filename = QtGui.QFileDialog.getOpenFileName(None,'Add file', self.picturepath)[0]
        self.Say(filename)
        self.GUI.txt_FileToList.clear()
        self.GUI.txt_FileToList.insertPlainText(filename)
        self.GUI.list_FilesToJoin.addItem(filename)
   
    def AddPbClicked(self):
        """
        move txtbox content into list widget
        """
        self.Say("add element to list")
        #text = self.GUI.txt_FileToList.text()
        text = self.GUI.txt_FileToList.document().toPlainText()
        self.Say(text)
        self.GUI.list_FilesToJoin.addItem(text)
        
    def JoinPbClicked(self):
        """
        input = extract stuff out of list widget
        preferences = extract preferences out gui
        output = extract output pdf out of txtbox
        """
        self.Say("converting")
        
        #generate arguments
        preferences = self.ExtractPreferences()#preferences
        fileslist= self.ExtractList()#list items
        outputpath = self.GUI.txt_outputpdf.document().toPlainText()#path
        
        #execute conversion
        self.pdfconverter.Convert(preferences, fileslist, outputpath)
        self.Say("conversion finished")

    def ExtractList(self):
        #stopped here
        fileslist=[]
        for i in range(0, self.GUI.list_FilesToJoin.count()):
            #take always first item because it is deleted
            fileslist.append(self.GUI.list_FilesToJoin.takeItem(0).text())
        return fileslist

    def ExtractPreferences(self):
        """
        Annotation: the checkbox "onepdf" is removed: if output is empty  no output file will be generated
        """
        preferences = {}
        preferences["flipflag"] = self.GUI.checkbx_flip.isChecked()

        preferences["contrast"] = float(self.GUI.slider_contrast.value())/10
        preferences["brightness"] = float(self.GUI.slider_brightness.value())/10
        preferences["sharpness"] = float(self.GUI.slider_sharpness.value())/10
        return preferences

    def Say(self, status_message):
        self.GUI.label_status.setText(status_message)

app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()
scan_gui = _scan_gui(window)
window.show()
#scan_gui.show()
sys.exit(app.exec_())



