'''Let's look out how TextChoice class is working

from myblog.models import Post

Post.Status.choices # [('DF', 'Draft'), ('PB', 'Published')]

Post.Status.labels # ['Draft', 'Published']

Post.Status.values # ['DF', 'PB']

Post.Status.names # ['DRAFT', 'PUBLISHED']
'''
