import xmltodict
import pprint
import re
import string




def parsePrefix(prefix):
        if re.findall(r"(\d+)\((.*)\)", prefix):
                values = re.findall(r"(\d+)\((.*)\)", prefix)
        else:
                return prefix, []
        prefix_start = values[0][0]
        prefix_ext = values[0][1]
        items = string.split(prefix_ext, ',')
        a = []
        for item in items:
                if (re.findall(r"^\d$", item)):
                        #print "found single digit : "+item
                        a.append(prefix_start + str(item))
                if (re.findall(r"^(\d)\-\d$", item)):
                        rng = re.findall(r"^(\d)\-(\d)$", item)
                        start = int(rng[0][0])
                        stop = int(rng[0][1])
                        #print "found range : " + str(start) + ", stop: " + str(stop)
                        if stop==0:
                                for x in range(start, 10):
                                        a.append(prefix_start + str(x))
                        else:
                                for x in range(start, stop+1):
                                        a.append(prefix_start + str(x))
        return prefix_start, a



with open('pl_networks.xml') as fd:
    obj = xmltodict.parse(fd.read())

tbl = obj['tablica']['numery']['plmn']
for record in tbl:
        #prefix = record['numer']
        #print("Prefix: " + record['numer'])
        (pr, mylist) = parsePrefix(record['numer'])
        if len(mylist) > 0:
                for _aa in mylist:
                        print record['operator'].encode('unicode-escape') + ":  " + _aa
        else:
                print record['operator'].encode('unicode-escape') + ":  " + pr
