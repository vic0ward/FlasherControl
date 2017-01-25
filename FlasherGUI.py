# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FlasherGUI_v1.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!


import socket
import flasher
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def __init__(self, MainWindow):

        self.this_flasher = flasher.Flasher()
        self.pulse_status = 0

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(695, 731)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Ethernet setup
        self.ethernet = QtWidgets.QGroupBox(self.centralwidget)
        self.ethernet.setEnabled(True)
        self.ethernet.setGeometry(QtCore.QRect(20, 10, 311, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ethernet.setFont(font)
        self.ethernet.setObjectName("ethernet")

        self.host = QtWidgets.QLineEdit(self.ethernet)
        self.host.setGeometry(QtCore.QRect(170, 60, 121, 21))
        self.host.setObjectName("host")
        self.label_host = QtWidgets.QLabel(self.centralwidget)
        self.label_host.setGeometry(QtCore.QRect(190, 50, 91, 16))
        self.label_host.setObjectName("label_host")

        self.ip_address = QtWidgets.QLineEdit(self.ethernet)
        self.ip_address.setGeometry(QtCore.QRect(20, 60, 131, 21))
        self.ip_address.setObjectName("ip_address")
        self.ip_address.setInputMask('000.000.000.000;_')
        self.label_ip_address = QtWidgets.QLabel(self.centralwidget)
        self.label_ip_address.setGeometry(QtCore.QRect(40, 50, 71, 16))
        self.label_ip_address.setObjectName("label_ip_address")

        # Communication handling
        self.serial_link = QtWidgets.QGroupBox(self.centralwidget)
        self.serial_link.setEnabled(True)
        self.serial_link.setGeometry(QtCore.QRect(390, 10, 281, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.serial_link.setFont(font)
        self.serial_link.setObjectName("serial_link")

        self.start_com = QtWidgets.QPushButton(self.serial_link)
        self.start_com.setGeometry(QtCore.QRect(10, 25, 80, 40))
        self.start_com.setObjectName("start_com")
        # self.start_com.clicked.connect(self.start_com_clicked)

        self.stop_com = QtWidgets.QPushButton(self.serial_link)
        self.stop_com.setGeometry(QtCore.QRect(90, 25, 80, 40))
        self.stop_com.setObjectName("stop_com")
        # self.stop_com.clicked.connect(self.stop_com_clicked)

        self.label_com_started = QtWidgets.QLabel(self.serial_link)
        self.label_com_started.setGeometry(QtCore.QRect(20, 70, 141, 20))
        self.label_com_started.setText("")
        self.label_com_started.setPixmap(QtGui.QPixmap("BlackLed.png"))
        self.label_com_started.setObjectName("label_com_started")

        self.led_tx = QtWidgets.QLabel(self.serial_link)
        self.led_tx.setGeometry(QtCore.QRect(230, 40, 21, 16))
        self.led_tx.setText("")
        self.led_tx.setPixmap(QtGui.QPixmap("BlackLed.png"))
        self.led_tx.setObjectName("led_tx")

        self.led_rx = QtWidgets.QLabel(self.serial_link)
        self.led_rx.setGeometry(QtCore.QRect(230, 60, 21, 16))
        self.led_rx.setText("")
        self.led_rx.setPixmap(QtGui.QPixmap("BlackLed.png"))
        self.led_rx.setObjectName("led_rx")

        self.label_serial_link_tx = QtWidgets.QLabel(self.serial_link)
        self.label_serial_link_tx.setGeometry(QtCore.QRect(200, 40, 25, 20))
        self.label_serial_link_tx.setObjectName("label_serial_link_tx")
        self.label_serial_link_rx = QtWidgets.QLabel(self.serial_link)
        self.label_serial_link_rx.setGeometry(QtCore.QRect(200, 60, 25, 20))
        self.label_serial_link_rx.setObjectName("label_serial_link_rx")

        # Turning LEDs ON and OFF
        self.led_status = QtWidgets.QGroupBox(self.centralwidget)
        self.led_status.setEnabled(True)
        self.led_status.setGeometry(QtCore.QRect(20, 120, 211, 541))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.led_status.setFont(font)
        self.led_status.setObjectName("led_status")
        self.frame_set_status = QtWidgets.QFrame(self.led_status)
        self.frame_set_status.setGeometry(QtCore.QRect(10, 60, 191, 201))
        self.frame_set_status.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_set_status.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_set_status.setObjectName("frame_set_status")

        x_start = 10
        x_step = 35
        y_start = 170
        y_step = -40

        led_geo = ((0, 0), (2, 0), (4, 0),
                   (1, 1), (3, 1),
                   (0, 2), (2, 2), (4, 2),
                   (1, 3), (3, 3),
                   (0, 4), (2, 4), (4, 4))

        self.led_set_status = []

        for led_id in range(13):
            self.led_set_status.append(QtWidgets.QCheckBox(self.frame_set_status))
            self.led_set_status[led_id].setGeometry(
                QtCore.QRect(x_start + x_step * led_geo[led_id][0],
                             y_start + y_step * led_geo[led_id][1], 41, 20))
            obj_name = "led_set_status_"
            obj_name += str(led_id)
            self.led_set_status[led_id].setObjectName(obj_name)
            # self.led_set_status[led_id].stateChanged.connect(self.send_new_config)

        self.label_set_status = QtWidgets.QLabel(self.led_status)
        self.label_set_status.setGeometry(QtCore.QRect(10, 40, 91, 16))
        self.label_set_status.setObjectName("label_set_status")
        self.led_set_status_all = QtWidgets.QCheckBox(self.led_status)
        self.led_set_status_all.setGeometry(QtCore.QRect(160, 40, 41, 18))
        self.led_set_status_all.setObjectName("led_set_status_all")
        # self.led_set_status_all.stateChanged.connect(self.send_new_config)

        self.frame_get_status = QtWidgets.QFrame(self.led_status)
        self.frame_get_status.setGeometry(QtCore.QRect(10, 320, 191, 201))
        self.frame_get_status.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_get_status.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_get_status.setObjectName("frame_get_status")

        self.led_get_status = []
        self.label_led_get_status = []

        for led_id in range(13):
            self.led_get_status.append(QtWidgets.QLabel(self.frame_get_status))
            self.led_get_status[led_id].setGeometry(
                QtCore.QRect(x_start + x_step * led_geo[led_id][0],
                             y_start + y_step * led_geo[led_id][1], 15, 16))
            self.led_get_status[led_id].setText("")
            self.led_get_status[led_id].setPixmap(QtGui.QPixmap("BlackLed.png"))
            obj_name = "led_get_status_"
            obj_name += str(led_id+1)
            self.led_get_status[led_id].setObjectName(obj_name)

            self.label_led_get_status.append(QtWidgets.QLabel(self.frame_get_status))
            self.label_led_get_status[- 1].setGeometry(
                QtCore.QRect(x_start + 20 + x_step * led_geo[led_id - 1][0],
                             y_start + y_step * led_geo[led_id - 1][1], 21, 16))
            self.label_led_get_status[- 1].setText(str(led_id))
            obj_name = "label_led_get_status_"
            obj_name += str(led_id)
            self.label_led_get_status[- 1].setObjectName(obj_name)

        self.label_get_status = QtWidgets.QLabel(self.led_status)
        self.label_get_status.setGeometry(QtCore.QRect(10, 300, 91, 16))
        self.label_get_status.setObjectName("label_get_status")

        self.label_led_all = QtWidgets.QLabel(self.led_status)
        self.label_led_all.setGeometry(QtCore.QRect(180, 300, 21, 16))
        self.label_led_all.setObjectName("label_led_all")

        """
        Frame including all functions to set the pulse properties
        - LED voltage
        - Pulse frequency
        - Pulse width
        - Pulse duration
        - Pulse frequency divider
        """

        # Flasher control
        self.flasher_control = QtWidgets.QGroupBox(self.centralwidget)
        self.flasher_control.setGeometry(QtCore.QRect(250, 120, 421, 461))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.flasher_control.setFont(font)
        self.flasher_control.setObjectName("flasher_control")

        self.status_request = QtWidgets.QPushButton(self.flasher_control)
        self.status_request.setGeometry(QtCore.QRect(260, 50, 141, 41))
        self.status_request.setObjectName("status_request")

        self.send_configuration = QtWidgets.QPushButton(self.flasher_control)
        self.send_configuration.setGeometry(QtCore.QRect(260, 120, 141, 41))
        self.send_configuration.setObjectName("send_configuration")

        self.reset = QtWidgets.QPushButton(self.flasher_control)
        self.reset.setGeometry(QtCore.QRect(260, 190, 141, 41))
        self.reset.setObjectName("reset")

        self.label_temperature = QtWidgets.QLabel(self.flasher_control)
        self.label_temperature.setGeometry(QtCore.QRect(150, 435, 151, 20))
        self.label_temperature.setObjectName("label_temperature")

        # Pulse frequency
        self.frame_pulse_frequency = QtWidgets.QFrame(self.flasher_control)
        self.frame_pulse_frequency.setGeometry(QtCore.QRect(20, 280, 221, 51))
        self.frame_pulse_frequency.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pulse_frequency.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pulse_frequency.setObjectName("frame_pulse_frequency")
        self.pulse_frequency = QtWidgets.QSpinBox(self.frame_pulse_frequency)
        self.pulse_frequency.setGeometry(QtCore.QRect(10, 15, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pulse_frequency.setFont(font)
        self.pulse_frequency.setObjectName("pulse_frequency")
        # self.pulse_frequency.valueChanged.connect(self.send_new_config)
        self.label_res_pulse_frequency = QtWidgets.QLabel(self.frame_pulse_frequency)
        self.label_res_pulse_frequency.setGeometry(QtCore.QRect(160, 20, 51, 16))
        self.label_res_pulse_frequency.setObjectName("label_res_pulse_frequency")

        # Pulse frequency divider
        self.frequency_divider = QtWidgets.QSpinBox(self.frame_pulse_frequency)
        self.frequency_divider.setGeometry(QtCore.QRect(110, 15, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frequency_divider.setFont(font)
        self.frequency_divider.setObjectName("frequency_divider")
        # self.frequency_divider.valueChanged.connect(self.send_new_config)
        self.label_pulse_frequency_div = QtWidgets.QLabel(self.frame_pulse_frequency)
        self.label_pulse_frequency_div.setGeometry(QtCore.QRect(100, 20, 16, 16))
        self.label_pulse_frequency_div.setObjectName("label_pulse_frequency_div")

        # Pulse width
        self.frame_pulse_width = QtWidgets.QFrame(self.flasher_control)
        self.frame_pulse_width.setGeometry(QtCore.QRect(20, 370, 221, 51))
        self.frame_pulse_width.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pulse_width.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pulse_width.setObjectName("frame_pulse_width")

        self.pulse_width = QtWidgets.QSpinBox(self.frame_pulse_width)
        self.pulse_width.setGeometry(QtCore.QRect(10, 15, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pulse_width.setFont(font)
        self.pulse_width.setObjectName("pulse_width")
        # self.pulse_width.valueChanged.connect(self.send_new_config)
        self.label_res_pulse_width = QtWidgets.QLabel(self.frame_pulse_width)
        self.label_res_pulse_width.setGeometry(QtCore.QRect(80, 20, 131, 16))
        self.label_res_pulse_width.setObjectName("label_res_pulse_width")

        # Pulse output
        self.frame_light_pulse = QtWidgets.QFrame(self.flasher_control)
        self.frame_light_pulse.setGeometry(QtCore.QRect(260, 280, 151, 141))
        self.frame_light_pulse.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_light_pulse.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_light_pulse.setObjectName("frame_light_pulse")

        self.start_pulse = QtWidgets.QPushButton(self.frame_light_pulse)
        self.start_pulse.setGeometry(QtCore.QRect(10, 70, 61, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.start_pulse.setFont(font)
        self.start_pulse.setObjectName("start_pulse")
        # self.start_pulse.clicked.connect(self.start_pulse_clicked)

        self.stop_pulse = QtWidgets.QPushButton(self.frame_light_pulse)
        self.stop_pulse.setGeometry(QtCore.QRect(80, 70, 61, 41))
        self.stop_pulse.setObjectName("stop_pulse")
        # self.stop_pulse.clicked.connect(self.stop_pulse_clicked)

        self.label_pulse_started = QtWidgets.QLabel(self.frame_light_pulse)
        self.label_pulse_started.setGeometry(QtCore.QRect(60, 110, 41, 20))
        self.label_pulse_started.setText("")
        self.label_pulse_started.setPixmap(QtGui.QPixmap("BlackLed.png"))
        self.label_pulse_started.setObjectName("label_pulse_started")

        self.flash_duration = QtWidgets.QSpinBox(self.frame_light_pulse)
        self.flash_duration.setGeometry(QtCore.QRect(10, 30, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.flash_duration.setFont(font)
        self.flash_duration.setObjectName("flash_duration")
        # self.flash_duration.valueChanged.connect(self.send_new_config)

        self.label_flash_duration = QtWidgets.QLabel(self.frame_light_pulse)
        self.label_flash_duration.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.label_flash_duration.setObjectName("label_flash_duration")
        self.label_flash_duration = QtWidgets.QLabel(self.frame_light_pulse)
        self.label_flash_duration.setGeometry(QtCore.QRect(100, 30, 41, 16))
        self.label_flash_duration.setObjectName("label_flash_duration")

        self.label_pulse_frequency = QtWidgets.QLabel(self.flasher_control)
        self.label_pulse_frequency.setGeometry(QtCore.QRect(20, 260, 101, 16))
        self.label_pulse_frequency.setObjectName("label_pulse_frequency")

        self.label_pulse_width = QtWidgets.QLabel(self.flasher_control)
        self.label_pulse_width.setGeometry(QtCore.QRect(20, 350, 101, 16))
        self.label_pulse_width.setObjectName("label_pulse_width")

        self.label_light_pulse = QtWidgets.QLabel(self.flasher_control)
        self.label_light_pulse.setGeometry(QtCore.QRect(260, 260, 101, 16))
        self.label_light_pulse.setObjectName("label_light_pulse")

        self.frame_led_voltage = QtWidgets.QFrame(self.flasher_control)
        self.frame_led_voltage.setGeometry(QtCore.QRect(20, 50, 221, 181))
        self.frame_led_voltage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_led_voltage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_led_voltage.setObjectName("frame_led_voltage")

        self.pulse_voltage_get = QtWidgets.QProgressBar(self.frame_led_voltage)
        self.pulse_voltage_get.setGeometry(QtCore.QRect(30, 30, 151, 23))
        self.pulse_voltage_get.setMinimum(77)
        self.pulse_voltage_get.setMaximum(165)
        self.pulse_voltage_get.setProperty("value", 125)
        self.pulse_voltage_get.setObjectName("pulse_voltage_get")

        self.lalbel_pulse_lower_lim = QtWidgets.QLabel(self.frame_led_voltage)
        self.lalbel_pulse_lower_lim.setGeometry(QtCore.QRect(30, 20, 31, 16))
        self.lalbel_pulse_lower_lim.setObjectName("lalbel_pulse_lower_lim")

        self.lalbel_pulse_upper_lim = QtWidgets.QLabel(self.frame_led_voltage)
        self.lalbel_pulse_upper_lim.setGeometry(QtCore.QRect(160, 20, 31, 16))
        self.lalbel_pulse_upper_lim.setObjectName("lalbel_pulse_upper_lim")

        self.led_set_voltage = QtWidgets.QDoubleSpinBox(self.frame_led_voltage)
        self.led_set_voltage.setGeometry(QtCore.QRect(50, 75, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.led_set_voltage.setFont(font)
        self.led_set_voltage.setObjectName("led_set_voltage")
        # self.led_set_voltage.valueChanged.connect(self.send_new_config)

        self.label_led_voltage = QtWidgets.QLabel(self.frame_led_voltage)
        self.label_led_voltage.setGeometry(QtCore.QRect(140, 80, 31, 16))
        self.label_led_voltage.setObjectName("label_led_voltage")

        self.label_under_voltage = QtWidgets.QLabel(self.frame_led_voltage)
        self.label_under_voltage.setGeometry(QtCore.QRect(40, 140, 51, 20))
        self.label_under_voltage.setText("")
        self.label_under_voltage.setPixmap(QtGui.QPixmap("BlackLed.png"))
        self.label_under_voltage.setObjectName("label_under_voltage")
        self.label_led_voltage_under = QtWidgets.QLabel(self.frame_led_voltage)
        self.label_led_voltage_under.setGeometry(QtCore.QRect(50, 120, 41, 16))
        self.label_led_voltage_under.setObjectName("label_led_voltage_under")

        self.label_over_voltage = QtWidgets.QLabel(self.frame_led_voltage)
        self.label_over_voltage.setGeometry(QtCore.QRect(130, 140, 51, 20))
        self.label_over_voltage.setText("")
        self.label_over_voltage.setPixmap(QtGui.QPixmap("BlackLed.png"))
        self.label_over_voltage.setObjectName("label_over_voltage")
        self.label_led_voltage_over = QtWidgets.QLabel(self.frame_led_voltage)
        self.label_led_voltage_over.setGeometry(QtCore.QRect(140, 120, 31, 16))
        self.label_led_voltage_over.setObjectName("label_led_voltage_over")

        self.label_frame_led_voltage = QtWidgets.QLabel(self.flasher_control)
        self.label_frame_led_voltage.setGeometry(QtCore.QRect(20, 30, 101, 16))
        self.label_frame_led_voltage.setObjectName("label_frame_led_voltage")

        self.i_o = QtWidgets.QGroupBox(self.centralwidget)
        self.i_o.setGeometry(QtCore.QRect(250, 590, 421, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.i_o.setFont(font)
        self.i_o.setObjectName("i_o")
        self.check_trigger_out = QtWidgets.QCheckBox(self.i_o)
        self.check_trigger_out.setGeometry(QtCore.QRect(260, 30, 85, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.check_trigger_out.setFont(font)
        self.check_trigger_out.setObjectName("check_trigger_out")
        # self.check_trigger_out.stateChanged.connect(self.send_new_config)

        self.check_fiber_2 = QtWidgets.QCheckBox(self.i_o)
        self.check_fiber_2.setGeometry(QtCore.QRect(130, 30, 85, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.check_fiber_2.setFont(font)
        self.check_fiber_2.setObjectName("check_fiber_2")
        # self.check_fiber_2.stateChanged.connect(self.send_new_config)

        self.check_fiber_1 = QtWidgets.QCheckBox(self.i_o)
        self.check_fiber_1.setGeometry(QtCore.QRect(10, 30, 85, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.check_fiber_1.setFont(font)
        self.check_fiber_1.setObjectName("check_fiber_1")
        # self.check_fiber_1.stateChanged.connect(self.send_new_config)

        self.led_fib_1 = QtWidgets.QLabel(self.i_o)
        self.led_fib_1.setGeometry(QtCore.QRect(10, 50, 21, 16))
        self.led_fib_1.setText("")
        self.led_fib_1.setPixmap(QtGui.QPixmap("BlackLed.png"))
        self.led_fib_1.setObjectName("led_fib_1")
        self.led_fib_2 = QtWidgets.QLabel(self.i_o)
        self.led_fib_2.setGeometry(QtCore.QRect(130, 50, 21, 16))
        self.led_fib_2.setText("")
        self.led_fib_2.setPixmap(QtGui.QPixmap("BlackLed.png"))
        self.led_fib_2.setObjectName("led_fib_2")

        self.led_fib_1_fault = QtWidgets.QLabel(self.i_o)
        self.led_fib_1_fault.setGeometry(QtCore.QRect(80, 30, 21, 36))
        self.led_fib_1_fault.setText("")
        self.led_fib_1_fault.setPixmap(QtGui.QPixmap("BlackLed.png"))
        self.led_fib_1_fault.setObjectName("led_fib_1_fault")
        self.led_fib_2_fault = QtWidgets.QLabel(self.i_o)
        self.led_fib_2_fault.setGeometry(QtCore.QRect(200, 30, 21, 36))
        self.led_fib_2_fault.setText("")
        self.led_fib_2_fault.setPixmap(QtGui.QPixmap("BlackLed.png"))
        self.led_fib_2_fault.setObjectName("led_fib_2_fault")

        self.led_trigger_out = QtWidgets.QLabel(self.i_o)
        self.led_trigger_out.setGeometry(QtCore.QRect(260, 50, 21, 16))
        self.led_trigger_out.setText("")
        self.led_trigger_out.setPixmap(QtGui.QPixmap("BlackLed.png"))
        self.led_trigger_out.setObjectName("led_trigger_out")

        self.flasher_control.raise_()
        self.led_status.raise_()
        self.serial_link.raise_()
        self.ethernet.raise_()
        self.label_ip_address.raise_()
        self.label_host.raise_()
        self.i_o.raise_()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 695, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.ip_address.setText(_translate("MainWindow", "129.194.052.090"))
        self.host.setText(_translate("MainWindow", "50001"))
        self.label_ip_address.setText(_translate("MainWindow", "IP address"))
        self.label_host.setText(_translate("MainWindow", "Serial link port"))
        self.ethernet.setTitle(_translate("MainWindow", "Ethernet"))
        self.serial_link.setTitle(_translate("MainWindow", "Serial link"))
        self.start_com.setText(_translate("MainWindow", "Start"))
        self.stop_com.setText(_translate("MainWindow", "Stop"))
        self.label_serial_link_tx.setText(_translate("MainWindow", "TX"))
        self.label_serial_link_rx.setText(_translate("MainWindow", "RX"))
        self.led_status.setTitle(_translate("MainWindow", "LED status"))

        for val, led_id in enumerate(self.led_set_status):
            led_id.setText(_translate("MainWindow", str(val + 1)))

        self.label_set_status.setText(_translate("MainWindow", "Change status"))
        self.led_set_status_all.setText(_translate("MainWindow", "All"))

        self.label_get_status.setText(_translate("MainWindow", "Current status"))
        self.label_led_all.setText(_translate("MainWindow", "All"))
        self.flasher_control.setTitle(_translate("MainWindow", "Flasher control"))
        self.status_request.setText(_translate("MainWindow", "Status request"))
        self.send_configuration.setText(_translate("MainWindow", "Send Configuration"))
        self.reset.setText(_translate("MainWindow", "Reset"))
        self.label_pulse_frequency_div.setText(_translate("MainWindow", "/"))
        self.label_res_pulse_frequency.setText(_translate("MainWindow", "="))
        self.label_res_pulse_width.setText(_translate("MainWindow", "x 62.5 ns = "))
        self.start_pulse.setText(_translate("MainWindow", "Start"))
        self.stop_pulse.setText(_translate("MainWindow", "Stop"))
        self.label_flash_duration.setText(_translate("MainWindow", "flash duration"))
        self.label_flash_duration.setText(_translate("MainWindow", "x 0.1 s"))
        self.label_pulse_frequency.setText(_translate("MainWindow", "Pulse frequency"))

        self.lalbel_pulse_lower_lim.setText(_translate("MainWindow", "7.7"))
        self.lalbel_pulse_upper_lim.setText(_translate("MainWindow", "16.5"))
        self.label_temperature.setText(_translate("MainWindow", "Temperature = 25 deg C"))

        self.pulse_frequency.setMinimum(300)
        self.pulse_frequency.setMaximum(10000)
        self.pulse_frequency.setSingleStep(100)
        self.pulse_frequency.setValue(1000)

        self.led_set_voltage.setMinimum(7.7)
        self.led_set_voltage.setMaximum(16.5)
        self.led_set_voltage.setSingleStep(0.5)
        self.led_set_voltage.setValue(12.5)

        self.pulse_width.setMinimum(1)
        self.pulse_width.setMaximum(1000)
        self.pulse_width.setSingleStep(1)
        self.pulse_width.setValue(4)

        self.frequency_divider.setMinimum(1)
        self.frequency_divider.setMaximum(3000)
        self.frequency_divider.setSingleStep(1)
        self.frequency_divider.setValue(1)

        self.flash_duration.setMinimum(0)
        self.flash_duration.setMaximum(1023)
        self.flash_duration.setSingleStep(1)
        self.flash_duration.setValue(1)

        self.label_pulse_width.setText(_translate("MainWindow", "Pulse width"))
        self.label_light_pulse.setText(_translate("MainWindow", "Light Pulse"))
        self.label_led_voltage.setText(_translate("MainWindow", "Volts"))
        self.label_led_voltage_under.setText(_translate("MainWindow", "Under"))
        self.label_led_voltage_over.setText(_translate("MainWindow", "Over"))
        self.label_frame_led_voltage.setText(_translate("MainWindow", "Led voltage"))
        self.i_o.setTitle(_translate("MainWindow", "I/O"))
        self.check_trigger_out.setText(_translate("MainWindow", "Trigger Out"))
        self.check_fiber_2.setText(_translate("MainWindow", "Fiber 2"))
        self.check_fiber_1.setText(_translate("MainWindow", "Fiber 1"))

        self.start_com.clicked.connect(self.start_com_clicked)
        self.stop_com.clicked.connect(self.stop_com_clicked)

        for led_id in range(13):
            self.led_set_status[led_id].stateChanged.connect(self.send_new_config)

        self.led_set_status_all.stateChanged.connect(self.send_new_config)
        self.pulse_frequency.valueChanged.connect(self.send_new_config)
        self.frequency_divider.valueChanged.connect(self.send_new_config)
        self.pulse_width.valueChanged.connect(self.send_new_config)
        self.led_set_voltage.valueChanged.connect(self.send_new_config)
        self.flash_duration.valueChanged.connect(self.send_new_config)
        self.start_pulse.clicked.connect(self.start_pulse_clicked)
        self.stop_pulse.clicked.connect(self.stop_pulse_clicked)
        self.check_fiber_1.stateChanged.connect(self.send_new_config)
        self.check_fiber_2.stateChanged.connect(self.send_new_config)
        self.check_trigger_out.stateChanged.connect(self.send_new_config)


    def start_com_clicked(self):
        res = self.this_flasher.connect_flasher(str(self.ip_address.text()), int(self.host.text()))
        if res == 1:
            self.label_com_started.setPixmap(QtGui.QPixmap("GreenLed.png"))
        else:
            self.label_com_started.setPixmap(QtGui.QPixmap("RedLed.png"))

    def stop_com_clicked(self):
        self.this_flasher.close_connect_flasher()
        self.label_com_started.setPixmap(QtGui.QPixmap("RedLed.png"))

    def start_pulse_clicked(self):
        self.pulse_status = 1
        self.label_pulse_started.setPixmap(QtGui.QPixmap("GreenLed.png"))

    def stop_pulse_clicked(self):
        self.pulse_status = 0
        self.label_pulse_started.setPixmap(QtGui.QPixmap("BlackLed.png"))

    def get_status_clicked(self):
        self.this_flasher.get_flasher_status()

    def reset_flasher(self):
        self.this_flasher.reset_flasher()

    def send_new_config(self):
        self.this_flasher.init_request()
        print('-------------------------')

        # Setting led status
        new_led_status = []
        for i in range(13):
            if self.led_set_status_all.isChecked():
                new_led_status.append(1)
            else:
                new_led_status.append(int(self.led_set_status[i].isChecked()))

        self.this_flasher.change_led_status(new_led_status)

        # Setting led voltage
        self.this_flasher.change_led_voltage(self.led_set_voltage.value())

        # Setting pulse duration
        self.this_flasher.change_pulse_duration(self.flash_duration.value())

        # Setting pulse frequency
        self.this_flasher.change_pulse_frequency(self.pulse_frequency.value())

        # Setting freq divider
        self.this_flasher.change_freq_divider(self.frequency_divider.value())

        # Setting pulse width
        self.this_flasher.change_pulse_width(self.pulse_width.value())

        # Checking io status
        new_io_status = []
        new_io_status.append(self.pulse_status)
        new_io_status.append(int(self.check_trigger_out.isChecked()))
        new_io_status.append(int(self.check_fiber_1.isChecked()))
        new_io_status.append(int(self.check_fiber_2.isChecked()))
        self.this_flasher.change_io_status(new_io_status)

        self.led_tx.setPixmap(QtGui.QPixmap("GreenLed.png"))
        self.this_flasher.send_new_config()
        self.led_tx.setPixmap(QtGui.QPixmap("BlackLed.png"))
        self.led_rx.setPixmap(QtGui.QPixmap("GreenLed.png"))
        self.display_config()
        self.led_rx.setPixmap(QtGui.QPixmap("BlackLed.png"))

    def display_config(self):
        # Update led status
        for i in range(13):
            led_id = self.this_flasher.data_frame_ans['led_status']['led_order'][i]-1
            if self.this_flasher.data_frame_ans['led_status']['value'][i]:
                self.led_get_status[led_id].setPixmap(QtGui.QPixmap("GreenLed.png"))
            else:
                self.led_get_status[led_id].setPixmap(QtGui.QPixmap("BlackLed.png"))

        # Update led voltage
        self.pulse_voltage_get.setValue(int(self.this_flasher.data_frame_ans['led_voltage']['convert']()*10))

        # Update pulse duration
        self.flash_duration.setValue(self.this_flasher.data_frame_ans['pulse_duration']['value'])

        # Update Pulse frequency
        self.pulse_frequency.setValue(self.this_flasher.data_frame_ans['pulse_frequency']['convert']())

        # Update freqency divider
        self.frequency_divider.setValue(self.this_flasher.data_frame_ans['freq_divider']['value'])
        try:
            self.label_res_pulse_frequency.setText('= '+str(int(self.this_flasher.data_frame_ans['pulse_frequency'][
                                                                'convert']()/self.this_flasher.data_frame_ans[
            'freq_divider']['value'])))
        except ZeroDivisionError:
            self.label_res_pulse_frequency.setText('= error')

        # Update pulse width
        self.pulse_width.setValue(self.this_flasher.data_frame_ans['pulse_width']['value'])
        self.label_res_pulse_width.setText('x 64.5 ns = '+str(self.this_flasher.data_frame_ans['pulse_width'][
                                                                  'value']*64.5)+' ns')
        # Update temperature
        self.label_temperature.setText('Temperature = '+str(int(self.this_flasher.data_frame_ans['temperature'][
                                                                'convert']()))+'deg C')

        # Update voltage status
        if self.this_flasher.data_frame_ans['voltage_status']['value'][0] == 0:
            self.label_under_voltage.setPixmap(QtGui.QPixmap("GreenLed.png"))
        else:
            self.label_under_voltage.setPixmap(QtGui.QPixmap("RedLed.png"))

        if self.this_flasher.data_frame_ans['voltage_status']['value'][1] == 0:
            self.label_over_voltage.setPixmap(QtGui.QPixmap("GreenLed.png"))
        else:
            self.label_over_voltage.setPixmap(QtGui.QPixmap("RedLed.png"))

        if self.this_flasher.data_frame_ans['voltage_status']['value'][2] == 0:
            self.led_fib_1_fault.setPixmap(QtGui.QPixmap("GreenLed.png"))
        else:
            self.led_fib_1_fault.setPixmap(QtGui.QPixmap("RedLed.png"))

        if self.this_flasher.data_frame_ans['voltage_status']['value'][3] == 0:
            self.led_fib_2_fault.setPixmap(QtGui.QPixmap("GreenLed.png"))
        else:
            self.led_fib_2_fault.setPixmap(QtGui.QPixmap("RedLed.png"))

         # Update io status

        if self.this_flasher.data_frame_ans['io_status']['value'][0] == 0:
            self.label_pulse_started.setPixmap(QtGui.QPixmap("BlackLed.png"))
        else:
            self.label_pulse_started.setPixmap(QtGui.QPixmap("GreenLed.png"))

        if self.this_flasher.data_frame_ans['io_status']['value'][1] == 0:
            self.label_over_voltage.setPixmap(QtGui.QPixmap("GreenLed.png"))
        else:
            self.label_over_voltage.setPixmap(QtGui.QPixmap("RedLed.png"))

        if self.this_flasher.data_frame_ans['io_status']['value'][2] == 0:
            self.led_fib_1_fault.setPixmap(QtGui.QPixmap("GreenLed.png"))
        else:
            self.led_fib_1_fault.setPixmap(QtGui.QPixmap("RedLed.png"))

        if self.this_flasher.data_frame_ans['io_status']['value'][3] == 0:
            self.led_fib_2_fault.setPixmap(QtGui.QPixmap("GreenLed.png"))
        else:
            self.led_fib_2_fault.setPixmap(QtGui.QPixmap("RedLed.png"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
