from nose.tools import eq_

from . import util
from .. import entity


def test_normalize():
    wb_doc = util.load_blob('Q7251')
    Q7251 = entity.normalize(wb_doc)

    eq_({lang for lang in Q7251.labels},
        {'ur', 'arz', 'ka', 'gsw', 'fi', 'tg', 'be', 'ru', 'lt', 'mr', 'yue',
         'hif', 'en-ca', 'la', 'eu', 'lb', 'da', 'th', 'de-ch', 'yo', 'ga',
         'mwl', 'pa', 'ckb', 'az', 'sq', 'kk', 'is', 'ar', 'gl', 'vi', 'new',
         'te', 'ht', 'sk', 'be-tarask', 'sh', 'fr', 'scn', 'ja', 'uk', 'pt-br',
         'ba', 'nl', 'et', 'co', 'ko', 'ku', 'cs', 'en', 'fa', 'io', 'br',
         'lij', 'eo', 'de', 'it', 'as', 'sl', 'ilo', 'pnb', 'sv', 'el', 'mt',
         'tt', 'zh', 'or', 'pam', 'hu', 'gan', 'mn', 'ce', 'ca', 'oc', 'yi',
         'id', 'sw', 'nb', 'sco', 'jbo', 'ro', 'ta', 'mg', 'gd', 'mk', 'nan',
         'zh-cn', 'gu', 'fur', 'tl', 'cy', 'bs', 'rue', 'lmo', 'fy', 'ms',
         'hr', 'bg', 'en-gb', 'pms', 'tr', 'bn', 'hy', 'sa', 'pl', 'kn', 'an',
         'sgs', 'hi', 'fo', 'es', 'vo', 'uz', 'war', 'nn', 'pt', 'ml', 'af',
         'jv', 'sr', 'li', 'ast', 'sah', 'zh-hans', 'he', 'lv'})
    eq_({label for label in Q7251.labels.values()},
        {'Алан Тюрінг', 'ਅਲਾਨ ਟੂਰਿੰਗ', 'অ্যালান টুরিং', 'एलेन त्युरिङ्ग', 'ಅಲೆನ್ ಟ್ಯೂರಿಂಗ್',  # noqa
         'ଆଲାନ ଟ୍ୟୁରିଙ୍ଗ', 'Ալան Թյուրինգ', 'Alan Türinq',
         'الان تورينج', 'آلان تورنج', 'Алан Тюринг', 'אלן טיורינג', 'Alan Tyuring',  # noqa
         'ئالان تیورینگ', 'Элан Т’юрынг', 'ალან ტიურინგი',
         'Алан Матисон Тьюринг', 'Алън Тюринг', 'الان ٹورنگ',
         'అలాన్ ట్యూరింగ్\u200c', 'Тьюринг, Алан', 'Alans Tjūrings', '圖靈',
         'ઍલન ટ્યુરિંગ', 'ایلن تورنگ', 'עלן טיורינג', 'एलेन ट्यूरिंग', 'ॲलन ट्युरिंग',  # noqa
         'Alan Mathison Turing', 'এলান ট্যুৰিং', 'آلن تورینگ', 'അലൻ ട്യൂറിംഗ്',
         '.alan turin', 'Alanus Mathison Turing', 'Алан Матысан Цьюрынг',
         'Alan M. Turing', 'Алан Тюрінґ', 'Alans Tiorėngs',
         'Алан Матисон Тюринг', 'Алан Тьюринг', 'அலன் டூரிங்', '艾伦·图灵',
         '앨런 튜링', 'Алан Тјуринг', 'แอลัน ทัวริง', 'アラン・チューリング',
         'Alanu Turing', 'Άλαν Τούρινγκ', 'Alan TURING', 'Tyuring',
         'Alan Turing'})

    eq_({lang for lang in Q7251.descriptions},
        {'fa', 'en', 'sv', 'as', 'nb', 'pam', 'sk', 'de', 'zh-cn', 'zh', 'nl',
         'es', 'gl', 'ilo', 'ko', 'zh-hans', 'da', 'fr', 'pl', 'ru', 'it',
         'nn'})
    eq_(Q7251.descriptions['en'],
        "British mathematician, logician, cryptanalyst, and computer " +
        "scientist")

    eq_({lang for lang in Q7251.aliases},
        {'be-tarask', 'ja', 'jbo', 'ru', 'fr', 'ko', 'it', 'de', 'en'})
    eq_(set(Q7251.aliases['en']),
        {'Alan Mathison Turing'})

    eq_({dbname
         for dbname, sitelink in Q7251.sitelinks.items()
         if len(sitelink['badges']) > 0},
        {'ruwiki', 'enwiki', 'lawiki', 'aswiki'})

    wb_doc = util.load_blob('P21')
    P21 = entity.normalize(wb_doc)

    eq_({lang for lang in P21.labels},
        {'ckb', 'br', 'eo', 'an', 'ilo', 'zh-sg', 'mg', 'zh-hans', 'fy', 'pl',
         'rm', 'sv', 'be-tarask', 'en-ca', 'ht', 'min', 'io', 'ksh', 'nb',
         'ku-latn', 'ca', 'ta', 'fr', 'be', 'ka', 'gu', 'cy', 'kk', 'et',
         'zh-mo', 'eu', 'tg', 'bg', 'uz', 'uk', 'vo', 'ar', 'kn', 'ja', 'hu',
         'ne', 'pt-br', 'bn', 'oc', 'it', 'ia', 'se', 'zh-tw', 'mk', 'nds-nl',
         'cs', 'sr-ec', 'fa', 'da', 'zh-my', 'ko', 'zh-hant', 'ms', 'de', 'ga',
         'as', 'es', 'sl', 'sr', 'lv', 'sk', 'tr', 'lb', 'frr', 'sr-el', 'hy',
         'ce', 'is', 'ro', 'fo', 'sco', 'tokipona', 'yi', 'el', 'mzn', 'en-gb',
         'or', 'scn', 'mai', 'pt', 'gl', 'sq', 'hr', 'ru', 'tl', 'en', 'fi',
         'nds', 'ml', 'pa', 'nl', 'nn', 'ba', 'gsw', 'lt', 'la', 'te', 'hi',
         'he', 'bs', 'zh-hk', 'zh', 'af', 'ast', 'mr', 'vi', 'th', 'yue',
         'zh-cn', 'id'})
    eq_({label for label in P21.labels.values()},
        {'Slach', 'लिङ्ग', 'lahy-vavy', 'sexe', 'sekse of geslacht', 'nem',
         'gnéis nó inscne', 'lytis', 'стать', 'sexus', '性別', 'pohlaví',
         'sexu', 'பாலினம்', 'стен-боьршалла', 'geslag', 'sexo', 'Geschlecht',
         'sèxe', 'Reizh pe jener', 'sex', 'ڕەگەز', 'gen', 'ಲಿಂಗ', 'ҷинс',
         'sukupuoli', 'sexua edo generoa', 'sekso', 'ଲିଙ୍ଗ', 'zayend', 'লিঙ্গ',
         'pol', 'sèks', 'ਲਿੰਗ', 'cinsiyet', 'gjinia', 'מין', 'sesso o genere',
         'جنسیت', 'płeć', 'Geslecht (Person)', 'meli anu mije', 'sugu', 'เพศ',
         '성별', 'jinsi', 'sessu o gèniri', 'giới tính', 'սեռ', 'სქესი',
         'sexuo', 'spol', 'jinih kalamin', 'sexe ou genre', 'kasarian',
         'लिंग', 'లింగం', 'pohlavie', 'kyn', 'пол', 'jantina', 'køn',
         'жыныс', 'sexo o género', 'الجنس', 'sex or gender',
         'et Jeschlääsch', 'લિંગ અથવા જાતિ', '性别', 'jenis kelamin',
         'kjønn', 'стаць', 'rhyw', 'sexo ou género', 'kön',
         'Gschlächt', 'dzimums', 'schlattaina', 'soahkabealli', 'φύλο',
         'geslacht', 'енесе', 'ലിംഗം'})

    eq_({lang for lang in P21.descriptions},
        {'hu', 'lv', 'ru', 'id', 'da', 'pl', 'kk', 'nl', 'tl', 'zh-hk', 'fi',
         'sq', 'hi', 'tr', 'cs', 'ta', 'sr-ec', 'ba', 'rm', 'ksh', 'scn', 'hr',
         'zh-hant', 'en-ca', 'zh-hans', 'eu', 'ka', 'eo', 'fa', 'uk', 'br',
         'ko', 'gu', 'sv', 'it', 'zh', 'nds', 'ml', 'ja', 'is', 'fo', 'en-gb',
         'ilo', 'he', 'ca', 'bg', 'zh-tw', 'ast', 'or', 'sr', 'de', 'vi',
         'sr-el', 'nb', 'fr', 'pt-br', 'en', 'gl', 'cy', 'ar', 'es', 'el',
         'mzn', 'be-tarask', 'pt'})
    eq_(P21.descriptions['en'],
        'sexual identity of subject: male (Q6581097), female (Q6581072), ' +
        'intersex (Q1097630), transgender female (Q1052281), transgender ' +
        'male (Q2449503). Animals: male animal (Q44148), female animal ' +
        '(Q43445). Groups of same gender use "subclass of" (P279)')

    eq_({lang for lang in P21.aliases},
        {'vi', 'eu', 'ast', 'cs', 'he', 'fr', 'gu', 'ta', 'pt', 'or', 'ko',
         'en-gb', 'tokipona', 'fa', 'ar', 'hu', 'ga', 'ka', 'an', 'en', 'zh',
         'it', 'es', 'nl', 'en-ca', 'be-tarask', 'is', 'lt', 'af', 'zh-hans',
         'ca', 'ba'})
    eq_(set(P21.aliases['en']),
        {'intersex', 'biological sex', 'gender', 'sex', 'gender identity',
         'female', 'woman', 'male', 'man', 'gender expression'})

    eq_({dbname
         for dbname, sitelink in P21.sitelinks.items()
         if len(sitelink['badges']) > 0},
        set())

    wb_doc = util.load_blob('Q1700481')
    Q1700481 = entity.normalize(wb_doc)

    eq_({lang for lang in Q1700481.labels},
        {'zh', 'cy', 'nb', 'ca', 'it', 'pt', 'es', 'zh-cn', 'fa', 'fr', 'da',
         'ja', 'en', 'de', 'zh-hant', 'pl', 'nl'})
    eq_({label for label in Q1700481.labels.values()},
        {'ミネアポリス美術館', 'Sefydliad Celf Minneapolis',
         'Instituto de Artes de Minneapolis', '明尼阿波利斯美術館',
         'موسسه هنر مینیاپولیس', 'Minneapolis Institute of Art',
         '明尼阿波利斯艺术学院', 'Instituto de Arte de Mineápolis',
         '明尼阿波利斯藝術學院'})

    eq_({lang for lang in Q1700481.descriptions},
        {'cy', 'nl', 'en', 'fr'})
    eq_(Q1700481.descriptions['en'],
        'art museum in Minneapolis, Minnesota')

    eq_({lang for lang in Q1700481.aliases},
        {'ca', 'da', 'fr', 'de', 'pl', 'en', 'it', 'nl'})
    eq_(set(Q1700481.aliases['en']),
        {'ARTSMIA', 'Minneapolis Institute of Arts'})

    eq_({dbname
         for dbname, sitelink in Q1700481.sitelinks.items()
         if len(sitelink['badges']) > 0},
        set())

    wb_doc = util.load_blob('Q18627581')
    Q18627581 = entity.normalize(wb_doc)

    eq_({lang for lang in Q18627581.labels},
        {'ca', 'gsw', 'sl', 'en', 'min', 'vi', 'li', 'lb', 'vls', 'sw',
         'en-gb', 'ms', 'nl', 'eu', 'gd', 'en-ca', 'pcd', 'nn', 'pt', 'sc',
         'wo', 'pms', 'an', 'mg', 'scn', 'nb', 'ast', 'de-at', 'sr-el',
         'ie', 'lij', 'ia', 'et', 'da', 'sk', 'co', 'is', 'bar', 'eo',
         'vo', 'ga', 'it', 'io', 'fi', 'sv', 'hu', 'fur', 'gl', 'zu',
         'de', 'pt-br', 'br', 'kg', 'vec', 'pl', 'cs', 'frp', 'de-ch',
         'rm', 'es', 'cy', 'nrm', 'nds-nl', 'id', 'fr', 'sco', 'ro',
         'hr', 'oc', 'nds', 'wa', 'nap', 'af'})
    eq_({label for label in Q18627581.labels.values()},
        {'Aaron Halfaker'})

    eq_({lang for lang in Q18627581.descriptions},
        {'en-gb', 'nl', 'en'})
    eq_(Q18627581.descriptions['en'],
        'American computer scientist')

    eq_({lang for lang in Q18627581.aliases},
        set())

    eq_({dbname
         for dbname, sitelink in Q18627581.sitelinks.items()
         if len(sitelink['badges']) > 0},
        set())
