# MySQL Veritabanı İşlemleri

Bu kod örneği, Python programı aracılığıyla MySQL veritabanında çeşitli işlemleri gerçekleştirmeyi gösterir. Aşağıda kod örneği adım adım açıklanmıştır.

## Bağlantı Oluşturma

MySQL veritabanına bağlanmak için `MySQL` sınıfını kullanıyoruz. Bağlantı ayarları aşağıdaki gibi yapılmalıdır:

```python
db = MySQL(
logfile="./log/log.txt",
 user="root",
 host="localhost",
 pw="",
 db="blog")
```

 -**logfile**: Hataların kaydedileceği log dosyasının yolu.<br>
 -**user**: MySQL kullanıcı adı.<br>
 -**host**: MySQL sunucu adresi.<br>
 -**pw**: MySQL şifresi.<br>
 -**db**: Kullanılacak veritabanının adı.
## Tablo Oluşturma
Yeni bir tablo oluşturmak için **shape_table** yöntemini kullanırız. paramarr parametresi, tablo sütunlarını temsil eden bir liste içerir. Örneğin:

```python
db.shape_table(paramarr=['id', 'isim', 'soyisim'], tablename='kullanicilar')
```
Bu kod, **kullanicilar** adında bir tablo oluşturur ve *id*, *isim* ve *soyisim* sütunlarını içerir.

## Veri Ekleme
Tabloya veri eklemek için **append_line** yöntemini kullanırız. paramarr parametresi, sütunlara karşılık gelen veri değerlerini içeren bir listedir. Örneğin:

```python
db.append_line(tablename='kullanicilar', paramarr=['id1', 'Ahmet', 'Altın'])
```

Bu kod, **kullanicilar** tablosuna yeni bir satır ekler.

## Veri Alma
Tablodan veri almak için **get_table** yöntemini kullanırız. Bu yöntem, belirtilen tablodaki verileri bir liste olarak döndürür. Örneğin:

```python
data = db.get_table(tablename='kullanicilar')
print(data)
```
Bu kod, **kullanicilar** tablosundaki verileri alır ve ekrana yazdırır.

## Veri Güncelleme
Tablodaki verileri güncellemek için update_raw yöntemini kullanırız. Bu yöntem, belirli bir koşulu sağlayan satırlardaki verileri günceller. Örneğin:

```python
db.update_raw(tablename="kullanicilar", ValueThatChange="soyisim", NewValue="Demir", findBy="id", point="id1")
```
Bu kod, **kullanicilar** tablosunda *id* değeri *id1* olan satırların *soyisim* sütununu *Demir* olarak günceller.

## Veri Silme
Tablodan veri silmek için **delete_row** yöntemini kullanırız. Bu yöntem, belirli bir koşulu sağlayan satırları siler. Örneğin:

```python
db.delete_row(tablename='kullanicilar', colname='id', value='id1')
```
Bu kod, **kullanicilar** tablosunda *id* değeri *id1* olan satırları siler.

## Tablo Silme
Tabloyu silmek için **delete_table** yöntemini kullanırız. Örneğin:

```python
db.delete_table(tablename='kullanicilar')
```
Bu kod, **kullanicilar** tablosunu tamamen siler.
