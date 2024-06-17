import os
from xml.etree.ElementTree import Element, SubElement, tostring

def generate_sitemap(domain, directory):
   urlset = Element('urlset')
   urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')

   for root, dirs, files in os.walk(directory):
       for file in files:
           if file.endswith('.html'):
               html_file = os.path.join(root, file)
               url = SubElement(urlset, 'url')
               loc = SubElement(url, 'loc')
               
               if file == 'index.html' and root == directory:
                   loc.text = domain
               else:
                   relative_path = os.path.relpath(html_file, directory)
                   url_path = relative_path.replace('\\', '/')
                   loc.text = f"{domain}/{url_path}"

   sitemap_xml = tostring(urlset, encoding='utf-8').decode('utf-8')
   return sitemap_xml

# ドメインとローカルのフォルダーをユーザーから入力
domain = input("ドメインを入力してください: ")
folder = input("ローカルのフォルダーパスを入力してください: ").replace('\\', '\\\\')

# サイトマップを生成
sitemap = generate_sitemap(domain, folder)

# サイトマップをファイルに保存
with open('sitemap.xml', 'w', encoding='utf-8') as file:
   file.write(sitemap)