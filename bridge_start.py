import MQTTBridge
import sys

if __name__ == '__main__':
    args = sys.argv[1:]

    if len(args) >= 4:
        bridge = MQTTBridge.MQTTBridge(config_filename=args[2],
                                       id=args[3])
        try:
            bridge.start(host=args[0], port=int(args[1]))
            while True:
                x = input()
        except KeyboardInterrupt:
            bridge.finish()