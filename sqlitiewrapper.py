"""
Created By: ! Kontragerilla ღ ヅ#1019 and Ouburursel#4098
github ! Kontragerilla ღ ヅ#1019: https://github.com/FurkiYildirim
github Ouburursel#4098 :  https://github.com/darkmechanism
"""

from sqlite3 import connect
from datetime import datetime


class Log:
    def __init__(self, filename):
        self.__filename = open(filename, "a")

    def plog(self, log):
        date = f'[{datetime.now().year}-{datetime.now().month}-{datetime.now().day}  {datetime.now().hour}.{datetime.now().minute}.{datetime.now().second}]'
        self.__filename.write(date + " " + log + "\n")


class DbWrapper:
    def __init__(self, filename:str, log="log.txt"):
        self.__filename = filename
        self.__logfile = Log(log)

    def ShapeTable(self, paramarr: list, tablename:str) -> bool:
        """
        :param paramarr: Sütunların olduğu kısım
        :param tablename: Table'ın adı
        :return:
        """
        # Bu kısım sütun oluşturmaya yarar
        try:
            DbOverseer = connect(self.__filename)
            DbCursor = DbOverseer.cursor()
            DbCursor.execute(f"CREATE TABLE {tablename} ({', '.join(paramarr)})")
            DbOverseer.commit()
            DbOverseer.close()
            self.__logfile.plog(f"{self.__filename}: Created table {tablename} with variables {paramarr}.")
            return True
        except Exception as err:
            self.__logfile.plog(f"{self.__filename}: Error: [{err}]")
            return False

    def AppendLine(self, paramarr:list, tablename:str) -> bool:
        """

        :param paramarr: bulunan table'a göre veri eklemeye yarar
        :param tablename: table isim
        :return:
        """
        # Bu kısım table'a yeni veriler eklemeye yarar
        try:
            DbOverseer = connect(self.__filename)
            DbCursor = DbOverseer.cursor()
            temp = [f"'{i}'" for i in paramarr]
            DbCursor.execute(f"INSERT INTO {tablename} VALUES ({', '.join(temp)})")
            DbOverseer.commit()
            DbOverseer.close()
            self.__logfile.plog(f"{self.__filename}: Appended line to table '{tablename}' with variables {paramarr}.")
            return True
        except Exception as err:
            self.__logfile.plog(f"{self.__filename}: Error: [{err}]")
            return False
    def GetTable(self, tablename:str) -> list or bool:
        """

        :param tablename:
        :return: Liste şeklinde veriler dönecek
        """
        # Bu kısım bulunan şablondaki tüm veriyi çeker
        try:
            DbOverseer = connect(self.__filename)
            DbCursor = DbOverseer.cursor()
            DbCursor.execute(f"SELECT * FROM {tablename}")
            LineInfo = DbCursor.fetchall()
            DbOverseer.commit()
            DbOverseer.close()
            self.__logfile.plog(f"{self.__filename}: Requested table {tablename}.")
            return LineInfo
        except Exception as err:
            self.__logfile.plog(f"{self.__filename}: Error: [{err}]")
            return False
    def update_raw(self, tableName:str, valueThatChange:str, point:str, newValue:str, findBy:str) -> bool:
        """

        :param tableName:
        :param valueThatChange: Sütun ismi
        :param point: Neye göre bulunancağının beklenen değeri
        :param newValue: Yeni veririn ismi
        :param findBy: Neye göre bulunacağı
        :return:
        """
        # Bu kısım bi değeri değiştirmeye yarıyor
        try:
            DbOverseer = connect(self.__filename)
            DbCursor = DbOverseer.cursor()
            DbCursor.execute(f"UPDATE {tableName} SET {valueThatChange} = '{newValue}' WHERE {findBy} = '{point}'")
            DbOverseer.commit()
            DbOverseer.close()
            self.__logfile.plog(f"{self.__filename}: Updated value {newValue}.")
            return True
        except Exception as err:
            self.__logfile.plog(f"{self.__filename}: Error: [{err}]")
            return False
    def DeleteTable(self, tablename:str) -> bool:
        """

        :param tablename:
        :return:
        """
        # Table'yi silmeye yarar
        try:
            DbOverseer = connect(self.__filename)
            DbCursor = DbOverseer.cursor()
            DbCursor.execute(f"DROP TABLE IF EXISTS {tablename}")
            DbOverseer.commit()
            DbOverseer.close()
            self.__logfile.plog(f"{self.__filename}: Deleted table '{tablename}'.")
            return True
        except Exception as err:
            self.__logfile.plog(f"{self.__filename}: Error: [{err}]")
            return False

    def DeleteRow(self, tablename:str, Id:str, value:str) -> bool:
        """

        :param tablename:
        :param Id: hangi sütündan silineceği
        :return:
        """
        try:
            DbOverseer = connect(self.__filename)
            DbCursor = DbOverseer.cursor()
            DbCursor.execute(f"DELETE FROM {tablename} WHERE {Id}='{value}'")
            DbOverseer.commit()
            DbOverseer.close()
            self.__logfile.plog(f"{self.__filename}: Deleted value from '{tablename}' value is '{Id}' = '{value}'.")
            return True
        except Exception as err:
            self.__logfile.plog(f"{self.__filename}: Error: [{err}]")
            return False

