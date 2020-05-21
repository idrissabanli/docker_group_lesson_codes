def user_info(ad, soyad, **kwargs):
    print('ad', ad)
    print('soyad', soyad)
    print('kwargs', kwargs)
    for key, value in kwargs.items():
        print(key, value)

user_info("Idris", "Shabanli", gender="man", email="idris@gmail.com")