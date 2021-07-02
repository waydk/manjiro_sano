from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from tg_bot.utils.keyboards.main_keyboard import help_markup, back_keyboard, main_markup


async def command_help(message: types.Message):
    if message.chat.type == 'supergroup':
        username = await message.bot.get_me()
        await message.answer(
            "You can see the commands in the bot",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(text="Help", url=f"t.me/{username['username']}?start=help")
                    ]
                ])
        )
    else:
        await message.answer(f"Hello <code>{message.from_user.first_name}</code>\n"
                             f"Im Sano Manjiro anime themed group management\n",
                             reply_markup=help_markup)


async def show_help(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.answer(f"Hello <code>{call.from_user.first_name}</code>\n"
                              f"Im Sano Manjiro anime themed group management\n",
                              reply_markup=help_markup)


async def show_info_anime(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_text(
        text='<code>/anime</code> - Сommand to '
             'search for information about anime\n'
             '(<code>/anime</code> title_anime)',
        reply_markup=back_keyboard
    )


async def show_anti_flood_info(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_text(
        "<code>!mute /mute</code> - prohibit a user from writing"
        "for a certain period of time (!ro 1 spam)\n"
        "<code>!unmute /unmute</code> - to allow writing again (!un_ro)\n"
        "<code>!ban /ban</code> - Remove a user from the group (!ban)\n"
        "<code>!un_ban /un_ban</code> - Ability to return to the group (!un_ban)",
        reply_markup=back_keyboard
    )


async def show_funny_info(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_text(
        "<code>/kick</code> - An entertaining command that allows you to hit another user (/kick)\n"
        "<code>/say</code> - with this command you can make the bot say something (/say text)",
        reply_markup=back_keyboard
    )


async def show_service_info(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_text(
        f"<code>/set_welcome</code> - Allows you to set the chat greeting (/set_welcome some text)\n"
        f"<code>/set_farewell</code> -Allows you to set a goodbye for users (/set_farewell some text)",
        reply_markup=back_keyboard
    )


async def back_to_help(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_text(
        f"Hello <code>{call.from_user.first_name}</code>\n"
        f"Im Sano Manjiro anime themed group management\n",
        reply_markup=help_markup
    )
