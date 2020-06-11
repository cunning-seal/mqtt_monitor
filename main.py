from  Device import Device
import datetime
if __name__ == '__main__':
    publisher = Device("1")
    subscriber = Device("123")

    device_list = []
    device_list.append(publisher)
    device_list.append(subscriber)

    try:
        for device in device_list:
            device.start()

        while True:
            x = input()
            if x == "q":
                break
            if x == "a":
                publisher.publish("/basic/1", str(datetime.datetime.now().time().strftime("%H:%M")))
            if x == "b":
                publisher.publish("/basic/2", str(datetime.datetime.now().time().strftime("%H:%M")))

        for device in device_list:
            device.finish()
    except KeyboardInterrupt:
        for device in device_list:
            device.finish()
