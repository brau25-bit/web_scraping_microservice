from src.exception.error import CustomError
from src.builder.search_builder import SearchBuilder
from src.builder.series_builder import ChapterBuilder, SeriesBuilder
from src.builder.chapters_builder import ChapterImgBuilder, EspecifiedChapterBuilder

from bs4 import BeautifulSoup
import re
class Manhwa18Parser:

    def __init__(self, html: str):
        self.soup = BeautifulSoup(html, "lxml")
        self.base_url = "https://manhwa18.cc"

    def search(self):
        manga_list = []

        manga = self.soup.find_all(attrs={"class": "manga-item"})

        if not manga:
            raise CustomError("Not posible to parse", 500, "not-parsed")
        
        manga_count = 0

        for element in manga:
            manga_count += 1
            title = self.get_title(element)
            cover = self.get_image_link(element)
            latest_chapter = self.get_latest_chapter(element)
            published_at = self.get_date_published(element)
            series_url = self.get_link(element)

            series = (
                SearchBuilder()
                .number(manga_count)
                .title(title)
                .cover(cover)
                .latest_chapter(latest_chapter)
                .publish_date(published_at)
                .series_url(series_url)
                .build()
            )   

            manga_list.append(series)

        return manga_list
    
    def getSeries(self):
        summary_content = self.soup.find(attrs={"class": "post-status"})

        if not summary_content:
            raise CustomError("Not posible to parse", 500, "not-parsed")
        
        chapters = self.soup.find(attrs={"class": 'panel-manga-chapter'}).find_all('li')

        chapter_list = []
        
        for chapter in chapters:

            chapter_url = self.get_link(chapter)
            chapter_name = self.get_chapter_name(chapter)
            chapter_release_date = self.get_chapter_release_date(chapter)

            chapter_build = (
                ChapterBuilder()
                .chapter(chapter_name)
                .chapter_release_date(chapter_release_date)
                .chapter_url(chapter_url)
                .build()
            )

            chapter_list.append(chapter_build)

        series = (
            SeriesBuilder()
            .post_content(self.get_release_date_and_status(summary_content))
            .chapters(chapter_list)
            .build()
        )

        return series
    
    def getChapter(self):
        manga_container = self.soup.find(attrs={"class": "read-manga"})

        if not manga_container:
            raise CustomError("Not posible to parse", 500, "not-parsed")

        chapter_images_container = manga_container.find(attrs={"class": "read-content"}).find_all("img")

        chapter_imgs = []
        chapter_img = {}

        for chapter in chapter_images_container:
            meta_data = self.get_chapter_page_number(chapter)
            image = self.get_chapter_image(chapter)

            chapter_img = (
                ChapterImgBuilder()
                .page_number(meta_data["page"])
                .image(image)
                .build()
            )
            
            chapter_imgs.append(chapter_img)
        
        chapter_general = (
            EspecifiedChapterBuilder()
            .chapter(meta_data["chapter"])
            .manga_chapter(chapter_imgs)
            .build()
        )

        return chapter_general

    ## Metodos usados dentro de search

    def get_title(self, element):
         return element.find('a').get('title')
    
    def get_link(self, element):
         manga_name = element.find('a').get('href')
         return f"{self.base_url}{manga_name}"
    
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
    
    def get_chapter_release_date(self, element):
        span = element.find('span')

        if span: 
            release_date = span.getText(separator=' ', strip=True)
        else:
            release_date = "NEW"

        return release_date
    
    def get_chapter_name(self, element):
        return element.find('a').getText(separator=' ', strip=True)
    
    def get_chapter_image(self, element):
        return element.get("data-src")
    
    def get_chapter_page_number(self, element):
        img_alt = element.get("alt")

        match = re.search(r"Chapter\s+(\d+)\s+Page\s+(\d+)", img_alt)

        if match:
            chapter = int(match.group(1))
            page = int(match.group(2))


        return {
            "chapter": chapter,
            "page": page
        }