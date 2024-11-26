from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtSql import  QSqlTableModel 
from tableModel import TableModel
import sys
from movieSql import *
from designDbConnect import Moviedb


class MainWindow(QMainWindow):

    
    def __init__(self):
        super(MainWindow, self).__init__()

        self.db = Moviedb()
        self.setupUi(self)

        self.btnAdd.clicked.connect(self.add_movie) 
        self.btnUpdate.clicked.connect(self.update_movie)
        self.btnDelete.clicked.connect(self.delete_movie)

        if not self.db.connection.is_connected():
            print("Database connection failed")
            return

        self.load_tables()
        self.comboBox.currentIndexChanged.connect(self.load_table_data)

        self.setFixedSize(770,555)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(779, 557)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(10, 230, 93, 28))
        self.btnAdd.setObjectName("btnAdd")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(150, 320, 471, 153))
        self.tableView.setObjectName("tableView")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(150, 280, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(250, 80, 221, 140))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayoutUpdate = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayoutUpdate.setContentsMargins(0, 0, 0, 0)
        self.formLayoutUpdate.setObjectName("formLayoutUpdate")
        self.lblMovieUpdate = QtWidgets.QLabel(self.layoutWidget)
        self.lblMovieUpdate.setObjectName("lblMovieUpdate")
        self.formLayoutUpdate.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblMovieUpdate)
        self.lineMovieUpdate = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineMovieUpdate.setObjectName("lineMovieUpdate")
        self.formLayoutUpdate.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineMovieUpdate)
        self.lblDateUpdate = QtWidgets.QLabel(self.layoutWidget)
        self.lblDateUpdate.setObjectName("lblDateUpdate")
        self.formLayoutUpdate.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblDateUpdate)
        self.lineDateUpdate = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineDateUpdate.setObjectName("lineDateUpdate")
        self.formLayoutUpdate.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineDateUpdate)
        self.lblActorsUpdate = QtWidgets.QLabel(self.layoutWidget)
        self.lblActorsUpdate.setObjectName("lblActorsUpdate")
        self.formLayoutUpdate.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblActorsUpdate)
        self.lineActorsUpdate = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineActorsUpdate.setObjectName("lineActorsUpdate")
        self.formLayoutUpdate.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineActorsUpdate)
        self.lblDirectorsUpdate = QtWidgets.QLabel(self.layoutWidget)
        self.lblDirectorsUpdate.setObjectName("lblDirectorsUpdate")
        self.formLayoutUpdate.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblDirectorsUpdate)
        self.lineDirectorsUpdate = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineDirectorsUpdate.setObjectName("lineDirectorsUpdate")
        self.formLayoutUpdate.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineDirectorsUpdate)
        self.lineGenreUpdate = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineGenreUpdate.setObjectName("lineGenreUpdate")
        self.formLayoutUpdate.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineGenreUpdate)
        self.lblGenreUpdate = QtWidgets.QLabel(self.layoutWidget)
        self.lblGenreUpdate.setObjectName("lblGenreUpdate")
        self.formLayoutUpdate.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblGenreUpdate)
        self.btnUpdate = QtWidgets.QPushButton(self.centralwidget)
        self.btnUpdate.setGeometry(QtCore.QRect(250, 230, 93, 28))
        self.btnUpdate.setObjectName("btnUpdate")
        self.btnDelete = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelete.setGeometry(QtCore.QRect(620, 80, 93, 28))
        self.btnDelete.setObjectName("btnDelete")
        self.lineIdDelete = QtWidgets.QLineEdit(self.centralwidget)
        self.lineIdDelete.setGeometry(QtCore.QRect(620, 40, 136, 22))
        self.lineIdDelete.setObjectName("lineIdDelete")
        self.lblUp = QtWidgets.QLabel(self.centralwidget)
        self.lblUp.setGeometry(QtCore.QRect(250, 10, 344, 21))
        self.lblUp.setObjectName("lblUp")
        self.lineIdUpdate = QtWidgets.QLineEdit(self.centralwidget)
        self.lineIdUpdate.setGeometry(QtCore.QRect(250, 40, 137, 22))
        self.lineIdUpdate.setObjectName("lineIdUpdate")
        self.lblAdd = QtWidgets.QLabel(self.centralwidget)
        self.lblAdd.setGeometry(QtCore.QRect(11, 11, 173, 21))
        self.lblAdd.setObjectName("lblAdd")
        self.lblDel = QtWidgets.QLabel(self.centralwidget)
        self.lblDel.setGeometry(QtCore.QRect(620, 10, 95, 21))
        self.lblDel.setObjectName("lblDel")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 80, 218, 140))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.formAdd = QtWidgets.QFormLayout(self.layoutWidget1)
        self.formAdd.setContentsMargins(0, 0, 0, 0)
        self.formAdd.setObjectName("formAdd")
        self.lblMovie = QtWidgets.QLabel(self.layoutWidget1)
        self.lblMovie.setObjectName("lblMovie")
        self.formAdd.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblMovie)
        self.lineMovieAdd = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineMovieAdd.setObjectName("lineMovieAdd")
        self.formAdd.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineMovieAdd)
        self.lblDate = QtWidgets.QLabel(self.layoutWidget1)
        self.lblDate.setObjectName("lblDate")
        self.formAdd.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblDate)
        self.lineDateAdd = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineDateAdd.setObjectName("lineDateAdd")
        self.formAdd.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineDateAdd)
        self.lblActors = QtWidgets.QLabel(self.layoutWidget1)
        self.lblActors.setObjectName("lblActors")
        self.formAdd.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblActors)
        self.lineActorsAdd = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineActorsAdd.setObjectName("lineActorsAdd")
        self.formAdd.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineActorsAdd)
        self.lblDirectors = QtWidgets.QLabel(self.layoutWidget1)
        self.lblDirectors.setObjectName("lblDirectors")
        self.formAdd.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblDirectors)
        self.lineDirectorsAdd = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineDirectorsAdd.setObjectName("lineDirectorsAdd")
        self.formAdd.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineDirectorsAdd)
        self.lblGenres = QtWidgets.QLabel(self.layoutWidget1)
        self.lblGenres.setObjectName("lblGenres")
        self.formAdd.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblGenres)
        self.lineGenreAdd = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineGenreAdd.setObjectName("lineGenreAdd")
        self.formAdd.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineGenreAdd)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 779, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DataBase App"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.lblMovieUpdate.setText(_translate("MainWindow", "movie name:"))
        self.lblDateUpdate.setText(_translate("MainWindow", "movie date:"))
        self.lblActorsUpdate.setText(_translate("MainWindow", "actors:"))
        self.lblDirectorsUpdate.setText(_translate("MainWindow", "directors:"))
        self.lblGenreUpdate.setText(_translate("MainWindow", "genres:"))
        self.btnUpdate.setText(_translate("MainWindow", "Update"))
        self.btnDelete.setText(_translate("MainWindow", "Delete "))
        self.lblUp.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Enter the ID of the movie you want to uptade:</span></p></body></html>"))
        self.lblAdd.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Add movie information:</span></p></body></html>"))
        self.lblDel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Delete by id:</span></p></body></html>"))
        self.lblMovie.setText(_translate("MainWindow", "movie name:"))
        self.lblDate.setText(_translate("MainWindow", "movie date:"))
        self.lblActors.setText(_translate("MainWindow", "actors:"))
        self.lblDirectors.setText(_translate("MainWindow", "directors:"))
        self.lblGenres.setText(_translate("MainWindow", "genres: "))

    def load_tables(self):
        cursor = self.db.get_cursor()
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()

        for table in tables:
            self.comboBox.addItem(table[0])

        cursor.close()

    def load_table_data(self,table_name=None):
        table_name = self.comboBox.currentText()
        cursor = self.db.get_cursor()
        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()
        headers = [i[0] for i in cursor.description]  

        model = TableModel(rows, headers)  
        self.tableView.setModel(model)  

        cursor.close()

    def closeEvent(self,event):
        self.db.close_connection()  
        table_name = self.comboBox.currentText()

        model = QSqlTableModel(self)
        model.setTable(table_name)
        model.select()

        self.tableView.setModel(model)

    def add_movie(self):
        movie_name = self.lineMovieAdd.text()
        movie_date = self.lineDateAdd.text()
        directors = self.lineDirectorsAdd.text().split(",")
        actors = self.lineActorsAdd.text().split(",")
        types = self.lineGenreAdd.text().split(",")

        
        movie_add_id = MoviesInfo.add_movie_info(movie_name, movie_date)

        for director in directors:
            director_add_id = MoviesInfo.add_Director(director)
        for actor in actors:
            actor_add_id = MoviesInfo.add_Actor(actor)
        for type in types:
            type_add_id = MoviesInfo.add_Movie_types(type)

        MoviesInfo.add_movie_director(movie_add_id, director_add_id)   
        MoviesInfo.add_movie_actor(movie_add_id, actor_add_id)
        MoviesInfo.add_movie_type_info(movie_add_id, type_add_id)

        self.lineMovieAdd.clear()
        self.lineDateAdd.clear()
        self.lineDirectorsAdd.clear()
        self.lineActorsAdd.clear()
        self.lineGenreAdd.clear()

        current_table = self.comboBox.currentText()
        self.load_table_data(current_table)

    def update_movie(self):
        
        id_up=int(self.lineIdUpdate.text())
        movie_name = self.lineMovieUpdate.text()
        movie_date = self.lineDateUpdate.text()
        directors = self.lineDirectorsUpdate.text().split(",")
        actors = self.lineActorsUpdate.text().split(",")
        types = self.lineGenreUpdate.text().split(",")

        MoviesUptade.update_movie_info(movie_name,movie_date,id_up)
        for director in directors:
            MoviesUptade.update_director(director,id_up)
        for actor in actors:
            MoviesUptade.update_actor(actor,id_up)
        for type in types:
            MoviesUptade.update_movie_types(type,id_up)

        self.lineIdUpdate.clear()
        self.lineMovieUpdate.clear()
        self.lineDateUpdate.clear()
        self.lineDirectorsUpdate.clear()
        self.lineActorsUpdate.clear()
        self.lineGenreUpdate.clear()

        current_table = self.comboBox.currentText()
        self.load_table_data(current_table)
      
    def delete_movie(self):

        id_del=int(self.lineIdDelete.text())

        MovieInfoDelete.delete_info(id_del)

        self.lineIdDelete.clear()

        current_table = self.comboBox.currentText()
        self.load_table_data(current_table)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()