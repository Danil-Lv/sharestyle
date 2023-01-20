from transliterate import slugify
from datetime import datetime


def make_slug(text):
    return f'{slugify(text, "uk")}-{str(int(datetime.timestamp(datetime.today())))}'















# def rus_to_eng():
#     rus_to_eng_dict = {
#         'а': 'a',
#         'б': 'b',
#         'в': 'v',
#         'г': 'g',
#         'д': 'd',
#         'е': 'a',
#         'ё': 'a',
#         'ж': 'a',
#         'з': 'a',
#         'и': 'a',
#         'й': 'a',
#         'к': 'a',
#         'л': 'a',
#         'м': 'a',
#         'н': 'a',
#         'о': 'a',
#         'п': 'a',
#         'р': 'a',
#         'с': 'а',
#         'т': 'a',
#         'у': 'a',
#         'ф': 'a',
#         'х': 'a',
#         'ц': 'a',
#         'ч': 'a',
#         'ш': 'a',
#         'щ': 'a',
#         'ъ': 'a',
#         'ы': 'a',
#         'ь': 'a',
#         'э': 'a',
#         'ю': 'a',
#         'я': 'a',
#
#
#     }