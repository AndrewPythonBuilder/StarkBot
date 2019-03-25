import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, Contact, KeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
import constants
answers = True
otvet = False

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
updater = Updater(token=constants.token)
dispatcher = updater.dispatcher

def start(bot, update):
    global answers
    message = update.message
    bot.send_message(286077227, message.chat.id)
    if answers == True:
        buttons = [[InlineKeyboardButton('Хорошо', callback_data='Yes'), InlineKeyboardButton('Не хочу', callback_data='No')]]
        keyboard = InlineKeyboardMarkup(buttons)
        bot.send_message(message.chat.id, 'Дабы понять, что это именно ты, пройди, пожалуйста небольшой тестик)', reply_markup=keyboard)
    else:
        bottons = [['Посмотреть']]
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(message.chat.id, 'пока доступна всего одна кнопка, скоро будет обновление, прости', reply_markup=keyboard)

def answer_questions(bot, update):
    global otvet
    message = update.message
    if otvet == True:
        otvet = False
        if str(message.text).lower() == 'карима' or str(message.text).lower() == 'амина':
            buttons = [[InlineKeyboardButton('Не знаю', callback_data='0')],[InlineKeyboardButton('GitLab — сайт и система управления репозиториями кода для Git', callback_data='1')]]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.send_message(message.chat.id, 'Что такое git.lab', reply_markup=keyboard)
    elif message.text == 'Посмотреть':
        bot.send_message(message.chat.id, constants.stih)
    else:
        bot.send_message(286077227, message.text)


def botton(bot, update):
    global answers, otvet
    query = update.callback_query
    if query.message.text == 'Дабы понять, что это именно ты, пройди, пожалуйста небольшой тестик)':
        if str(query.data) == 'Yes':
            buttons = [[InlineKeyboardButton('9', callback_data='9'), InlineKeyboardButton('10', callback_data='10')]]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.send_message(query.message.chat.id, 'Найди корни уравнения y = x^2-18x+81',
                             reply_markup=keyboard)
        else:
            buttons = [[InlineKeyboardButton('9', callback_data='9'), InlineKeyboardButton('10', callback_data='10')]]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.send_message(query.message.chat.id, 'Ну ладно, тогда найди корни уравнения y = x^2-18x+81', reply_markup=keyboard)
    elif query.message.text == 'Ну ладно, тогда найди корни уравнения y = x^2-18x+81' or query.message.text == 'Найди корни уравнения y = x^2-18x+81':
        if str(query.data == '9'):
            buttons = [[InlineKeyboardButton('Imagine Dragons', callback_data='Imagine_Dragons'), InlineKeyboardButton('Coldplay', callback_data='Coldplay'),
                        InlineKeyboardButton('Ой, да не помню я', callback_data='We')]]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.send_message(query.message.chat.id, 'Выбери правильное название группы последней песни у тебя в ВК', reply_markup=keyboard)
        else:
            bot.send_message(query.message.chat.id, 'Ты уверена, что правильно посчитала? Проверь-ка)')
    elif query.message.text ==  'Выбери правильное название группы последней песни у тебя в ВК':
        if str(query.data) == 'Imagine_Dragons':
            buttons = [[InlineKeyboardButton('910', callback_data='910'), InlineKeyboardButton('911', callback_data='911'), InlineKeyboardButton('918', callback_data='918')],[InlineKeyboardButton('2411', callback_data='2411'),
                                                                                                                                                                           InlineKeyboardButton(
                                                                                                                                                                               '510',
                                                                                                                                                                               callback_data='510'), InlineKeyboardButton('701', callback_data='701')]]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.send_message(query.message.chat.id, 'Тебе даны какие-то числа, выбери оно из тех, которые тебе о чем-то говорят',
                             reply_markup=keyboard)
        else:
            bot.send_message(query.message.chat.id, 'Видимо что-то изменилась, но правильный ответ Imaginе Dragons. Нажми, пожалуйста, на эту кнопку')
    elif query.message.text == 'Тебе даны какие-то числа, выбери оно из тех, которые тебе о чем-то говорят':
        if str(query.data) == '910' or str(query.data) == '510' or str(query.data) == '2411':
            buttons = [[InlineKeyboardButton('Казань', callback_data='0'), InlineKeyboardButton('Питер', callback_data='1'), InlineKeyboardButton('Инно', callback_data='2')]]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.send_message(query.message.chat.id,
                             'Чисто интуитивно тыкни на город',
                             reply_markup=keyboard)
        else:
            bot.send_message(query.message.chat.id, 'Да, видимо я не предугадал это... \n Тогда давай попробуем так. Напиши одно из имен из твоих лицейских подруг')
            otvet = True

    elif query.message.text == 'Чисто интуитивно тыкни на город':
        if str(query.data) == '1':
            buttons = [
                [InlineKeyboardButton('iPhone8', callback_data='0'), InlineKeyboardButton('iPhoneXR', callback_data='1'),
                 InlineKeyboardButton('Браслет Pondora', callback_data='2')], [InlineKeyboardButton('ничего', callback_data='Tr')]]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.send_message(query.message.chat.id, 'Вот, если бы тебе молодой человек на 8 месяцев отношений дал выбор подарка, что бы ты выбрала?', reply_markup=keyboard)
        else:
            bot.send_message(query.message.chat.id,
                             'Да, видимо я не предугадал это... \n Тогда давай попробуем так. Напиши одно из имен из твоих лицейских подруг')
            otvet = True
    elif query.message.text == 'Вот, если бы тебе молодой человек на 8 месяцев отношений дал выбор подарка, что бы ты выбрала?':
        if str(query.data) == 'Tr':
            buttons = [[InlineKeyboardButton('Интересно', callback_data='0'),
                        InlineKeyboardButton('Нет', callback_data='1')]]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.send_message(query.message.chat.id,
                             'Скажи честно, тебе интересно?',
                             reply_markup=keyboard)
        else:
            bot.send_message(query.message.chat.id,
                             'Да, видимо я не предугадал это... \n Тогда давай попробуем так. Напиши одно из имен из твоих лицейских подруг')
            otvet = True
    elif query.message.text == 'Скажи честно, тебе интересно?':
        bot.send_message(286077227, 'Андрей, ты - уебок, блять ей не интересно. Реально, много времени занимает этот "тестик". ЕЕ ответ: ' + str(query.data))
        answers = False
        bottons = [['Посмотреть']]
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(query.message.chat.id, 'Прости, что отнял у тебя так много времени. Спасибо) \n Все то, что ты сможешь увидеть дальше.. прости.. Я люблю тебя', reply_markup=keyboard)
    elif query.message.text == 'Что такое git.lab':
        if str(query.data) == 'Не знаю':
            bot.send_message(query.message.chat.id, 'Честно, я тоже не знал, пока не загуглил')
            buttons = [
                [InlineKeyboardButton('Не знаю', callback_data='0'), InlineKeyboardButton('Благотворительность', callback_data='1')],[InlineKeyboardButton('Андрей, сначала надо заработать этот миллион, ну совсем замечтался', callback_data='2')]]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.send_message(query.message.chat.id, 'Что бы ты сделала, будь у тебя 1000000$', reply_markup=keyboard)
        else:
            bot.send_message(query.message.chat.id,'Ничоси ты умная. Честно, даже я не знал, пока не загуглил')
            bot.send_message(query.message.chat.id, 'Честно, я тоже не знал, пока не загуглил')
            buttons = [[InlineKeyboardButton('Не знаю', callback_data='0'),
                        InlineKeyboardButton('Благотворительность', callback_data='1')], [
                InlineKeyboardButton('Андрей, сначала надо заработать этот миллион, ну совсем замечтался',
                                     callback_data='2')]]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.send_message(query.message.chat.id, 'Что бы ты сделала, будь у тебя 1000000$', reply_markup=keyboard)
    elif query.message.text == 'Что бы ты сделала, будь у тебя 1000000$':
        buttons = [
            [InlineKeyboardButton('Интересно', callback_data='0'), InlineKeyboardButton('Нет', callback_data='1')]]
        keyboard = InlineKeyboardMarkup(buttons)
        bot.send_message(query.message.chat.id, 'Скажи честно, тебе интересно. Я надеюсь, это не тот, маршрут, который я не продумал, так как у меня на этом моменте закончилась фантазия. Знаю, можно было много придумать..', reply_markup=keyboard)

    elif query.message.text == 'Скажи честно, тебе интересно. Я надеюсь, это не тот, маршрут, который я не продумал, так как у меня на этом моменте закончилась фантазия. Знаю, можно было много придумать..':
        bot.send_message(286077227,
                         'Андрей, ты - уебок, блять ей не интересно. Она прошла не весь тестик. ЕЕ ответ: ' + str(
                             query.data))
        answers = False
        bottons = [['Посмотреть']]
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(query.message.chat.id,
                         'Прости, что отнял у тебя так много времени. Спасибо) \n Все то, что ты сможешь увидеть дальше.. прости.. Я люблю тебя',
                         reply_markup=keyboard)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(CallbackQueryHandler(botton))
answer_handler = MessageHandler(Filters.all, answer_questions)
dispatcher.add_handler(answer_handler)
updater.start_polling(timeout=5, clean=True )