# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acq4\devices\PrairiePhotostimulator\moduleTemplate.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(447, 437)
        self.gridLayout_2 = QtGui.QGridLayout(Form)
        self.gridLayout_2.setMargin(3)
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.markPointsBtn = FeedbackButton(Form)
        self.markPointsBtn.setCheckable(True)
        self.markPointsBtn.setObjectName(_fromUtf8("markPointsBtn"))
        self.gridLayout_2.addWidget(self.markPointsBtn, 0, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.iterationsSpin = QtGui.QSpinBox(Form)
        self.iterationsSpin.setObjectName(_fromUtf8("iterationsSpin"))
        self.gridLayout.addWidget(self.iterationsSpin, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.iterDelaySpin = QtGui.QSpinBox(Form)
        self.iterDelaySpin.setObjectName(_fromUtf8("iterDelaySpin"))
        self.gridLayout.addWidget(self.iterDelaySpin, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.pointsParamTree = ParameterTree(Form)
        self.pointsParamTree.setObjectName(_fromUtf8("pointsParamTree"))
        self.gridLayout_2.addWidget(self.pointsParamTree, 1, 1, 2, 1)
        self.stimulusParamTree = ParameterTree(Form)
        self.stimulusParamTree.setObjectName(_fromUtf8("stimulusParamTree"))
        self.gridLayout_2.addWidget(self.stimulusParamTree, 2, 0, 1, 1)
        self.gridLayout_2.setRowStretch(2, 5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.markPointsBtn.setText(_translate("Form", "Mark Points", None))
        self.label.setText(_translate("Form", "Iterations:", None))
        self.label_2.setText(_translate("Form", "IterationDelay:", None))

from acq4.pyqtgraph import FeedbackButton
from acq4.pyqtgraph.parametertree import ParameterTree
