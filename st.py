def setting():
    _s = '''[PW]
password:None_'''

    while True:
        try:
            global _setting
            _setting = open('setting.ini', 'r', encoding='utf-8')
            break
        except FileNotFoundError:
            _setting = open('setting.ini', 'w', encoding='utf-8')
            _setting.write(_s)
            _setting.close()

    _txt = _setting.read()
    return _txt


if __name__ == '__main__':
    print(setting())
