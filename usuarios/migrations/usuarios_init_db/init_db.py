from usuarios.models import Usuario
from datetime import date


# Execute this script when you want to initialize your database's table usuarios_usuario
# with some base records, note that 'linkage' and 'josemhenao' have superuser privileges

# 1) run shell:
#    python manage.py shell
# 2) Import this script
#    from usuarios.migrations.usuarios_init_db import init_db
# 3) Call the function
#    init_db.insert_usuarios()


def insert_usuarios():
    linkage = Usuario(username='linkage', email='linkage@linkage.com', birth_date=date.today(), is_staff=True,
                         is_superuser=True)
    linkage.set_password('linkage123')
    linkage.save()

    josemhenao = Usuario(username='josemhenao', email='josemhenao@linkage.com', birth_date=date.today(), is_staff=True,
                         is_superuser=True)
    josemhenao.set_password('josemhenao123')
    josemhenao.save()

    mfhenao88 = Usuario(username='mfhenao88', email='mfhenao88@linkage.com', birth_date=date.today())
    mfhenao88.set_password('mfhenao88123')
    mfhenao88.save()

    juanjosegdoj = Usuario(username='juanjosegdoj', email='juanjosegdoj@linkage.com', birth_date=date.today())
    juanjosegdoj.set_password('juanjosegdoj123')
    juanjosegdoj.save()

    marthacardonae = Usuario(username='marthacardonae', email='marthacardonae@linkage.com', birth_date=date.today())
    marthacardonae.set_password('marthacardonae123')
    marthacardonae.save()

    usuario1 = Usuario(username='usuario1', email='usuario1@linkage.com', birth_date=date.today())
    usuario1.set_password('usuario1123')
    usuario1.save()

    usuario2 = Usuario(username='usuario2', email='usuario2@linkage.com', birth_date=date.today())
    usuario2.set_password('usuario2123')
    usuario2.save()

    usuario3 = Usuario(username='usuario3', email='usuario3@linkage.com', birth_date=date.today())
    usuario3.set_password('usuario3123')
    usuario3.save()

    usuario4 = Usuario(username='usuario4', email='usuario4@linkage.com', birth_date=date.today())
    usuario4.set_password('usuario4123')
    usuario4.save()

    usuario5 = Usuario(username='usuario5', email='usuario5@linkage.com', birth_date=date.today())
    usuario5.set_password('usuario5123')
    usuario5.save()

    usuario6 = Usuario(username='usuario6', email='usuario6@linkage.com', birth_date=date.today())
    usuario6.set_password('usuario6123')
    usuario6.save()
