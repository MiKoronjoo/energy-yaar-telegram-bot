from telepot.namedtuple import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

from classes import State


def keyboard_maker(keyboard_labels):
    my_keyboard = []
    for row in keyboard_labels:
        keyboard_row = []
        for label in row:
            keyboard_row.append(KeyboardButton(text=label))

        my_keyboard.append(keyboard_row)

    return ReplyKeyboardMarkup(keyboard=my_keyboard, resize_keyboard=True)


# button labels
bl_start = 'باشه؛ شروع کن'
bl_about_us = 'درباره‌ی ما'
bl_calcule = 'بریم سراغ حساب کتاب'
bl_plan_review = 'بررسی طرح'
bl_t3000 = '۳۰۰۰ تومان'
bl_t4000 = '۴۰۰۰ تومان'
bl_t5600 = '۵۶۰۰ تومان'
bl_recalcule = 'با قیمت‌های دیگه حساب کن'

# error messages
err_bad_input = '''ورودی اشتباهه!
لطفا یکی از گزینه ها رو انتخاب کن'''

err_val = '''ورودی استاندارد نیست!
لطفا ورودی رو به عدد وارد کن'''

# messages
text_1 = '''سلام رفیق 👋
بیا یه دنیای خیالی 😬 رو فرض کنیم که دولت سر عقل میاد و به جای دادن یارانه به ثروتمندای جامعه؛ فکری به حال فقیر فقرا بکنه و یه کمی وضعشون رو از این بدتر نکنه! 🙏
یکی از بهترین راه ها اینه که دولت ماهیانه به هر ایرانی مثلا ۲۰ لیتر سهمیه ی بنزین ۱۰۰۰ تومانی بده و آدم ها هم بتونند سهم شون رو تو یه سامانه ی آنلاین به پُرمصرف ها بفروشند. 💰
اگر یه دقیقه وقت داشته باشی؛ «انرژی یار» بهت میگه از اجرای این طرح چقدر سود میکنی.
اگر پایه ای، شروع کنیم ...'''

text_2 = '''به نام خدا
سلام رفقا؛

همون طوری که دیدید ربات انرژی‌یار بهتون کمک میکنه ببینید با اجرای طرح دادن سهمیه‌ی بنزین به هر فرد ایرانی چقدر گیرتون میاد یا چقدر میتونید به فقرا بدون دخالت نهادهای دولتی کمک برسونید.
درواقع انرژی‌یار مدل ساده شده‌ای از طرح اندیشکده حکمرانی شریف (وابسته به پژوهشکده سیاست‌گذاری دانشگاه صنعتی شریف) هست.
با کلیک روی «بررسی طرح» میتونید طرح اندیشکده رو مشاهده کنید و ضمن مطالعه‌اش ما را از نظراتتون بهره‌مند کنید. علاوه بر این میتونید با آدرس ایمیل %s یا آیدی تلگرامی %s با ما در ارتباط باشید.
به امید سربلندی و به‌روزی ایران و ایرانی'''

question_1 = 'خانواده‌ی شما چند نفره است؟'
question_2 = 'ماهیانه حدود چند لیتر بنزین مصرف می‌کنی؟'

text_3 = 'فرض کن بنزین آزاد به یکی از قیمت‌های زیر فروخته بشه؛ یکیشون رو انتخاب کن و بگو اگر بنزین اون قیمت بشه؛ ماهیانه چند لیتر مصرف می‌کنی؟'

text_4 = 'اگر بنزین بشه %s ماهیانه چقدر مصرف می‌کنی؟'

result_pos = 'با اجرای این طرح %d تومان پول گیرتون میاد.'
result_neg = 'داری مرام میذاری و به فقرا به‌طور مستقیم و بی‌دخالت دولت %d تومان کمک می‌کنی.'

msg_state = {
    State.MAIN_MENU.value: text_1,
    State.ABOUT_US.value: text_2,
    State.Q1_SIZE.value: question_1,
    State.Q2_USE.value: question_2,
    State.Q3_P.value: text_3,
}

# reply keyboards
no_rkb = ReplyKeyboardRemove()

rkb_result = keyboard_maker([[bl_recalcule]])

rkb_state = {
    State.MAIN_MENU.value: keyboard_maker([[bl_about_us, bl_start]]),
    State.ABOUT_US.value: keyboard_maker([[bl_plan_review, bl_calcule]]),
    State.Q1_SIZE.value: no_rkb,
    State.Q2_USE.value: no_rkb,
    State.Q3_P.value: keyboard_maker([[bl_t5600, bl_t4000, bl_t3000]]),
    State.Q4_ECG: no_rkb,
    State.RESULT: rkb_result,
}
