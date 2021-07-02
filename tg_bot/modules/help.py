from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from tg_bot.utils.keyboards.main_keyboard import help_markup, back_keyboard, main_markup


async def command_help(message: types.Message):
    if message.chat.type == 'supergroup':
        username = await message.bot.get_me()
        await message.answer_photo(
            "You can see the commands in the bot",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(text="Help", url=f"t.me/{username['username']}?start=help")
                    ]
                ])
        )
    else:
        await message.answer_photo(photo='https://i2.wp.com/duniamasa.com/wp-content'
                                         '/uploads/2021/04/mikey.jpg?resize=1200%2C675&ssl=1',
                                   caption=f"Hello <code>{message.from_user.first_name}</code>\n"
                                           f"Im Sano Manjiro anime themed group management\n",
                                   reply_markup=help_markup)


async def show_help(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_caption(f"Hello <code>{call.from_user.first_name}</code>\n"
                                    f"Im Sano Manjiro anime themed group management\n",
                                    reply_markup=help_markup)


async def show_info_anime(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_caption(
        '<code>/anime</code> - Сommand to '
        'search for information about anime\n'
        '(<code>/anime</code> title_anime)',
        reply_markup=back_keyboard
    )


async def show_anti_flood_info(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_caption(
        "<code>!mute /mute</code> - prohibit a user from writing"
        "for a certain period of time (!ro 1 spam)\n"
        "<code>!unmute /unmute</code> - to allow writing again (!un_ro)\n"
        "<code>!ban /ban</code> - Remove a user from the group (!ban)\n"
        "<code>!un_ban /un_ban</code> - Ability to return to the group (!un_ban)",
        reply_markup=back_keyboard
    )


async def show_funny_info(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_caption(
        "<code>/kick</code> - An entertaining command that allows you to hit another user (/kick)\n"
        "<code>/say</code> - with this command you can make the bot say something (/say text)",
        reply_markup=back_keyboard
    )


async def show_service_info(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_caption(
        f"<code>/set_welcome</code> - Allows you to set the chat greeting (/set_welcome some text)\n"
        f"<code>/set_farewell</code> -Allows you to set a goodbye for users (/set_farewell some text)",
        reply_markup=back_keyboard
    )


async def back_to_help(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_caption(
        f"Hello <code>{call.from_user.first_name}</code>\n"
        f"Im Sano Manjiro anime themed group management\n",
        reply_markup=help_markup
    )


async def back_to_start(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_caption(
        f"Hi, <i>{call.from_user.full_name}</i>. I'm a Telegram bot for"
        f" managing groups\n<code>(click the buttons below)</code> ",
        reply_markup=main_markup
    )
