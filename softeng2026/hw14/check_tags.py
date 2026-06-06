import os, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'do_it_django_prj.settings')
sys.stdout.reconfigure(encoding='utf-8')

import django
django.setup()

from blog.models import Post, Tag

print("=== Tags in DB ===")
for t in Tag.objects.all():
    count = t.post_set.count()
    print(f"Tag id={t.pk}, name={t.name}, slug={t.slug}, connected posts={count}")

print("\n=== Posts and their tags ===")
for p in Post.objects.all():
    tag_names = [tg.name for tg in p.tags.all()]
    print(f"Post {p.pk}: {p.title} => tags: {tag_names}")
