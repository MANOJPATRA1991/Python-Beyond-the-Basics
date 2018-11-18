def main():
    try:
        b'\x81'.decode('utf-8')
    except UnicodeError as e:
        print(e)
        print('encoding:', e.encoding)
        print('reason:', e.reason)
        print('object:', e.object)
        print('start:', e.start)
        print('end:', e.end)
        # encoding: utf - 8
        # reason: invalid
        # start
        # byte
        # object: b'\x81'
        # start: 0
        # end: 1


if __name__ == '__main__':
    main()