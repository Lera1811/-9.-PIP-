#Задача 2. Добавьте в бота игру «Угадай числа». Бот загадывает число от 1 до 1000. Когда игрок угадывает его, бот выводит количество сделанных ходов.

@bot.message_handler(commands=['start'])
def start(message: types.Message):
    rnumber = random.randint(1, 1000)
    bot.send_message(message.chat.id, 'Отгадайте число от 1 до 1000, у вас 5 попыток')
    bot.register_next_step_handler(message, get_number, 1, rnumber)


def get_number(message: types.Message, try_num: int, right_num: int):
    if message.text.isdigit():
        if right_num == int(message.text):
            bot.send_message(message.chat.id, 'Вы отгадали число!')
        else:
            if try_num >= 4:
                bot.send_message(message.chat.id, 'Мимо! Попытки кончились!')
                return

            if right_num < int(message.text):
                bot.send_message(message.chat.id, 'Загаданное число меньше введенного.')
            else:
                bot.send_message(message.chat.id, 'Загаданное число больше введенного.')
            bot.register_next_step_handler(message, get_number, try_num + 1, right_num)

    else:
        bot.send_message(message.chat.id, 'Вы ввели не число. Попробуйте еще раз.')
        bot.register_next_step_handler(message, get_number, try_num, right_num)