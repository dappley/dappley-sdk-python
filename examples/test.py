from dappleyPython.Dappley import Dappley


def send_transaction_test():
    c = Dappley("127.0.0.1", "50051")
    data = c.send_transaction("dVZhMRtH8fvVTU6Dy9KDLCozDKcgQYyH4H", "ch93EdQb9aCpiyyH5ANv4VAPC8vuJPtLi1", 1,
                              "77ac1b16314d62c839c3b955e194cffc3fe212fb381b0d265889accaba6f43db", 1, 30000, 1,
                              '{"function":"put_sensor_sign","args":["sensor-04","hash-04"]}')
    print (data)


if __name__ == '__main__':
    send_transaction_test()