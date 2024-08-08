from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import BoundFilter
from inc.config import LIST_ADMIN_ID

class IsAdmin(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin):
        self.is_admin = is_admin

    async def check(self, message):
        return str(message.from_user.id) in LIST_ADMIN_ID

page_data_requests = 0
page_data_contacts = 0

page_data_requests = 0
page_data_contacts = 0

def create_pagination_keyboard(page, pages, prefix):
    ikb = InlineKeyboardMarkup(row_width=3)
    if page > 0:
        ikb.add(InlineKeyboardButton(text='Предыдущая', callback_data=f'{prefix}.prev'))
    ikb.add(InlineKeyboardButton(text=f'{page + 1}/{pages}', callback_data=f'{prefix}.page_info'))
    if page < pages - 1:
        ikb.add(InlineKeyboardButton(text='Следующая', callback_data=f'{prefix}.next'))
    return ikb

async def handle_pagination(call, page, pages, get_page_data_func, prefix):
    if call.data == f"{prefix}.next" and page < pages - 1:
        page += 1
    elif call.data == f"{prefix}.prev" and page > 0:
        page -= 1
    ikb = create_pagination_keyboard(page, pages, prefix)
    await call.message.edit_text(text="\n".join(get_page_data_func()[page]), reply_markup=ikb)
    return page

async def call_data_process(call: types.CallbackQuery, getpagerequests, get_list_contact, getpagephones):
    global page_data_requests, page_data_contacts
    if (prefix := call.data.split('.')[0]) == 'requests':
        requests = getpagerequests()
        pages_data = len(requests)
        page_data_requests = await handle_pagination(call, page_data_requests, pages_data, lambda: requests, 'requests')
    elif prefix == 'phones':
        contacts = get_list_contact()[1]
        pages = (len(contacts) + 9) // 10
        page_data_contacts = await handle_pagination(call, page_data_contacts, pages, getpagephones, 'phones')
