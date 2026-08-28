import os
import uuid
import json
import time
import requests
import telebot
from telebot import types

TOKEN = "8764469565:AAGxm_R_jygX8ti1Irl1vwSEMWC_Ijfsta4"
ADMIN_ID = 608502324
TEMP_DIR = "temp"
MAX_SIZE = 50 * 1024 * 1024
CONFIG_FILE = "config.json"
USERS_FILE = "users.json"

os.makedirs(TEMP_DIR, exist_ok=True)
bot = telebot.TeleBot(TOKEN)

EMOJI_DOWN = "<tg-emoji emoji-id='5963087934696459905'>⬇️</tg-emoji>"
EMOJI_UP = "<tg-emoji emoji-id='6039391666547201160'>⬆️</tg-emoji>"
EMOJI_SEND = "<tg-emoji emoji-id='6039573425268201570'>📤</tg-emoji>"
EMOJI_SHIELD = "<tg-emoji emoji-id='6030537007350944596'>🛡</tg-emoji>"
EMOJI_FOLDER = "<tg-emoji emoji-id='6039630677182254664'>📂</tg-emoji>"
EMOJI_INBOX = "<tg-emoji emoji-id='6041730074376410123'>📥</tg-emoji>"
EMOJI_MEGAPHONE = "<tg-emoji emoji-id='6021418126061605425'>📢</tg-emoji>"
EMOJI_SPEAKER = "<tg-emoji emoji-id='6039454987250044861'>🔊</tg-emoji>"
EMOJI_BELL = "<tg-emoji emoji-id='6039486778597970865'>🔔</tg-emoji>"
EMOJI_CAMERA = "<tg-emoji emoji-id='6030506650522096180'>📷</tg-emoji>"
EMOJI_FILM = "<tg-emoji emoji-id='5944777041709633960'>🎞</tg-emoji>"
EMOJI_HEART = "<tg-emoji emoji-id='6037533152593842454'>❤️</tg-emoji>"
EMOJI_BOOK = "<tg-emoji emoji-id='6037286673010660132'>📖</tg-emoji>"
EMOJI_LEFT = "<tg-emoji emoji-id='6039519841256214245'>⬅️</tg-emoji>"
EMOJI_CLOCK = "<tg-emoji emoji-id='5850317551090800862'>⏰</tg-emoji>"
EMOJI_CHECK = "<tg-emoji emoji-id='5843596438373667352'>✅️</tg-emoji>"
EMOJI_CHECK2 = "<tg-emoji emoji-id='6041919344995209164'>✅</tg-emoji>"
EMOJI_GOLD = "<tg-emoji emoji-id='6037428784888549034'>🥇</tg-emoji>"
EMOJI_VIDEO = "<tg-emoji emoji-id='5886579539064132088'>🎥</tg-emoji>"
EMOJI_MIC = "<tg-emoji emoji-id='6030722571412967168'>🎤</tg-emoji>"
EMOJI_PHONE = "<tg-emoji emoji-id='6039605143601680423'>📞</tg-emoji>"
EMOJI_ROBOT = "<tg-emoji emoji-id='5983580310292402968'>🤖</tg-emoji>"
EMOJI_CHAT = "<tg-emoji emoji-id='6030784887093464891'>💬</tg-emoji>"
EMOJI_BULB = "<tg-emoji emoji-id='5891120964468480450'>💡</tg-emoji>"
EMOJI_SLEEP = "<tg-emoji emoji-id='5983401171501454028'>💤</tg-emoji>"
EMOJI_LOCK = "<tg-emoji emoji-id='5776227595708273495'>🔒</tg-emoji>"
EMOJI_LOCK2 = "<tg-emoji emoji-id='5778570255555105942'>🔒</tg-emoji>"
EMOJI_18 = "<tg-emoji emoji-id='5922610170034132416'>🔞</tg-emoji>"
EMOJI_PIN = "<tg-emoji emoji-id='6030399199030284183'>📍</tg-emoji>"
EMOJI_USER = "<tg-emoji emoji-id='6032994772321309200'>👤</tg-emoji>"
EMOJI_USERS = "<tg-emoji emoji-id='6032609071373226027'>👥</tg-emoji>"
EMOJI_PLUS = "<tg-emoji emoji-id='6033108709213736873'>➕</tg-emoji>"
EMOJI_TARGET = "<tg-emoji emoji-id='6032949275732742941'>🎯</tg-emoji>"
EMOJI_GIFT = "<tg-emoji emoji-id='6032644646587338669'>🎁</tg-emoji>"
EMOJI_STAR = "<tg-emoji emoji-id='6034923938486684992'>⭐️</tg-emoji>"
EMOJI_SMILE = "<tg-emoji emoji-id='5774034804450267485'>🙂</tg-emoji>"
EMOJI_ANGRY = "<tg-emoji emoji-id='6044118213631938928'>😡</tg-emoji>"
EMOJI_BEAR = "<tg-emoji emoji-id='6044004057696177711'>🐻</tg-emoji>"
EMOJI_PARTY = "<tg-emoji emoji-id='6041731551845159060'>🎉</tg-emoji>"
EMOJI_WAVE = "<tg-emoji emoji-id='6041921818896372382'>👋</tg-emoji>"
EMOJI_HASH = "<tg-emoji emoji-id='5850693253355017860'>#️⃣</tg-emoji>"
EMOJI_SUN = "<tg-emoji emoji-id='5938525265838739643'>☀️</tg-emoji>"
EMOJI_MOON = "<tg-emoji emoji-id='5769143090103193926'>🌙</tg-emoji>"
EMOJI_TV = "<tg-emoji emoji-id='6044356915029348425'>📺</tg-emoji>"
EMOJI_WINDOW = "<tg-emoji emoji-id='6035353688619356485'>🪟</tg-emoji>"
EMOJI_PINNED = "<tg-emoji emoji-id='6043896193887506430'>📌</tg-emoji>"
EMOJI_BOX = "<tg-emoji emoji-id='5778672437122045013'>📦</tg-emoji>"
EMOJI_PICTURE = "<tg-emoji emoji-id='5775903948447682435'>🖼</tg-emoji>"
EMOJI_PLANE = "<tg-emoji emoji-id='5927118708873892465'>✈️</tg-emoji>"
EMOJI_PAGE = "<tg-emoji emoji-id='6050643982646513651'>📄</tg-emoji>"
EMOJI_PENCIL = "<tg-emoji emoji-id='5771847914477326786'>✏️</tg-emoji>"
EMOJI_CROWN = "<tg-emoji emoji-id='5805553606635559688'>👑</tg-emoji>"
EMOJI_DIAMOND = "<tg-emoji emoji-id='5836907383292436018'>💎</tg-emoji>"
EMOJI_WRENCH = "<tg-emoji emoji-id='5836997023554870252'>🔨</tg-emoji>"
EMOJI_SEARCH = "<tg-emoji emoji-id='5874960879434338403'>🔎</tg-emoji>"
EMOJI_GEAR = "<tg-emoji emoji-id='5877260593903177342'>⚙️</tg-emoji>"
EMOJI_TAG = "<tg-emoji emoji-id='6039565797406282001'>🏷</tg-emoji>"
EMOJI_CHART = "<tg-emoji emoji-id='6030537810509828330'>⏲</tg-emoji>"
EMOJI_MONEY = "<tg-emoji emoji-id='5904359114531675993'>💰</tg-emoji>"
EMOJI_PAPERCLIP = "<tg-emoji emoji-id='5776138384942567185'>📎</tg-emoji>"
EMOJI_SUPPORT = "<tg-emoji emoji-id='6030722571412967168'>🎤</tg-emoji>"
EMOJI_SHARE = "<tg-emoji emoji-id='6039422865189638057'>📣</tg-emoji>"

ICON_BELL = "6039486778597970865"
ICON_CHECK = "6041919344995209164"
ICON_USER = "6032994772321309200"
ICON_CHART = "6030537810509828330"
ICON_SEND = "6039573425268201570"
ICON_GEAR = "5877260593903177342"
ICON_USERS = "6032609071373226027"
ICON_DOWN = "5963087934696459905"
ICON_STAR = "6034923938486684992"
ICON_SUPPORT = "6030722571412967168"
ICON_SHARE = "6039422865189638057"

def load_json(filename, default):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    return default

def save_json(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

DEFAULT_CONFIG = {
    "subscription_channel": "verusername",
    "subscription_enabled": True,
    "download_count": 0
}

config = load_json(CONFIG_FILE, DEFAULT_CONFIG)
users_data = load_json(USERS_FILE, {})

def save_config():
    save_json(CONFIG_FILE, config)

def save_users():
    save_json(USERS_FILE, users_data)

def is_admin(user_id):
    return user_id == ADMIN_ID

def get_user(user_id):
    uid = str(user_id)
    if uid not in users_data:
        users_data[uid] = {
            "first_seen": time.time(),
            "downloads": 0,
            "blocked": False
        }
        save_users()
    return users_data[uid]

def check_subscription(user_id):
    if not config["subscription_enabled"]:
        return True
    channel = config["subscription_channel"]
    if not channel:
        return True
    try:
        chat_member = bot.get_chat_member("@" + channel, user_id)
        return chat_member.status in ["member", "administrator", "creator"]
    except Exception:
        return False

def download_tiktok(url):
    api_url = "https://tikwm.com/api/"
    params = {"url": url}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    resp = requests.get(api_url, params=params, headers=headers, timeout=30)
    data = resp.json()
    if data.get("code") != 0:
        raise Exception("TikTok API error")
    video_url = data["data"]["play"]
    filename = str(uuid.uuid4()) + ".mp4"
    filepath = os.path.join(TEMP_DIR, filename)
    r = requests.get(video_url, headers=headers, timeout=60)
    with open(filepath, "wb") as f:
        f.write(r.content)
    return filepath

def compress_video(input_path, max_size_mb=49):
    output_path = input_path.rsplit(".", 1)[0] + "_compressed.mp4"
    current_size = os.path.getsize(input_path)
    if current_size <= max_size_mb * 1024 * 1024:
        return input_path
    try:
        import subprocess
        probe_cmd = [
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            input_path
        ]
        duration = float(subprocess.check_output(probe_cmd).decode().strip())
        target_size = max_size_mb * 1024 * 1024 * 0.9
        target_bitrate = int((target_size * 8) / duration)
        cmd = [
            "ffmpeg", "-i", input_path,
            "-b:v", str(target_bitrate),
            "-maxrate", str(target_bitrate),
            "-bufsize", str(target_bitrate * 2),
            "-preset", "fast",
            "-c:v", "libx264",
            "-c:a", "aac",
            "-b:a", "96k",
            "-y",
            output_path
        ]
        subprocess.run(cmd, check=True, capture_output=True, timeout=300)
        if os.path.exists(output_path) and os.path.getsize(output_path) < current_size:
            os.remove(input_path)
            return output_path
    except:
        pass
    return input_path

@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    user = get_user(user_id)
    first_name = message.from_user.first_name
    is_group = message.chat.type in ["group", "supergroup"]

    if not is_group and not check_subscription(user_id):
        channel = config["subscription_channel"]
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(
            "Подписаться",
            url=f"https://t.me/{channel}",
            icon_custom_emoji_id=ICON_BELL,
            style="primary"
        ))
        markup.add(types.InlineKeyboardButton(
            "Проверить подписку",
            callback_data="check_sub",
            icon_custom_emoji_id=ICON_CHECK,
            style="success"
        ))
        text = (
            f"{EMOJI_WAVE} {first_name}, привет!\n\n"
            f"{EMOJI_LOCK} Для использования бота необходима подписка на канал @{channel}!\n\n"
            f"{EMOJI_STAR} После подписки нажми кнопку проверки."
        )
        bot.send_message(message.chat.id, text, reply_markup=markup, parse_mode="HTML")
        return

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(
        "Мой профиль",
        callback_data="my_profile",
        icon_custom_emoji_id=ICON_USER,
        style="primary"
    ))
    markup.add(types.InlineKeyboardButton(
        "Поддержка",
        url="https://t.me/vocma",
        icon_custom_emoji_id=ICON_SUPPORT,
        style="success"
    ))

    if is_group:
        text = (
            f"{EMOJI_WAVE} {first_name}, привет!\n\n"
            f"{EMOJI_DOWN} Я скачиваю видео из TikTok без водяного знака.\n"
            f"{EMOJI_PAPERCLIP} Просто отправь ссылку на видео прямо в этот чат!"
        )
    else:
        text = (
            f"{EMOJI_WAVE} {first_name}, привет!\n\n"
            f"{EMOJI_DOWN} Я скачиваю видео из TikTok без водяного знака.\n"
            f"{EMOJI_PAPERCLIP} Просто отправь мне ссылку на видео.\n\n"
            f"{EMOJI_CHAT} Работаю в личке и группах.\n"
            f"{EMOJI_STAR} Добавь меня в группу и качай видео прямо там!"
        )

    sent_msg = bot.send_message(message.chat.id, text, reply_markup=markup, parse_mode="HTML")

    if not is_group:
        try:
            bot.pin_chat_message(message.chat.id, sent_msg.message_id, disable_notification=True)
        except:
            pass

@bot.callback_query_handler(func=lambda call: call.data == "check_sub")
def check_sub_callback(call):
    user_id = call.from_user.id
    if check_subscription(user_id):
        bot.answer_callback_query(call.id, "Подписка активна!")
        bot.delete_message(call.message.chat.id, call.message.message_id)
        start(call.message)
    else:
        bot.answer_callback_query(call.id, "Ты ещё не подписался!")

@bot.callback_query_handler(func=lambda call: call.data == "my_profile")
def my_profile(call):
    user = get_user(call.from_user.id)
    downloads = user.get("downloads", 0)
    first_seen = time.strftime("%d.%m.%Y", time.localtime(user.get("first_seen", time.time())))
    text = f"Скачиваний: {downloads}\nВ боте с: {first_seen}"
    bot.answer_callback_query(call.id, text, show_alert=True)

@bot.message_handler(commands=["admin"])
def admin_panel(message):
    if not is_admin(message.from_user.id):
        bot.reply_to(message, f"{EMOJI_LOCK} Нет доступа", parse_mode="HTML")
        return

    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("Статистика", callback_data="admin_stats", icon_custom_emoji_id=ICON_CHART, style="primary"),
        types.InlineKeyboardButton("Рассылка", callback_data="admin_broadcast", icon_custom_emoji_id=ICON_SEND, style="success"),
        types.InlineKeyboardButton("Настройки", callback_data="admin_settings", icon_custom_emoji_id=ICON_GEAR, style="primary"),
        types.InlineKeyboardButton("Пользователи", callback_data="admin_users", icon_custom_emoji_id=ICON_USERS, style="primary"),
        types.InlineKeyboardButton("Скачивания", callback_data="admin_downloads", icon_custom_emoji_id=ICON_DOWN, style="primary"),
    )
    bot.send_message(message.chat.id, f"{EMOJI_CROWN} Админ-панель", reply_markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data.startswith("admin_"))
def admin_callbacks(call):
    if not is_admin(call.from_user.id):
        bot.answer_callback_query(call.id, "Нет доступа")
        return

    if call.data == "admin_stats":
        total_users = len(users_data)
        total_downloads = sum(u.get("downloads", 0) for u in users_data.values())
        blocked = sum(1 for u in users_data.values() if u.get("blocked"))
        text = f"Пользователей: {total_users}\nСкачиваний: {total_downloads}\nЗаблокировано: {blocked}"
        bot.answer_callback_query(call.id, text, show_alert=True)

    elif call.data == "admin_broadcast":
        msg = bot.send_message(
            call.message.chat.id,
            f"{EMOJI_SEND} Введи текст для рассылки.\n"
            f"Просто скопируй премиум эмодзи и вставь в текст.",
            parse_mode="HTML"
        )
        bot.register_next_step_handler(msg, process_broadcast)

    elif call.data == "admin_settings":
        show_settings(call.message)

    elif call.data == "admin_users":
        total = len(users_data)
        text = f"Всего пользователей: {total}"
        bot.answer_callback_query(call.id, text, show_alert=True)

    elif call.data == "admin_downloads":
        total_downloads = sum(u.get("downloads", 0) for u in users_data.values())
        text = f"Всего скачиваний: {total_downloads}"
        bot.answer_callback_query(call.id, text, show_alert=True)

def show_settings(message):
    channel = config["subscription_channel"]
    enabled = config["subscription_enabled"]

    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("Сменить канал", callback_data="set_channel_menu", icon_custom_emoji_id=ICON_BELL, style="primary"),
        types.InlineKeyboardButton(
            f"Подписка: {'Вкл' if enabled else 'Выкл'}",
            callback_data="toggle_sub_menu",
            icon_custom_emoji_id=ICON_CHECK,
            style="success" if enabled else "danger"
        ),
        types.InlineKeyboardButton("Назад", callback_data="back_to_admin", icon_custom_emoji_id=ICON_DOWN, style="danger"),
    )

    text = (
        f"{EMOJI_GEAR} Настройки:\n\n"
        f"{EMOJI_BELL} Канал: @{channel}\n"
        f"{EMOJI_CHECK2} Подписка: {'включена' if enabled else 'выключена'}"
    )
    bot.edit_message_text(text, message.chat.id, message.message_id, reply_markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "set_channel_menu")
def set_channel_menu(call):
    if not is_admin(call.from_user.id):
        return
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Отмена", callback_data="back_to_admin", icon_custom_emoji_id=ICON_DOWN, style="danger"))
    msg = bot.send_message(
        call.message.chat.id,
        f"{EMOJI_BELL} Введи username канала (без @) или нажми Отмена:",
        reply_markup=markup,
        parse_mode="HTML"
    )
    bot.register_next_step_handler(msg, process_channel)

def process_channel(message):
    if not is_admin(message.from_user.id):
        return
    
    if message.text == "Отмена" or message.text == "/cancel":
        bot.reply_to(message, f"{EMOJI_LEFT} Отменено", parse_mode="HTML")
        admin_panel(message)
        return
    
    channel = message.text.strip().lstrip("@")
    if not channel:
        bot.reply_to(message, f"{EMOJI_ANGRY} Введи нормальный username", parse_mode="HTML")
        return
    
    config["subscription_channel"] = channel
    save_config()
    bot.reply_to(message, f"{EMOJI_CHECK2} Канал: @{channel}", parse_mode="HTML")
    admin_panel(message)

@bot.callback_query_handler(func=lambda call: call.data == "toggle_sub_menu")
def toggle_sub_menu(call):
    if not is_admin(call.from_user.id):
        return
    config["subscription_enabled"] = not config["subscription_enabled"]
    save_config()
    state = "включена" if config["subscription_enabled"] else "выключена"
    bot.answer_callback_query(call.id, f"Подписка {state}")
    show_settings(call.message)

@bot.callback_query_handler(func=lambda call: call.data == "back_to_admin")
def back_to_admin(call):
    if not is_admin(call.from_user.id):
        return
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("Статистика", callback_data="admin_stats", icon_custom_emoji_id=ICON_CHART, style="primary"),
        types.InlineKeyboardButton("Рассылка", callback_data="admin_broadcast", icon_custom_emoji_id=ICON_SEND, style="success"),
        types.InlineKeyboardButton("Настройки", callback_data="admin_settings", icon_custom_emoji_id=ICON_GEAR, style="primary"),
        types.InlineKeyboardButton("Пользователи", callback_data="admin_users", icon_custom_emoji_id=ICON_USERS, style="primary"),
        types.InlineKeyboardButton("Скачивания", callback_data="admin_downloads", icon_custom_emoji_id=ICON_DOWN, style="primary"),
    )
    bot.edit_message_text(f"{EMOJI_CROWN} Админ-панель", call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode="HTML")

def process_broadcast(message):
    if not is_admin(message.from_user.id):
        return
    
    if message.text == "Отмена" or message.text == "/cancel":
        bot.reply_to(message, f"{EMOJI_LEFT} Отменено", parse_mode="HTML")
        admin_panel(message)
        return
    
    text = message.text
    sent = 0
    for uid in users_data:
        try:
            bot.send_message(int(uid), text, parse_mode="HTML")
            sent += 1
            time.sleep(0.1)
        except:
            pass
    bot.reply_to(message, f"{EMOJI_CHECK2} Отправлено: {sent}", parse_mode="HTML")

@bot.message_handler(func=lambda m: m.text and ("tiktok.com" in m.text or "vm.tiktok" in m.text or "vt.tiktok" in m.text))
def handle_tiktok(message):
    user_id = message.from_user.id
    user = get_user(user_id)
    is_group = message.chat.type in ["group", "supergroup"]

    if user.get("blocked"):
        bot.reply_to(message, f"{EMOJI_LOCK} Ты заблокирован", parse_mode="HTML")
        return

    if not is_group and not check_subscription(user_id):
        channel = config["subscription_channel"]
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(
            "Подписаться",
            url=f"https://t.me/{channel}",
            icon_custom_emoji_id=ICON_BELL,
            style="primary"
        ))
        markup.add(types.InlineKeyboardButton(
            "Проверить",
            callback_data="check_sub",
            icon_custom_emoji_id=ICON_CHECK,
            style="success"
        ))
        bot.reply_to(
            message,
            f"{EMOJI_LOCK} Подпишись на @{channel}",
            reply_markup=markup,
            parse_mode="HTML"
        )
        return

    url = message.text.strip()
    wait_msg = bot.reply_to(message, f"{EMOJI_VIDEO} Скачиваю...", parse_mode="HTML")

    try:
        filepath = download_tiktok(url)

        if os.path.getsize(filepath) > MAX_SIZE:
            bot.edit_message_text(
                f"{EMOJI_BOX} Файл большой, сжимаю...",
                message.chat.id,
                wait_msg.message_id,
                parse_mode="HTML"
            )
            filepath = compress_video(filepath)

        if os.path.getsize(filepath) > MAX_SIZE:
            bot.edit_message_text(
                f"{EMOJI_ANGRY} Файл больше 50 МБ",
                message.chat.id,
                wait_msg.message_id
            )
            os.remove(filepath)
            return

        bot_name = bot.get_me().username

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(
            "Поделиться с другом",
            switch_inline_query=f"Привет! Я использую этого бота для скачивания видео из Тиктока без водяного знака. Заходи!",
            icon_custom_emoji_id=ICON_SHARE,
            style="primary"
        ))

        with open(filepath, "rb") as video:
            bot.send_video(
                message.chat.id,
                video,
                caption=f"{EMOJI_HEART} Скачано в @{bot_name}",
                reply_to_message_id=message.message_id,
                reply_markup=markup,
                parse_mode="HTML"
            )

        bot.delete_message(message.chat.id, wait_msg.message_id)
        os.remove(filepath)

        user["downloads"] = user.get("downloads", 0) + 1
        save_users()
        config["download_count"] = config.get("download_count", 0) + 1
        save_config()

    except Exception as e:
        bot.edit_message_text(
            f"{EMOJI_ANGRY} Не удалось скачать видео. Попробуй ещё раз или отправь другую ссылку.",
            message.chat.id,
            wait_msg.message_id,
            parse_mode="HTML"
        )

if __name__ == "__main__":
    print("✅ Бот запущен")
    bot.infinity_polling(timeout=60, long_polling_timeout=30)