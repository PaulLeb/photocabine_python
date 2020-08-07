import cv2
import numpy as np
import dropbox
import calendar
import time
import os

from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError

cap = cv2.VideoCapture(0)

dbx = dropbox.Dropbox("bfJ8RSMjhCAAAAAAAAAAAXeXyocfiMuce5TcNF1o0LdmII-Gc2qcLtt-2hHY-p3Y")

    # Check that the access token is valid
try:
    dbx.users_get_current_account()
except AuthError as err:
    sys.exit(
        "ERROR: Invalid access token; try re-generating an access token from the app console on the web.")


while(True):
    ret, frame = cap.read()

    cv2.imshow("frame", frame)

    key = cv2.waitKey(1)

    if key == ord('t'):
    #    cv2.imwrite('test.png',frame) 
        timestamp = calendar.timegm(time.gmtime())
        cv2.imwrite(filename=str(timestamp)+".jpg", img=frame)

        with open("./"+str(timestamp)+".jpg", 'rb') as f:
            try:
                dbx.files_upload(f.read(), "/"+str(timestamp)+".jpg", mode=WriteMode('overwrite'))
            except ApiError as err:
                print(err)
                sys.exit()
         
        os.remove("./"+str(timestamp)+".jpg")

    elif key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()