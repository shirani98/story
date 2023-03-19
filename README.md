# tag
list of all tags by pagination : http://127.0.0.1:8000/api/v1/tag/?page=1
search in tags : http://127.0.0.1:8000/api/v1/tag/?q
add a tag : http://127.0.0.1:8000/api/v1/tag/add
delete a tag = http://127.0.0.1:8000/api/v1/tag/change/'id' (by admin)
update a tag = http://127.0.0.1:8000/api/v1/tag/change/'id' (by admin)

# story
list of all story by pagination : http://127.0.0.1:8000/api/v1/story/list/?page=1
list of user story : 127.0.0.1:8000/api/v1/story/list/?username='username'
add a story : http://127.0.0.1:8000/api/v1/story/add/
update a story : http://127.0.0.1:8000/api/v1/story/change/'slug'
delete a story : http://127.0.0.1:8000/api/v1/story/change/'slug'

# saved story
list of saved story by pagination : http://127.0.0.1:8000/api/v1/story/save-story-list/
saved story : http://127.0.0.1:8000/api/v1/story/save-story/'slug'
delete saved story : http://127.0.0.1:8000/api/v1/story/delete-saved-story/'slug'

# comment
list all comment by pagination: http://127.0.0.1:8000/api/v1/comment/list/ (for admin)
list of all story comment : http://127.0.0.1:8000/api/v1/comment/list/?storyslug='slug'
add a comment : http://127.0.0.1:8000/api/v1/comment/add/'story-slug'
update a comment : http://127.0.0.1:8000/api/v1/comment/change/'comment-id'
delete a comment : http://127.0.0.1:8000/api/v1/comment/change/'comment-id'
list of user comments : http://127.0.0.1:8000/api/v1/comment/user-comment/
list of story comments : http://127.0.0.1:8000/api/v1/comment/story-comment/'story-slug'

# category
list of all story : http://127.0.0.1:8000/api/v1/category/list/
add a category : http://127.0.0.1:8000/api/v1/category/add/
update a category : http://127.0.0.1:8000/api/v1/category/change/'id'
delete a category : http://127.0.0.1:8000/api/v1/category/change/'id'

# search
search with body, brief, alias name : http://127.0.0.1:8000/api/v1/story/search/?q='a'
search category : http://127.0.0.1:8000/api/v1/story/search/?category='a'
search user : http://127.0.0.1:8000/api/v1/story/search/?user='a'
search tag : http://127.0.0.1:8000/api/v1/story/search/?user='tag'


# account
registere user : http://127.0.0.1:8000/api/v1/accounts/registration/
activate user : http://127.0.0.1:8000/api/v1/accounts/activation/'token' 
show last 10 users : http://127.0.0.1:8000/api/v1/accounts/last-user
list of all users : http://127.0.0.1:8000/api/v1/accounts/list/ (for admin)
change password by admin : http://127.0.0.1:8000/api/v1/accounts/change-password-admin/'id'
disable user by admin : http://127.0.0.1:8000/api/v1/accounts/disable-user-admin/'id'
search in user accounts by admin : http://127.0.0.1:8000/api/v1/accounts/list/?q='str'

# jwt
get token : http://127.0.0.1:8000/api/token/
refresh token : http://127.0.0.1:8000/api/token/refresh/
