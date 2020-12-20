# Try reading ReadMe.md #

import instascrap

# Initial SETUP
track_name = ''  # Username of insta which you want to scrap
username = ''    # username of dummy insta account
password = ''    # password of dummy insta account
location = ''    # add location if u want to save at any particular location

insta = instascrap.InstaScrap(track_name)

insta.login(username, password)

# Followers scrap
followers = insta.followers()
print("followers", followers)

followers_list = insta.followers_list(loc=location)  # saves as a txt document in the given location
print(followers_list)

# Following scrap
following = insta.following()
print("following", following)

following_list = insta.following_list()  # Doesn't save any txt document
print(following_list)

# Scrap BIO
bio = insta.bio(loc='cwd')  # Saves bio as txt document in the current directory
print(bio)

# Scrap POST
post = insta.post()
print("Post", post)

# Download all post
insta.images(profile=True)  # Saves profile picture in separate folder
                            # You can add 'loc' parameter too if you want to store it in particular folder
