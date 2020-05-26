import img2pdf
import os
import time


#pip3 install img2pdf

dirname = os.path.expanduser(os.curdir) #os.path.expanduser("~/Downloads/bot")

def pdfYap():
	fileTime = time.localtime()
	fileName = time.strftime("%Y%M%d%H%m%S.pdf", fileTime)
	with open(fileName,"wb") as f:
		imgs = []
		for fname in os.listdir(dirname):
			if not fname.endswith(".png"):
				continue
			path = os.path.join(dirname, fname)
			if os.path.isdir(path):
				continue
			imgs.append(path)
		f.write(img2pdf.convert(imgs))
	return fileName