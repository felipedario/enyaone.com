
import os
import re
import cssmin
from PIL import Image
from bs4 import BeautifulSoup

def optimize_assets(html_files, css_file):
    # --- 1. CSS Optimization ---
    minified_css_file = os.path.splitext(css_file)[0] + ".min.css"
    if os.path.exists(css_file):
        with open(css_file, 'r', encoding='ISO-8859-1') as f:
            css_content = f.read()

        css_content = re.sub(r'@import url\\(.*?\\);', '', css_content)
        minified_css = cssmin.cssmin(css_content)

        with open(minified_css_file, 'w', encoding='ISO-8859-1') as f:
            f.write(minified_css)
        print(f"Minified {css_file} to {minified_css_file}")
    else:
        print(f"CSS file not found: {css_file}")
        return

    # --- 2. HTML and Image Optimization ---
    for html_file in html_files:
        if not os.path.exists(html_file):
            print(f"HTML file not found: {html_file}")
            continue

        with open(html_file, 'r', encoding='ISO-8859-1') as f:
            soup = BeautifulSoup(f, 'lxml')

        # Image optimization
        for img_tag in soup.find_all('img'):
            if img_tag.find_parent('picture'):
                continue
            img_path = img_tag.get('src')
            if img_path and img_path.lower().endswith(('.jpg', '.jpeg', '.png')):
                if os.path.exists(img_path):
                    try:
                        img = Image.open(img_path)
                        webp_path = os.path.splitext(img_path)[0] + ".webp"
                        img.save(webp_path, "webp", quality=85)

                        picture_tag = soup.new_tag('picture')
                        source_tag = soup.new_tag('source', srcset=webp_path, type='image/webp')
                        picture_tag.append(source_tag)
                        img_tag.wrap(picture_tag)
                        source_tag.insert_after(img_tag)
                        print(f"Processed image: {img_path}")
                    except Exception as e:
                        print(f"Could not process image {img_path}: {e}")

        # Font and CSS delivery optimization
        if soup.head:
            # Add font links
            soup.head.insert(0, soup.new_tag('link', rel='preconnect', href='https://fonts.googleapis.com'))
            soup.head.insert(1, soup.new_tag('link', rel='preconnect', href='https://fonts.gstatic.com', crossorigin=''))
            soup.head.insert(2, soup.new_tag('link', href='https://fonts.googleapis.com/css2?family=Alegreya:ital,wght@0,400;0,700;1,400;1,700&family=Lato:ital,wght@0,400;0,700;1,400;1,700&display=swap', rel='stylesheet'))

            # Update CSS link
            original_css_link = soup.find('link', href=css_file)
            if original_css_link:
                preload_link = soup.new_tag('link', rel='preload', href=minified_css_file, **{'as': 'style', 'onload': "this.onload=null;this.rel='stylesheet'"})
                original_css_link.insert_after(preload_link)

                noscript_tag = soup.new_tag('noscript')
                fallback_link = soup.new_tag('link', rel='stylesheet', href=minified_css_file)
                noscript_tag.append(fallback_link)
                preload_link.insert_after(noscript_tag)

                original_css_link.decompose()

        # Update encoding
        meta_charset = soup.find('meta', charset=True)
        if meta_charset:
            meta_charset['charset'] = 'utf-8'
        else:
            meta_tag = soup.new_tag('meta', charset='utf-8')
            if soup.head:
                soup.head.insert(0, meta_tag)

        meta_http_equiv = soup.find('meta', attrs={'http-equiv': 'content-type'})
        if meta_http_equiv:
            meta_http_equiv.decompose()

        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Optimized HTML file: {html_file}")

if __name__ == "__main__":
    html_files = [
        "index.html", "all-enya-songs.html", "enya-biography.html",
        "enya-songs-albums.html", "roma-ryan-nicky.html", "a-day-without-rain.html",
        "watermark.html", "enya-dark-sky-island.html", "shepherd-moons.html",
        "and-winter-came.html"
    ]
    css_file = "style-enya-lyrics.css"
    optimize_assets(html_files, css_file)
