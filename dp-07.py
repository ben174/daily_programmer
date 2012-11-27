#!/usr/bin/python

import re 

def main(): 
    input = "*italic* **bold** super^script^script ~~strikethrough~~ "\
            "[reddit!](http://www.reddit.com) blah blah  `inline code text!`"\
            " blah blah \* **escape formatting** \*"
    print "INPUT: %s" % (input)


    ret = input
    ret = re.sub(r"\\\*(.*?)\\\*", r"<!-- \1 -->", ret)
    ret = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", ret)
    ret = re.sub(r"\*(.*?)\*", r"<i>\1</b>", ret)
    ret = re.sub(r"\^(.*?)\^", r"<sup>\1</sup>", ret)
    ret = re.sub(r"~~(.*?)~~", r"<s>\1</s>", ret)
    ret = re.sub(r"\[(.*?)\]\((.*?)\)", r"<a href=\"\2\">\1</a>", ret)


    print "OUTPUT: %s" % (ret)


if __name__ == '__main__': 
    main()
