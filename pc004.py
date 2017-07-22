import urllib.request

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
parameter = "12345"
parameter = "83763"

def callUrl(para, call):
    call += 1

    connection = urllib.request.urlopen(url + para)
    html = connection.read()

    print(html.decode())

    id = str(html.decode()).split("and the next nothing is ")

    if id[1] != "" and len(id[1]) > 0:
        callUrl(id[1], call)
    else:
        print(id)


callUrl(parameter, 0) # peak.html