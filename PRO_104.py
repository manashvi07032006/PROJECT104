import cv2

img = cv2.imread("Solar_system.jpg")
cv2.imshow("SOLAR_SYS", img)

font = cv2.FONT_HERSHEY_PLAIN

image = cv2.putText(img, 'SOLAR SYSTEM', (480,40),  cv2.FONT_HERSHEY_TRIPLEX,  
                   1.5, (82,202,243), 2, cv2.LINE_AA) 

image = cv2.putText(img, 'Sun', (80,100),  cv2.FONT_HERSHEY_TRIPLEX,  
                   2, (30,30,255), 3, cv2.LINE_AA) 

image = cv2.putText(img, 'Mercury', (100,190),  font,  
                   1.4, (246,246,246), 1, cv2.LINE_AA) 

image = cv2.putText(img, 'Venus', (190,260),  font,  
                   1.4, (0,255,255), 1, cv2.LINE_AA) 

image = cv2.putText(img, 'Earth', (290,260),  font,  
                   1.4, (0,255,22), 1, cv2.LINE_AA) 

image = cv2.putText(img, 'Mars', (380,260),  font,  
                   1.4, (104,104,255), 1, cv2.LINE_AA) 

image = cv2.putText(img, 'Jupiter', (550,380),  font,  
                   1.4, (173,229,255), 1, cv2.LINE_AA) 

image = cv2.putText(img, 'Saturn', (750,300),  font,  
                   1.4, (76,184,255), 1, cv2.LINE_AA) 

image = cv2.putText(img, 'Uranus', (970,300),  font,  
                   1.4, (250, 234, 182), 1, cv2.LINE_AA) 

image = cv2.putText(img, 'Neptune', (1120,300),  font,  
                   1.4, (255, 0, 88), 1, cv2.LINE_AA)

cv2.imshow("OUTPUT", img)
cv2.imwrite("Solar_system_with_name.jpg", img)
cv2.waitKey(0)