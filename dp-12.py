#!/usr/bin/python

import urllib2, re, time

base = "http://www.reddit.com"
index_url = "/r/nosleep/top/"

def main(): 
    index_source = ""
    while True: 
        try: 
            index_source = urllib2.urlopen(base+index_url).read()
            break
        except: 
            # Failed to retrieve index source. Trying again...
            time.sleep(1)

    title_regex = re.compile(r'<a class="title .*? href="(.*?)" >(.*?)</a>')

    for match in title_regex.findall(index_source): 
        story_url = match[0]
        story_title = match[1]
        print "=== %s ===" % story_title
        story_source = ""
        while True: 
            try: 
                story_source = urllib2.urlopen(base+story_url).read()
                break
            except: 
                # Failed to retrieve story source. Trying again...
                time.sleep(1)
            
        body_regex = re.compile(r'<div class="expando".*?class="md">(.*?)</div>', re.DOTALL)
        body = body_regex.findall(story_source)[0]
        print body


if __name__ == '__main__': 
    main()
