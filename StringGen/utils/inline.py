from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup,Message

from config import SUPPORT_CHAT,OWNER_ID


keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="بدا استخراج الجلسة 🖥️", callback_data="gensession")
                    ],
                    [
                    InlineKeyboardButton("سـورس القرش", url="https://t.me/X_YI1I")
                    ],
                    [
                    InlineKeyboardButton("مـعـلـومات الـمـطـور", url="t.me/X_Y1I"),
                ],
                [
                    InlineKeyboardButton("الـمـطـور👷", user_id=OWNER_ID),
                    InlineKeyboardButton("اوامـر الـبـوت", url="https://t.me/c/1825352491/23")
                ]
            ]
        )

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="بايروجورام v1", callback_data="pyrogram1"),
            InlineKeyboardButton(text="بايروجورام v2", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="تليثون", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="استخرج مجدداً", callback_data="gensession")]]
)
