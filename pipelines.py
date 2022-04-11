# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3



class RealestatescrapyPipeline:

    def __init__(self):
        self.con = sqlite3.connect("apartments.db")
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS apartments (
        city text,
        district text,
        price integer,
        rooms integer,
        sq_m integer,
        floor text,
        link text
        )""")

    def process_item(self, item, spider):

        if len(item['name']) < 2:
            item['name'].append('None')

        if len(item['ro_sp_fl']) < 6:
            item['ro_sp_fl'].append(item['ro_sp_fl'][-1])

        try:
            self.cur.execute("insert into apartments values (?, ?, ?, ?, ?, ?, ?)",
                              (item['name'][0],
                                  item['name'][1],
                                  int(item['price']),
                                  int(item['ro_sp_fl'][0]),
                                  int(item['ro_sp_fl'][2]),
                                  item['ro_sp_fl'][5],
                                item['link'][0]
                                ))
            self.con.commit()
            return item

        except KeyError:
            pass




