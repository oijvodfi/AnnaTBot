from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

#Начальное меню
btnAbout = KeyboardButton("✨ Обо мне ✨")
btnAbout2 = KeyboardButton("🙌 О закрытом канале 🙌")
btnMysub = KeyboardButton("Моя подписка")
btnsubmonth = KeyboardButton("Приобрести подписку")
#btnPromo = KeyboardButton("Пробный период")
btncallAnna = KeyboardButton("Написать мне")
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.add(btnAbout)
mainMenu.add(btnAbout2)
mainMenu.row(btnMysub, btnsubmonth, btncallAnna)
#mainMenu.add(btnPromo)

sub_inline_markup = InlineKeyboardMarkup(row_width=1)

#Оплата
btnsubmonth = InlineKeyboardButton(text="1 месяц за 2990₽", callback_data="submonth")
btnsub6month = InlineKeyboardButton(text="6 месяцев за 15000₽ (-17%)", callback_data="sub6month")

sub_inline_markup.insert(btnsubmonth)
sub_inline_markup.insert(btnsub6month)

#АДМИН-ПАНЕЛЬ
btnUsers = KeyboardButton("Количество пользователей")
btnMailing = KeyboardButton("Рассылка")
btnToMain = KeyboardButton("На главную")
admin = ReplyKeyboardMarkup(resize_keyboard=True)
admin.add(btnMailing)
admin.row(btnUsers)
admin.add(btnToMain)

#АП-СПИСОК ПОЛЬЗОВАТЕЛЕЙ
btnUsersAll = KeyboardButton("Отобразить всех пользователей")
btnGoBack = KeyboardButton("Назад")
Users = ReplyKeyboardMarkup(resize_keyboard=True)
Users.add(btnUsersAll)
Users.row(btnGoBack)

#АП-РАССЫЛКА
btnAll = KeyboardButton("Написать сообщение всем")
btnPaid = KeyboardButton("Написать сообщение оплатившим")
btnNonPaid = KeyboardButton("Написать сообщение не оплатившим")
btnGoBack = KeyboardButton("Назад")
Mailings = ReplyKeyboardMarkup(resize_keyboard=True)
Mailings.add(btnAll)
Mailings.add(btnPaid)
Mailings.add(btnNonPaid)
Mailings.add(btnGoBack)

#Опросник
btnDa = KeyboardButton("Да, готов(а)")
btnNet = KeyboardButton("Нет, пока не готов(а)")

opros = ReplyKeyboardMarkup(resize_keyboard=True)
opros.add(btnDa)
opros.add(btnNet)

btnMale = KeyboardButton("Мужской")
btnFemale = KeyboardButton("Женский")

opros2 = ReplyKeyboardMarkup(resize_keyboard=True)
opros2.add(btnMale)
opros2.add(btnFemale)

#Моя подписка
btnExpiryDate = KeyboardButton("Дата окончания подписки")
btnRenew = KeyboardButton("Продлить подписку")
btnToMain = KeyboardButton("На главную")
MySub2 = ReplyKeyboardMarkup(resize_keyboard=True)
MySub2.add(btnExpiryDate)
MySub2.add(btnRenew)
MySub2.add(btnToMain)

#Кнопки для связи с Анной
btncallAnna = InlineKeyboardButton("Анна Марченко", url="https://t.me/anna_marchenko_psy")

Anna_inline_markup = InlineKeyboardMarkup().add(btncallAnna)
