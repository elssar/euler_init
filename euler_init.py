#!/usr/bin/python

# Python script that will take in a Project Euler problem number and create a file
# with the problem text in the comments.
# Requires PyYaml and Requests

"""
-----
Usage|
-----
python euler_init.py problem_number* language file_name

* required

In case you don't specify a language, the program will default to Python.
In case you don't specify a file name, it will be defaulted to the problem number.
"""

__author__= 'Akshay Bist <elssar@altrawcode.com>'
__license__= 'BSD License'

from os import getcwd
from sys import argv, path
from yaml import load
from requests import get
from BeautifulSoup import BeautifulSoup as bs, BeautifulStoneSoup as bss

def get_problem(number):
    problem= get('http://projecteuler.net/problem='+number, headers={'user-agent': 'euler-init'})
    try:
        if problem.status_code==404:
            raise Exception('Problem {0} does not exist'.format(str(number)))
        elif problem.status_code!=200:
            raise Exception('Error - '+`problem.status_code`)
        html= bs(problem.text)
        question= unicode(bss(html.find('h2').text, convertEntities= bss.ALL_ENTITIES))
        statement= html.find('div', {'class': 'problem_content'}).text
        return question, statement
    except Exception, e:
        print e
        return None
    
def main():
    if len(argv)<2 or len(argv)>4 or not argv[1].isdigit():
        print 'Invalid input!!!'
        print __doc__
        return
    problem= get_problem(argv[1])
    if problem is None:
        return
    with open(path[0]+'/config.yaml', 'r') as f:
        config= load(f.read())
    ext= '.py'
    name= 'problem_'+argv[1]
    if len(argv)==3:
        if argv[2] in config['languages']:
            ext= '.'+argv[2]
        else:
            name= argv[2]
    if len(argv)==4:
        if argv[2] not in config['languages']:
            print 'Error!! Unknown extension'
            return
        ext= '.'+argv[2]
        name= argv[3]
    lines= []
    lines.append('Problem {0} of Project Euler\n'.format(argv[1]))
    lines.append('http://projecteuler.net/problem='+argv[1]+'\n')
    lines.append(problem[0]+'\n')
    lines.append(problem[1]+'\n')
    lines.append(config['author']['name']+'\n')
    if len(config['languages'][ext[1:]])==2:
        lines.append(config['languages'][ext[1:]][1]+'\n')
        lines.insert(0, config['languages'][ext[1:]][0]+'\n')
    with open(getcwd()+'/'+name+ext, 'w') as f:
        x= ''
        if len(config['languages'][ext[1:]])==1:
            x= config['languages'][ext[1:]][0]
        for line in lines:
            f.writelines(x+line)

if __name__=='__main__':
    main()