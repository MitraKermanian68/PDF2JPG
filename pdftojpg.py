from pdf2image import convert_from_path



images = convert_from_path(r"C:\Users\User\Desktop\introduction of orientalism.pdf" ,poppler_path=r"C:\Users\User\Desktop\mitra11111\pdf to jpg\Release-23.11.0-0\poppler-23.11.0\Library\bin")

x=1
for image in images:
    image.save('output'+str(x)+'.jpg', 'JPEG')
    x+=1