import qrcode,os

def generate_QR(code):
	qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=2,)
	qr.add_data(str(code))
	qr.make(fit=True)
	img=qr.make_image(fill_color="white", back_color="black")
	img.save(os.path.join(r"D:\Resolute AI\QRcode\savedQR",str(code)+".png"))
	print("QR Generated")



# def meter_code(mother_code,printer_signal):
def generate_code(mothercode,printer_signal="T"):
	default_meter_code="00000"
	increament=1

	while printer_signal!="F":
		printer_signal=input("Enter printer_signal: ")

		if printer_signal=="T":
			meter_code=default_meter_code[:-len(str(increament))]+str(increament)
			increament=increament+1

			print("Printer_Signal & metercode increased!!!")
			code=mothercode+meter_code
			print(f"code:{code}")
			generate_QR(code)

		if printer_signal=="None":
			print("printer_signal=False; break loop!!!")




def main(weldsem_signal="None",printer_signal="on"):
	default_mother_code="rai000000"
	weldsem_signal="F"
	increament=0

	while weldsem_signal!="E": 
		weldsem_signal=input("Enter weldsem_signal: ")
		
		if weldsem_signal=="T":
			increament+=1
			print("Weldsem_Signal & mothercode increased!!!")

		mother_code=default_mother_code[:-len(str(increament))]+str(increament)
		generate_code(mother_code,printer_signal="T")

#main()



# def meter_code(mother_code,printer_signal):
# def generate_code(mothercode,printer_signal="on"):#"T"):
# 	default_meter_code="00000"
# 	increament=1

# 	while printer_signal!="None":
# 		#printer_signal=input("Enter printer_signal: ")

# 		if printer_signal=="on":#"T":
# 			meter_code=default_meter_code[:-len(str(increament))]+str(increament)
# 			increament=increament+1

# 			print("Printer_Signal & metercode increased!!!")
# 			code=mothercode+meter_code
# 			print(f"code:{code}")

# 		if printer_signal=="None":
# 			print("printer_signal=False; break loop!!!")




# def main(weldsem_signal="None",printer_signal="None"):
# 	default_mother_code="rai000000"
# 	weldsem_signal="printer_signal"#"F"
# 	increament=0

# 	while weldsem_signal!="E": 
# 		#weldsem_signal=input("Enter weldsem_signal: ")
		
# 		if weldsem_signal=="on":#"T":
# 			increament+=1
# 			print("Weldsem_Signal & mothercode increased!!!")

# 		mother_code=default_mother_code[:-len(str(increament))]+str(increament)
# 		generate_code(mother_code,printer_signal="on")#"T")

#main()