from bs4 import BeautifulSoup
import requests
from Course import Course

class Scraper:
    def __init__(self):
        self.courses = []

    def get_page(self):
        doc = BeautifulSoup(
            requests.get("http://learn-co-curriculum.github.io/site-for-scraping/courses").text,
            'html.parser'
        )
        return doc

    def get_courses(self):
        return self.get_page().select('.post')

    def make_courses(self):
        for course in self.get_courses():
            # Extract data with error handling for missing elements
            title = course.select("h2")[0].text if course.select("h2") else ''
            date = course.select(".date")[0].text if course.select(".date") else ''
            description = course.select("p")[0].text if course.select("p") else ''

            # Only create course if there's valid data
            if title and date and description:
                new_course = Course(title, date, description)
                self.courses.append(new_course)
        return self.courses

    def print_courses(self):
        for course in self.make_courses():
            print(course)

# To run the scraper and print courses
if __name__ == '__main__':
    scraper = Scraper()
    scraper.print_courses()