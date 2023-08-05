from urllib.parse import urlsplit, parse_qs
import csv

url = """https://www.mydomain.com/page-name?utm_content=textlink&utm_medium=social&utm_source=twitter&utm_campaign=fallsale"""

split_url = urlsplit(url)
params = parse_qs(split_url.query)
parsed_url = [
	split_url.netloc,
	split_url.path,
	params['utm_content'][0],
	params['utm_medium'][0],
	params['utm_source'][0],
	params['utm_campaign'][0],
]
all_urls = [parsed_url]
export_file = "export_file.csv"

with open(export_file, 'w') as fp:
	csvw = csv.writer(fp, delimiter='|')
	csvw.writerows(all_urls)

fp.close()
