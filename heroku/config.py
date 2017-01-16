import requests
import json
import time
from datetime import datetime, date
from telebot import types

APPID = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'  # openweathermap token
agunda_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
agunda_botan_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

u = b'\xE2\x98\x94'.decode('utf-8')
s = b'\xE2\x9B\x85'.decode('utf-8')
sc = b'\xE2\x98\x80'.decode('utf-8') + b'\xE2\x98\x81'.decode('utf-8')

mainmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
mainmenu.row('Мæн тыххай👼', 'Обо мне')
mainmenu.row(s + 'боныхъæд абон (погода сегодня)')
mainmenu.row(s + 'боныхъæд 5 боны (на 5 дней)')

weathertoday = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
weathertoday.row('Дзæуджыхъæу', 'Мæскуы')
weathertoday.row('Алагир', 'Цыкола', 'Ӕрыдон')
weathertoday.row('Чъреба', 'Дзау', 'Питер')
weathertoday.row('Беслæн', 'Джызæл', 'Мæздæг')
weathertoday.row('Кæрдзын', 'Змейкæ', 'Уозрек')
weathertoday.row('Мызур', 'Налцыкк', 'Тбилис')
weathertoday.row('Уæллаг Ларс', 'Зæрæмæг')
weathertoday.row('Уæл. Фыййагдон', 'Черменыхъæу')
weathertoday.row('Ростов-Доныл', 'Сочи')
weathertoday.row('фæстæмæ (назад)')

weatherforecast = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
weatherforecast.row('Дзæуджыхъæy', 'Мæскyы')
weatherforecast.row('Алагиp', 'Цыколa', 'Ӕрыдoн')
weatherforecast.row('Чъребa', 'Дзаy', 'Питеp')
weatherforecast.row('Беcлæн', 'ДЖызæл', 'Mæздæг')
weatherforecast.row('Кæpдзын', 'Змeйкæ', 'Уозрeк')
weatherforecast.row('Мызуp', 'Нaлцыкк', 'Тбилиc')
weatherforecast.row('Уæллаг Ларc', 'Зæpæмæг')
weatherforecast.row('Уæл. Фыййагдoн', 'Черменыхъæy')
weatherforecast.row('Ростов-Дoныл', 'Сoчи')
weatherforecast.row('фæстæмæ (назад)')

iron_description = ['Æгас цу, мæ ном хуыйны @Agunda_bot,ыз дын баххуыс кæндзæн ратæлмац кæнын уырыссаг ныхæстах',
                    ' ирон æвзагмæ,ирон ныхæстæ та уырыссагма, иннæ 5 бон цы боныхъæд уыдзан, уи базонын. ',
                    'Цæмæй менюмæ бахизай,уый тыххай ныффысс "меню" кæнæ та квадратыл наххац текст кам хъауы фыссын, уым.\n',
                    '"Æ"йы бæсты пайда кæн @\n',
                    'Кæд дам исты фарстатæ,уынаффæтæ ис, æви тæлмац хъæуы сраст кæнын,уæд ныффыссут ардам: @russik']
rus_description = ['Привет! Меня зовут @Agunda_bot. Я помогу тебе перевести слова с русского на осетинский и с осетинского на русский.',
                   ' Узнаю прогноз погоды на ближайшие 5 дней. ',
                   'Для перехода в меню напиши «меню» или нажми на квадратики в поле ввода текста.\n',
                   'Вместо «Æ» используй @.\n',
                   'Если у тебя есть какие-либо вопросы, предложения или правки к переводам — пиши сюда: @russsik1']
iron_description = iron_description[0] + iron_description[1] + iron_description[2] + iron_description[3] + iron_description[4]
rus_description = rus_description[0] + rus_description[1] + rus_description[2]+rus_description[3]+rus_description[4]

wtd = {'Дзæуджыхъæу': 473249,
       'Мæскуы': 524901,
       'Алагир': 802078,
       'Цыкола': 568184,
       'Ӕрыдон': 581179,
       'Чъреба': 611403,
       'Дзау': 614217,
       'Питер': 498817,
       'Беслæн': 576697,
       'Джызæл': 561437,
       'Мæздæг': 524736,
       'Кæрдзын': 552555,
       'Змейкæ': 462383,
       'Уозрек': 487871,
       'Мызур': 525990,
       'Налцыкк': 523523,
       'Тбилис': 611717,
       'Уæллаг Ларс': 614087,
       'Зæрæмæг': 799349,
       'Уæл. Фыййагдон': 475003,
       'Черменыхъæу': 569132,
       'Ростов-Доныл': 501175,
       'Сочи': 491422}

wfd = {'Дзæуджыхъæy': 473249,
       'Мæскyы': 524901,
       'Алагиp': 802078,
       'Цыколa': 568184,
       'Ӕрыдoн': 581179,
       'Чъребa': 611403,
       'Дзаy': 614217,
       'Питеp': 498817,
       'Беcлæн': 576697,
       'ДЖызæл': 561437,
       'Mæздæг': 524736,
       'Кæpдзын': 552555,
       'Змeйкæ': 462383,
       'Уозрeк': 487871,
       'Мызуp': 525990,
       'Нaлцыкк': 523523,
       'Тбилиc': 611717,
       'Уæллаг Ларc': 614087,
       'Зæpæмæг': 799349,
       'Уæл. Фыййагдoн': 475003,
       'Черменыхъæy': 569132,
       'Ростов-Дoныл': 501175,
       'Сoчи': 491422}

weather_desc = {'clear sky': [b'\xE2\x98\x80'.decode('utf-8'), b'\xF0\x9F\x8C\x8C'.decode('utf-8')],
                'few clouds': ['🌤', b'\xE2\x98\x81'.decode('utf-8')],
                'scattered clouds': [b'\xE2\x9B\x85'.decode('utf-8'), b'\xE2\x98\x81'.decode('utf-8')],
                'broken clouds': [b'\xE2\x98\x81'.decode('utf-8'), b'\xE2\x98\x81'.decode('utf-8')],
                'shower rain': ['🌧', '🌧'],
                'rain': ['🌦', '🌧'],
                'thunderstorm': ['⛈', '⛈'],
                'snow': ['🌨', '🌨'],
                'mist': ['🌫', '🌫'],
                'thunderstorm with light rain': ['⛈', '⛈'],
                'thunderstorm with rain': ['⛈', '⛈'],
                'thunderstorm with heavy rain': ['⛈', '⛈'],
                'light thunderstorm': ['⛈', '⛈'],
                'heavy thunderstorm': ['⛈', '⛈'],
                'ragged thunderstorm': ['⛈', '⛈'],
                'thunderstorm with light drizzle': ['⛈', '⛈'],
                'thunderstorm with drizzle': ['⛈', '⛈'],
                'thunderstorm with heavy drizzle': ['⛈', '⛈'],
                'light intensity drizzle': ['🌧', '🌧'],
                'drizzle': ['🌧', '🌧'],
                'heavy intensity drizzle': ['🌧', '🌧'],
                'light intensity drizzle rain': ['🌧', '🌧'],
                'drizzle rain': ['🌧', '🌧'],
                'heavy intensity drizzle rain': ['🌧', '🌧'],
                'shower rain and drizzle': ['🌧', '🌧'],
                'heavy shower rain and drizzle': ['🌧', '🌧'],
                'shower drizzle': ['🌧', '🌧'],
                'light rain': ['🌦', '🌧'],
                'moderate rain': ['🌦', '🌧'],
                'heavy intensity rain': ['🌦', '🌧'],
                'very heavy rain': ['🌦', '🌧'],
                'extreme rain': ['🌦', '🌧'],
                'freezing rain': ['🌨', '🌨'],
                'light intensity shower rain': ['🌧', '🌧'],
                'shower rain': ['🌧', '🌧'],
                'heavy intensity shower rain': ['🌧', '🌧'],
                'ragged shower rain': ['🌧', '🌧'],
                'light snow': ['🌨', '🌨'],
                'heavy snow': ['🌨', '🌨'],
                'sleet': ['🌨', '🌨'],
                'shower sleet': ['🌨', '🌨'],
                'light rain and snow': ['🌨', '🌨'],
                'rain and snow': ['🌨', '🌨'],
                'light shower snow': ['🌨', '🌨'],
                'shower snow': ['🌨', '🌨'],
                'heavy shower snow': ['🌨', '🌨'],
                'smoke': ['🌫', '🌫'],
                'haze': ['🌫', '🌫'],
                'sand, dust whirls': ['🌫', '🌫'],
                'fog': ['🌫', '🌫'],
                'sand': ['🌫', '🌫'],
                'dust': ['🌫', '🌫'],
                'volcanic ash': ['🌫', '🌫'],
                'squalls': ['🌫', '🌫'],
                'tornado': ['🌫', '🌫'],
                'overcast clouds': [b'\xE2\x98\x81'.decode('utf-8'), b'\xE2\x98\x81'.decode('utf-8')],
                'tornado': ['', ''],
                'tropical storm': ['', ''],
                'hurricane': ['', ''],
                'cold': ['', ''],
                'hot': ['', ''],
                'windy': ['', ''],
                'hail': ['', ''],
                'calm': ['', ''],
                'light breeze': ['', ''],
                'gentle breeze': ['', ''],
                'moderate breeze': ['', ''],
                'fresh breeze': ['', ''],
                'strong breeze': ['', ''],
                'high wind, near gale': ['', ''],
                'gale': ['', ''],
                'severe gale': ['', ''],
                'storm': ['', ''],
                'violent storm': ['', '']}

d = {0: '',
    1:'иу',
    2: 'дыууæ',
    3:'æртæ',
    4:'цыппар',
    5:'фондз',
    6:'æхсæз',
    7:'авд',
    8:'аст',
    9:'фараст',
    10: 'дæс',
    11: 'иуæндæс',
    12: 'дыууадæс',
    13: 'æртындæс',
    14: 'цыппæрдæс',
    15: 'фынддæс',
    16: 'æхсæрдæс',
    17: 'æвддæс',
    18: 'æстдæс',
    19: 'нудæс',
    20: ['дыууын', 'ссæдз'],
    30: ['æртын', 'дæсæмæссæдз'],
    40: ['цыппор', 'цыппур', 'дыууиссæдзы'],
    50: ['фæндзай', 'дæс æмæ дыууиссæдзы'],
    60: ['æхсай', 'æртиссæдзы'],
    70: ['æвдай', 'дæс æмæ æртиссæдзы'],
    80: ['æстай', 'цыппарыссæдзы'],
    90: ['нæуæдз', 'дæс æмæ цыппарыссæдзы'],
    100: 'сæдæ',
    1000: 'мин',
    1000000: 'миллион'}


def getCurrentWeather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?id='+str(request)+'&APPID='+APPID
    response = requests.get(url)
    return json.loads(response.content.decode('utf-8'))


def getFiveDaysWeather(request):
    url = 'http://api.openweathermap.org/data/2.5/forecast?id='+str(request)+'&APPID='+APPID
    response = requests.get(url)
    return json.loads(response.content.decode('utf-8'))


def dayofweek(u):
    days = {0: '<b>Къуырисæр(пн)</b>',
           1: '<b>Дыццæг(вт)</b>',
           2: '<b>Æртыццæг(ср)</b>',
           3: '<b>Цыппæрæм(чт)</b>',
           4: '<b>Майрæмбон(пт)</b>',
           5: '<b>Сабат(сб)</b>',
           6: '<b>Хуыцаубон(вс)</b>'}
    u = date(int(u[0:4]), int(u[5:7]), int(u[8:10])).weekday()
    return days[u]


def weatherForecastFun(b):
    s = ''
    d = weather_desc
    for i in range(len(b['list'])):
        if b['list'][i]['dt_txt'][11:13] == '12':
            s = s + dayofweek(b['list'][i]['dt_txt'])+', '+b['list'][i]['dt_txt'][8:10]+ '\n'
            s = s + 'Сихорафон'+b'\xF0\x9F\x8C\x9D'.decode('utf-8')+'🌡'+str(round(float(b['list'][i]['main']['temp'])-273.15, 1))+'°C\n'
            s = s + '🌥'+str(b['list'][i]['clouds']['all'])+'% '+d[b['list'][i]['weather'][0]['description']][0]+'\n'
        elif b['list'][i]['dt_txt'][11:13] == '18':
            s = s + 'Изæр'+b'\xF0\x9F\x8C\x9A'.decode('utf-8')+'🌡'+str(round(float(b['list'][i]['main']['temp'])-273.15, 1))+'°C\n'
            s = s + '🌥'+str(b['list'][i]['clouds']['all'])+'% '+d[b['list'][i]['weather'][0]['description']][0]+'\n'
        elif b['list'][i]['dt_txt'][11:13] == '03':
            s = s + 'Æхсæв'+b'\xF0\x9F\x8C\x9C'.decode('utf-8')+'🌡'+str(round(float(b['list'][i]['main']['temp'])-273.15, 1))+'°C\n'
            s = s + '🌥'+str(b['list'][i]['clouds']['all'])+'% '+d[b['list'][i]['weather'][0]['description']][1]+'\n'
            s = s + '***\n'
    return s


def weatherCurrentFun(b):
    d = weather_desc
    a = getCurrentWeather(b)
    sunrise = time.strftime("%H:%M:%S", time.gmtime(a['sys']['sunrise'] + 10800))
    sunset = time.strftime("%H:%M:%S", time.gmtime(a['sys']['sunset'] + 10800))

    def windDeg(degree):
        degree = degree['wind']['deg']
        if degree <= 22.5 or degree > 337.5:
            degree = b'\xE2\xAC\x86'.decode('utf-8')
        elif degree > 22.5 or degree <= 67.5:
            degree = b'\xE2\x86\x97'.decode('utf-8')
        elif degree > 67.5 or degree <= 112.5:
            degree = b'\xE2\x9E\xA1'.decode('utf-8')
        elif degree > 112.5 or degree <= 157.5:
            degree = b'\xE2\x86\x98'.decode('utf-8')
        elif degree > 157.5 or degree <= 202.5:
            degree = b'\xE2\xAC\x87'.decode('utf-8')
        elif degree > 202.5 or degree <= 247.5:
            degree = b'\xE2\x86\x99'.decode('utf-8')
        elif degree > 247.5 or degree <= 292.5:
            degree = b'\xE2\xAC\x85'.decode('utf-8')
        elif degree > 292.5 or degree <= 337.5:
            degree = b'\xE2\x86\x96'.decode('utf-8')
        return degree

    s = '<b>Сейчас</b>🌡' + str(round(float(a['main']['temp']) - 273.15, 1)) + '°C\n'
    s = s + 'Асæстад(облачн)🌥' + str(a['clouds']['all']) + '% , ' + d[a['weather'][0]['description']][0] + '\n'
    s = s + 'Уымæлад(влажность): ' + str(a['main']['humidity']) + '%\n'
    s = s + 'Дымгæ(ветер): ' + str(a['wind']['speed']) + 'м/с' + windDeg(a) + '\n'
    a = getFiveDaysWeather(b)
    for i in range((len(a['list']))):
        if str(datetime.today())[8:10] != a['list'][i]['dt_txt'][8:10]:
            break
        else:
            if a['list'][i]['dt_txt'][11:13] == '12':
                s = s + '<b>Сихорафон</b>' + b'\xF0\x9F\x8C\x9D'.decode('utf-8') + '🌡' + \
                    str(round(float(a['list'][i]['main']['temp']) - 273.15, 1)) + '°C\n'
                s = s + 'Асæстад🌥' + str(a['list'][i]['clouds']['all']) + '% ' + \
                    d[a['list'][i]['weather'][0]['description']][0] + '\n'
                s = s + 'Уымæлад: ' + str(a['list'][i]['main']['humidity']) + '%\n'
                s = s + 'Дымгæ: ' + str(a['list'][i]['wind']['speed']) + 'м/с' + windDeg(a['list'][i]) + '\n'
            elif a['list'][i]['dt_txt'][11:13] == '18':
                s = s + '<b>Изæр</b>' + b'\xF0\x9F\x8C\x9A'.decode('utf-8') + '🌡' + \
                    str(round(float(a['list'][i]['main']['temp']) - 273.15, 1)) + '°C\n'
                s = s + 'Асæстад🌥' + str(a['list'][i]['clouds']['all']) + '% ' + \
                    d[a['list'][i]['weather'][0]['description']][0] + '\n'
                s = s + 'Уымæлад: ' + str(a['list'][i]['main']['humidity']) + '%\n'
                s = s + 'Дымгæ: ' + str(a['list'][i]['wind']['speed']) + 'м/с' + windDeg(a['list'][i]) + '\n'
            elif a['list'][i + 2]['dt_txt'][11:13] == '03':
                s = s + '<b>Æхсæв</b>' + b'\xF0\x9F\x8C\x9C'.decode('utf-8') + '🌡' + \
                    str(round(float(a['list'][i + 2]['main']['temp']) - 273.15, 1)) + '°C\n'
                s = s + 'Асæстад🌥' + str(a['list'][i + 2]['clouds']['all']) + '% ' + \
                    d[a['list'][i + 2]['weather'][0]['description']][1] + '\n'
                s = s + 'Уымæлад: ' + str(a['list'][i + 2]['main']['humidity']) + '%\n'
                s = s + 'Дымгæ: ' + str(a['list'][i + 2]['wind']['speed']) + 'м/с' + windDeg(a['list'][i + 2]) + '\n'
    s = s + b'\xF0\x9F\x8C\x84'.decode('utf-8')+sunrise+' '+b'\xF0\x9F\x8C\x87'.decode('utf-8')+sunset
    return s


def digits(n):
    def tens(n):
        if int(n) in d:
            s = d[int(n)]
        else:
            s = d[int(n[:1]) * 10][0] + ' ' + d[int(n[1:2])]
        return s

    def zeroornot(n, m):
        if n == '0':
            s = ''
        else:
            s = d[int(n)] + ' ' + d[m] + ' '
        return s

    if len(str(int(n))) == 1:  # str(int(n)) защита от нуля в начале
        s = d[int(n)]
    elif len(str(int(n))) == 2:
        s = tens(n)
    elif len(str(int(n))) == 3:
        s = d[int(n[:1])] + ' ' + d[100] + ' ' + tens(n[1:3])
    elif len(str(int(n))) == 4:
        if n[:1] == '1':
            s = d[1000] + ' ' + zeroornot(n[1:2], 100) + tens(n[2:4])
        else:
            s = d[int(n[:1])] + ' ' + d[1000] + 'ы ' + zeroornot(n[1:2], 100) + tens(n[2:4])
    elif len(str(int(n))) == 5:
        if int(n[:2]) in d:
            s = d[int(n[:2])] + ' ' + d[1000] + 'ы ' + zeroornot(n[2:3], 100) + tens(n[3:5])
        else:
            s = tens(n[:2]) + ' ' + d[1000] + 'ы ' + zeroornot(n[2:3], 100) + tens(n[3:5])
    elif len(str(int(n))) == 6:
        s = d[int(n[:1])] + ' ' + d[100] + ' ' + tens(n[1:3]) + ' ' + d[1000] + 'ы '
        s = s + zeroornot(n[3:4], 100) + tens(n[4:6])
    return s



def getresponse(message):
    response = requests.get('https://saubakh.ml/db/%s' % message)
    sp = ''
    for i in (response.content.decode('utf-8')).split('_'):
        sp = sp + i + '\n'
    return sp

