from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from tg_bot.utils.keyboards.main_keyboard import help_markup, back_keyboard, main_markup


async def command_help(message: types.Message):
    """
    bot info
    """
    if message.chat.type == 'private':
        await message.answer_photo(photo='https://i2.wp.com/duniamasa.com/wp-content'
                                         '/uploads/2021/04/mikey.jpg?resize=1200%2C675&ssl=1',
                                   caption=f"Here you can find out what commands are in the bot\n"
                                           f"<code>Click the buttons below</code>",
                                   reply_markup=help_markup)
    else:
        username = await message.bot.get_me()
        await message.answer(
            "You can see all the information in the bot",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(text="Go to the bot's PM", url=f"t.me/{username['username']}?start=help")
                    ]
                ])
        )


async def show_help(call: CallbackQuery):
    """
    show bot info
    """
    await call.answer(cache_time=1)
    await call.message.edit_caption(caption=f"This is where you can find out what "
                                            f"commands are in the bot\n"
                                            f"<code>Click the buttons below</code>",
                                    reply_markup=help_markup)


async def show_anti_flood_info(call: CallbackQuery):
    """
    show antiflood info
    """
    await call.answer(cache_time=1)
    await call.message.edit_caption(
        "<code>!mute /mute</code> - command to restrict the user"
        "for a certain period (!ro 1 спам)\n"
        "<code>!unmute /unmute</code> - to give back to the user (!unmute)\n"
        "<code>!ban /ban</code> - Remove the user from the conversation, limit the ability to return (!ban)\n"
        "<code>!unban /unban</code> - To give you an opportunity to get back into the conversation (!unban)",
        reply_markup=back_keyboard
    )


async def show_funny_info(call: CallbackQuery):
    """
    show funny info
    """
    await call.answer(cache_time=1)
    await call.message.edit_caption(
        "<code>/kick</code> - The ability to fuck with another user's foot (/kick)\n"
        "<code>/say</code> - Make the bot say something (/say text)",
        reply_markup=back_keyboard
    )


async def show_service_info(call: CallbackQuery):
    """
    show service info
    """
    await call.answer(cache_time=1)
    await call.message.edit_caption(
        f"<code>/set_welcome</code> - Set the chat greeting (/set_welcome hello)\n"
        f"<code>/set_farewell</code> - Set farewell in chat (/set_farewell for now)",
        reply_markup=back_keyboard
    )


async def back_to_help(call: CallbackQuery):
    """
    button back
    """
    await call.answer(cache_time=1)
    await call.message.edit_caption(
        f"Here you can find out what commands are in the bot\n"
        f"<code>Click the buttons below</code>",
        reply_markup=help_markup
    )


async def back_to_start(call: CallbackQuery):
    """
    button back
    """
    await call.answer(cache_time=1)
    await call.message.edit_caption(
        f"Hi, {call.from_user.full_name}. I'm a Telegram bot to manage chats\n"
        f"For all questions: @waydk\n"
        f"<code>Click the buttons below</code> ",
        reply_markup=main_markup
    )
