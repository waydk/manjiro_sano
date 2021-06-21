from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

admin_callback = CallbackData('act', 'name')

main_markup = InlineKeyboardMarkup(row_width=2)
admin_info = InlineKeyboardButton(text='admin', callback_data=admin_callback.new("show_info"))
main_markup.insert(admin_info)
