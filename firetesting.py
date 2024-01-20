
# import cv2
# import numpy as np
# import smtplib
# import playsound
# import threading

# Alarm_Status = False
# Email_Status = False
# Fire_Reported = 0

# def play_alarm_sound_function():
# 	while True:
# 		playsound.playsound('alarm.wav',True)

# # def send_mail_function():

# #     recipientEmail = "reddyrrithwik@gmail.com"
# #     recipientEmail = recipientEmail.lower()

# #     try:
# #         server = smtplib.SMTP('smtp.gmail.com', 587)
# #         server.ehlo()
# #         server.starttls()
# #         server.login("rokkamrithwik@gmail.com", "#Rithwik27")
# #         server.sendmail('rokkamrithwik@gmail.com', recipientEmail, "Warning A Fire Accident has been reported on ABC Company")
# #         print("sent to {}".format(recipientEmail))
# #         server.close()
# #     except Exception as e:
# #     	print(e)


# video = cv2.VideoCapture("video.mp4") # If you want to use webcam use Index like 0,1.

# while True:
#     (grabbed, frame) = video.read()
#     if not grabbed:
#         break

#     frame = cv2.resize(frame, (960, 540))

#     blur = cv2.GaussianBlur(frame, (21, 21), 0)
#     hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

#     lower = [18, 50, 50]
#     upper = [35, 255, 255]
#     lower = np.array(lower, dtype="uint8")
#     upper = np.array(upper, dtype="uint8")

#     mask = cv2.inRange(hsv, lower, upper)

#     output = cv2.bitwise_and(frame, hsv, mask=mask)

#     no_red = cv2.countNonZero(mask)

#     if int(no_red) > 50:
#         Fire_Reported = Fire_Reported + 1

#     cv2.imshow("output", output)

#     if Fire_Reported >= 1:

#         if Alarm_Status == False:
#             threading.Thread(target=play_alarm_sound_function).start()
#             Alarm_Status = True

#         # if Email_Status == False:
#         #     threading.Thread(target=send_mail_function).start()
#         #     Email_Status = True


#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cv2.destroyAllWindows()
# video.release()


import cv2
import numpy as np
import pygame

Alarm_Status = False
Email_Status = False
Fire_Reported = 0

def play_alarm_sound_function():
    pygame.mixer.init()
    pygame.mixer.music.load('alarm.wav')
    pygame.mixer.music.play()

video = cv2.VideoCapture("video3.mp4")

while True:
    (grabbed, frame) = video.read()
    if not grabbed:
        break

    frame = cv2.resize(frame, (960, 540))

    blur = cv2.GaussianBlur(frame, (21, 21), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    lower = [18, 50, 50]
    upper = [35, 255, 255]
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    mask = cv2.inRange(hsv, lower, upper)

    output = cv2.bitwise_and(frame, hsv, mask=mask)

    no_red = cv2.countNonZero(mask)

    if int(no_red) > 1500:
        Fire_Reported = Fire_Reported + 1

    cv2.imshow("output", output)

    if Fire_Reported >= 1:

        if Alarm_Status == False:
            play_alarm_sound_function()
            Alarm_Status = True

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
video.release()
