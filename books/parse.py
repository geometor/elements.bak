import frontmatter
from pathlib import Path

def under(str, under='='):
    """TODO: Docstring for under.
    :returns: TODO

    """
    return under * len(str)

root = Path('.')
for f in root.glob('**/*.md'):
    print(f)
    md = frontmatter.load(f)
    print(md['title'])
    print(under(md['title']))

#  print(post.keys())
