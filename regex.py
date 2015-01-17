import re
code = """
#### this is a sample method
def method_name():
  # code goes here!
#### this is a sample class
class ClassName(object):
  # code goes here!
"""

COMMENT_CATCHER = '\#{3}.*\n'
COMMENT_FILE = open('./comments.txt', 'w')

def save_to_file(comment):
  COMMENT_FILE.write(comment)

comment = re.search(COMMENT_CATCHER, code)

while comment:
  save_to_file(comment.group(0))
  code = code.replace(comment.group(0), "")
  comment = re.search(COMMENT_CATCHER, code)

print("done!")