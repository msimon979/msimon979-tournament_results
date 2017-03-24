#
# Database access functions for the web forum.
#

import time
import psycopg2
import bleach

## Database connection
DB = []

## Get posts from database.
def GetAllPosts():
  DB = psycopg2.connect("dbname=forum")
  c = DB.cursor()
  c.execute("select time, content from posts order by time desc")
  posts = ({'content': str(row[1]), 'time': str(row[0])}
          for row in c.fetchall())
  DB.close
  return posts

## Add a post to the database.
def AddPost(content):
  DB = psycopg2.connect("dbname=forum")
  c = DB.cursor()
  clean_content = bleach.clean(content)
  c.execute("insert into posts (content) values (%s)",
            (clean_content,))
  DB.commit()
  DB.close()
