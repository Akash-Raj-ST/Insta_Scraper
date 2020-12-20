# __INSTA_SCRAPER__


__What can you do with this *INSTA_SCRAPER*?__<br>
For the given insta username you can.
- get the number of followers.
- get the number of following.
- get the number of posts.
- get the bio.
- get the list of names of followers.
- get the list of names of following.
- Download all the post and profile pic.
## <ins>How to scrap?
__All you need is__:
1. An insta account (Dummy account recommended).
2. Username of account which you want to scrap.
3. Make sure the insta account which you are trying to scrape is public, or the account is followed by dummy insta account.

*Yea it's that simple.*<br>
__First,__ Initial Setup
```
import instascrap 

track_name = '#Username of insta account which u want to scrap'
user_name = '#dummy insta username'
password = '#dummy insta password'

insta = instascrap.InstaScrap() #Create an object

insta.login(user_name, password) #Logins to instagram
```
__Lets scrap,__<br>
<ins>1.followers
```
followers = insta.followers() #No.of followers
```
```
followers_list = insta.followers_list() #List of names of followers
```
<ins>2.following
```
following = insta.following() #No.of following
```
```
followes_list = insta.following_list() #List of names of followers
```
<ins>3.Bio
```
bio = insta.bio() #Returns the bio of the track_name
```
```
#It contains optional argument 'loc'. You can use it if you want to save bio as txt document.

location ='#location where you want to save bio as txt document'

bio = insta.bio(loc=location)
```
__OR__
```
bio = inst.bio(loc='cwd') #To save bio as txt document in the current directory

```
<ins>4.Post
```
post = insta.post() #No.of post
```
__To download the post__<br>
Method 1:
```
images = insta.images() #To scrap the post
```
It scraps the image and stores it in the current directory

Method 2:<br>
It contains 2 __optional parameters__ 'loc' and 'profile'
```
loc = ' ' #location where you want to create a folder and save the post

profile = ' ' #It take value 'True' or 'False'. Assign True if you want to store profile pic in separate folder else the default value is False.

images = insta.images(loc='',profile='')
```
---
---
I have also created an [__Insta bot__]() which uses similar scraping technique to alert through discord when someone __unfollows__.
********
