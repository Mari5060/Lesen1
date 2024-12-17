import json
import os
from PIL import Image, ImageFilter, ImageEnhance
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import*

def pil2pixmap(im):
    if im.mode == "RGB":
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
    elif  im.mode == "RGBA":
        r, g, b, a = im.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif im.mode == "L":
        im = im.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QImage(data, im.size[0], im.size[1], QImage.Format.Format_ARGB32)
    pixmap = QPixmap.fromImage(qim)
    return pixmap

app = QApplication([])
window = QWidget()
window.setWindowTitle("Ізі Фотошоп")
main_line = QHBoxLayout()
main_line_2 = QVBoxLayout()
main_line_3 = QVBoxLayout()
v2 = QHBoxLayout()
v3 = QHBoxLayout()
window_width, window_height = 800, 500
window.resize(window_width, window_height)
window.move(0,0)

btn_1 = QPushButton("Папка")
btn_2 = QPushButton("Збільшення різкості")
btn_3 = QPushButton("Ефект нерізкості")
btn_4 = QPushButton("Дзеркало")
btn_5 = QPushButton("Насиченість")
btn_6 = QPushButton("Ч/Б")
btn_7 = QPushButton("Контури")
btn_8 = QPushButton("Повернути")
btn_9 = QPushButton("Розмиття")
btn_10 = QPushButton("Покращення")
btn_11 = QPushButton("Тиснення")
list_1 = QListWidget()
list_2 = QLabel("Картинка")

main_line_3.addWidget(btn_1)
v2.addWidget(btn_2)
v2.addWidget(btn_3)
v2.addWidget(btn_4)
v3.addWidget(btn_5)
v2.addWidget(btn_7)
v3.addWidget(btn_8)
v3.addWidget(btn_9)
v3.addWidget(btn_10)
v3.addWidget(btn_11)
v2.addWidget(btn_6)
main_line_3.addWidget(list_1)
main_line_2.addWidget(list_2)

app.setStyleSheet("""
QPushButton:hover { 
    background-color : #5E7F97;
    color: 	#003153;
    
}

QPushButton { 
    background-color : #779ECB;
    color: 	#301934;
    
    
}
QListWidget{
    background-color : #93B4BE;
    color: 	#003153;
}
QLabel{
    background-color : #F0F8FF;
    color: 	#003153;
}
    """)

class ImageProcessor:
    def __init__(self):
        self.folder = None
        self.image = None
        self.filename = None

    def picture_load(self):
        image_path = os.path.join(self.folder, self.filename)
        self.image = Image.open(image_path)

    def image_show(self):
        pixel = pil2pixmap(self.image)
        list_2.setPixmap(pixel)

    def mirror_img(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.image_show()

    def fewgy(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.image_show()

    def lplpplpl(self):
        self.image = self.image.filter(ImageFilter.CONTOUR)
        self.image_show()

    def bw(self):
        self.image = self.image.convert("L")
        self.image_show()

    def dfdf(self):
        Imaggg, idj = QInputDialog.getText(window, "Налаштування різкості", "Введіть число різкості")

        self.image = ImageEnhance.Brightness(self.image).enhance(float(Imaggg))
        self.image_show()

    def tyty(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.image_show()

    def mimim(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.image_show()

    def nbnb(self):
        self.image = self.image.filter(ImageFilter.EDGE_ENHANCE)
        self.image_show()

    def oioio(self):
        self.image = self.image.filter(ImageFilter.EMBOSS)
        self.image_show()

    def lflsdlf(self):
        self.image = self.image.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
        self.image_show()



image_processor = ImageProcessor()


def open_directory():
    folder = QFileDialog.getExistingDirectory()
    image_processor.folder = folder
    files = os.listdir(folder)
    list_1.clear()
    for file in files:
        if file.endswith("png") or file.endswith("jpg") or file.endswith("jfif"):
            list_1.addItem(file)


def show_chosen_image():
    image_processor.filename = list_1.currentItem().text()
    image_processor.picture_load()
    image_processor.image_show()

list_1.currentRowChanged.connect(show_chosen_image)
btn_2.clicked.connect(image_processor.fewgy)
btn_4.clicked.connect(image_processor.mirror_img)
btn_7.clicked.connect(image_processor.lplpplpl)
btn_6.clicked.connect(image_processor.bw)
btn_5.clicked.connect(image_processor.dfdf)
btn_8.clicked.connect(image_processor.tyty)
btn_9.clicked.connect(image_processor.mimim)
btn_10.clicked.connect(image_processor.nbnb)
btn_11.clicked.connect(image_processor.oioio)
btn_3.clicked.connect(image_processor.lflsdlf)
btn_1.clicked.connect(open_directory)
main_line.addLayout(main_line_3)
main_line.addLayout(main_line_2)
main_line_2.addLayout(v2)
main_line_2.addLayout(v3)
window.setLayout(main_line)
window.show()
app.exec()