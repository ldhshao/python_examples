from ebooklib import epub
from urllib.request import urlopen
import lxml.html
from lxml.cssselect import CSSSelector
from lxml.etree import tostring
from lxml import etree
from datetime import date
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

def is_ancestor(ancestor, child):
    parent = child.getparent()
    while(parent is not None and parent != ancestor):
        parent = parent.getparent()
    return (parent == ancestor)

def epub_write_coolshell():
    book = epub.EpubBook()
    today = date.today()
   
    article_title = 'coolshell-%d%d%d' % (today.year, today.month, today.day)
    # set metadata
    book.set_identifier('id123456')
    book.set_title(article_title)
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
   
    title_xpath = "//h1[@class='entry-title']"
    content_xpath = "//article/div[@class='entry-content']"
    end_xpath = "//p[re:match(., '全文完')]"
    match = CSSSelector('h2.entry-title a')
    for chapter in match(tree):
        href = chapter.get('href')
        print(href)
        response = urlopen(href)
        content = response.read().decode('utf-8', 'ignore')
        response.close()
        chapter_tree = lxml.html.fromstring(content)
        title = chapter_tree.xpath(title_xpath)[0].text
        content_tree = chapter_tree.xpath(content_xpath)[0]
        if end_xpath.find('re:match') > -1:
            last_item = content_tree.xpath(end_xpath, namespaces={"re": "http://exslt.org/regular-expressions"})[0]
        else:
            last_item = content_tree.xpath(end_xpath)[0]
        b_del = False
        for item in content_tree.getchildren():
            if b_del:
                content_tree.remove(item)
            if item == last_item:
                b_del = True
        img_xpath = "//img"
        for img_item in content_tree.xpath(img_xpath):
            if is_ancestor(content_tree, img_item):
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
        chapter_content = tostring(content_tree, encoding='unicode')
        chapter_file = 'chap_%02d.xhtml' % chapter_no
    
        # create chapter
        c1 = epub.EpubHtml(title=title, file_name=chapter_file, lang='hr')
        c1.content='<html><body><h1>'+title+'</h1>'+chapter_content+'</body></html>'
        book.add_item(c1)
        chapter_tocs.append(epub.Link(chapter_file, title, title))
        book.spine.append(c1)
        chapter_no = chapter_no + 1 
        #if chapter_no > 2:
        #    break
    
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
    epub.write_epub(article_title + '.epub', book, {})

def get_image_from_url(url, img_local):
    try:
        with urlopen(url) as img_url:
            with open(img_local, 'wb') as f:
                f.write(img_url.read())
    except Exception:
        print('Error in read %s' % url)

def deal_csarticle_content(filename, content_xpath, end_xpath):
    print(content_xpath)
    with open(filename, 'rb') as f:
        tree = lxml.html.fromstring(f.read())
    content_path = etree.XPath( content_xpath)
    print(len(content_path(tree)))
    content_item = content_path(tree)[0]
    print('len of content %d' % len(content_item))
    item_cnt = 0
    del_cnt = 0
    b_del = False
    if end_xpath.find('re:match') > -1:
        last_item = content_item.xpath(end_xpath, namespaces={"re": "http://exslt.org/regular-expressions"})
    else:
        last_item = content_item.xpath(end_xpath)
    print(len(last_item))
    for item in content_item.getchildren():
        item_cnt = item_cnt + 1
        if b_del:
            content_item.remove(item)
            del_cnt = del_cnt + 1
            continue
        if item == last_item[0]:
            b_del = True
    print('item_cnt %d, del_cnt %d' % (item_cnt, del_cnt)) 
    with open('test.html', 'wb') as f:
        f.write(tostring(content_item, encoding='utf-8'))

def csarticle_handler_test():
    deal_csarticle_content('articles_19840.html', "//article/div[@class='entry-content']", "//p[re:match(., '全文完')]")

if __name__ == '__main__':
    #epub_write_test()
    epub_write_coolshell()
    #get_image_from_url('https://coolshell.cn/wp-content/uploads/2019/10/HOL_blocking.png', 'hol_blocking.png')
    #get_image_from_url('https://coolshell.cn/wp-content/uploads/2019/10/HOL_blocking.png', '/home/test/hol_blocking.png')
    #csarticle_handler_test()
