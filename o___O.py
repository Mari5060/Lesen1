from PIL import Image
from PIL import ImageFilter
#with Image.open('img_1.png')as pic_original:
    #print('Зображення відкрито \nРозмір:', pic_original.size)
    #print('Формат:' , pic_original.format)
    #print('Режим:' , pic_original.mode)
    #pic_original.show()

print('1 = Розмити')
print('2 = Ч/Б')
print('3 = дізнатись інформацію про зображення')
print('4 = Виділити контук і робить зображення білим')
answer = input('Ваша дія?')
if answer == '1':
    with Image.open('img_1.png')as pic_original:
        pic_blured = pic_original.filter(ImageFilter.GaussianBlur(10))
        pic_blured.save('blured.jpg')
        pic_blured.show()
elif answer == '2':
    with Image.open('img_1.png') as pic_original:
        pic_gray = pic_original.convert('L')
        pic_gray.save('gray.jpg')
        pic_gray.show()
elif answer == '3':
    with Image.open('img_1.png')as pic_original:
        print('Зображення відкрито \nРозмір:', pic_original.size)
        print('Формат:' , pic_original.format)
        print('Режим:' , pic_original.mode)
        pic_original.show()
elif answer == '4':
    with Image.open('img_1.png')as pic_original:
        pic_contour = pic_original.filter(ImageFilter.CONTOUR)
        pic_contour.save('contour.jpg')
        pic_contour.show()









