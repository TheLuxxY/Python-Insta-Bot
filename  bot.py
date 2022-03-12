from instapy import InstaPy
from instapy import smart_run

user = "aionwashere"
my_pass = "game2loft"

session = InstaPy(username = user,
                                 password = my_pass,
                                 headless_browser = False)
                                 
with smart_ran(session):
    session.set_realtionship_bound(enabled = True,
	                                       delimit_by_numbers = True,
	                                       max_followers = 500,
	                                       min_followers = 30
	                                       min_following = 10)
	                                      
    session.set_do_follow(True, percentage = 100)	
    session.set_dont_like(['nsfw', 'kai ,'' ford'])  
    session.like_by_tage(['bmw', 'Thar'], amount = 10 )                                  