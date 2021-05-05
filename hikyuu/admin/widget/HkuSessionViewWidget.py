# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
import resource

from PyQt5 import QtWidgets, QtCore, QtGui

_translate = QtCore.QCoreApplication.translate


class HkuSessionViewWidget(QtWidgets.QDockWidget):
    def __init__(self, parent=None):
        super(HkuSessionViewWidget, self).__init__(parent)
        self.setObjectName("HKUServerViewWidget")
        self.tree = QtWidgets.QTreeWidget(self)
        self.setWidget(self.tree)
        #self.tree.header().setVisible(False)
        self.tree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.icons = [QtGui.QIcon(':/icon/server_16.png')]  # 记录每一级别的图标
        #item_0 = QtWidgets.QTreeWidgetItem(self.tree)
        #item_0.setIcon(0, QtGui.QIcon(':/icon/server_16.png'))
        #item_1 = QtWidgets.QTreeWidgetItem(item_0)
        #item_0 = QtWidgets.QTreeWidgetItem(self.tree)

        self.initContextMenu()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def initContextMenu(self):
        self.server_menu = QtWidgets.QMenu(self)
        self.server_menu.addAction(self.parent().action_dict['action_new_file_session'])
        self.server_menu.addAction(self.parent().action_dict['action_edit_file_session'])
        self.server_menu.addAction(self.parent().action_dict['action_del_file_session'])
        self.tree.customContextMenuRequested.connect(self.on_tree_customContextMenuRequested)

    def on_tree_customContextMenuRequested(self, pos):
        item = self.tree.itemAt(pos)
        if item:
            self.server_menu.exec(QtGui.QCursor.pos())

    def addSession(self, session):
        item = QtWidgets.QTreeWidgetItem(self.tree)
        item.setText(0, session.name)
        item.setIcon(0, self.icons[0])
        item.setData(0, QtCore.Qt.UserRole, session)
        if (session.name == "admin"):
            subitem = QtWidgets.QTreeWidgetItem(item)
            subitem.setText(0, _translate("HkuSessionViewWidget", "users"))
        else:
            account = _translate("HkuSessionViewWidget", "account")
            funds = _translate("HkuSessionViewWidget", "funds")
            orders = _translate("HkuSessionViewWidget", "orders")
            fillse = _translate("HkuSessionViewWidget", "fills")
            positons = _translate("HkuSessionViewWidget", "positions")
            names = ['account', 'funds', 'orders']

    def modifySession(self, item, session):
        item.setText(0, session.name)
        item.setData(0, QtCore.Qt.UserRole, session)

    def retranslateUi(self):
        self.tree.headerItem().setText(0, _translate("HkuSessionViewWidget", "name"))
        self.tree.headerItem().setText(1, _translate("HkuSessionViewWidget", "status"))
        __sortingEnabled = self.tree.isSortingEnabled()
        #self.tree.setSortingEnabled(False)
        #self.tree.topLevelItem(0).setText(0, _translate("HkuSessionViewWidget", "local"))
        #self.tree.topLevelItem(0).child(0).setText(0, _translate("HkuSessionViewWidget", "account"))
        #self.tree.topLevelItem(1).setText(0, _translate("HkuSessionViewWidget", "other"))
        self.tree.setSortingEnabled(__sortingEnabled)