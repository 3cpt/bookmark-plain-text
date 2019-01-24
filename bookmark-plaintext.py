import sys  
import os
import re

def main():  
   filepath = sys.argv[1]

   if not os.path.isfile(filepath):
       print("File does not exist")
       sys.exit()

   with open(filepath, encoding="utf8") as fp:
       for line in fp:
           search_title(line)
           search_url(line)

def search_title(current_line):
    if "LAST_MODIFIED" in current_line:
        result = re.search('">(.*)</H3', current_line)
        if result.group(1) is not None:
            print (result.group(1))

def search_url(current_line):
    if "http" in current_line:
        aux_link = re.search('<A HREF="(.*)"[ \t]ADD_DATE=', current_line)
        #print (aux_link)
        if aux_link is not None:
            aux_name = re.search('"[ \t]*>(.*)</A>', current_line)
            if aux_name is not None:
                print ("{} - {}".format(aux_name.group(1), aux_link.group(1)))

if __name__ == '__main__':  
   main()
