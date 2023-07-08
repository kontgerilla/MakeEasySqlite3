### Alacağınız hataları log dosyasına bakarak öğrenebilirsiniz.
    
# Örnek sınıf tanımlama
## xampp benzeri uygulamalar kullanarak serveri aktif hale getiriniz. Yoksa bağlantı gerçekleşemez.
### var olan bir olan bir log dosyası olmak zorunda değildir. Oluşturulacaktır.
```print('Databaseye bağlanılıyor')```
```db = MySQL(logfile="./log/log.txt", user="root", host="localhost", pw="", db="blog")```
```print("Databaseye bağlandı")```
### Örnek Tablo oluşturma, paramarr sutunları ifade ediyor
db.shape_table(paramarr=['id','isim','soyisim'], tablename='kullanicilar')
    
# Tabloya veri ekleme 'kullanicilar' tablosuna. paramarr elemanları sutun sayısı kadar olmak zorunda
db.append_line(tablename='kullanicilar', paramarr=['id1', 'furkan', 'yıldırım'])
print("veri eklendi")
db.append_line(tablename='kullanicilar', paramarr=['id2', 'Metehan', 'Tüfek'])
print("bir veri daha eklendi")
# Tablodaki verileri alma fonksiyonu 'kulanicilar tablosundan'
# Geri dönüş değeri liste şeklindedir.
print("Veriler alınıyor")
data = db.get_table(tablename='kullanicilar')
print(data)
print("Veriler alındı")
# Tablodaki veriyi güncelleme, örnein soyisimi değiştirelim.
# ValueThatChange : değişecek sutunun isimidir.
# NewValue : Sutunda bulunan değerimizin artık yeni değeridir. Mesela Furkan ise önceki değeri Artık Mete diye değişecek gibi.
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
# örneğin idsini bildiğimiz furkan kullanıcısını silelim
print("Bir kullanıcı silindi")
db.delete_row(tablename='kullanicilar', colname='id', value='id1')
print(db.get_table(tablename='kullanicilar'))
    
# İstediğimiz var olan tabloyu silemye yarar.
print('"kullanicilar" tablosu sildindi')
db.delete_table(tablename='kullanicilar')
