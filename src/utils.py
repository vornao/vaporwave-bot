import random

inline_cache_time = 1

start_msg = "\
ₓ˚. ୭ ˚○◦˚.˚◦○˚ ୧ .˚ₓ\nWelcome to VaporwaveBot!\nₓ˚. ୭ ˚○◦˚.˚◦○˚ ୧ .˚ₓ\n\n\
Usage: from your message input bar type:\n\n\
***@vprwavebot your-text-here***\n\n\
Send /help for more informations"

help_msg = "This is an inline bot, use it from the input bar of any chat!\n\n\
*@vprwavebot type-here-your-message\n\n \
*A prompt will now show, tap on the aesthetic quote you like\u2728\n\n\
Under Construction!"

privacy_msg = "This bot does not store, in any way, user's private messages, \
as well as inline requests' private text.\n\n"


ascii_akward = [
    "(ʘ_ʘ)",
    "(ʘ‿ʘ)",
    "(ಠ_ಠ)",
    "(◕_◕)",
    "(◕‿◕)",
    "\(◕ ◡ ◕\)",
    "(¬_¬)",
    "ᶘ ᵒᴥᵒᶅ",
    "(´・ω・｀)",
]
sparkles = [
    "✧･ﾟ: *✧･ﾟ:*",
    "*:･ﾟ✧*:･ﾟ✧",
    "ₓ˚. ୭ ˚○◦˚.˚◦○˚ ୧ .˚ₓ",
    "｡･:*:･ﾟ★,｡･:*:･ﾟ☆",
    "｡･:*:･ﾟ★,｡･:*:･ﾟ☆",
    "‧͙⁺˚*･༓☾",
    "☽༓･*˚⁺‧͙",
]
emoji_sparkles = "\u2728"
fullwidth = {i: chr(i + 0xFEE0) for i in range(0x21, 0x7F)}
hiragana = [chr(i) for i in range(0x3040, 0x309F)]


def random_hiragana() -> str:
    s = ""
    for x in range(3):
        s += random.choice(hiragana)
    return s


def vaporize(s: str) -> str:
    vaporized = s.translate(fullwidth)
    return vaporized


def hiramize(s: str) -> str:
    hiramized = vaporize(s)
    hiramized += "  "
    hiramized += random_hiragana()
    return hiramized


def emojize(s: str) -> str:
    emojized = vaporize(s)
    emojized += "  " + random.choice(ascii_akward)
    return emojized


def sparkleize(s: str) -> str:
    sparkleized = emoji_sparkles + "  "
    sparkleized += vaporize(s) + "  "
    sparkleized += emoji_sparkles
    return sparkleized
