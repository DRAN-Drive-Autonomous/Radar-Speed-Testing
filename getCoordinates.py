import cv2

startY = 803
startX = 0
img = cv2.imread("./temp.png")
img = img[startY:, startX:]
image = img.copy()
cv2.imshow("Mouse Handler Image", image)
def mouse_click(event, x, y, 
                flags, param):
      
    # to check if left mouse 
    # button was clicked
    if event == cv2.EVENT_LBUTTONDOWN:
          
        # font for left click event
        font = cv2.FONT_HERSHEY_TRIPLEX
        tempx = startX + x
        tempy = startY + y
        LB = f'({tempx}, {tempy})'
        print(LB)
          
        # display that left button 
        # was clicked.
        cv2.putText(image, LB, (x, y), 
                    font, 0.7, 
                    (255, 0, 0), 
                    1) 
        cv2.imshow("Mouse Handler Image", image)
        
cv2.setMouseCallback("Mouse Handler Image", mouse_click)
   
cv2.waitKey()
cv2.imwrite("./result.png", image)
  
# close all the opened windows.
cv2.destroyAllWindows()