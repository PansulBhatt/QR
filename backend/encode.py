import pyqrcode

qr = pyqrcode.create('https://www.linkedin.com/in/pansulbhatt',
	mode='binary')

qr.png('images/code.png', scale=6)

qr.show()
