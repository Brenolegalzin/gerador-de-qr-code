import qrcode
import tkinter
screen = tkinter.Tk()
screen.title("gerador de qr code")
screen.geometry("500x500")
text1 = tkinter.Label(screen, text="quantidade de quadrados :")
text1.pack()
quadrados = tkinter.Entry(screen)
quadrados.pack()
text2 = tkinter.Label(screen, text="tamanho do qr code :")
text2.pack()
tamanho = tkinter.Entry(screen)
tamanho.pack()
text3 = tkinter.Label(screen, text="url :")
text3.pack()
url = tkinter.Entry(screen)
url.pack()
count = 0
def createQrCode():
	global count
	count += 1
	count = str(count)
	quantidade = int(quadrados.get())
	sizeOfCode = int(tamanho.get())
	link = url.get()
	code = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=sizeOfCode, border=sizeOfCode)
	imagem = code.make_image(fill_color="black",back_color="white")
	imagem.save("codigo"+count+".png")
	count = int(count)
button = tkinter.Button(screen, text="criar", command=createQrCode)
button.pack()
screen.mainloop()
