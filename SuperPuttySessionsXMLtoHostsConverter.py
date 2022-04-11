import xmltodict

with open('sessions.xml', 'rU') as sessionsxml:
    for line in sessionsxml:
        try:
            hosts_dict = xmltodict.parse(line)
            session=dict(hosts_dict['SessionData'])
            print(session['@Host'] + " " + (session["@SessionName"]).split(' ', 1)[0])
            hosts = open("hosts.txt", "a")
            hosts.write(session['@Host'] + " " + (session["@SessionName"]).split(' ', 1)[0]+"\n")
        except:
            print("")

hosts.close()

