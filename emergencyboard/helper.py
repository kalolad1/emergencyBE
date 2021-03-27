from .models import Link
import random


def get_random_link():
    num = get_random_number_from_range(len(LinkSet.link_set))
    return LinkSet.link_set[num]


def get_random_number_from_range(upper_bound):
    return random.randint(0, upper_bound - 1)


class LinkSet:
    link_set = [
        'http://orig01.deviantart.net/dbc2/f/2015/101/9/5/the_world_breaks_everyone_by_cjprevett-d8pbiwz.jpg',
        'http://66.media.tumblr.com/df76ca9abf7144457417c7799887c713/tumblr_mrtk48XqgE1sem4coo1_500.jpg',
        'http://i.imgur.com/LsEonNl.jpg',
        'https://i.redd.it/u8i2b1egpcl11.png',
        'https://www.reddit.com/r/BingeEatingDisorder/comments/92w9vj/one_day_at_a_time_again_and_again_how_ive_been/',
        'https://www.reddit.com/r/BingeEatingDisorder/comments/aou736/if_youre_about_to_binge_remember_these_things/',
        'https://www.reddit.com/r/BingeEatingDisorder/comments/fhl6ac/20_days_binge_free_vs_178_days_binge_free/',
        'https://www.reddit.com/r/BingeEatingDisorder/comments/hu0y0f/on_my_bedroom_doorframe_to_read_before_i_get_to/',
        'https://www.reddit.com/r/BingeEatingDisorder/comments/fw5m16/10_months_binge_free_6_months_in_a_calorie/',
        'https://www.reddit.com/r/BingeEatingDisorder/comments/ismf5u/im_hoping_this_might_help_someone_dont_give_up/',
        'https://www.reddit.com/r/BingeEatingDisorder/comments/dy3xjt/this_just_helped_me_avoid_a_binge/',
        'https://www.reddit.com/r/BingeEatingDisorder/comments/maemk2/almost_binged_i_even_put_the_order_in_online_but/',
        'https://www.reddit.com/r/BingeEatingDisorder/comments/l4aej2/after_a_lifetime_of_bed_im_100_days_binge_free/',
        'https://i.pinimg.com/564x/49/15/f2/4915f23b9e5b06885ce474c42bd28386.jpg',
        'https://pilbox.themuse.com/image.jpg?filter=antialias&h=541&opt=1&pos=top-left&prog=1&q=keep&url=https%3A%2F%2Fcms-assets.themuse.com%2Fmedia%2Flead%2F15120.jpg%3Fv%3D73346cb41cf44e1ff68d5ab6e4dda2196615ffee&w=767',
        'https://images-na.ssl-images-amazon.com/images/I/71AUUyzfpxL.jpg',
        'https://www.reddit.com/r/BingeEatingDisorder/comments/mb4l9k/guess_what_i_did_today/',
        'https://www.reddit.com/r/BingeEatingDisorder/comments/lyeiq9/i_have_60_days_clean_today_i_have_not_binged_or/',
        'https://www.reddit.com/r/BingeEatingDisorder/comments/m26ece/food_is_not/',
        'https://pilbox.themuse.com/image.jpg?url=https%3A%2F%2Fassets.themuse.com%2Fuploaded%2Fattachments%2F13240.jpg%3Fv%3Dfc25c5c63f9affc57a40c69dfc128dcfd6b8d9d710f8b8df896a9738d6d2274a&prog=1&w=780',
        'https://i.pinimg.com/236x/e9/40/89/e9408922f1eb22880cb2d3c9e95b2317.jpg',
        'https://i.pinimg.com/originals/9b/1f/38/9b1f3876fc0fc5784fd8871485a8ab14.jpg',
    ]
