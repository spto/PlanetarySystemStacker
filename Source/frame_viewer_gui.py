# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frame_viewer_gui.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frame_viewer(object):
    def setupUi(self, frame_viewer):
        frame_viewer.setObjectName("frame_viewer")
        frame_viewer.resize(900, 630)
        frame_viewer.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.grid_layout = QtWidgets.QGridLayout(frame_viewer)
        self.grid_layout.setObjectName("grid_layout")
        self.groupBox_frame_sorting = QtWidgets.QGroupBox(frame_viewer)
        self.groupBox_frame_sorting.setObjectName("groupBox_frame_sorting")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_frame_sorting)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButton_quality = QtWidgets.QRadioButton(self.groupBox_frame_sorting)
        self.radioButton_quality.setObjectName("radioButton_quality")
        self.gridLayout_2.addWidget(self.radioButton_quality, 1, 0, 1, 1)
        self.radioButton_chronological = QtWidgets.QRadioButton(self.groupBox_frame_sorting)
        self.radioButton_chronological.setObjectName("radioButton_chronological")
        self.gridLayout_2.addWidget(self.radioButton_chronological, 0, 0, 1, 1)
        self.spinBox_chronological = QtWidgets.QSpinBox(self.groupBox_frame_sorting)
        self.spinBox_chronological.setObjectName("spinBox_chronological")
        self.gridLayout_2.addWidget(self.spinBox_chronological, 0, 1, 1, 1)
        self.spinBox_quality = QtWidgets.QSpinBox(self.groupBox_frame_sorting)
        self.spinBox_quality.setObjectName("spinBox_quality")
        self.gridLayout_2.addWidget(self.spinBox_quality, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.groupBox_frame_sorting, 3, 3, 1, 1)
        self.groupBox_stacking_fraction = QtWidgets.QGroupBox(frame_viewer)
        self.groupBox_stacking_fraction.setObjectName("groupBox_stacking_fraction")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_stacking_fraction)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_number_frames = QtWidgets.QLabel(self.groupBox_stacking_fraction)
        self.label_number_frames.setObjectName("label_number_frames")
        self.gridLayout_3.addWidget(self.label_number_frames, 0, 0, 1, 1)
        self.spinBox_number_frames = QtWidgets.QSpinBox(self.groupBox_stacking_fraction)
        self.spinBox_number_frames.setMinimum(1)
        self.spinBox_number_frames.setObjectName("spinBox_number_frames")
        self.gridLayout_3.addWidget(self.spinBox_number_frames, 0, 1, 1, 1)
        self.label_percentage_frames = QtWidgets.QLabel(self.groupBox_stacking_fraction)
        self.label_percentage_frames.setObjectName("label_percentage_frames")
        self.gridLayout_3.addWidget(self.label_percentage_frames, 1, 0, 1, 1)
        self.spinBox_percentage_frames = QtWidgets.QSpinBox(self.groupBox_stacking_fraction)
        self.spinBox_percentage_frames.setMinimum(1)
        self.spinBox_percentage_frames.setMaximum(100)
        self.spinBox_percentage_frames.setObjectName("spinBox_percentage_frames")
        self.gridLayout_3.addWidget(self.spinBox_percentage_frames, 1, 1, 1, 1)
        self.pushButton_set_stacking_limit = QtWidgets.QPushButton(self.groupBox_stacking_fraction)
        self.pushButton_set_stacking_limit.setMinimumSize(QtCore.QSize(250, 0))
        self.pushButton_set_stacking_limit.setObjectName("pushButton_set_stacking_limit")
        self.gridLayout_3.addWidget(self.pushButton_set_stacking_limit, 2, 0, 1, 2)
        self.grid_layout.addWidget(self.groupBox_stacking_fraction, 2, 3, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(frame_viewer)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.grid_layout.addWidget(self.buttonBox, 4, 3, 1, 1)
        self.slider_frames = QtWidgets.QSlider(frame_viewer)
        self.slider_frames.setMaximum(1000)
        self.slider_frames.setPageStep(20)
        self.slider_frames.setOrientation(QtCore.Qt.Horizontal)
        self.slider_frames.setObjectName("slider_frames")
        self.grid_layout.addWidget(self.slider_frames, 4, 0, 1, 1)
        self.pushButton_play = QtWidgets.QPushButton(frame_viewer)
        self.pushButton_play.setObjectName("pushButton_play")
        self.grid_layout.addWidget(self.pushButton_play, 4, 2, 1, 1)
        self.pushButton_stop = QtWidgets.QPushButton(frame_viewer)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.grid_layout.addWidget(self.pushButton_stop, 4, 1, 1, 1)
        self.label_matplotlib = QtWidgets.QLabel(frame_viewer)
        self.label_matplotlib.setObjectName("label_matplotlib")
        self.grid_layout.addWidget(self.label_matplotlib, 0, 3, 2, 1)
        self.grid_layout.setColumnStretch(0, 5)

        self.retranslateUi(frame_viewer)
        QtCore.QMetaObject.connectSlotsByName(frame_viewer)

    def retranslateUi(self, frame_viewer):
        _translate = QtCore.QCoreApplication.translate
        frame_viewer.setWindowTitle(_translate("frame_viewer", "Form"))
        self.groupBox_frame_sorting.setTitle(_translate("frame_viewer", "Frame sorting"))
        self.radioButton_quality.setToolTip(_translate("frame_viewer", "Frames are ordered by their overall sharpness."))
        self.radioButton_quality.setText(_translate("frame_viewer", "By quality"))
        self.radioButton_chronological.setToolTip(_translate("frame_viewer", "Frames are ordered chronologically."))
        self.radioButton_chronological.setText(_translate("frame_viewer", "Chronological"))
        self.spinBox_chronological.setToolTip(_translate("frame_viewer", "Enter a value or use the spin box arrows to select a (chronological) frame index."))
        self.spinBox_quality.setToolTip(_translate("frame_viewer", "Enter a value or use the spin box arrows to select a (quality) frame index."))
        self.groupBox_stacking_fraction.setTitle(_translate("frame_viewer", "Fraction of frames to be stacked"))
        self.label_number_frames.setText(_translate("frame_viewer", "Number of frames"))
        self.spinBox_number_frames.setToolTip(_translate("frame_viewer", "Enter a value or use the spin box arrows to set the number of frames to be stacked."))
        self.label_percentage_frames.setText(_translate("frame_viewer", "Percentage"))
        self.spinBox_percentage_frames.setToolTip(_translate("frame_viewer", "Enter a value or use the spin box arrows to set the percentage of frames to be stacked."))
        self.pushButton_set_stacking_limit.setToolTip(_translate("frame_viewer", "Adjust the number of best frames to be stacked at each alignment point such that the current frame is the worst one to be included."))
        self.pushButton_set_stacking_limit.setText(_translate("frame_viewer", "Set limit to current frame"))
        self.buttonBox.setToolTip(_translate("frame_viewer", "Exit the viewer. Press \'OK\' to save the stack size, or \'cancel\' to discard changes."))
        self.slider_frames.setToolTip(_translate("frame_viewer", "Use the slider to select the frame to be displayed. As an alternative,\n"
"you can select the frame with the \'frame sorting\' spinboxes."))
        self.pushButton_play.setToolTip(_translate("frame_viewer", "Start a frame display video. Frames are ordered as selected in the \'frame sorting\' section."))
        self.pushButton_play.setText(_translate("frame_viewer", "Play"))
        self.pushButton_stop.setToolTip(_translate("frame_viewer", "Stop the frame display video."))
        self.pushButton_stop.setText(_translate("frame_viewer", "Stop"))
        self.label_matplotlib.setText(_translate("frame_viewer", "Matplotlib placeholder"))

