from pathlib import Path
import scrapy


class CoursesSpider(scrapy.Spider):
    name = 'courses'
    BASE_URL = 'https://calendar.carleton.ca/undergrad/courses/'

    def start_requests(self):
        yield scrapy.Request(self.BASE_URL, self.parse)

    def parse(self, response):
        for course in response.css('.course p'):
            for course_link in course.css('a'):
                
                course_url = self.BASE_URL + course_link.css('::attr(href)').get()
                
                yield response.follow(course_url, self.parse_course)
    
    def parse_course(self, response):
        for course in response.css(".courseblock"):
            course_code = course.css('.courseblockcode::text').get()
            course_name = course.css('strong span::text').getall()
            course_name = ' '.join(course_name).strip().split('\n')[-1]

            yield {
                'course_code': course_code,
                'course_name': course_name,
            }


            
            
        
