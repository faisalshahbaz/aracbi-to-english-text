#pip install googletrans
#pip install langdetect
#https://py-googletrans.readthedocs.io/en/latest/
from googletrans import Translator
translator = Translator(service_urls=[
      'translate.google.com'])

translations = translator.translate(['عبدالفتاح، علي ،أنطوني، عبد المنعم، علي، أولي جاما، أنس، عبود، أحمد، عَمر، عمار، شمشون علي، سليمان علي'], dest='en')
for translation in translations:
    print(translation.origin, ' -> ', translation.text)
