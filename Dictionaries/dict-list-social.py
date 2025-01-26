user = {
    'username': 'johny',
    'online'  : True,
    'email'   : 'Johny@lucky.me',
    'rating'  : 10000000,
    'friends' : [
        'Marry',   # subvalues
        'Peter',
        'Helen', 
    ]

}
rating = user['rating']
if rating == 0:
   display_rating = "No likes"
elif 1 <= rating <= 999:
    display_rating = f"{rating}Likes"
elif 1000 <= rating <= 1_000_000:
    display_rating = f"{rating/1000}k Likes"
elif 1_000_000 <= rating <= 1_000_000_000:
    display_rating = f"{rating/1_000_000:.2f}M Likes"
elif 1_000_000_000 <= rating <= 10_000_000_000:
    display_rating = f"{rating/1_000_000_000:.2f}T Likes"
else:
    display_rating = "Invalid rating"


# Print user data
print(user['username']),
print(user['email']),
print("Rating:", display_rating)
print('Friends List:'),
for friend in range(len(user['friends'])):   
    print('>>', user['friends'][friend])

while True:
    new_friend = input('Add friend name (or type "stop" to finish): ')
    if new_friend.lower() == 'stop':
        break                           # Exit the loop 
    user['friends'].append(new_friend)  # Add the new friend to the list

print("\nUpdated Friends List:")
for friend in user['friends']:
    print('>>', friend)

# HW1: add some friends from keyboard <-- input + loop
# hint: list.append("value")
# HW2: if+else - arithmetic:
#      user['rating']   0 ....10 000 000 000
# 0 -> No likes
# 1 ... 999 -> Likes
# 1000 ... 1 000 000 -> (123456 likes) -> 123k likes
# 1000000+ ... 1000 000 000 -> M xx.xxLikes
# 1000 000 000 .. 10 000 000 000 -> T xx.xxLikes
