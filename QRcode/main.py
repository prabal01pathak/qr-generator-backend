import qrcode,os

def generate_QR(code):
	qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=2,)
	qr.add_data(str(code))
	qr.make(fit=True)
	img=qr.make_image(fill_color="white", back_color="black")
	img.save(os.path.join(r"D:\Resolute AI\QRcode\savedQR",str(code)+".png"))
	print("QR Generated")



def generate_metercode(mothercode,printer_signal="T"):
	#global metercode
	metercode="00001"
	met_code=0
	while printer_signal=="T":
		printer_signal=input("Enter printer_signal: ")
		
		if printer_signal=="T":
			metercode=metercode[:-len(str(met_code))]+str(met_code)
			met_code=met_code+1
			print("Printer_Signal & metercode increased!!!")

		code=mothercode+metercode
		print(f"code:{code}")
		generate_QR(code)

		


##############
# Driver Code
##############

met_code=1
mothercode="rai000000"
weldsem_signal="F"
m_code=0

while weldsem_signal!="E": 
	weldsem_signal=input("Enter weldsem_signal: ")
	
	if weldsem_signal=="T":
		m_code+=1
		print("Weldsem_Signal & mothercode increased!!!")

	mothercode_=mothercode[:-len(str(m_code))]+str(m_code)
	generate_metercode(mothercode_,printer_signal="T")
	






