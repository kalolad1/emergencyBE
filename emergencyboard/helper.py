from .models import Link
import random


def get_random_link():
    links = Link.objects.all()
    num = get_random_number_from_range(len(links))
    return Link.objects.get(id=num)


def get_random_number_from_range(upper_bound):
    return random.randint(0, upper_bound)
