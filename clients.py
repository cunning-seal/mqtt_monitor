from  Device import Device
import datetime
import random
import time
if __name__ == '__main__':
    publisher = Device("1")
    subscriber = Device("456")

    device_list = []
    device_list.append(publisher)
    device_list.append(subscriber)

    try:
        for device in device_list:
            device.start()
        # device_list[1].subscribe("basic/1")
        while True:
            time.sleep(0.3)
            publisher.publish("basic/2", random.randint(1,10))
            # str(datetime.datetime.now().time().strftime("%H:%M"))
            # if x == "a":
            #     publisher.publish("/basic/1", str(datetime.datetime.now().time().strftime("%H:%M")))
            # if x == "b":
            #     publisher.publish("/basic/2", str(datetime.datetime.now().time().strftime("%H:%M")))

        for device in device_list:
            device.finish()
    except KeyboardInterrupt:
        for device in device_list:
            device.finish()
