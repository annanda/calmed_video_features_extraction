def round_frametime(number):
    base = 0.04
    value = round(base * round((number / base)), 2)
    # value = round((number / base), 2)
    # if value == 0.0:
    #     value = 0
    return value


if __name__ == '__main__':
    print(round_frametime(1.8459999999999999))
    print(round_frametime(1.806))
    print(round_frametime(0.0))
    print(round_frametime(0.562))
    print(round_frametime(29.851999999999997))
    print(round_frametime(11.040000000000001))
