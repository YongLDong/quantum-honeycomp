# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(973, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.nsuper_struct = QtWidgets.QLineEdit(self.tab_2)
        self.nsuper_struct.setObjectName("nsuper_struct")
        self.gridLayout_5.addWidget(self.nsuper_struct, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 0, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.show_structure = QtWidgets.QPushButton(self.tab_2)
        self.show_structure.setObjectName("show_structure")
        self.gridLayout_8.addWidget(self.show_structure, 1, 0, 1, 1)
        self.show_structure_3d = QtWidgets.QPushButton(self.tab_2)
        self.show_structure_3d.setObjectName("show_structure_3d")
        self.gridLayout_8.addWidget(self.show_structure_3d, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.nbands = QtWidgets.QLineEdit(self.tab)
        self.nbands.setObjectName("nbands")
        self.gridLayout_3.addWidget(self.nbands, 2, 1, 1, 1)
        self.nk_bands = QtWidgets.QLineEdit(self.tab)
        self.nk_bands.setObjectName("nk_bands")
        self.gridLayout_3.addWidget(self.nk_bands, 1, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 0, 0, 1, 1)
        self.bands_operator = QtWidgets.QComboBox(self.tab)
        self.bands_operator.setObjectName("bands_operator")
        self.bands_operator.addItem("")
        self.bands_operator.addItem("")
        self.gridLayout_3.addWidget(self.bands_operator, 0, 1, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.show_bands = QtWidgets.QPushButton(self.tab)
        self.show_bands.setObjectName("show_bands")
        self.gridLayout_9.addWidget(self.show_bands, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.delta_ldos_single = QtWidgets.QLineEdit(self.tab_3)
        self.delta_ldos_single.setObjectName("delta_ldos_single")
        self.gridLayout_4.addWidget(self.delta_ldos_single, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 1, 0, 1, 1)
        self.nsuper_ldos_single = QtWidgets.QLineEdit(self.tab_3)
        self.nsuper_ldos_single.setObjectName("nsuper_ldos_single")
        self.gridLayout_4.addWidget(self.nsuper_ldos_single, 3, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 3, 0, 1, 1)
        self.energy_ldos_single = QtWidgets.QLineEdit(self.tab_3)
        self.energy_ldos_single.setObjectName("energy_ldos_single")
        self.gridLayout_4.addWidget(self.energy_ldos_single, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 2, 0, 1, 1)
        self.nk_ldos_single = QtWidgets.QLineEdit(self.tab_3)
        self.nk_ldos_single.setObjectName("nk_ldos_single")
        self.gridLayout_4.addWidget(self.nk_ldos_single, 2, 1, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.show_ldos_single = QtWidgets.QPushButton(self.tab_3)
        self.show_ldos_single.setObjectName("show_ldos_single")
        self.gridLayout_10.addWidget(self.show_ldos_single, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_35 = QtWidgets.QGridLayout()
        self.gridLayout_35.setObjectName("gridLayout_35")
        self.ne_ldos = QtWidgets.QLineEdit(self.tab_7)
        self.ne_ldos.setObjectName("ne_ldos")
        self.gridLayout_35.addWidget(self.ne_ldos, 0, 1, 1, 1)
        self.delta_ldos = QtWidgets.QLineEdit(self.tab_7)
        self.delta_ldos.setObjectName("delta_ldos")
        self.gridLayout_35.addWidget(self.delta_ldos, 3, 1, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.tab_7)
        self.label_43.setObjectName("label_43")
        self.gridLayout_35.addWidget(self.label_43, 3, 0, 1, 1)
        self.nk_ldos = QtWidgets.QLineEdit(self.tab_7)
        self.nk_ldos.setObjectName("nk_ldos")
        self.gridLayout_35.addWidget(self.nk_ldos, 1, 1, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.tab_7)
        self.label_44.setObjectName("label_44")
        self.gridLayout_35.addWidget(self.label_44, 0, 0, 1, 1)
        self.label_45 = QtWidgets.QLabel(self.tab_7)
        self.label_45.setObjectName("label_45")
        self.gridLayout_35.addWidget(self.label_45, 1, 0, 1, 1)
        self.label_46 = QtWidgets.QLabel(self.tab_7)
        self.label_46.setObjectName("label_46")
        self.gridLayout_35.addWidget(self.label_46, 2, 0, 1, 1)
        self.window_ldos = QtWidgets.QLineEdit(self.tab_7)
        self.window_ldos.setObjectName("window_ldos")
        self.gridLayout_35.addWidget(self.window_ldos, 2, 1, 1, 1)
        self.nsuper_ldos = QtWidgets.QLineEdit(self.tab_7)
        self.nsuper_ldos.setObjectName("nsuper_ldos")
        self.gridLayout_35.addWidget(self.nsuper_ldos, 4, 1, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.tab_7)
        self.label_47.setObjectName("label_47")
        self.gridLayout_35.addWidget(self.label_47, 4, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_35)
        self.show_interactive_ldos = QtWidgets.QPushButton(self.tab_7)
        self.show_interactive_ldos.setObjectName("show_interactive_ldos")
        self.verticalLayout_2.addWidget(self.show_interactive_ldos)
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.delta_dos = QtWidgets.QLineEdit(self.tab_4)
        self.delta_dos.setEnabled(False)
        self.delta_dos.setObjectName("delta_dos")
        self.gridLayout_6.addWidget(self.delta_dos, 0, 1, 1, 1)
        self.nume_dos = QtWidgets.QLineEdit(self.tab_4)
        self.nume_dos.setEnabled(False)
        self.nume_dos.setObjectName("nume_dos")
        self.gridLayout_6.addWidget(self.nume_dos, 2, 1, 1, 1)
        self.numpol_dos = QtWidgets.QLineEdit(self.tab_4)
        self.numpol_dos.setObjectName("numpol_dos")
        self.gridLayout_6.addWidget(self.numpol_dos, 3, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.tab_4)
        self.label_17.setObjectName("label_17")
        self.gridLayout_6.addWidget(self.label_17, 4, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.tab_4)
        self.label_14.setEnabled(False)
        self.label_14.setObjectName("label_14")
        self.gridLayout_6.addWidget(self.label_14, 2, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.tab_4)
        self.label_13.setEnabled(False)
        self.label_13.setObjectName("label_13")
        self.gridLayout_6.addWidget(self.label_13, 0, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setObjectName("label_15")
        self.gridLayout_6.addWidget(self.label_15, 3, 0, 1, 1)
        self.nk_dos = QtWidgets.QLineEdit(self.tab_4)
        self.nk_dos.setObjectName("nk_dos")
        self.gridLayout_6.addWidget(self.nk_dos, 4, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.tab_4)
        self.label_18.setObjectName("label_18")
        self.gridLayout_6.addWidget(self.label_18, 1, 0, 1, 1)
        self.ewindow_dos = QtWidgets.QLineEdit(self.tab_4)
        self.ewindow_dos.setObjectName("ewindow_dos")
        self.gridLayout_6.addWidget(self.ewindow_dos, 1, 1, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.show_dos = QtWidgets.QPushButton(self.tab_4)
        self.show_dos.setObjectName("show_dos")
        self.gridLayout_12.addWidget(self.show_dos, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.show_fermi_surface = QtWidgets.QPushButton(self.tab_6)
        self.show_fermi_surface.setObjectName("show_fermi_surface")
        self.verticalLayout.addWidget(self.show_fermi_surface)
        self.gridLayout_37 = QtWidgets.QGridLayout()
        self.gridLayout_37.setObjectName("gridLayout_37")
        self.label_52 = QtWidgets.QLabel(self.tab_6)
        self.label_52.setObjectName("label_52")
        self.gridLayout_37.addWidget(self.label_52, 1, 0, 1, 1)
        self.delta_fs = QtWidgets.QLineEdit(self.tab_6)
        self.delta_fs.setObjectName("delta_fs")
        self.gridLayout_37.addWidget(self.delta_fs, 2, 1, 1, 1)
        self.energy_fs = QtWidgets.QLineEdit(self.tab_6)
        self.energy_fs.setObjectName("energy_fs")
        self.gridLayout_37.addWidget(self.energy_fs, 0, 1, 1, 1)
        self.label_54 = QtWidgets.QLabel(self.tab_6)
        self.label_54.setObjectName("label_54")
        self.gridLayout_37.addWidget(self.label_54, 2, 0, 1, 1)
        self.nk_fs = QtWidgets.QLineEdit(self.tab_6)
        self.nk_fs.setObjectName("nk_fs")
        self.gridLayout_37.addWidget(self.nk_fs, 1, 1, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.tab_6)
        self.label_40.setObjectName("label_40")
        self.gridLayout_37.addWidget(self.label_40, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_37)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.delta_kbands = QtWidgets.QLineEdit(self.tab_5)
        self.delta_kbands.setObjectName("delta_kbands")
        self.gridLayout_11.addWidget(self.delta_kbands, 1, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.tab_5)
        self.label_29.setObjectName("label_29")
        self.gridLayout_11.addWidget(self.label_29, 3, 0, 1, 1)
        self.window_kbands = QtWidgets.QLineEdit(self.tab_5)
        self.window_kbands.setObjectName("window_kbands")
        self.gridLayout_11.addWidget(self.window_kbands, 3, 1, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.tab_5)
        self.label_31.setObjectName("label_31")
        self.gridLayout_11.addWidget(self.label_31, 5, 0, 1, 1)
        self.nv_kbands = QtWidgets.QLineEdit(self.tab_5)
        self.nv_kbands.setObjectName("nv_kbands")
        self.gridLayout_11.addWidget(self.nv_kbands, 5, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.tab_5)
        self.label_27.setObjectName("label_27")
        self.gridLayout_11.addWidget(self.label_27, 1, 0, 1, 1)
        self.ne_kbands = QtWidgets.QLineEdit(self.tab_5)
        self.ne_kbands.setObjectName("ne_kbands")
        self.gridLayout_11.addWidget(self.ne_kbands, 2, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.tab_5)
        self.label_28.setObjectName("label_28")
        self.gridLayout_11.addWidget(self.label_28, 2, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.tab_5)
        self.label_30.setObjectName("label_30")
        self.gridLayout_11.addWidget(self.label_30, 4, 0, 1, 1)
        self.scale_kbands = QtWidgets.QLineEdit(self.tab_5)
        self.scale_kbands.setObjectName("scale_kbands")
        self.gridLayout_11.addWidget(self.scale_kbands, 4, 1, 1, 1)
        self.nk_kbands = QtWidgets.QLineEdit(self.tab_5)
        self.nk_kbands.setObjectName("nk_kbands")
        self.gridLayout_11.addWidget(self.nk_kbands, 0, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.tab_5)
        self.label_19.setObjectName("label_19")
        self.gridLayout_11.addWidget(self.label_19, 0, 0, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_11, 0, 0, 1, 1)
        self.show_dosbands = QtWidgets.QPushButton(self.tab_5)
        self.show_dosbands.setObjectName("show_dosbands")
        self.gridLayout_13.addWidget(self.show_dosbands, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.gridLayout_7.addWidget(self.tabWidget, 0, 1, 3, 1)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(self.tab_8)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.cell_size = QtWidgets.QLineEdit(self.tab_8)
        self.cell_size.setObjectName("cell_size")
        self.gridLayout_2.addWidget(self.cell_size, 0, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_27 = QtWidgets.QGridLayout()
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.remove_single_bonded = QtWidgets.QCheckBox(self.tab_9)
        self.remove_single_bonded.setEnabled(True)
        self.remove_single_bonded.setChecked(False)
        self.remove_single_bonded.setObjectName("remove_single_bonded")
        self.gridLayout_27.addWidget(self.remove_single_bonded, 0, 0, 1, 1)
        self.remove_selected = QtWidgets.QCheckBox(self.tab_9)
        self.remove_selected.setObjectName("remove_selected")
        self.gridLayout_27.addWidget(self.remove_selected, 1, 0, 1, 1)
        self.select_atoms_removal = QtWidgets.QPushButton(self.tab_9)
        self.select_atoms_removal.setObjectName("select_atoms_removal")
        self.gridLayout_27.addWidget(self.select_atoms_removal, 2, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_27)
        self.tabWidget_2.addTab(self.tab_9, "")
        self.gridLayout_7.addWidget(self.tabWidget_2, 2, 0, 1, 1)
        self.tabWidget_3 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.tab_12)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.tab_12)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_12)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_12)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_12)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.tinter = QtWidgets.QLineEdit(self.tab_12)
        self.tinter.setObjectName("tinter")
        self.gridLayout.addWidget(self.tinter, 0, 1, 1, 1)
        self.interlayer_bias = QtWidgets.QLineEdit(self.tab_12)
        self.interlayer_bias.setObjectName("interlayer_bias")
        self.gridLayout.addWidget(self.interlayer_bias, 1, 1, 1, 1)
        self.mAB = QtWidgets.QLineEdit(self.tab_12)
        self.mAB.setObjectName("mAB")
        self.gridLayout.addWidget(self.mAB, 2, 1, 1, 1)
        self.fermi = QtWidgets.QLineEdit(self.tab_12)
        self.fermi.setObjectName("fermi")
        self.gridLayout.addWidget(self.fermi, 3, 1, 1, 1)
        self.set_half_filling = QtWidgets.QRadioButton(self.tab_12)
        self.set_half_filling.setObjectName("set_half_filling")
        self.gridLayout.addWidget(self.set_half_filling, 4, 1, 1, 1)
        self.gridLayout_14.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.tabWidget_3.addTab(self.tab_12, "")
        self.gridLayout_7.addWidget(self.tabWidget_3, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 973, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Twisted bilayer graphene"))
        self.nsuper_struct.setText(_translate("MainWindow", "3"))
        self.label_12.setText(_translate("MainWindow", "Supercell"))
        self.show_structure.setText(_translate("MainWindow", "Show structure"))
        self.show_structure_3d.setText(_translate("MainWindow", "Show structure 3D"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Structure"))
        self.label_7.setText(_translate("MainWindow", "nbands"))
        self.label_6.setText(_translate("MainWindow", "nkpoints"))
        self.nbands.setText(_translate("MainWindow", "20"))
        self.nk_bands.setText(_translate("MainWindow", "100"))
        self.label_16.setText(_translate("MainWindow", "Operator"))
        self.bands_operator.setItemText(0, _translate("MainWindow", "None"))
        self.bands_operator.setItemText(1, _translate("MainWindow", "Valley"))
        self.show_bands.setText(_translate("MainWindow", "Bandstructure"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Bands"))
        self.delta_ldos_single.setText(_translate("MainWindow", "0.01"))
        self.label_9.setText(_translate("MainWindow", "Energy"))
        self.nsuper_ldos_single.setText(_translate("MainWindow", "3"))
        self.label_10.setText(_translate("MainWindow", "Supercell"))
        self.energy_ldos_single.setText(_translate("MainWindow", "0.0"))
        self.label_8.setText(_translate("MainWindow", "Smearing"))
        self.label_11.setText(_translate("MainWindow", "# kpoints"))
        self.nk_ldos_single.setText(_translate("MainWindow", "10"))
        self.show_ldos_single.setText(_translate("MainWindow", "Show LDOS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Single LDOS"))
        self.ne_ldos.setText(_translate("MainWindow", "300"))
        self.delta_ldos.setText(_translate("MainWindow", "0.01"))
        self.label_43.setText(_translate("MainWindow", "Smearing"))
        self.nk_ldos.setText(_translate("MainWindow", "16"))
        self.label_44.setText(_translate("MainWindow", "# of energies"))
        self.label_45.setText(_translate("MainWindow", "# of kpoints"))
        self.label_46.setText(_translate("MainWindow", "Energy window"))
        self.window_ldos.setText(_translate("MainWindow", "0.4"))
        self.nsuper_ldos.setText(_translate("MainWindow", "3"))
        self.label_47.setText(_translate("MainWindow", "Supercell"))
        self.show_interactive_ldos.setText(_translate("MainWindow", "Show LDOS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "LDOS"))
        self.delta_dos.setText(_translate("MainWindow", "0.01"))
        self.nume_dos.setText(_translate("MainWindow", "4000"))
        self.numpol_dos.setText(_translate("MainWindow", "1000"))
        self.label_17.setText(_translate("MainWindow", "# kpoints"))
        self.label_14.setText(_translate("MainWindow", "# of energies"))
        self.label_13.setText(_translate("MainWindow", "Smearing"))
        self.label_15.setText(_translate("MainWindow", "# polynomials"))
        self.nk_dos.setText(_translate("MainWindow", "200"))
        self.label_18.setText(_translate("MainWindow", "Energy window"))
        self.ewindow_dos.setText(_translate("MainWindow", "0.5"))
        self.show_dos.setText(_translate("MainWindow", "Show DOS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "DOS"))
        self.show_fermi_surface.setText(_translate("MainWindow", "Fermi surface"))
        self.label_52.setText(_translate("MainWindow", "# of kpoints"))
        self.delta_fs.setText(_translate("MainWindow", "0.1"))
        self.energy_fs.setText(_translate("MainWindow", "0.0"))
        self.label_54.setText(_translate("MainWindow", "Smearing"))
        self.nk_fs.setText(_translate("MainWindow", "100"))
        self.label_40.setText(_translate("MainWindow", "Energy"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Fermi surface"))
        self.delta_kbands.setText(_translate("MainWindow", "0.01"))
        self.label_29.setText(_translate("MainWindow", "Energy window"))
        self.window_kbands.setText(_translate("MainWindow", "0.5"))
        self.label_31.setText(_translate("MainWindow", "# vectors"))
        self.nv_kbands.setToolTip(_translate("MainWindow", "Number of vectors in KPM, increase this number to remove noise"))
        self.nv_kbands.setText(_translate("MainWindow", "2"))
        self.label_27.setText(_translate("MainWindow", "Smearing"))
        self.ne_kbands.setText(_translate("MainWindow", "400"))
        self.label_28.setText(_translate("MainWindow", "# of energies"))
        self.label_30.setText(_translate("MainWindow", "KPM scale"))
        self.scale_kbands.setText(_translate("MainWindow", "4.0"))
        self.nk_kbands.setText(_translate("MainWindow", "100"))
        self.label_19.setText(_translate("MainWindow", "# of kpoints"))
        self.show_dosbands.setToolTip(_translate("MainWindow", "This is equivalent to band structure calculation, but it can be applied for very large systems"))
        self.show_dosbands.setText(_translate("MainWindow", "Show DOS Bands"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "DOS Bands"))
        self.label_5.setText(_translate("MainWindow", "Cell size"))
        self.cell_size.setText(_translate("MainWindow", "7"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("MainWindow", "Geometry"))
        self.remove_single_bonded.setToolTip(_translate("MainWindow", "Remove atoms that have a single bond in the structure"))
        self.remove_single_bonded.setText(_translate("MainWindow", "Remove single bonds"))
        self.remove_selected.setText(_translate("MainWindow", "Remove selected atoms"))
        self.select_atoms_removal.setText(_translate("MainWindow", "Select atoms to remove"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), _translate("MainWindow", "Modify geometry"))
        self.label.setText(_translate("MainWindow", "Interlayer"))
        self.label_2.setText(_translate("MainWindow", "Electric bias"))
        self.label_3.setText(_translate("MainWindow", "AB imbalance"))
        self.label_4.setText(_translate("MainWindow", "Fermi energy"))
        self.tinter.setText(_translate("MainWindow", "0.4"))
        self.interlayer_bias.setText(_translate("MainWindow", "0.0"))
        self.mAB.setText(_translate("MainWindow", "0.0"))
        self.fermi.setText(_translate("MainWindow", "0.0"))
        self.set_half_filling.setText(_translate("MainWindow", "Measure with respect to half filling"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_12), _translate("MainWindow", "Hamiltonian"))

