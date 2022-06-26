from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton as ib
kbmain = ReplyKeyboardMarkup(resize_keyboard=True)
kbmain.row("⚡️ Чек", "🌿 Чек за рефов")
kbmain.row("🏡 Профиль", "❓ FAQ")
kbcheck = InlineKeyboardMarkup()
kbcheck.add(ib("Одна карта", callback_data="check_one"), ib("Массчек", callback_data="check_many"))
kbchecksub = InlineKeyboardMarkup()
kbchecksub.add(ib("Канал", url="t.me/VAX_TEAM"), ib("Проверить", callback_data="check_sub"))
kbprofile = ReplyKeyboardMarkup(resize_keyboard=True)
kbprofile.row("💳Пополнить", "🤲 Выдать чек", "🐍Назад")
kbcancel = InlineKeyboardMarkup().add(ib("⛔Отмена", callback_data="check_cancel"))
kbq = ReplyKeyboardMarkup(resize_keyboard=True)
kbq.row("✅Проверить оплату","🐍Назад")
kb_tconfirm = ReplyKeyboardMarkup(resize_keyboard=True)
kb_tconfirm.row("✅Подтверждаю")
kb_tconfirm.row("❌Отмена")
kbadmin = ReplyKeyboardMarkup(resize_keyboard=True)
kbadmin.row("📟Статистика","✉️Рассылка")
kbadmin.row("💰Установить баланс", "💵Выдать баланс")
kbban = ReplyKeyboardMarkup(resize_keyboard=True)
kbban.row("🔒Забанить", "🔓Разбанить")
kbban.row("🔐Проверить на бан", "🐍Назад")
kbadmin.row("🔒Бан-система", "🐍Назад")
kbsend = ReplyKeyboardMarkup(resize_keyboard=True)
kbsend.row("С фото","Без фото"," 🐍Назад")
kbchannel = InlineKeyboardMarkup().add(ib("⚡Канал", url="t.me/VAX_TEAM"))