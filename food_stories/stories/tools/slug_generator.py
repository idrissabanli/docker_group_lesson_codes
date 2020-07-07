  
from time import time


# Custom slugify function
def slugify(title):
    symbol_mapping = (
        (' ', '-'),
        ('.', '-'),
        (',', '-'),
        ('!', '-'),
        ('?', '-'),
        ("'", '-'),
        ('"', '-'),
        ('ə', 'e'),
        ('ı', 'i'),
        ('ö', 'o'),
        ('ğ', 'g'),
        ('ü', 'u'),
        ('ş', 's'),
        ('ç', 'c'),
        ('&', '-'),
    )

    title_url = title.strip().lower()

    for before, after in symbol_mapping:
        title_url = title_url.replace(before, after)

    return title_url