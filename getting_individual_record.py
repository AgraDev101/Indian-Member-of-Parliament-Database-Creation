from bs4 import BeautifulSoup
import requests
import io
import time
# from url_output import urls
import pandas as pd
from fake_useragent import UserAgent
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

urls = ["import from url url_output.py"]

data = []

for url in urls:
	ua = UserAgent()
	retry_strategy = Retry(
		total=3,
		backoff_factor=2,
		status_forcelist=[429, 500, 502, 503, 504, 413],
		)
	adapter = HTTPAdapter(max_retries=retry_strategy)
	http = requests.Session()
	http.mount("https://", adapter)
	http.mount("http://", adapter)
	res = http.get(url, headers={'User-Agent': ua.chrome})
	cont = res.content
	soup = BeautifulSoup(cont, "html.parser")

	d = {}

	try:
		name = soup.find("h2", {"class": "field-content"}).text
		name = name.strip()
		d["name"] = name
		if (name == ""):
			d["name"] = "Not Found"
	except:
		pass
	
	for info in soup.find_all("p"):
		try:
			key = info.find("span", {"class": "view-label"}).text
			key = key.strip()
			
			key = key.replace("Constituency:", "constituency").replace("Party:", "party").replace("Father's Name:", "fathers_name").replace("Mother's Name:", "mothers_name").replace("Birth Place:", "birth_place").replace("Spouse Name:", "spouse_name").replace("SONS:", "sons").replace("State Name:", "state_name").replace("Permanent Address:", "permanent_address").replace("Present Address:", "present_address").replace("Email Id:", "email_id").replace("Education Qualifications:", "education_qualifications").replace("Countries Visited:", "countries_visited").replace("OTHER INFO:", "other_info").replace("Positions Held:", "positions_held")

			if (key == ""):
				key = "nil"
		except:
			pass

		try:
			value = info.find("span", {"class": "view-output"}).text
			value = value.strip()
			value = value.replace("\n", "").replace("   ", " ").replace("  ", " ")
			if (value == ""):
				value = "not available"
		except:
			pass

		d.setdefault("state_name", "not available")
		d.setdefault("countries_visited", "not available")
		d.setdefault("education_qualifications", "not available")
		d.setdefault("email_id", "not available")
		d.setdefault("present_address", "not available")
		d.setdefault("permanent_address", "not available")
		d.setdefault("sons", "not available")
		d.setdefault("spouse_name", "not available")
		d.setdefault("birth_place", "not available")
		d.setdefault("mothers_name", "not available")
		d.setdefault("fathers_name", "not available")
		d.setdefault("other_info", "not available")
		d.setdefault("positions_held", "not available")

		d[key] = value
	
	data.append(d)
	print(str(len(data)) + " record(s) added")
	time.sleep(1)

with open("collection.py", "w") as f:
	f.seek(0)
	f.write("data = " + str(data))


print("total records: " + str(len(data)))


