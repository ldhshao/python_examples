from ebooklib import epub
from urllib.request import urlopen
import lxml.html
from lxml.cssselect import CSSSelector
from lxml.etree import tostring
import re

def epub_write_test():
    book = epub.EpubBook()
    
    # set metadata
    book.set_identifier('id123456')
    book.set_title('Sample book')
    book.set_language('en')
    
    book.add_author('Author Authorowski')
    book.add_author('Danko Bananko', file_as='Gospodin Danko Bananko', role='ill', uid='coauthor')
    
    # create chapter
    c1 = epub.EpubHtml(title='Intro', file_name='chap_01.xhtml', lang='hr')
    c1.content=u'<h1>Intro heading</h1><p>Zaba je skocila u baru.</p>'
    # add chapter
    book.add_item(c1)

    c2 = epub.EpubHtml(title='Chap 1', file_name='chap_02.xhtml', lang='hr')
    c2.content=u'<h1>Chap 1</h1><p>This is chap 1 content.</p>'
    book.add_item(c2)
    
    c3 = epub.EpubHtml(title='Chap 2', file_name='chap_03.xhtml', lang='hr')
    c3.content=u'<h1>Chap 2</h1><p>This is chap 2 content.</p>'
    book.add_item(c3)
    
    c4 = epub.EpubHtml(title='Chap 3', file_name='chap_04.xhtml', lang='hr')
    c4.content=u'<h1>Chap 3</h1><p>This is chap 3 content.</p>'
    book.add_item(c4)
    
    # define Table Of Contents
    #book.toc = (epub.Link('chap_01.xhtml', 'Introduction', 'intro'),
    #             (epub.Section('Simple book'),
    #             (c1, ))
    #            )
    book.toc = (epub.Link('chap_01.xhtml', 'Introduction', 'intro'),
                epub.Link('chap_02.xhtml', 'Chap 1', 'Chap 1'),
                epub.Link('chap_03.xhtml', 'Chap 2', 'Chap 2'),
                epub.Link('chap_04.xhtml', 'Chap 3', 'Chap 3')
                )
    
    # add default NCX and Nav file
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    
    # define CSS style
    style = 'BODY {color: white;}'
    nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
    
    # add CSS file
    book.add_item(nav_css)
    
    # basic spine
    book.spine = ['nav', c1, c2, c3, c4]
    
    # write to the file
    epub.write_epub('test.epub', book, {})

def epub_write_coolshell():
    book = epub.EpubBook()
    
    # set metadata
    book.set_identifier('id123456')
    book.set_title('Coolshell 20191014')
    book.set_language('en')
    
    book.add_author('Chen hao')

    #read html; fetch the title; fetch the text content
    response = urlopen('https://coolshell.cn/')
    content = response.read().decode('utf-8', 'ignore')
    response.close()
    with open('coolshell.html', 'w') as f:
        f.write(content)
    tree = lxml.html.fromstring(content)
        
    chapter_tocs = []
    book.spine = ['nav']
    chapter_no = 1
    
    match = CSSSelector('h2.entry-title a')
    for chapter in match(tree):
        href = chapter.get('href')
        print(href)
        response = urlopen(href)
        content = response.read().decode('utf-8', 'ignore')
        response.close()
        chapter_tree = lxml.html.fromstring(content)
        match_title = CSSSelector('h1.entry-title')
        title = match_title(chapter_tree)[0].text
        match_content = CSSSelector('div.entry-content')
        content_tree = match_content(chapter_tree)[0]
        match_img = CSSSelector('img')
        for img_item in match_img(content_tree):
            img_url = img_item.get('src')
            listtmp = re.split('/+', img_url)
            jpg_name = listtmp[-1]
            img_local = '%02d%s' % (chapter_no, jpg_name)
            print('img ' + img_url + ' local ' + img_local)
            get_image_from_url(img_url, img_local)
            img_item.set('src', img_local)
            #add the image to book
            img_item = epub.EpubImage()
            img_item.file_name = img_local
            try:
                img_item.content = open(img_local, 'rb').read()
            except Exception:
                print('Error open %s' % img_local)
            book.add_item(img_item)
        chapter_content = tostring(match_content(chapter_tree)[0], encoding='unicode')
        chapter_file = 'chap_%02d.xhtml' % chapter_no
    
        # create chapter
        c1 = epub.EpubHtml(title=title, file_name=chapter_file, lang='hr')
        c1.content='<html><body><h1>'+title+'</h1>'+chapter_content+'</body></html>'
        book.add_item(c1)
        chapter_tocs.append(epub.Link(chapter_file, title, title))
        book.spine.append(c1)
        chapter_no = chapter_no + 1 
        if chapter_no > 2:
            break
    
    match = CSSSelector('div.entry-content')
    chapter_content = tostring(match(tree)[0], encoding='unicode')
    

    # define Table Of Contents
    book.toc = tuple(chapter_tocs)
    #book.toc = (epub.Link('chap_01.xhtml', 'Introduction', 'intro'),
    #             (epub.Section('Simple book'),
    #             (c1, ))
    #            )
    #book.toc = (epub.Link('chap_01.xhtml', chapter_title, chapter_title)
    #            )
    
    # add default NCX and Nav file
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    
    # define CSS style
    style = 'BODY {color: white;}'
    nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
    
    # add CSS file
    book.add_item(nav_css)
    
    # basic spine
    #book.spine = ['nav', c1]
    
    # write to the file
    epub.write_epub('coolshell.epub', book, {})

def get_image_from_url(url, img_local):
    try:
        with urlopen(url) as img_url:
            with open(img_local, 'wb') as f:
                f.write(img_url.read())
    except Exception:
        print('Error in read %s' % url)

if __name__ == '__main__':
    #epub_write_test()
    epub_write_coolshell()
    #get_image_from_url('https://coolshell.cn/wp-content/uploads/2019/10/HOL_blocking.png', 'hol_blocking.png')
    #get_image_from_url('https://coolshell.cn/wp-content/uploads/2019/10/HOL_blocking.png', '/home/test/hol_blocking.png')
