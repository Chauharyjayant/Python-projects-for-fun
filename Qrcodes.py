#There is an awesome library called the qrcode which will be able to create qr codes with just some lines of code
import qrcode as qr

#using a function called make and then using save function of qrcode library to save the qrdcode image
img = qr.make("Hello here you can add any link any data which will be shown whenever the user will scan the Qr code")
img.save("Qrcode.png")

#you can also have some modification with qrcode to make the Qrcode more beautiful which you can read seperately i have not mentioned them here 