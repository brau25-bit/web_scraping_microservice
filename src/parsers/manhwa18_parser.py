from bs4 import BeautifulSoup

class Manhwa18Parser:

    def __init__(self, html: str):
        self.soup = BeautifulSoup(html, "lxml")
        self.base_url = "https://manhwa18.cc"

    def search(self):
        manga_list = []

        manga = self.soup.find_all(attrs={"class": "manga-item"})
        count = 0

        for element in manga:
            count += 1
            title = self.get_title(element)
            cover = self.get_image_link(element)
            latest_chapter = self.get_latest_chapter(element)
            published_at = self.get_date_published(element)
            series_url = self.get_link(element)

            series_dic = {
                "number": count,
                "title": title,
                "cover": cover,
                "latest_chapter": latest_chapter,
                "published_at": published_at,
                "series_url": f"{self.base_url}{series_url}"
            }

            manga_list.append(series_dic)

        return manga_list
    
    def getSeries(self):
        summary_content = self.soup.find(attrs={"class": "post-status"})
        
        chapters = self.soup.find(attrs={"class": 'panel-manga-chapter'}).find_all('li')

        chapter_list = []

        count = 0
        
        for chapter in chapters:
            count+=1

            chapter_url = self.get_chapter_url(chapter)
            chapter_name = self.get_chapter_name(chapter)
            chapter_release_date = self.get_chapter_release_date(chapter)

            chapter_dict = {
                "number": count,
                "chapter": chapter_name,
                "chapter_release_date":chapter_release_date,
                "chapter_url": f"{self.base_url}{chapter_url}"
            }

            chapter_list.append(chapter_dict)

        series_dict = {
            "post_content": self.get_release_date_and_status(summary_content),
            "chapters": chapter_list
        }


        return series_dict
    
    def getChapters(self):
        return "Hola"
    

    ## Metodos usados dentro de search

    def get_title(self, element):
         return element.find('a').get('title')
    
    def get_link(self, element):
         return element.find('a').get('href')
    
    def get_image_link(self, element):
         return element.find('img').get('data-src')
    
    def get_latest_chapter(self, element):
        return element.find(attrs={"class": "list-chapter"}).find('a').getText()
    
    def get_date_published(self, element):
        return element.find(attrs={"class": "list-chapter"}).find('span', {'class': 'post-on'}).getText(separator=' ', strip=True)
    
    ## Metodos usados dentro de series
    
    def get_release_date_and_status(self, element):
        elements = element.find_all(class_="post-content_item")

        post_content = {}

        for element in elements:
            heading = element.find(attrs={'class': 'summary-heading'}).find('h5').getText(separator=' ', strip=True)
            
            text = element.find(attrs={'class': 'summary-content'}).getText(separator=' ', strip=True)
            
            post_content[heading] = text
            

        return post_content

    def get_chapter_url(self, element):
        return element.find('a').get('href')
    
    def get_chapter_release_date(self, element):
        return element.find('span').getText(separator=' ', strip=True)
    
    def get_chapter_name(self, element):
        return element.find('a').getText(separator=' ', strip=True)
    
    def get_chapter_image(self, element):
        return