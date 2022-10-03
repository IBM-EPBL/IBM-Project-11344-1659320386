import random

while(True):
    Val1 = random.randint(10, 99)
    Val2 = random.randint(10, 99)

    if(Val1 > 35 and Val2 > 60):
        print("High temperature and Humidity of : ", Val1, Val2, "=> Alarm is turned on!!!!")
    elif(Val1 < 35 and Val2 < 60):
        print("Normal temperature and Humidity of : ", Val1, Val2, "=> Alarm is turned off!!!!")
    break