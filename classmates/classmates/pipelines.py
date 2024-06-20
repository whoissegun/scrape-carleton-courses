# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface

import os
from dotenv import load_dotenv
from supabase import create_client, Client


load_dotenv()

class ClassmatesPipeline:
    def __init__(self):
        self.supabase = create_client(os.environ['SUPABASE_URL'], os.environ['SUPABASE_KEY'])
        
        try:
            data = self.supabase.auth.sign_in_with_password({"email": os.environ["SUPABASE_AUTH_USER_EMAIL"], "password": os.environ["SUPABASE_AUTH_USER_PASSWORD"]})
        except Exception as e:
            raise Exception(f"Error logging in: {e}")

        

    def close_spider(self, spider):
        # Log out of the database
        try:
            self.supabase.auth.sign_out()
        except Exception as e:
            spider.logger.error(f"Error logging out: {e}")

    def process_item(self, item, spider):
        # Insert the item into the database
        try:
            response = self.supabase.table("courses").insert({
                "name": item.get('course_name'), 
                "course_code": item.get('course_code'), 
                "school": 1
            }).execute()
        except Exception as e:
            spider.logger.error(f"Error inserting item: {e}")

        return item
