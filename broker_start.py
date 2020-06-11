import Bridge

if __name__ == '__main__':
    bridge = Bridge.MQTTBridge("1488", "../test.txt")


    try:
        bridge.start()
        while True:
            x = input()
    except KeyboardInterrupt:
        bridge.finish()