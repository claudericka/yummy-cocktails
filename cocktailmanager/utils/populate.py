from cocktailmanager.models import Cocktail, User

def populate():
    clean_all()
    billytheking = User(first_name="Billy",
                        last_name="The King",
                        username='BKing',
                        password="1234")
    billytheking.save()
    cocktail = Cocktail(
        name="Mojito",
        glass="Glass type",
        method="shaker",
        difficulty=3,
        user=billytheking,
        price="cheap"
    )
    cocktail.save()


def clean_all():
    User.objects.all().delete()
    Cocktail.objects.all().delete()