from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

admin_callback = CallbackData('act', 'name')
help_callback = CallbackData('act', 'name')
close_callback = CallbackData("act", "name")

main_markup = InlineKeyboardMarkup(row_width=2)
help_info = InlineKeyboardButton(text='Help', callback_data=help_callback.new(name="show_info"))
source_code = InlineKeyboardButton(text='Source code', url='https://github.com/waydk/manjiro_sano')
author_channel = InlineKeyboardButton(text='Author', url='https://t.me/waydkch')
add_group = InlineKeyboardButton(text='Add Mikey to your group', url='https://t.me/manjiro_sano_robot?startgroup=new')
main_markup.insert(help_info)
main_markup.insert(author_channel)
main_markup.insert(source_code)
main_markup.insert(add_group)

help_markup = InlineKeyboardMarkup(row_width=3)
anime_button = InlineKeyboardButton(text='Anime', callback_data=admin_callback.new(name="anime_info"))
anti_flood_button = InlineKeyboardButton(text='Anti-Flood', callback_data=admin_callback.new(name="antiflood_info"))
fun_button = InlineKeyboardButton(text='Fun', callback_data=admin_callback.new(name="fan_info"))
service_button = InlineKeyboardButton(text='Service-Messages', callback_data=help_callback.new(name="service"))
help_markup.insert(anime_button)
help_markup.insert(anti_flood_button)
help_markup.insert(fun_button)
help_markup.insert(service_button)

back_keyboard = InlineKeyboardMarkup()
back_button = InlineKeyboardButton(text='back', callback_data=help_callback.new(name='back'))
back_keyboard.insert(back_button)

back_keyboard_start = InlineKeyboardMarkup()
back_button_start = InlineKeyboardButton(text='back', callback_data=help_callback.new(name='back_start'))
back_keyboard_start.insert(back_button_start)
