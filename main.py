import asyncio
import logging
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, executor, types, filters
from aiogram.types.message import ContentType
from aiogram.types import PreCheckoutQuery
import markups as nav
from db import DataBase
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor
import datetime
import time
import os
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
YOOTOKEN = os.getenv('YOOTOKEN')

logging.basicConfig(level=logging.INFO)

#Initialize bot
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
invite_links = {}

db = DataBase('/data/database.db')

class Form(StatesGroup):
    name = State() 
    age = State() 
    gender = State()
    why = State()

#Начальное меню
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
     user_id = message.from_user.id
     if not db.user_exists(user_id):
        username = message.from_user.username
        db.add_user(user_id, username)
        user = message.from_user
        name = user.first_name
        await message.answer(f"Здравствуйте, {name} 🌸\n\nЭто чат-бот Анны Марченко \nИнстаграм: (instagram.com/annamarchenko_psy)\nОсновной телеграм канал: (t.me/annamarchenko_psy)"
                             f"\n\nЧтобы получить доступ в закрытый канал с заданиями, выберите «Приобрести подписку», или напишите текстом", reply_markup = nav.mainMenu, parse_mode=ParseMode.MARKDOWN)
        await message.answer(f'Почему канал «Трансформация» - это хорошо для вас?:'
                             f'\n\n1. Каждодневные настраивающие техники для развития позитивного мышления'
                             f'\n2. Упражнения для развития осознанности, чтобы быть защищенными от любых манипуляций'
                             f'\n3. Тренировка эмоционального интеллекта для лучшего понимания себя и других'
                             f'\n4. Техники для ощущения опоры под собой, для уверенного поведения в разных жизненных ситуациях'
                             f'\n5. Упражнения для внутреннего спокойствия, чтобы быть в гармонии с собой'
                             f'\n\nВ чем секрет программы ❓'
                             f'\nКомплексный и разносторонний подход, накопительный эффект!'
                             f'\n\nПочему лучше зайти в чат на 6 месяцев❓❗️'
                             f'\nВ начале программы идет раскачка, ближе к 3-му месяцу будет происходить индивидуальная трансформация'
                             f'\nза счет работы с техниками личной терапии (которые каждый может делать самостоятельно и инкогнито),'
                             f'\nпридет внутренняя свобода, уверенность, станете смелее, проработаете прошлый опыт, не заходя в негативные воспоминания.'
                             f'\n\n📌 Стоимость до 31.10 — 2990 руб. в месяц.'
                             f'\nПри оплате на 6 месяцев - скидка')

#[МП]Об Анне
@dp.message_handler(filters.Text(equals="✨ Обо мне ✨"))
async def cmd_handler(message: types.Message):
    await message.answer(f"✨ Дипломированный психолог со стажем более 17 лет.\n\n"
                         f"✨ Закончила СПбГУ факультет психологии: работаю со страхами, тревогами, неопределенностью в жизни.\n\n"
                         f"✨ Использую краткосрочные методы терапии, что позволяет быстро и эффективно решить вопрос без миллионных сессий.\n\n"
                         f"✨ Регулярно принимаю участие в международных конференциях по работе с психическими травмами.\n"
                          "Супервизиях, связанных с темами абьюза, семейной терапии, стресса и эмоциональной нестабильности.\n\n"
                         f"✨ В своей работе использую комплексный подход, учитывая все индивидуальные особенности каждого, кто приходит ко мне за поддержкой.\n\n"
                         f"✨ Понимаю, насколько важно, живя в большом городе, не потерять себя, оставаться активными, спокойными и гармоничными.\n\n"
                         f"Именно поэтому для поддержки людей я создала данную программу 🙏\n\n")
    
#[МП]О закрытом канале
@dp.message_handler(filters.Text(equals="🙌 О закрытом канале 🙌"))
async def cmd_handler(message: types.Message):
    await message.answer(f"Программа для тех, кто:\n"
                         f"— хочет прокачать новые привычки и изменить старые\n"
                         f"— хочет стать спокойнее и гармоничнее\n"
                         f"— хочет стать улучшенной версией себя\n"
                         f"— хочет быть свободным, без ограничивающих убеждений и установок\n\n"
                         f"Я объединила все мировые психологические, духовные практики и знания, способные быстро помочь найти ответы и прийти в гармонию с собой 🙌\n\n"
                         f"Программа включает 1 прямой эфир в месяц.")


#[МП]Пробный период/Опросник [ППО]
#@dp.message_handler(filters.Text(equals="Пробный период"))
#async def cmd_start(message: types.Message):
#    user_id = message.from_user.id
#    if db.get_onetimepromo(user_id) == 1:
#        await message.answer("Извините, вы уже использовали пробный период.")
#    else:
#        await message.reply("Чтобы получить пробный период на 2 дня - необходимо пройти небольшой опрос-знакомство. Вы готовы?", reply_markup = nav.opros)

#[ППО]Не готов
#@dp.message_handler(filters.Text(equals="Нет, пока не готов(а)"))
#async def cmd_handler(message: types.Message):
#    await message.reply("Хорошо, возвращаю вас обратно!", reply_markup=nav.mainMenu)

#[ППО]Готов
#@dp.message_handler(filters.Text(equals="Да, готов(а)"))
#async def cmd_start(message: types.Message):
#    user_id = message.from_user.id
#    await Form.name.set()
#    markupsrem = types.ReplyKeyboardRemove()
#    await message.reply("Отлично! Как я могу к вам обращаться?", reply_markup=markupsrem)

#[ППО]Сколько лет?
#@dp.message_handler(state=Form.name)
#async def process_name(message: types.Message, state: FSMContext):
#    if not db.user_exists(message.from_user.id):
#     db.set_firstname(message.from_user.id, message.text)
#    async with state.proxy() as data:
#        data['firstname'] = message.text
#
#    await Form.next()
#    await message.reply("Сколько вам лет?")
#    markup = types.ReplyKeyboardRemove()

#[ППО]Возраст цифрами
#@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.age)
#async def process_age_invalid(message: types.Message):
#    return await message.reply("Напишите, пожалуйста, возраст цифрами")

#[ППО]Выбор пола
#@dp.message_handler(lambda message: message.text.isdigit(), state=Form.age)
#async def process_age(message: types.Message, state: FSMContext):
#    await Form.next()
#    await state.update_data(age=int(message.text))
#    if not db.user_exists(message.from_user.id):
#     db.set_ages(message.from_user.id, message.text)
#
#    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
#    markup.add("М", "Ж")
#
#    await message.reply("Укажите пол (кнопкой)", reply_markup=markup)

#[ППО]Отказ пол
#@dp.message_handler(lambda message: message.text not in ["М", "Ж"], state=Form.gender)
#async def process_gender_invalid(message: types.Message):
#    return await message.reply("Не знаю такой пол. Укажите, пожалуйста, пол кнопкой на клавиатуре")

#[ППО]Рассказ
#@dp.message_handler(state=Form.gender)
#async def process_gender(message: types.Message, state: FSMContext):
#    async with state.proxy() as data:
#        if(not db.user_exists(message.from_user.id)):
#         db.set_gender(message.from_user.id, message.text)
#        data['gender'] = message.text
#        markup = types.ReplyKeyboardRemove()
#
#    await Form.next()
#    markupsrem = types.ReplyKeyboardRemove()
#    await message.reply("Пожалуйста, расскажите: Что устраивает, а что хотелось бы изменить в своей жизни?", reply_markup=markupsrem)

#Генерирование пригласительной ссылки
async def create_invite_link(channel_id):
    member_count = await bot.get_chat_members_count(chat_id=channel_id)
    response = await bot.create_chat_invite_link(chat_id=channel_id, member_limit=member_count - 1)
    invite_link = response.invite_link
    return invite_link

#[ППО]Успешно + промо
#@dp.message_handler(state=Form.why)
#async def process_why(message: types.Message, state: FSMContext):
#    if(not db.user_exists(message.from_user.id)):
#     db.set_why(message.from_user.id, message.text)
#    async with state.proxy() as data:
#        data['why'] = message.text
#    invite_link = await create_invite_link(-1001870585668)
#    invite_links[invite_link] = 1
#    await message.reply("Опрос пройден. Большое спасибо за уделённое время! Вам выдана подписка на 2 дня", reply_markup=nav.mainMenu)
#    await message.answer(text=f"Ваша ссылка на закрытый канал:\n{invite_link}")
#    await asyncio.sleep(3)
#    await message.answer(text=f"Благодарю Вас, что решили попробовать принять участие! \n\nОбещаю, ПРИ УСЛОВИИ 😉 что Вы задержитесь хотя бы на 6 месяцев со мной, то: \nСтанете спокойнее, гармоничнее, более защищеннее от любых манипуляций. \n\nА если сформулируете свою задачу, то мы постараемся ее решить вместе!!! \n\nЯ буду постоянно Вас поддерживать на этом пути. \nВсе будет в легком и комфортном формате.")
#    user_id = message.from_user.id
#    expiry_date = datetime.datetime.now() + datetime.timedelta(days=2)
#    db.set_onetimepromo(user_id, 1)
#    db.set_promo(user_id)
#    db.set_is_paid(user_id, 1)
#    reminder_date = expiry_date - datetime.timedelta(days=1)
#    if datetime.datetime.now() >= reminder_date:
#            await bot.send_message(user_id, "Ваша подписка закончится через 24 часа!", reply_markup=nav.MySub2)
#
#    await state.finish()

#МОЯ ПОДПИСКА [МП]
@dp.message_handler(filters.Text(equals="Моя подписка"))
async def my_sub_handler(message: types.Message):
    user_id = message.from_user.id
    is_paid = db.get_is_paid(user_id)
    
    if is_paid == 1:
        user = message.from_user
        name = user.first_name
        await message.answer(f"Добро пожаловать в раздел 'Моя подписка', {name}!\n\n" "Что хотите сделать?", reply_markup=nav.MySub2)
    else:
        await message.answer("У вас нет активной подписки. Пожалуйста, оформите подписку, чтобы получить доступ к разделу 'Моя подписка'.")

@dp.message_handler(filters.Text(equals="На главную"))
async def cmd_handler(message: types.Message):
        if message.chat.type == 'private':
            await message.answer("Хорошо, возвращаю вас на главную", reply_markup=nav.mainMenu)
#[МП] Дата окончания подписки
@dp.message_handler(filters.Text(equals="Дата окончания подписки"))
async def my_sub_date_handler(message: types.Message):
    user_id = message.from_user.id
    expiry_date = db.get_expiry_date(user_id)
    if expiry_date is not None:
        expiry_date_formatted = str(expiry_date)[:-10]
        message = f"Дата окончания вашей подписки: \n<b>{expiry_date_formatted}</b>"
        await bot.send_message(user_id, message, parse_mode="HTML")

#[МП] Продлить подписку
@dp.message_handler(filters.Text(equals="Продлить подписку"))
async def cmd_handler(message: types.Message):
    await bot.send_message(message.from_user.id, "Выберите интересующий срок подписки", reply_markup = nav.sub_inline_markup)

#[ГМ]Связаться с Анной
@dp.message_handler(filters.Text(equals="Написать мне"))
async def cmd_handler(message: types.Message):
    await message.answer("Если у вас возникла какая-то ошибка или остались вопросы - вот мой телеграм:", reply_markup = nav.Anna_inline_markup)

#АДМИН-ПАНЕЛЬ [АП]
allowed_user_ids = [1009701651, 951854396, 711940612]

@dp.message_handler(filters.Text(equals="admin_panel"))
async def cmd_handler(message: types.Message):
        if message.chat.type == 'private':
           if message.from_user.id in allowed_user_ids:
            await message.answer("Здравствуйте, Анна\nКакое действие вы хотите выполнить?", reply_markup=nav.admin)

#[АП]Количество пользователей
@dp.message_handler(filters.Text(equals="Количество пользователей"))
async def cmd_handler(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id in allowed_user_ids:
            total_users = db.get_total_users()
            paid_users = db.get_is_paid(is_paid=1)
            non_paid_users = db.get_is_paid(is_paid=0)
            await message.answer(f"Общее число пользователей: {total_users}\n"
                                 f"Число оплативших пользователей: {len(paid_users)}\n"
                                 f"Число не оплативших пользователей: {len(non_paid_users)}")

#[АП]Рассылка меню
@dp.message_handler(filters.Text(equals="Рассылка"))
async def cmd_handler(message: types.Message):
        if message.chat.type == 'private':
           if message.from_user.id in allowed_user_ids:
            await message.answer("Выбрана кнопка 'Рассылка'\nПожалуйста, выберите базу пользователей", reply_markup=nav.Mailings)

@dp.message_handler(filters.Text(equals="Написать сообщение всем"))
async def cmd_handler(message: types.Message):
        if message.chat.type == 'private':
           if message.from_user.id in allowed_user_ids:
            await message.answer("Чтобы сделать рассылку для всех - напишите:\n/sendall ваш текст")

@dp.message_handler(filters.Text(equals="Написать сообщение оплатившим"))
async def cmd_handler(message: types.Message):
        if message.chat.type == 'private':
           if message.from_user.id in allowed_user_ids:
            await message.answer("Чтобы сделать рассылку только для оплативших - напишите:\n/sendpaid ваш текст")

@dp.message_handler(filters.Text(equals="Написать сообщение не оплатившим"))
async def cmd_handler(message: types.Message):
        if message.chat.type == 'private':
           if message.from_user.id in allowed_user_ids:
            await message.answer("Чтобы сделать рассылку только для не оплативших - напишите:\n/sendnonpaid ваш текст")

@dp.message_handler(filters.Text(equals="Назад"))
async def cmd_handler(message: types.Message):
        if message.chat.type == 'private':
           if message.from_user.id in allowed_user_ids:
            await message.answer("Хорошо, возвращаю вас назад", reply_markup=nav.admin)

#[Рассылка] по всем пользователям
@dp.message_handler(commands=['sendall'])
async def cmd_handler(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id in allowed_user_ids:
            text = message.text[9:]
            users = db.get_allusers()
            for row in users:
                try:
                    await bot.send_message(row, text)
                    if int(row[1]) == 1:
                         db.set_active(row, 1)
                except:
                    db.set_active(row, 0)
    await bot.send_message(message.from_user.id, "Успешная рассылка")

#[Рассылка] по оплатившим пользователям
@dp.message_handler(commands=['sendpaid'])
async def cmd_handler(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id in allowed_user_ids:
            text = message.text[10:]
            users = db.get_allusers()
            for row in users:
                try:
                    if db.get_is_paid(row):
                        await bot.send_message(row, text)
                        db.set_active(row, 1)
                except:
                    db.set_active(row, 0)
    await bot.send_message(message.from_user.id, "Успешная рассылка")

#[Рассылка] по не оплатившим пользователям
@dp.message_handler(commands=['sendnonpaid'])
async def cmd_handler(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id in allowed_user_ids:
            text = message.text[13:]
            users = db.get_allusers()
            for row in users:
                try:
                    if not db.get_is_paid(row):
                        await bot.send_message(row, text)
                        db.set_active(row, 1)
                except:
                    db.set_active(row, 0)
    await bot.send_message(message.from_user.id, "Успешная рассылка")

#[ГМ]Покупка подписки
@dp.message_handler()
async def bot_message(message:types.Message):
    if message.chat.type == "private":
        if message.text == "Приобрести подписку":
            await bot.send_message(message.from_user.id, "Выберите интересующий срок подписки", reply_markup = nav.sub_inline_markup)

#[Покупка] на 1 мес
@dp.callback_query_handler(text="submonth")
async def submonth(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_invoice(chat_id=call.from_user.id, title="Оформление подписки на 1 месяц",
        description="Чтобы приобрести подписку - нажмите кнопку и следуйте дальнейшим инструкциям", 
        payload="month_sub", 
        provider_token=YOOTOKEN, 
        currency="RUB", 
        start_parameter="test_bot", 
        prices=[{"label": "Руб", "amount": 299000}])

#Обработка оплат
@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_pay(message: types.Message):
    user_id = message.from_user.id
    expiry_date = datetime.datetime.now() + datetime.timedelta(days=30)
    if message.successful_payment.invoice_payload == "month_sub":
        invite_link = await create_invite_link(-1001870585668)
        invite_links[invite_link] = 1
        await message.reply("Покупка успешна! Вам выдана подписка на 1 месяц"
                            f"За 3 дня до окончания вам придет напоминание о продлении подписки, в случае, если этого не произойдет, доступ к каналу будет закрыт")
        await asyncio.sleep(3)
        await message.answer(text=f"Благодарю Вас, что решили попробовать принять участие! \n\nОбещаю, ПРИ УСЛОВИИ 😉 что Вы задержитесь хотя бы на 6 месяцев со мной, то: \nСтанете спокойнее, гармоничнее, более защищеннее от любых манипуляций. \n\nА если сформулируете свою задачу, то мы постараемся ее решить вместе!!! \n\nЯ буду постоянно Вас поддерживать на этом пути. \nВсе будет в легком и комфортном формате.")
        await message.answer(text=f"Ваша ссылка на закрытый канал:\n{invite_link}")
        if not db.user_exists_month(user_id):
            db.add_user_month(user_id)
            db.set_is_paid(message.from_user.id, 1)
            db.set_paid_month(user_id)
    if datetime.datetime.now() >= expiry_date:
        chat_id = 1001870585668
        await bot.kick_chat_member(chat_id, user_id)
    else:
        reminder_date = expiry_date - datetime.timedelta(days=3)
    if datetime.datetime.now() >= reminder_date:
        await bot.send_message(user_id, "Ваша подписка закончится через 3 дня!", reply_markup=nav.MySub2)

    elif message.successful_payment.invoice_payload == "6month_sub":
        invite_link = await create_invite_link(-1001870585668)
        invite_links[invite_link] = 1
        await message.reply("Оплата успешна! Вам выдана подписка на 6 месяцев"
                            f"За 3 дня до окончания вам придет напоминание о продлении подписки, в случае, если этого не произойдет, доступ к каналу будет закрыт")
        await asyncio.sleep(3)
        await message.answer(text=f"Благодарю Вас, что решили попробовать принять участие! \n\nОбещаю, ПРИ УСЛОВИИ 😉 что Вы задержитесь хотя бы на 6 месяцев со мной, то: \nСтанете спокойнее, гармоничнее, более защищеннее от любых манипуляций. \n\nА если сформулируете свою задачу, то мы постараемся ее решить вместе!!! \n\nЯ буду постоянно Вас поддерживать на этом пути. \nВсе будет в легком и комфортном формате.")
        await message.answer(text=f"Ваша ссылка на закрытый канал:\n{invite_link}")
        if not db.user_exists_sixmonth(user_id):
            db.add_user_sixmonth(user_id)
            db.set_is_paid(message.from_user.id, 1)
            db.set_paid_sixmonth(user_id)
    reminder_date = expiry_date - datetime.timedelta(days=3)
    if datetime.datetime.now() >= reminder_date:
        await bot.send_message(user_id, "Ваша подписка закончится через 3 дня!", reply_markup=nav.MySub2)

#[Покупка] на 6 мес
@dp.callback_query_handler(text="sub6month")
async def submonth(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_invoice(chat_id=call.from_user.id, title="Оформление подписки на 6 месяцев",
        description="Чтобы приобрести подписку - нажмите кнопку и следуйте дальнейшим инструкциям", 
        payload="6month_sub", 
        provider_token=YOOTOKEN, 
        currency="RUB", 
        start_parameter="test_bot", 
        prices=[{"label": "Руб", "amount": 1500000}])

@dp.pre_checkout_query_handler(state="*")
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

#Автоматическая проверка подписки    
async def check_subscription_expiry():
    current_date = datetime.datetime.now()
    users = db.get_allusers()
    for user_id in users:
        expiry_date = db.get_expiry_date(user_id)
        if expiry_date is not None and expiry_date < current_date:
                chat_id = 1001870585668
                await bot.kick_chat_member(chat_id, user_id)

async def run_check():
    while True:
        await check_subscription_expiry()
        await asyncio.sleep(48860)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(run_check())
    executor.start_polling(dp, skip_updates=True)