# -*- coding: utf-8 -*-
import mysql.connector
from datetime import datetime


# Bu sınıf MySQL sınıfına child olarak loglamaya yarar. Private bir sınıftır.
class _Log:
    def __init__(self, filename: str):
        self.__filename = open(filename, "a") # Filename dosya konumu olarak tanımlar. Or .../log.txt
        

    def plog(self, log) -> none:
        '''
        log: spesifik log yazısı
        '''
        date = f'[{datetime.now().year}-{datetime.now().month}-{datetime.now().day}  {datetime.now().hour}.{datetime.now().minute}.{datetime.now().second}]'  # Log yapılan tarihi string olarak tanımlar.
        self.__filename.write(date + " " + log + "\n")  # Dosyaya yazma kısımı

#  Bu sınıf sql'i daha kullanışlı yapıp loglama yapmaya yarıyor.
class MySQL(_Log):
    """
    DATABASE
    """

    def __init__(self, logfile, host, user, pw, db):
        # Log sınıfının super fonksiyonu
        super().__init__(filename=logfile)
        try:
            # Bağlanılacak database giriş bilgileri.
            self._DB = mysql.connector.connect(
                host=host,
                user=user,
                password=pw,
                database=db
            )
            self.__logfile.plog(f"{self.__filename}: Connected to {_DB}")
        except Exception:
            raise Exception("Did not connect creation with database")
        self.__logfile = Log(logfile)
        self.__filename = db
    # Database içinde istenilen sütunları içeren bir tablo oluşturur. İstenilen sütunlar liste türünde girilmelidir.
    def shape_table(self, paramarr: list, tablename: str) -> bool:
        """
        :param paramarr: Sütunların olduğu kısım
        :param tablename: Table'ın adı
        :return:
        """
        # Bu kısım sütun oluşturmaya yarar
        try:
            query = f"CREATE TABLE {tablename} ({', '.join(paramarr)})"
            cursor = self._DB.cursor()
            cursor.execute(query)

            self._DB.commit()
            self.__logfile.plog(f"{self.__filename}: Created table {tablename} with variables {paramarr}.")
            return True
        except Exception as err:
            self.__logfile.plog(f"{self.__filename}: Error: [{err}]")
             return False
            
    # Burada database içinde istenilen tabloya satır ekleniyor.
    # ISTENILEN SATIRI EKLEMEK ICIN TABLDOA BULUNAN SUTUN KADAR DEGER EKLNMEK ZORUNDA!
    # Geri dönen değer başarılı ve başarsız olarak bool değeri dönüyor.
    def append_line(self, paramarr: list, tablename: str) -> bool:
        """
        :rtype: object
        :param paramarr: bulunan table'a göre veri eklemeye yarar
        :param tablename: table isim
        :return:
        """
        # Bu kısım table'a yeni veriler eklemeye yarar
        try:
            query =f"INSERT INTO {tablename} VALUES ({', '.join(temp)})"
            cursor = self._DB.cursor()
            temp = [f"'{i}'" for i in paramarr]
            cursor.execute(query)
            self._DB.commit()
            self.__logfile.plog(f"{self.__filename}: Appended line to table '{tablename}' with variables {paramarr}.")
            return True
        except Exception as err:
            self.__logfile.plog(f"{self.__filename}: Error: [{err}]")
            return False
    
    # DATABASE  içinde bulunan istenile tablodaki tüm satır değerlerini alıyor.
    # her satır bir tane sözlüktür, her elemean satırdır. Her sözlükteki anahtar kelime sutünu ifade ediyor. Değeri ise sutundaki satır değerini ifade ediyor
    def get_table(self, tablename: str) -> list or bool:
        """
        :param tablename:
        :return: Liste şeklinde veriler dönecek
        """
        dict_result = []  # => [{}]
        # Bu kısım bulunan şablondaki tüm veriyi çeker
        try:
            query = f"SELECT * FROM {tablename}"
            cursor = self._DB.cursor()
            cursor.execute(query)
            LineInfo = cursor.fetchall()
            desc = cursor.description
            colnames = []
            for _ in desc:
                colnames.append(_[0])

            self._DB.commit()
            self.__logfile.plog(f"{self.__filename}: Requested table {tablename}.")

            for _ in LineInfo:
                dict_result.append(dict(zip(colnames, _)))

            return dict_result  # [{}]

        except Exception as err:
            self.__logfile.plog(f"{self.__filename}: Error: [{err}]")
            return False
    
    # Burda istenilen satırdaki istenilen değeri değiştirmeye yarayan işlemler yapılıyor.
    # Fonkisyon açıklamasındaki değerleri okuyunuz.
    def update_raw(self, tableName: str, valueThatChange: str, point: str, newValue: str, findBy: str) -> bool:
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
            query = f"UPDATE {tableName} SET {valueThatChange} = '{newValue}' WHERE {findBy} = '{point}'"
            cursor = self._DB.cursor()
            cursor.execute(query)
            self._DB.commit()
            self.__logfile.plog(f"{self.__filename}: Updated value {newValue}.")
            return True
        except Exception as err:
            self.__logfile.plog(f"{self.__filename}: Error: [{err}]")
            return False
    
    # DATABASE'deki isteline tabloyu siler.
    def delete_table(self, tablename: str) -> bool:
        """
        :param tablename:
        :return:
        """
        # Table'yi silmeye yarar
        try:
            query = f"DROP TABLE IF EXISTS {tablename}"
            cursor = self._DB.cursor(query)
            cursor.execute()
            self._DB.commit()
            self.__logfile.plog(f"{self.__filename}: Deleted table '{tablename}'.")
            return True
        except Exception as err:
            self.__logfile.plog(f"{self.__filename}: Error: [{err}]")
            return False
    
    # Istenilen tablodaki istenilen satırı silmeye yarar.
    def delete_row(self, tablename: str, colname: str, value: str) -> bool:
        """
        :param tablename:
        :param colname: hangi sütündan silineceği
        :return:
        """
        try:
            query = f"DELETE FROM {tablename} WHERE {colname}='{value}'"
            cursor = self._DB.cursor()
            cursor.execute(query)
            self._DB.commit()
            self.__logfile.plog(f"{self.__filename}: Deleted value from '{tablename}' value is '{colname}' = '{value}'.")
            return True
        except Exception as err:
            self.__logfile.plog(f"{self.__filename}: Error: [{err}]")
            return False
    
    # Tablo içindeki istenilen satır bilgisini alır ve geri döner. Liste türü.
    def get_specific_row(self, tablename, colname, colname2, value):
        """
        Colname istenilen sütündaki verdiğimiz id ve valueler kullanılarak satır döndürülecek sözlük şeklinde
        :param tablename:
        :param Id:
        :param value:
        :return:
        """

        # TODO: spesifik tablo alınacak
        try:
            # db.get_specific_row(tablename="users", colname="passwords", colname2="username", value="60562eb61e2bac4f17460fa0dad443d7e8db6e61ba98dbbb954872c4d7b34bb5")
            query = f"SELECT {colname} FROM {tablename} WHERE {colname2}='{value}'"
            cursor = self._DB.cursor()
            cursor.execute(query)
            data = cursor.fetchone()
            self.__logfile.plog(f"{self.__filename}: Get value from '{tablename}' value is '{colname2}' = '{value}'.")
            return data
        except Exception as err:
            self.__logfile.plog(f"{self.__filename}: Error: [{err}]")
            return False
            
    # TODO: Daha fazla fonksiyon eklenebilir.


if __name__ == '__main__':
    # Alacağınız hataları log dosyasına bakarak öğrenebilirsiniz.
    
    # Örnek sınıf tanımlama
    # xampp benzeri uygulamalar kullanarak serveri aktif hale getiriniz. Yoksa bağlantı gerçekleşemez.
    # var olan bir olan bir log dosyası olmak zorunda değildir. Oluşturulacaktır.
    print('Databaseye bağlanılıyor')
    db = MySQL(logfile="./log/log.txt", user="root", host="localhost", pw="", db="blog")
    print("Databaseye bağlandı")
    # Örnek Tablo oluşturma, paramarr sutunları ifade ediyor
    db.shape_table(paramarr=['id','isim','soyisim'], tablename='kullanicilar')
    
    # Tabloya veri ekleme 'kullanicilar' tablosuna. paramarr elemanları sutun sayısı kadar olmak zorunda
    db.append_line(tablename='kullanicilar', paramarr=['id1', 'sercam', 'demir'])
    print("veri eklendi")
    db.append_line(tablename='kullanicilar', paramarr=['id2', 'selehattin', 'akbulut'])
    print("bir veri daha eklendi")
    # Tablodaki verileri alma fonksiyonu 'kulanicilar tablosundan'
    # Geri dönüş değeri liste şeklindedir.
    print("Veriler alınıyor")
    data = db.get_table(tablename='kullanicilar')
    print(data)
    print("Veriler alındı")
    # Tablodaki veriyi güncelleme, örnein soyisimi değiştirelim.
    # ValueThatChange : değişecek sutunun isimidir.
    # NewValue : Sutunda bulunan değerimizin artık yeni değeridir. Mesela sercam  ise önceki değeri Artık selehattin diye değişecek gibi.
    # findBy : O satırı hangi sutundaki değere bakılarak bulacağını belirtiyor.
    # point : findBy sutunu içindeki isetnilen değeri ifade ediyor.
    print("Kullancı bilgisi değiştiriliyor")
    db.update_raw(tablename="kullanicilar", ValueThatChange="soyisim", NewValue="Demir", findBy="id", point="id1")
    print(db.get_table(tablename='kullanicilar'))
    print("Kullanıcı bilgisi değiştiriliyor")
    # Tablo içerisinde istenilen SUTUNUN içerisindeki değeri almaya yarar.
    # Tüm sutunları  almak yerine sadece bir tane sutunun içideki bir tane değeri alırız.
    # colname : istenilen sutunun içerisindeki istediğimiz değer.
    # colname2 : colname içidenki değeri bulmamaız için kesin olarak bildiğimiz bir sutunu kullanırız
    # value: colname2 içidneki eşsiz olan bir değerdir.
    # Burada 'id2' değerine sahip oan kullanıcı kişisinin ismini alırıyoruz.
    print("Özel bir sutun deği alındı")
    print(db.get_specific_row(tablename='kullanicilar', colname='isim', colname2='id', value='id2'))
    
    # Tablo içeisinde istenile değeri silmek için kulkanılır.
    # colname : bileln sutun referansı
    # value : sutunun bildiğimiz değeri
    # örneğin idsini bildiğimiz sercam kullanıcısını silelim
    print("Bir kullanıcı silindi")
    db.delete_row(tablename='kullanicilar', colname='id', value='id1')
    print(db.get_table(tablename='kullanicilar'))
    
    # İstediğimiz var olan tabloyu silemye yarar.
    print('"kullanicilar" tablosu sildindi')
    db.delete_table(tablename='kullanicilar')
    
    
    
    
    
    
    
    
    
    
