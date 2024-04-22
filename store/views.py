from django.shortcuts import render
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

def index(request):
    context = {}
    return render(request, 'index.html', context)

def menu(request):
    latte_flavor_choices = Latte.FLAVOR_CHOICES
    latte_size_choices = Latte.SIZE_CHOICES

    macchiato_flavor_choices = Macchiato.FLAVOR_CHOICES
    macchiato_size_choices = Macchiato.SIZE_CHOICES

    cappuccino_flavor_choices = Cappuccino.FLAVOR_CHOICES
    cappuccino_size_choices = Cappuccino.SIZE_CHOICES

    espresso_flavor_choices = Espresso.FLAVOR_CHOICES
    espresso_size_choices = Espresso.SIZE_CHOICES

    original_flavor_choices = OriginalGlaze.FLAVOR_CHOICES
    original_size_choices = OriginalGlaze.SIZE_CHOICES

    strawberry_flavor_choices = Strawberry.FLAVOR_CHOICES
    strawberry_size_choices = Strawberry.SIZE_CHOICES

    vanilla_flavor_choices = Vanilla.FLAVOR_CHOICES
    vanilla_size_choices = Vanilla.SIZE_CHOICES

    chocolate_flavor_choices = Chocolate.FLAVOR_CHOICES
    chocolate_size_choices = Chocolate.SIZE_CHOICES

    boston_cream_flavor_choices = BostonCream.FLAVOR_CHOICES
    boston_cream_size_choices = BostonCream.SIZE_CHOICES

    jelly_flavor_choices = JellyDonut.FLAVOR_CHOICES
    jelly_size_choices = JellyDonut.SIZE_CHOICES

    maple_b_flavor_choices = MapleBacon.FLAVOR_CHOICES
    maple_bacon_size_choices = MapleBacon.SIZE_CHOICES

    smore_flavor_choices = Smore.FLAVOR_CHOICES
    smore_size_choices = Smore.SIZE_CHOICES

    cruller_flavor_choices = Cruller.FLAVOR_CHOICES
    cruller_size_choices = Cruller.SIZE_CHOICES

    pbnj_flavor_choices = PBNJ.FLAVOR_CHOICES
    pbnj_size_choices = PBNJ.SIZE_CHOICES

    bb_cake_flavor_choices = BlueberryCake.FLAVOR_CHOICES
    bb_cake_size_choices = BlueberryCake.SIZE_CHOICES
    
    lattes = Latte.objects.all()
    macchiatos = Macchiato.objects.all()
    cappuccinos = Cappuccino.objects.all()
    espressos = Espresso.objects.all()
    original = OriginalGlaze.objects.all()
    strawberry = Strawberry.objects.all()
    vanilla = Vanilla.objects.all()
    chocolate = Chocolate.objects.all()
    boston_cream = BostonCream.objects.all()
    jelly_donut = JellyDonut.objects.all()
    maple_bacon = MapleBacon.objects.all()
    smores = Smore.objects.all()
    crullers = Cruller.objects.all()
    pbnjs = PBNJ.objects.all()
    blueberry_cakes = BlueberryCake.objects.all()
    
    latte_prices = {latte.size: latte.price for latte in lattes}
    macchiato_prices = {macchiato.size: macchiato.price for macchiato in macchiatos}
    cappuccino_prices = {cappuccino.size: cappuccino.price for cappuccino in cappuccinos}
    espresso_prices = {espresso.size: espresso.price for espresso in espressos}
    original_prices = {original.size: original.price for original in original}
    strawberry_prices = {strawberry.size: strawberry.price for strawberry in strawberry}
    vanilla_prices = {vanilla.size: vanilla.price for vanilla in vanilla}
    chocolate_prices = {chocolate.size: chocolate.price for chocolate in chocolate}
    boston_cream_prices = {boston_cream.size: boston_cream.price for boston_cream in boston_cream}
    jelly_prices = {jelly_donut.size: jelly_donut.price for jelly_donut in jelly_donut}
    maple_bacon_prices = {maple_bacon.size: maple_bacon.price for maple_bacon in maple_bacon}
    smore_prices = {smore.size: smore.price for smore in smores}
    cruller_prices = {cruller.size: cruller.price for cruller in crullers}
    pbnj_prices = {pbnj.size: pbnj.price for pbnj in pbnjs}
    bb_cake_prices = {blueberry_cake.size: blueberry_cake.price for blueberry_cake in blueberry_cakes}

    context = {
        'latte_flavor_choices': latte_flavor_choices,
        'latte_size_choices': latte_size_choices,
        'latte_prices': latte_prices,

        'macchiato_flavor_choices': macchiato_flavor_choices,
        'macchiato_size_choices': macchiato_size_choices,
        'macchiato_prices': macchiato_prices,

        'cappuccino_flavor_choices': cappuccino_flavor_choices,
        'cappuccino_size_choices': cappuccino_size_choices,
        'cappuccino_prices': cappuccino_prices,

        'espresso_flavor_choices': espresso_flavor_choices,
        'espresso_size_choices': espresso_size_choices,
        'espresso_prices': espresso_prices,

        'original_flavor_choices': original_flavor_choices,
        'original_size_choices': original_size_choices,
        'original_prices': original_prices,

        'strawberry_flavor_choices': strawberry_flavor_choices,
        'strawberry_size_choices': strawberry_size_choices,
        'strawberry_prices': strawberry_prices,

        'vanilla_flavor_choices': vanilla_flavor_choices,
        'vanilla_size_choices': vanilla_size_choices,
        'vanilla_prices': vanilla_prices,

        'chocolate_flavor_choices': chocolate_flavor_choices,
        'chocolate_size_choices': chocolate_size_choices,
        'chocolate_prices': chocolate_prices,

        'boston_c_flavor_choices': boston_cream_flavor_choices,
        'boston_cream_size_choices': boston_cream_size_choices,
        'boston_cream_prices': boston_cream_prices,

        'jelly_flavor_choices': jelly_flavor_choices,
        'jelly_size_choices': jelly_size_choices,
        'jelly_prices': jelly_prices,

        'maple_b_flavor_choices': maple_b_flavor_choices,
        'maple_bacon_size_choices': maple_bacon_size_choices,
        'maple_bacon_prices': maple_bacon_prices,

        'smore_flavor_choices': smore_flavor_choices,
        'smore_size_choices': smore_size_choices,
        'smore_prices': smore_prices,

        'cruller_flavor_choices': cruller_flavor_choices,
        'cruller_size_choices': cruller_size_choices,
        'cruller_prices': cruller_prices,

        'pbnj_flavor_choices': pbnj_flavor_choices,
        'pbnj_size_choices': pbnj_size_choices,
        'pbnj_prices': pbnj_prices,

        'bb_cake_flavor_choices': bb_cake_flavor_choices,
        'bb_cake_size_choices': bb_cake_size_choices,
        'bb_cake_prices': bb_cake_prices,
    }
    return render(request, 'menu.html', context)


def checkout(request):
    context = {}
    return render(request, 'checkout.html', context)



def thankyou(request):
    context = {}
    return render(request, 'thankyou.html', context)
