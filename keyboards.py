from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from inc.config import OUTPUT_CHAT

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='💬 Открыть чат')
b2 = KeyboardButton(text='📖 Телефонная книга')
kb.add(b1).add(b2)

kb_chat = InlineKeyboardMarkup()
b1 = InlineKeyboardButton(text='💬 Чат', url=OUTPUT_CHAT)
kb_chat.add(b1)

kb_phonebook = ReplyKeyboardMarkup(resize_keyboard=True)
bp1 = KeyboardButton(text='Показать всех сотрудников')
bp2 = KeyboardButton(text='📄 Скачать EXEL')
bp3 = KeyboardButton(text='Ввести запрос')
bp4 = KeyboardButton(text='↪️ Назад')
kb_phonebook.add(bp1, bp2).add(bp3).add(bp4)

kb_phonebook_search = ReplyKeyboardMarkup(resize_keyboard=True)
bp3 = KeyboardButton(text='↪️ Назад')
kb_phonebook_search.add(bp3)

kb_request = ReplyKeyboardMarkup(resize_keyboard=True)
br1 = KeyboardButton(text='📝 Подать заявку')
# br2 = KeyboardButton(text='↪️ Назад')
# kb_request.add(br1).add(br2)
kb_request.add(br1)

admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
ap1 = KeyboardButton(text='Список заявок')
ap2 = KeyboardButton(text='Просмотреть заявку')
admin_panel.add(ap1).add(ap2)

ikb = InlineKeyboardMarkup(row_width=2)
ib2 = InlineKeyboardButton(text='Предыдущая', callback_data='phones.prev')
ib3 = InlineKeyboardButton(text='Следующая', callback_data='phones.next')
ikb.add(ib2, ib3)

ikb_request = InlineKeyboardMarkup(row_width=2)
ibr1 = InlineKeyboardButton(text='Назад', callback_data='page.prev')
ibr2 = InlineKeyboardButton(text='Вперед', callback_data='page.next')
ikb_request.add(ibr1, ibr2)

ra = ReplyKeyboardMarkup(resize_keyboard=True)
ra1 =  KeyboardButton(text='📝 Подать повторную заявку')
ra.add(ra1)