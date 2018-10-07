# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acq4/modules/MultiPatch/multipatchTemplate.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MultiPatch(object):
    def setupUi(self, MultiPatch):
        MultiPatch.setObjectName("MultiPatch")
        MultiPatch.resize(496, 283)
        self.gridLayout = QtWidgets.QGridLayout(MultiPatch)
        self.gridLayout.setObjectName("gridLayout")
        self.recordBtn = QtWidgets.QPushButton(MultiPatch)
        self.recordBtn.setCheckable(True)
        self.recordBtn.setObjectName("recordBtn")
        self.gridLayout.addWidget(self.recordBtn, 7, 0, 1, 1)
        self.coarseSearchBtn = QtWidgets.QPushButton(MultiPatch)
        self.coarseSearchBtn.setObjectName("coarseSearchBtn")
        self.gridLayout.addWidget(self.coarseSearchBtn, 1, 0, 1, 1)
        self.idleBtn = QtWidgets.QPushButton(MultiPatch)
        self.idleBtn.setObjectName("idleBtn")
        self.gridLayout.addWidget(self.idleBtn, 2, 0, 1, 1)
        self.fineSearchBtn = QtWidgets.QPushButton(MultiPatch)
        self.fineSearchBtn.setObjectName("fineSearchBtn")
        self.gridLayout.addWidget(self.fineSearchBtn, 1, 1, 1, 1)
        self.approachBtn = QtWidgets.QPushButton(MultiPatch)
        self.approachBtn.setObjectName("approachBtn")
        self.gridLayout.addWidget(self.approachBtn, 2, 2, 1, 1)
        self.sealBtn = QtWidgets.QPushButton(MultiPatch)
        self.sealBtn.setObjectName("sealBtn")
        self.gridLayout.addWidget(self.sealBtn, 4, 0, 1, 1)
        self.homeBtn = QtWidgets.QPushButton(MultiPatch)
        self.homeBtn.setObjectName("homeBtn")
        self.gridLayout.addWidget(self.homeBtn, 0, 0, 1, 1)
        self.setTargetBtn = QtWidgets.QPushButton(MultiPatch)
        self.setTargetBtn.setCheckable(True)
        self.setTargetBtn.setObjectName("setTargetBtn")
        self.gridLayout.addWidget(self.setTargetBtn, 0, 1, 1, 1)
        self.calibrateBtn = QtWidgets.QPushButton(MultiPatch)
        self.calibrateBtn.setCheckable(True)
        self.calibrateBtn.setObjectName("calibrateBtn")
        self.gridLayout.addWidget(self.calibrateBtn, 1, 2, 1, 1)
        self.aboveTargetBtn = QtWidgets.QPushButton(MultiPatch)
        self.aboveTargetBtn.setObjectName("aboveTargetBtn")
        self.gridLayout.addWidget(self.aboveTargetBtn, 2, 1, 1, 1)
        self.autoCalibrateBtn = QtWidgets.QPushButton(MultiPatch)
        self.autoCalibrateBtn.setObjectName("autoCalibrateBtn")
        self.gridLayout.addWidget(self.autoCalibrateBtn, 0, 2, 1, 1)
        self.hideMarkersBtn = QtWidgets.QPushButton(MultiPatch)
        self.hideMarkersBtn.setCheckable(True)
        self.hideMarkersBtn.setObjectName("hideMarkersBtn")
        self.gridLayout.addWidget(self.hideMarkersBtn, 4, 1, 1, 1)
        self.fastBtn = QtWidgets.QPushButton(MultiPatch)
        self.fastBtn.setCheckable(True)
        self.fastBtn.setObjectName("fastBtn")
        self.gridLayout.addWidget(self.fastBtn, 3, 2, 1, 1)
        self.slowBtn = QtWidgets.QPushButton(MultiPatch)
        self.slowBtn.setCheckable(True)
        self.slowBtn.setObjectName("slowBtn")
        self.gridLayout.addWidget(self.slowBtn, 3, 0, 1, 1)
        self.breakInBtn = QtWidgets.QPushButton(MultiPatch)
        self.breakInBtn.setObjectName("breakInBtn")
        self.gridLayout.addWidget(self.breakInBtn, 4, 2, 1, 1)
        self.stepInBtn = QtWidgets.QPushButton(MultiPatch)
        self.stepInBtn.setObjectName("stepInBtn")
        self.gridLayout.addWidget(self.stepInBtn, 5, 0, 1, 1)
        self.stepOutBtn = QtWidgets.QPushButton(MultiPatch)
        self.stepOutBtn.setObjectName("stepOutBtn")
        self.gridLayout.addWidget(self.stepOutBtn, 5, 1, 1, 1)
        self.moveInBtn = QtWidgets.QPushButton(MultiPatch)
        self.moveInBtn.setObjectName("moveInBtn")
        self.gridLayout.addWidget(self.moveInBtn, 5, 2, 1, 1)
        self.label = QtWidgets.QLabel(MultiPatch)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 6, 0, 1, 1)
        self.stepSizeSpin = SpinBox(MultiPatch)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stepSizeSpin.sizePolicy().hasHeightForWidth())
        self.stepSizeSpin.setSizePolicy(sizePolicy)
        self.stepSizeSpin.setObjectName("stepSizeSpin")
        self.gridLayout.addWidget(self.stepSizeSpin, 6, 1, 1, 1)
        self.toTargetBtn = QtWidgets.QPushButton(MultiPatch)
        self.toTargetBtn.setObjectName("toTargetBtn")
        self.gridLayout.addWidget(self.toTargetBtn, 6, 2, 1, 1)
        self.resetBtn = QtWidgets.QPushButton(MultiPatch)
        self.resetBtn.setObjectName("resetBtn")
        self.gridLayout.addWidget(self.resetBtn, 7, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 8, 1, 1, 1)
        self.matrixWidget = QtWidgets.QWidget(MultiPatch)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.matrixWidget.sizePolicy().hasHeightForWidth())
        self.matrixWidget.setSizePolicy(sizePolicy)
        self.matrixWidget.setObjectName("matrixWidget")
        self.matrixLayout = QtWidgets.QGridLayout(self.matrixWidget)
        self.matrixLayout.setContentsMargins(0, 0, 0, 0)
        self.matrixLayout.setSpacing(0)
        self.matrixLayout.setObjectName("matrixLayout")
        self.gridLayout.addWidget(self.matrixWidget, 0, 3, 9, 1)
        self.reSealBtn = QtWidgets.QPushButton(MultiPatch)
        self.reSealBtn.setObjectName("reSealBtn")
        self.gridLayout.addWidget(self.reSealBtn, 7, 1, 1, 1)

        self.retranslateUi(MultiPatch)
        Qt.QMetaObject.connectSlotsByName(MultiPatch)

    def retranslateUi(self, MultiPatch):
        _translate = Qt.QCoreApplication.translate
        MultiPatch.setWindowTitle(_translate("MultiPatch", "Form"))
        self.recordBtn.setText(_translate("MultiPatch", "Record"))
        self.coarseSearchBtn.setText(_translate("MultiPatch", "Coarse Search"))
        self.idleBtn.setText(_translate("MultiPatch", "Idle"))
        self.fineSearchBtn.setText(_translate("MultiPatch", "Fine Search"))
        self.approachBtn.setText(_translate("MultiPatch", "Approach"))
        self.sealBtn.setText(_translate("MultiPatch", "Seal"))
        self.homeBtn.setText(_translate("MultiPatch", "Home"))
        self.setTargetBtn.setText(_translate("MultiPatch", "Set target"))
        self.calibrateBtn.setText(_translate("MultiPatch", "Calibrate"))
        self.aboveTargetBtn.setText(_translate("MultiPatch", "Above target"))
        self.autoCalibrateBtn.setText(_translate("MultiPatch", "Auto cal."))
        self.hideMarkersBtn.setText(_translate("MultiPatch", "Hide Markers"))
        self.fastBtn.setText(_translate("MultiPatch", "Fast"))
        self.slowBtn.setText(_translate("MultiPatch", "Slow"))
        self.breakInBtn.setText(_translate("MultiPatch", "Break In"))
        self.stepInBtn.setText(_translate("MultiPatch", "Step in"))
        self.stepOutBtn.setText(_translate("MultiPatch", "Step out"))
        self.moveInBtn.setText(_translate("MultiPatch", "Move in"))
        self.label.setText(_translate("MultiPatch", "Step size"))
        self.toTargetBtn.setText(_translate("MultiPatch", "To target"))
        self.resetBtn.setText(_translate("MultiPatch", "Reset History"))
        self.reSealBtn.setText(_translate("MultiPatch", "ReSeal"))

from acq4.pyqtgraph import SpinBox
