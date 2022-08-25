from datetime import datetime as dt


def timer(data = 0):
    time = dt.now().strftime('%H:%M:%S')
    with open('loggirovanie.csv', 'a') as file:
        file.write('{};{}\n'
                   .format(time, data))

