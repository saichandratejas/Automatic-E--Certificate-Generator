import cv2
list_names =['Tejas','Arjun','Abhinav','Jack','Anirudh','Konda']

for index, name in enumerate(list_names):
	template =cv2.imread('C:\\Users\\user\\OneDrive\\Desktop\\Certificate Template neww.jpg')
	cv2.putText(template,name,(817,709),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,0),4)
	cv2.imwrite(r'C:\Users\user\OneDrive\Desktop\Generated-Certificates\ {}.jpg'.format(name.strip()),template)
	print('Processing Certificate {}/{}'.format(index+1,len(list_names)))
