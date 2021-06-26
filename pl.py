#! C:\Users\longv\AppData\Local\Programs\Python\Python39\python.exe
print("Content-type: text/html \n\n")
print('<h1>COVID TABLE</h1>')

import cgi
import csv

try:
    form = cgi.FieldStorage()
    a = form.getvalue("fname")
    file = open(a, 'r')
    csvfile = csv.reader(file)
    
    print('<!DOCTYPE html>')
    print('<head> \n <title>Snorlax - Display</title> \n </head>')
    print('<body>')
    print('<table width="" border="">')
    array = []
    
    for i in csvfile:
        array.append(i)
        print("<tr>")
        for j in range(len(array[0])):
            print("<th>{}</th>".format(i[j]))
        print("</tr>")
    print('</table>')
    print('<br/>')
    
    # print('<h1>Select Columns: ')
    # print('<select name="field">')
    # for i in array[0]:
    #     print('<option>{}</option>'.format(i))
    # print('</select>')
    # print('</h1>')
    # print('<input type="submit" value="Find"/>')

    print('</body>')
    print('</html>')
    
    file.close()
    
except FileNotFoundError:
    print("File not found, Back to enter again")
    print('<a href="project_question3.html"><button type="button">Back to Homepage</button></a>')
    
    
except:
    print('Nothing !!!')
    print('<a href="index.html"><button type="button">Back to Homepage</button></a>')