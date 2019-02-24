from .models import Link
import random


def get_random_link():
    num = get_random_number_from_range(len(LinkSet.link_set))
    return LinkSet.link_set[num]


def get_random_number_from_range(upper_bound):
    return random.randint(0, upper_bound)


class LinkSet:
    link_set = [
        'https://www.reddit.com/r/loseit/comments/ap3rcm/donated_an_entire_wardrobe_yesterday_nsv/',
        'http://orig01.deviantart.net/dbc2/f/2015/101/9/5/the_world_breaks_everyone_by_cjprevett-d8pbiwz.jpg',
        'http://66.media.tumblr.com/df76ca9abf7144457417c7799887c713/tumblr_mrtk48XqgE1sem4coo1_500.jpg',
        'http://i.imgur.com/LsEonNl.jpg',
        'https://i.redd.it/u8i2b1egpcl11.png',
        'https://www.reddit.com/r/BingeEatingDisorder/comments/8cvg9j/old_binge_habits_die_hard_even_when_youre_a/',
        'https://www.reddit.com/r/BingeEatingDisorder/comments/92w9vj/one_day_at_a_time_again_and_again_how_ive_been/',
        'https://www.reddit.com/r/BingeEatingDisorder/comments/aou736/if_youre_about_to_binge_remember_these_things/',
    ]
