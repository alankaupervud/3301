
import qrcode

b  = '104 116 116 112 115 58 47 47 103 111 111 46 115 117 47 67 85 111 77 55'
url = ''
for i in map(int, b.split()):
    url += chr(i)
print(url)


# пример данных

# имя конечного файла
filename = "site.png"
# генерируем qr-код
img = qrcode.make(url)
# сохраняем img в файл
img.save(filename)


