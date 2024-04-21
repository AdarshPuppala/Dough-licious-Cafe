from django.contrib import admin

# Register your models here.
from .models import Latte
from .models import Macchiato
from .models import Cappuccino
from .models import Espresso
from .models import OriginalGlaze
from .models import Strawberry
from .models import Vanilla
from .models import Chocolate
from .models import BostonCream
from .models import JellyDonut
from .models import MapleBacon
from .models import Smore
from .models import Cruller
from .models import PBNJ
from .models import BlueberryCake

admin.site.register(Latte)
admin.site.register(Macchiato)
admin.site.register(Cappuccino)
admin.site.register(Espresso)
admin.site.register(OriginalGlaze)
admin.site.register(Strawberry)
admin.site.register(Vanilla)
admin.site.register(Chocolate)
admin.site.register(BostonCream)
admin.site.register(JellyDonut)
admin.site.register(MapleBacon)
admin.site.register(Smore)
admin.site.register(Cruller)
admin.site.register(PBNJ)
admin.site.register(BlueberryCake)