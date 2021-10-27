from data.config import BIRTHDAYS_FILE, CHAT_ID
from datetime import datetime
import datetime as dt
from loader import bot
from time import sleep

SENT_TODAY = False

def parse_file():
    birthday_data = dict()

    for line in open(BIRTHDAYS_FILE).read().split('\n'):
        line = line.split(' ')

        if line[0] == '': # end of file
            break


        name = line[0]
        second_name = line[1]

        date_of_birth = datetime.strptime(line[2], "%d:%m:%Y")
        sex = line[3]
        ret = [date_of_birth, sex]
        full_name = name + ' ' + second_name

        birthday_data.update({full_name: ret})

    return birthday_data


def check_date_return_age(date: datetime.date):
    now = datetime.now()
    if now.day == date.day and now.month == date.month:
        return True, now.year - date.year
    return False, 0


def check_dates_for_all(names_dates: dict):
    """
    names_dates: {name_surname : [date_of_birth, sex]}
    res: bool
    age: int
    el: string {name_second-name}
    """
    birthdays = []
    for el in names_dates.keys():
        res, age = check_date_return_age(names_dates[el][0])
        if res:
            birthdays.append([el, age])

    return birthdays


def create_message_once(name, age):
    message = 'А сегодня день рождения отмечает {0}. С днюхой!'.format(name)
    return message


def create_message_month(names_dates: list):
    """
    names_dates = ['name' datetime.date_of_birthday]
    """
    res = "Именинники ближайщего месяца: \n"
    for el in names_dates:
        res += el[0] + ' ' + el[1].day + '.' + el[1].month + '\n'

    return  res


async def send_message_to_chat(message, chat_id=CHAT_ID):
    print("GG", message)
    await bot.send_message(chat_id=chat_id, text=message)
    print("WTF???")


def check_date_monthly(names_dates: dict):
    now_date = datetime.now() + dt.timedelta(days=30)
    res = []
    for el in names_dates.keys():
        if now_date > names_dates[el][0]:
            res.append([el, names_dates[el][0]])
    return res


async def main_process():
    global SENT_TODAY
    #print("HERE")
    print("YES", SENT_TODAY)
    names_dates = parse_file()
    SENT_TODAY = False
    while True:
        if 0 < datetime.now().hour < 2:
            SENT_TODAY = False

        if not SENT_TODAY:
            SENT_TODAY = True
            birthdays = check_dates_for_all(names_dates)
            print(birthdays)
            for el in birthdays:
                print("SENDIG???")
                await send_message_to_chat(create_message_once(el[0], el[1]))

        sleep(7200)


async def send_month_message():
    names_dates = parse_file()
    in_this_month = check_date_monthly(names_dates)
    message = create_message_month(in_this_month)
    await send_message_to_chat(message)


