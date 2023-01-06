from whois_format import list_expected_fmt
import whois
#import simplejson as json
import json

input_file = "domain2.txt"# "domain.csv"
cnt = 0
fin = open(input_file, 'r')
fout = "out1.txt"
for domain in fin:
    # if(cnt == 1000):
    #     break
    cnt += 1
    try:
        w = whois.whois(domain.strip())
        with open(fout, "a", encoding="utf-8") as f:
            f.writelines([domain.strip(), ",", str(w).replace("null", "None").replace("\n","").replace(" ",""), "\n"])
    except whois.parser.PywhoisError as err:
        with open(fout, "a", encoding="utf-8") as f:
            f.writelines(["ERR", " ", domain.strip(), "\n"])
fin.close()