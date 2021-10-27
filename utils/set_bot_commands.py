from aiogram import types


async def set_default_commands(dp):
   '''
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("start_sending", "start sending messages"),
            types.BotCommand("today_birthdays", "Who is birthday boy today?"),
            types.BotCommand("monthly_birthdays", "Who is birthday boy in this month?"),
            types.BotCommand('add_person', 'Add new person to list for this group'),
            types.BotCommand('update_person', 'Update information for person in this group'),
            types.BotCommand('remove_person', 'Remove person from list for this group'),
            types.BotCommand('add_person', 'Add new person to list for this group'),
        ]
    )
    '''
   await dp.bot.set_my_commands(
       [
           types.BotCommand("start_sending", "start sending messages"),


        ])
#types.BotCommand("monthly", 'birthday in this month')