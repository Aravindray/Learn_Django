'''Let's look out how TextChoice class is working

from myblog.models import Post

Post.Status.choices # [('DF', 'Draft'), ('PB', 'Published')]

Post.Status.labels # ['Draft', 'Published']

Post.Status.values # ['DF', 'PB']

Post.Status.names # ['DRAFT', 'PUBLISHED']
'''

'''
Let's create a new post using Django ORM - Object-Relational Mapper in shell

from django.contrib.auth.models import User
from myblog.models import Post

# Create

user = User.objects.get(username = 'workoutuser')
post = Post(title = 'Created using Django ORM',
            slug = 'created-using-django-orm',
            body = 'This is post body.',
            author = user)

post.save() # don't forget to save the changes

# Update

post.title = 'New Post Name'
post.save()

# Read

get() method retrieve single object whereas all() method retrieve all objects

# Filter

Post.objects.filter(publish__year = 2024, author__username = 'workoutuser')

wonder __year or __username those are designed by django team, IDK

There are 2 types to apply filter one separate by comma, or filter chaining

Post.objects.filter('condition 1', 'condition 2')
or
Post.objects.filter('condition 1').filter('condition 2')

# Delete

'''
