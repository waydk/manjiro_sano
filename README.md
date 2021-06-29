![manjiro_sano](https://w.wallhaven.cc/full/v9/wallhaven-v9ze1m.jpg)
# Anime telegram bot for group management
*Telegram bot written in python using aiogram as the framework, postgresql as the database*
## Available commands:
* <code>!ro /ro <time> <reason></code> - prohibit a user from writing for a certain period of time <b>(!ro 1 spam)</b>
* <code>!un_ro /un_ro</code> - to allow writing again <b>(!un_ro)</b>
* <code>!ban /ban</code> - Remove a user from the group <b>(!ban)</b>
* <code>!un_ban /un_ban</code> - Ability to return to the group <b>(!un_ban)</b>
* <code>/set_welcome</code> - Allows you to set the chat greeting <b>(/set_welcome some text)</b>
* <code>/set_farewell</code> -Allows you to set a goodbye for users <b>(/set_farewell some text)</b>
* <code>/kick</code> - An entertaining command that allows you to hit another user <b>(/kick)</b>
## Development
### System dependencies
* Python 3.9
* SQLAlchemy 1.3.24
* environs 8.0.0
* gino 1.0.1
* asyncpg 0.22.0
* aiogram 2.13
* loguru 0.5.3
### Setup environment
* Rename .env.dist to <b>.env</b>
* Fill in your <b>data</b>
* <code>ADMINS</code> is responsible for the list of bot administrators, so far not used
* <code>BOT_TOKEN</code> is responsible for the heart of the bot, without it it will not work, get in [BotFather](https://t.me/BotFather)
* <code>PG_HOST</code> is responsible for where your database is located
* <code>PG_USER and PG_PASSWORD</code> are needed to access the database
* <code>DATABASE</code> database name
