#pip install rosette.api

from rosette.api import API, NameTranslationParameters, RosetteException

api = API(user_key="f72df428f4394b14984984fbbdbbe51d", service_url='https://api.rosette.com/rest/v1/')

translated_name_data = ['عبدالفتاح علي' ,'أنطوني','عبدالمنعم',' علي',' أولي جاما', 'أنس', 'عبود', 'أحمد',' عَمر' ,'عمار','آمنة','شمشون ']
new_dict = dict()

for items in translated_name_data:
    params = NameTranslationParameters()
    params["name"] = items
    params["entityType"] = "PERSON"
    params["targetLanguage"] = "eng"
    params["targetScript"] = "Latn"
    new_dict = api.name_translation(params)
    print(items ,' -> ' , new_dict['translation'])
