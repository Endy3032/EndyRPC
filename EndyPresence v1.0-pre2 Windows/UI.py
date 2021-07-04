# Form implementation generated from reading ui file 'EndyPresence.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


import os, sys, webbrowser, json, requests
from urllib.request import urlretrieve
from PyQt6 import QtCore, QtGui, QtWidgets
current_dir = os.path.abspath(os.path.dirname(__file__))


def mask_image(imgdata, imgtype='png', size=88):
    image = QtGui.QImage.fromData(imgdata, imgtype)
    image.convertToFormat(QtGui.QImage.Format.Format_ARGB32)
    imgsize = image.width()
    out_img = QtGui.QImage(imgsize, imgsize, QtGui.QImage.Format.Format_ARGB32)
    out_img.fill(QtCore.Qt.GlobalColor.transparent)
    brush = QtGui.QBrush(image)
    painter = QtGui.QPainter(out_img)
    painter.setBrush(brush)
    painter.setPen(QtCore.Qt.PenStyle.NoPen)
    painter.drawEllipse(0, 0, imgsize, imgsize)
    painter.end()
    pr = QtGui.QWindow().devicePixelRatio()
    pm = QtGui.QPixmap.fromImage(out_img)
    pm.setDevicePixelRatio(pr)
    size *= pr
    return pm.scaled(size, size, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation)


def update_appid(id):
    with open(os.path.join(current_dir, 'Database.json'), 'r+') as db:
        data = json.load(db)
        other = data[0:4]
        appid = data[4]
        appid["AppID"] = id
        ls = [other[0], other[1], other[2], other[3], appid]
        db.seek(0)
        db.write(json.dumps(ls))
        db.truncate()


assets = []
with open(os.path.join(current_dir, 'Database.json'), 'r') as db:
    data = json.load(db)
    firstrun = data[0]['FR']
    rpcasset = data[1]["AD"]
    AppID = data[4]
    if firstrun: rpcasset = json.loads(requests.get(f'https://discordapp.com/api/oauth2/applications/{AppID["AppID"]}/assets').text)
    for i in rpcasset: assets.append(i["name"])


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(810, 600)
        MainWindow.setMinimumSize(QtCore.QSize(810, 600))
        MainWindow.setMaximumSize(QtCore.QSize(810, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(current_dir, 'Images', 'Endy.png')), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:#2C2F33; font: 300 20pt \"ABC Ginto Normal Trial\";")
        MainWindow.setIconSize(QtCore.QSize(512, 512))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(0, 0, 471, 50))
        self.Title_2 = QtWidgets.QLabel(self.centralwidget)
        self.Title_2.setGeometry(QtCore.QRect(0, 43, 471, 18))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        self.Title.setFont(font)
        self.Title.setStyleSheet("color: #7289DA; font: 700 23pt \"ABC Ginto Normal Trial\";")
        self.Title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Title.setObjectName("Title")
        self.Title_2.setFont(font)
        self.Title_2.setStyleSheet("color: #7289DA; font: 700 12pt \"ABC Ginto Normal Trial\";")
        self.Title_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Title_2.setObjectName("Title_2")
        self.Preview = QtWidgets.QLabel(self.centralwidget)
        self.Preview.setGeometry(QtCore.QRect(460, 0, 350, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        self.Preview.setFont(font)
        self.Preview.setStyleSheet("color: #7289DA; font: 700 23pt \"ABC Ginto Normal Trial\";")
        self.Preview.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Preview.setObjectName("Preview")
        self.PreviewPane = QtWidgets.QWidget(self.centralwidget)
        self.PreviewPane.setGeometry(QtCore.QRect(470, 125, 330, 326))
        self.PreviewPane.setStyleSheet("background-color: rgb(24, 25, 28); border-bottom-left-radius:8px; border-bottom-right-radius:8px;")
        self.PreviewPane.setObjectName("PreviewPane")
        self.b2txtl = QtWidgets.QLabel(self.PreviewPane)
        self.b2txtl.setGeometry(QtCore.QRect(17, 272, 296, 35))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.b2txtl.setFont(font)
        self.b2txtl.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.b2txtl.setStyleSheet("background-color: rgb(79, 84, 92); border-radius: 3px; font: 700 12pt \"ABC Ginto Normal Trial\"; color: #fff; color: #fff")
        self.b2txtl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.b2txtl.setObjectName("b2txtl")
        self.b1txtl = QtWidgets.QLabel(self.PreviewPane)
        self.b1txtl.setGeometry(QtCore.QRect(17, 228, 296, 35))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.b1txtl.setFont(font)
        self.b1txtl.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.b1txtl.setToolTip("")
        self.b1txtl.setStyleSheet("background-color: rgb(79, 84, 92); border-radius: 3px; font: 700 12pt \"ABC Ginto Normal Trial\"; color: #fff;")
        self.b1txtl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.b1txtl.setObjectName("b1txtl")
        self.appide = QtWidgets.QTextEdit(self.centralwidget)
        self.appide.setGeometry(QtCore.QRect(140, 105, 320, 35))
        self.appide.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.appide.setAutoFillBackground(False)
        self.appide.setStyleSheet("color: #99AAB6; font: 100 13pt \"ABC Ginto Normal Trial\";")
        self.appide.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.appide.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.appide.setTabChangesFocus(True)
        self.appide.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.NoWrap)
        self.appide.setReadOnly(True)
        self.appide.setAcceptRichText(False)
        self.appide.setObjectName("appide")
        self.limge = QtWidgets.QComboBox(self.centralwidget)
        self.limge.setGeometry(QtCore.QRect(140, 150, 320, 35))
        self.limge.setStyleSheet("color: #99AAB6; font: 100 13pt \"ABC Ginto Normal Trial\"; text-align: center;")
        self.limge.setEditable(False)
        self.limge.setObjectName("limge")
        self.simge = QtWidgets.QComboBox(self.centralwidget)
        self.simge.setGeometry(QtCore.QRect(140, 195, 320, 35))
        self.simge.setStyleSheet("color: #99AAB6; font: 100 13pt \"ABC Ginto Normal Trial\"; text-align: center;")
        self.simge.setObjectName("simge")
        self.ltxte = QtWidgets.QTextEdit(self.centralwidget)
        self.ltxte.setGeometry(QtCore.QRect(140, 240, 320, 35))
        self.ltxte.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.ltxte.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.ltxte.setAutoFillBackground(False)
        self.ltxte.setStyleSheet("color: #99AAB6; font: 100 13pt \"ABC Ginto Normal Trial\";")
        self.ltxte.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ltxte.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ltxte.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.ltxte.setTabChangesFocus(True)
        self.ltxte.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.NoWrap)
        self.ltxte.setAcceptRichText(False)
        self.ltxte.setObjectName("ltxte")
        self.stxte = QtWidgets.QTextEdit(self.centralwidget)
        self.stxte.setGeometry(QtCore.QRect(140, 285, 320, 35))
        self.stxte.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.stxte.setAutoFillBackground(False)
        self.stxte.setStyleSheet("color: #99AAB6; font: 100 13pt \"ABC Ginto Normal Trial\";")
        self.stxte.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.stxte.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.stxte.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.stxte.setTabChangesFocus(True)
        self.stxte.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.NoWrap)
        self.stxte.setAcceptRichText(False)
        self.stxte.setObjectName("stxte")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 60, 140, 35))
        self.label.setStyleSheet("color: #99AAB6; font: 500 16pt \"ABC Ginto Normal Trial\";")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 105, 140, 35))
        self.label_2.setStyleSheet("color: #99AAB6; font: 500 16pt \"ABC Ginto Normal Trial\";")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 195, 140, 35))
        self.label_3.setStyleSheet("color: #99AAB6; font: 500 16pt \"ABC Ginto Normal Trial\";")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 150, 140, 35))
        self.label_4.setStyleSheet("color: #99AAB6; font: 500 16pt \"ABC Ginto Normal Trial\";")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 285, 140, 35))
        self.label_5.setStyleSheet("color: #99AAB6; font: 500 16pt \"ABC Ginto Normal Trial\";")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 375, 140, 35))
        self.label_6.setStyleSheet("color: #99AAB6; font: 500 16pt \"ABC Ginto Normal Trial\";")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, 240, 140, 35))
        self.label_7.setStyleSheet("color: #99AAB6; font: 500 16pt \"ABC Ginto Normal Trial\";")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 330, 140, 35))
        self.label_8.setStyleSheet("color: #99AAB6; font: 500 16pt \"ABC Ginto Normal Trial\";")
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(0, 420, 140, 35))
        self.label_11.setStyleSheet("color: #99AAB6; font: 500 16pt \"ABC Ginto Normal Trial\";")
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(0, 465, 140, 35))
        self.label_12.setStyleSheet("color: #99AAB6; font: 500 16pt \"ABC Ginto Normal Trial\";")
        self.label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(0, 555, 140, 35))
        self.label_13.setStyleSheet("color: #99AAB6; font: 500 16pt \"ABC Ginto Normal Trial\";")
        self.label_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(0, 510, 140, 35))
        self.label_14.setStyleSheet("color: #99AAB6; font: 500 16pt \"ABC Ginto Normal Trial\";")
        self.label_14.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.detailse = QtWidgets.QTextEdit(self.centralwidget)
        self.detailse.setGeometry(QtCore.QRect(140, 330, 320, 35))
        self.detailse.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.detailse.setAutoFillBackground(False)
        self.detailse.setStyleSheet("color: #99AAB6; font: 100 13pt \"ABC Ginto Normal Trial\";")
        self.detailse.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.detailse.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.detailse.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.detailse.setTabChangesFocus(True)
        self.detailse.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.NoWrap)
        self.detailse.setAcceptRichText(False)
        self.detailse.setObjectName("detailse")
        self.statee = QtWidgets.QTextEdit(self.centralwidget)
        self.statee.setGeometry(QtCore.QRect(140, 375, 320, 35))
        self.statee.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.statee.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.statee.setAutoFillBackground(False)
        self.statee.setStyleSheet("color: #99AAB6; font: 100 13pt \"ABC Ginto Normal Trial\";")
        self.statee.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.statee.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.statee.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.statee.setTabChangesFocus(True)
        self.statee.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.NoWrap)
        self.statee.setAcceptRichText(False)
        self.statee.setObjectName("statee")
        self.b1txte = QtWidgets.QTextEdit(self.centralwidget)
        self.b1txte.setGeometry(QtCore.QRect(140, 420, 320, 35))
        self.b1txte.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.b1txte.setAutoFillBackground(False)
        self.b1txte.setStyleSheet("color: #99AAB6; font: 100 13pt \"ABC Ginto Normal Trial\";")
        self.b1txte.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.b1txte.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.b1txte.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.b1txte.setTabChangesFocus(True)
        self.b1txte.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.NoWrap)
        self.b1txte.setAcceptRichText(False)
        self.b1txte.setObjectName("b1txte")
        self.b1urle = QtWidgets.QTextEdit(self.centralwidget)
        self.b1urle.setGeometry(QtCore.QRect(140, 465, 320, 35))
        self.b1urle.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.b1urle.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.b1urle.setAutoFillBackground(False)
        self.b1urle.setStyleSheet("color: #99AAB6; font: 100 13pt \"ABC Ginto Normal Trial\";")
        self.b1urle.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.b1urle.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.b1urle.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.b1urle.setTabChangesFocus(True)
        self.b1urle.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.NoWrap)
        self.b1urle.setAcceptRichText(False)
        self.b1urle.setObjectName("b1urle")
        self.b2txte = QtWidgets.QTextEdit(self.centralwidget)
        self.b2txte.setGeometry(QtCore.QRect(140, 510, 320, 35))
        self.b2txte.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.b2txte.setAutoFillBackground(False)
        self.b2txte.setStyleSheet("color: #99AAB6; font: 100 13pt \"ABC Ginto Normal Trial\";")
        self.b2txte.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.b2txte.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.b2txte.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.b2txte.setTabChangesFocus(True)
        self.b2txte.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.NoWrap)
        self.b2txte.setAcceptRichText(False)
        self.b2txte.setObjectName("b2txte")
        self.b2urle = QtWidgets.QTextEdit(self.centralwidget)
        self.b2urle.setGeometry(QtCore.QRect(140, 555, 320, 35))
        self.b2urle.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.b2urle.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.b2urle.setAutoFillBackground(False)
        self.b2urle.setStyleSheet("color: #99AAB6; font: 100 13pt \"ABC Ginto Normal Trial\";")
        self.b2urle.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.b2urle.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.b2urle.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.b2urle.setTabChangesFocus(True)
        self.b2urle.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.NoWrap)
        self.b2urle.setAcceptRichText(False)
        self.b2urle.setObjectName("b2urle")
        self.PreviewPane_2 = QtWidgets.QWidget(self.centralwidget)
        self.PreviewPane_2.setGeometry(QtCore.QRect(470, 60, 330, 321))
        self.PreviewPane_2.setStyleSheet("background-color: \"#28292C\"; border-radius: 8px")
        self.PreviewPane_2.setObjectName("PreviewPane_2")
        self.PreviewPane_3 = QtWidgets.QWidget(self.centralwidget)
        self.PreviewPane_3.setGeometry(QtCore.QRect(487, 77, 101, 101))
        self.PreviewPane_3.setStyleSheet("background-color: rgb(24, 25, 28); border-radius:50px;")
        self.PreviewPane_3.setObjectName("PreviewPane_3")
        self.pfp = QtWidgets.QLabel(self.PreviewPane_3)
        self.pfp.setGeometry(QtCore.QRect(5, 5, 90, 90))
        self.pfp.setStyleSheet("border-radius: 45px;")
        self.pfp.setText("")
        self.pfp.setPixmap(QtGui.QPixmap(os.path.join(current_dir, 'Images', 'basepfp.png')))
        self.pfp.setScaledContents(True)
        self.pfp.setObjectName("pfp")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(490, 234, 290, 1))
        self.widget.setStyleSheet("background-color: rgb(38,39,41)")
        self.widget.setObjectName("widget")
        self.appnamel = QtWidgets.QLabel(self.centralwidget)
        self.appnamel.setGeometry(QtCore.QRect(564, 280, 210, 16))
        self.appnamel.setStyleSheet("background-color: rgba(24, 25, 28, 00); color: rgb(220, 221, 222); font: 500 13pt \"ABC Ginto Normal Trial\"; letter-spacing: 0.3px")
        self.appnamel.setObjectName("appnamel")
        self.statel = QtWidgets.QLabel(self.centralwidget)
        self.statel.setGeometry(QtCore.QRect(564, 317, 210, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.statel.setFont(font)
        self.statel.setStyleSheet("background-color: rgba(24, 25, 28, 00); font: 100 11pt \"ABC Ginto Normal Trial\"; color: #fff; letter-spacing: 0.03px")
        self.statel.setObjectName("statel")
        self.detailsl = QtWidgets.QLabel(self.centralwidget)
        self.detailsl.setGeometry(QtCore.QRect(564, 299, 210, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.detailsl.setFont(font)
        self.detailsl.setStyleSheet("background-color: rgba(24, 25, 28, 00); font: 100 11pt \"ABC Ginto Normal Trial\"; color: #fff; letter-spacing: 0.03px")
        self.detailsl.setObjectName("detailsl")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(488, 248, 200, 16))
        self.label_19.setStyleSheet("background-color: rgba(24, 25, 10, 00); color: rgb(185, 187, 190); font: 500 10pt \"ABC Ginto Normal Trial\"; letter-spacing: 0.3px;")
        self.label_19.setObjectName("label_19")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(487, 195, 290, 31))
        self.name.setStyleSheet("background-color: rgba(24, 25, 28, 00); font: 500 18pt \"ABC Ginto Normal Trial\"; letter-spacing: 0.05px")
        self.name.setObjectName("name")
        self.previewb = QtWidgets.QPushButton(self.centralwidget)
        self.previewb.setGeometry(QtCore.QRect(487, 465, 143, 30))
        self.previewb.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.previewb.setStyleSheet("background-color: rgb(79, 84, 92); border-radius: 3px; font: 500 12pt \"ABC Ginto Normal Trial\"; color: #fff;")
        self.previewb.setObjectName("previewb")
        self.rpcb = QtWidgets.QPushButton(self.centralwidget)
        self.rpcb.setGeometry(QtCore.QRect(487, 543, 296, 30))
        self.rpcb.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.rpcb.setStyleSheet("background-color: rgb(79, 84, 92); border-radius: 3px; font: 500 12pt \"ABC Ginto Normal Trial\"; color: #fff;")
        self.rpcb.setObjectName("rpcb")
        self.udatab = QtWidgets.QPushButton(self.centralwidget)
        self.udatab.setGeometry(QtCore.QRect(487, 504, 143, 30))
        self.udatab.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.udatab.setStyleSheet("background-color: rgb(79, 84, 92); border-radius: 3px; font: 500 12pt \"ABC Ginto Normal Trial\"; color: #fff;")
        self.udatab.setObjectName("udatab")
        self.PreviewPane_4 = QtWidgets.QWidget(self.centralwidget)
        self.PreviewPane_4.setGeometry(QtCore.QRect(470, 384, 330, 206))
        self.PreviewPane_4.setStyleSheet("background-color: \"#28292C\"; border-radius: 8px")
        self.PreviewPane_4.setObjectName("PreviewPane_4")
        self.uidl = QtWidgets.QLabel(self.centralwidget)
        self.uidl.setGeometry(QtCore.QRect(143, 60, 317, 35))
        self.uidl.setStyleSheet("color: #99AAB6; font: 100 13pt \"ABC Ginto Normal Trial\";")
        self.uidl.setText("")
        self.uidl.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.uidl.setObjectName("uidl")
        self.resetappidb = QtWidgets.QPushButton(self.centralwidget)
        self.resetappidb.setGeometry(QtCore.QRect(640, 504, 143, 30))
        self.resetappidb.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.resetappidb.setStyleSheet("background-color: rgb(79, 84, 92); border-radius: 3px; font: 500 12pt \"ABC Ginto Normal Trial\"; color: #fff;")
        self.resetappidb.setObjectName("resetappidb")
        self.updateappidb = QtWidgets.QPushButton(self.centralwidget)
        self.updateappidb.setGeometry(QtCore.QRect(640, 465, 143, 30))
        self.updateappidb.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.updateappidb.setStyleSheet("background-color: rgb(79, 84, 92); border-radius: 3px; font: 500 12pt \"ABC Ginto Normal Trial\"; color: #fff;")
        self.updateappidb.setObjectName("updateappidb")
        self.PreviewPane_4.raise_()
        self.PreviewPane_2.raise_()
        self.Title.raise_()
        self.Title_2.raise_()
        self.Preview.raise_()
        self.PreviewPane.raise_()
        self.appide.raise_()
        self.limge.raise_()
        self.simge.raise_()
        self.ltxte.raise_()
        self.stxte.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.detailse.raise_()
        self.statee.raise_()
        self.b1txte.raise_()
        self.b1urle.raise_()
        self.b2txte.raise_()
        self.b2urle.raise_()
        self.PreviewPane_3.raise_()
        self.widget.raise_()
        self.appnamel.raise_()
        self.detailsl.raise_()
        self.statel.raise_()
        self.label_19.raise_()
        self.name.raise_()
        self.previewb.raise_()
        self.rpcb.raise_()
        self.udatab.raise_()
        self.uidl.raise_()
        self.resetappidb.raise_()
        self.updateappidb.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EndyPresence"))
        self.Title.setText(_translate("MainWindow", "EndyPresence"))
        self.Title_2.setText(_translate("MainWindow", "v1.0-pre1"))
        self.Preview.setText(_translate("MainWindow", "Preview"))
        self.b2txtl.setText(_translate("MainWindow", "Button 2 Text"))
        self.b1txtl.setText(_translate("MainWindow", "Button 1 Text"))
        self.appide.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'ABC Ginto Normal Trial\'; font-size:18pt; font-weight:300; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.ltxte.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'ABC Ginto Normal Trial\'; font-size:18pt; font-weight:300; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.stxte.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'ABC Ginto Normal Trial\'; font-size:18pt; font-weight:300; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "User ID"))
        self.label_2.setText(_translate("MainWindow", "App ID"))
        self.label_3.setText(_translate("MainWindow", "Small IMG"))
        self.label_4.setText(_translate("MainWindow", "Large IMG"))
        self.label_5.setText(_translate("MainWindow", "Small TXT"))
        self.label_8.setText(_translate("MainWindow", "Details"))
        self.label_7.setText(_translate("MainWindow", "Large TXT"))
        self.label_6.setText(_translate("MainWindow", "State"))
        self.label_11.setText(_translate("MainWindow", "B1 Text"))
        self.label_12.setText(_translate("MainWindow", "B1 URL"))
        self.label_13.setText(_translate("MainWindow", "B2 URL"))
        self.label_14.setText(_translate("MainWindow", "B2 Text"))
        self.detailse.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'ABC Ginto Normal Trial\'; font-size:18pt; font-weight:300; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.statee.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'ABC Ginto Normal Trial\'; font-size:18pt; font-weight:300; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.b1txte.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'ABC Ginto Normal Trial\'; font-size:18pt; font-weight:300; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.b1urle.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'ABC Ginto Normal Trial\'; font-size:18pt; font-weight:300; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.b2txte.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'ABC Ginto Normal Trial\'; font-size:18pt; font-weight:300; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.b2urle.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'ABC Ginto Normal Trial\'; font-size:18pt; font-weight:300; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.appnamel.setText(_translate("MainWindow", "EndyPresence"))
        self.detailsl.setText(_translate("MainWindow", "Details"))
        self.statel.setText(_translate("MainWindow", "State"))
        self.label_19.setText(_translate("MainWindow", "PLAYING A GAME"))
        self.name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color: #fff;\">Name</span><span style=\" color:#b9bbbe;\">#XXXX</span></p></body></html>"))
        self.previewb.setText(_translate("MainWindow", "Update Preview"))
        self.rpcb.setText(_translate("MainWindow", "Update RPC"))
        self.udatab.setText(_translate("MainWindow", "Update User Data"))
        self.resetappidb.setText(_translate("MainWindow", "Reset AppID"))
        self.updateappidb.setText(_translate("MainWindow", "Update AppID"))

        self.udatab.clicked.connect(lambda: webbrowser.open("http://127.0.0.1:3032"))
        self.updateappidb.clicked.connect(lambda: update_appid(int(self.appide.toPlainText())))
        # self.updateappidb.clicked.connect(lambda: print('Passssss'))
        self.resetappidb.clicked.connect(lambda: update_appid(799634564875681792))
        self.resetappidb.clicked.connect(lambda: self.appide.setText(f'<p align="center">{str(799634564875681792)}</p>'))
        self.previewb.clicked.connect(self.update_preview)


    app = QtWidgets.QApplication(sys.argv)

    # restart_appid = QtWidgets.QMessageBox()
    # restart_appid.setText('EndyPresence - Update AppID ')


    def update(self, name, tag, hash, id):
        self.name.setText(f'<font color = #FFFFFF>{name}<font color=#B9BBBE>#{tag}</font>')
        self.uidl.setText(str(id))
        pfp_url = f'https://cdn.discordapp.com/avatars/{id}/{hash}.png?size=512'
        pfp_path = os.path.join(current_dir, 'Images', 'user_pfp.png')
        try:
            urlretrieve(pfp_url, pfp_path)
        except:
            update_msg = QtWidgets.QMessageBox()
            update_msg.setText('Failed to retrieve current profile picture. Using saved profile picture. Consider updating user data.')

        pfp = open(pfp_path, 'rb').read()
        pixmap = mask_image(pfp)
        self.pfp.setPixmap(pixmap)


    def update_appid_label(self, id):
        self.appide.setText(str(id))


    def update_preview(self):
        self.detailsl.setText(self.detailse.toPlainText() if len(self.detailse.toPlainText()) == 0 or len(self.detailse.toPlainText()) >= 2 else "Details must be >2 characters")
        self.statel.setText(self.statee.toPlainText() if len(self.statee.toPlainText()) == 0 or len(self.statee.toPlainText()) >= 2 else "State must be >2 characters")
        self.b1txtl.setText(self.b1txte.toPlainText() if len(self.b1txte.toPlainText()) == 0 or len(self.b1txte.toPlainText()) >= 2 else "B1 must be >2 characters")
        self.b2txtl.setText(self.b2txte.toPlainText() if len(self.b2txte.toPlainText()) == 0 or len(self.b2txte.toPlainText()) >= 2 else "B2 must be >2 characters")


    def load_presence(self):
        with open(os.path.join(current_dir, 'Database.json'), 'r') as db:
            data = json.load(db)
            presence_data = data[2]["PD"][0]
            self.limge.addItems(assets)
            self.simge.addItems(assets)
            self.limge.setCurrentIndex(assets.index(presence_data['limg']))
            self.simge.setCurrentIndex(assets.index(presence_data['simg']))
            self.ltxte.setText(presence_data['ltxt'])
            self.stxte.setText(presence_data['stxt'])
            self.detailse.setText(presence_data['details'])
            self.statee.setText(presence_data['state'])
            self.b1txte.setText(presence_data['b1txt'])
            self.b1urle.setText(presence_data['b1url'])
            self.b2txte.setText(presence_data['b2txt'])
            self.b2urle.setText(presence_data['b2url'])


    def save_presence(self):
        with open(os.path.join(current_dir, 'Database.json'), 'r+') as db:
            data = json.load(db)
            firstrun = data[0]
            asset = data[1]
            presence_data = data[2]
            other = data[3:]
            presence_data['PD'][0]['limg'] = str(self.limge.currentText())
            presence_data['PD'][0]['simg'] = str(self.simge.currentText())
            presence_data['PD'][0]['ltxt'] = self.ltxte.toPlainText()
            presence_data['PD'][0]['stxt'] = self.stxte.toPlainText()
            presence_data['PD'][0]['details'] = self.detailse.toPlainText()
            presence_data['PD'][0]['state'] = self.statee.toPlainText()
            presence_data['PD'][0]['b1txt'] = self.b1txte.toPlainText()
            presence_data['PD'][0]['b1url'] = self.b1urle.toPlainText()
            presence_data['PD'][0]['b2txt'] = self.b2txte.toPlainText()
            presence_data['PD'][0]['b2url'] = self.b2urle.toPlainText()
            ls = [firstrun, asset, presence_data, other[0], other[1]]
            db.seek(0)
            db.write(json.dumps(ls))
            db.truncate()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.ApplicationAttribute.AA_Use96Dpi)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
