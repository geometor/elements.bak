import frontmatter
from pathlib import Path
from m2r import convert

def under(str, under='='):
    return under * len(str)

root = Path('01/propositions')
for f in root.glob('**/*.md'):
    print(f)
    rf = f.parent / 'index.rst'
    md = frontmatter.load(f)
    with rf.open(mode='w') as newf:
        title = md['subtitle'] if md['subtitle'] else md['title']
        newf.write(title)
        newf.write('\n')
        newf.write(under(title))
        newf.write('\n')
        newf.write('\n')
        if md['taxonomy']['category']:
            cats = ', '.join(md['taxonomy']['category'])
            newf.write('.. index:: ' + cats)
            newf.write('\n')
            newf.write('\n')
        for img in f.parent.glob('*.png'):
            newf.write('.. image:: ' + str(img.name))
            newf.write('\n')
            newf.write('   :align: right')
            newf.write('\n')
            newf.write('   :width: 300px')
            newf.write('\n')
            newf.write('\n')


        content = md.content.replace('===', '')
        content = convert(content)
        newf.write(md.content)
#  print(post.keys())
