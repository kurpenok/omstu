# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(640, 480)
        main_window.setMinimumSize(QSize(640, 480))
        main_window.setMaximumSize(QSize(640, 480))
        font = QFont()
        font.setFamily(u"GOST type B")
        font.setPointSize(12)
        main_window.setFont(font)
        self.central_widget = QWidget(main_window)
        self.central_widget.setObjectName(u"central_widget")
        self.horizontalLayoutWidget = QWidget(self.central_widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(9, 9, 621, 441))
        self.horizontal_layout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontal_layout.setObjectName(u"horizontal_layout")
        self.horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.group_box_registration = QGroupBox(self.horizontalLayoutWidget)
        self.group_box_registration.setObjectName(u"group_box_registration")
        self.verticalLayoutWidget_2 = QWidget(self.group_box_registration)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(9, 29, 291, 401))
        self.vertical_layout_registration = QVBoxLayout(self.verticalLayoutWidget_2)
        self.vertical_layout_registration.setObjectName(u"vertical_layout_registration")
        self.vertical_layout_registration.setContentsMargins(0, 0, 0, 0)
        self.label_surname = QLabel(self.verticalLayoutWidget_2)
        self.label_surname.setObjectName(u"label_surname")

        self.vertical_layout_registration.addWidget(self.label_surname)

        self.line_edit_surname = QLineEdit(self.verticalLayoutWidget_2)
        self.line_edit_surname.setObjectName(u"line_edit_surname")

        self.vertical_layout_registration.addWidget(self.line_edit_surname)

        self.label_name = QLabel(self.verticalLayoutWidget_2)
        self.label_name.setObjectName(u"label_name")

        self.vertical_layout_registration.addWidget(self.label_name)

        self.line_edit_name = QLineEdit(self.verticalLayoutWidget_2)
        self.line_edit_name.setObjectName(u"line_edit_name")

        self.vertical_layout_registration.addWidget(self.line_edit_name)

        self.label_patronymic = QLabel(self.verticalLayoutWidget_2)
        self.label_patronymic.setObjectName(u"label_patronymic")

        self.vertical_layout_registration.addWidget(self.label_patronymic)

        self.line_edit_patronymic = QLineEdit(self.verticalLayoutWidget_2)
        self.line_edit_patronymic.setObjectName(u"line_edit_patronymic")

        self.vertical_layout_registration.addWidget(self.line_edit_patronymic)

        self.vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vertical_layout_registration.addItem(self.vertical_spacer)

        self.label_save_status = QLabel(self.verticalLayoutWidget_2)
        self.label_save_status.setObjectName(u"label_save_status")

        self.vertical_layout_registration.addWidget(self.label_save_status)

        self.push_button_save_user_info = QPushButton(self.verticalLayoutWidget_2)
        self.push_button_save_user_info.setObjectName(u"push_button_save_user_info")

        self.vertical_layout_registration.addWidget(self.push_button_save_user_info)


        self.horizontal_layout.addWidget(self.group_box_registration)

        self.group_box_questions = QGroupBox(self.horizontalLayoutWidget)
        self.group_box_questions.setObjectName(u"group_box_questions")
        self.verticalLayoutWidget = QWidget(self.group_box_questions)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 29, 291, 401))
        self.vertical_layout_questions = QVBoxLayout(self.verticalLayoutWidget)
        self.vertical_layout_questions.setObjectName(u"vertical_layout_questions")
        self.vertical_layout_questions.setContentsMargins(0, 0, 0, 0)
        self.text_edit_question = QTextEdit(self.verticalLayoutWidget)
        self.text_edit_question.setObjectName(u"text_edit_question")

        self.vertical_layout_questions.addWidget(self.text_edit_question)

        self.horizontal_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.vertical_layout_questions.addItem(self.horizontal_spacer)

        self.push_button_yes = QPushButton(self.verticalLayoutWidget)
        self.push_button_yes.setObjectName(u"push_button_yes")

        self.vertical_layout_questions.addWidget(self.push_button_yes)

        self.push_button_rather_yes = QPushButton(self.verticalLayoutWidget)
        self.push_button_rather_yes.setObjectName(u"push_button_rather_yes")

        self.vertical_layout_questions.addWidget(self.push_button_rather_yes)

        self.push_button_ignorance = QPushButton(self.verticalLayoutWidget)
        self.push_button_ignorance.setObjectName(u"push_button_ignorance")

        self.vertical_layout_questions.addWidget(self.push_button_ignorance)

        self.push_button_rather_no = QPushButton(self.verticalLayoutWidget)
        self.push_button_rather_no.setObjectName(u"push_button_rather_no")

        self.vertical_layout_questions.addWidget(self.push_button_rather_no)

        self.push_button_no = QPushButton(self.verticalLayoutWidget)
        self.push_button_no.setObjectName(u"push_button_no")

        self.vertical_layout_questions.addWidget(self.push_button_no)


        self.horizontal_layout.addWidget(self.group_box_questions)

        main_window.setCentralWidget(self.central_widget)
        self.status_bar = QStatusBar(main_window)
        self.status_bar.setObjectName(u"status_bar")
        main_window.setStatusBar(self.status_bar)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

