import frontmatter
from pathlib import Path
from m2r import convert

def under(str, under='='):
    return under * len(str)

root = Path('01/definitions')
for f in root.glob('**/*.md'):
    print(f)
    rf = f.parent / 'index.rst'
    md = frontmatter.load(f)
    print(md['title'])
    print(under(md['title']))
    with rf.open(mode='w') as newf:
        newf.write(md['title'])
        newf.write('\n')
        newf.write(under(md['title']))
        newf.write('\n')
        newf.write('\n')
        if md['taxonomy']['category']:
            cats = ','.join(md['taxonomy']['category'])
            newf.write('.. index:: ' + cats)
            newf.write('\n')
            newf.write('\n')

        content = md.content.replace('===', '')
        content = convert(content)
        newf.write(md.content)
#  print(post.keys())
