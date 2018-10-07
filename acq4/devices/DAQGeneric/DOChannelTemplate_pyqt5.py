# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acq4/devices/DAQGeneric/DOChannelTemplate.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = GroupBox(Form)
        font = Qt.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.preSetCheck = QtWidgets.QCheckBox(self.groupBox)
        font = Qt.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.preSetCheck.setFont(font)
        self.preSetCheck.setObjectName("preSetCheck")
        self.gridLayout.addWidget(self.preSetCheck, 0, 0, 1, 1)
        self.holdingCheck = QtWidgets.QCheckBox(self.groupBox)
        font = Qt.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.holdingCheck.setFont(font)
        self.holdingCheck.setObjectName("holdingCheck")
        self.gridLayout.addWidget(self.holdingCheck, 1, 0, 1, 1)
        self.preSetSpin = QtWidgets.QSpinBox(self.groupBox)
        font = Qt.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.preSetSpin.setFont(font)
        self.preSetSpin.setMaximum(1)
        self.preSetSpin.setObjectName("preSetSpin")
        self.gridLayout.addWidget(self.preSetSpin, 0, 1, 1, 1)
        self.holdingSpin = QtWidgets.QSpinBox(self.groupBox)
        font = Qt.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.holdingSpin.setFont(font)
        self.holdingSpin.setMaximum(1)
        self.holdingSpin.setObjectName("holdingSpin")
        self.gridLayout.addWidget(self.holdingSpin, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.functionCheck = QtWidgets.QCheckBox(self.frame)
        font = Qt.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.functionCheck.setFont(font)
        self.functionCheck.setObjectName("functionCheck")
        self.horizontalLayout.addWidget(self.functionCheck)
        self.displayCheck = QtWidgets.QCheckBox(self.frame)
        font = Qt.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.displayCheck.setFont(font)
        self.displayCheck.setChecked(True)
        self.displayCheck.setObjectName("displayCheck")
        self.horizontalLayout.addWidget(self.displayCheck)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.waveGeneratorWidget = StimGenerator(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.waveGeneratorWidget.sizePolicy().hasHeightForWidth())
        self.waveGeneratorWidget.setSizePolicy(sizePolicy)
        font = Qt.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.waveGeneratorWidget.setFont(font)
        self.waveGeneratorWidget.setObjectName("waveGeneratorWidget")
        self.verticalLayout.addWidget(self.waveGeneratorWidget)
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout_3.addWidget(self.groupBox)

        self.retranslateUi(Form)
        Qt.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = Qt.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "GroupBox"))
        self.preSetCheck.setText(_translate("Form", "Pre-set"))
        self.holdingCheck.setText(_translate("Form", "Holding"))
        self.functionCheck.setText(_translate("Form", "Enable Function"))
        self.displayCheck.setText(_translate("Form", "Display"))

from acq4.pyqtgraph import GroupBox
from acq4.util.generator.StimGenerator import StimGenerator
