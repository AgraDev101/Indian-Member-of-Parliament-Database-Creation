import pandas as pd
import sqlalchemy
import psycopg2
import time
from collection import data

df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)

time.sleep(10)

df2 = pd.read_csv("data.csv")

df2.rename(
	columns = {
		"name":"name",
		"constituency":"constituency",
		"party":"party",
		"fathers_name":"fathers_name",
		"mothers_name":"mothers_name",
		"birth_place":"birth_place",
		"spouse_name":"spouse_name",
		"sons":"sons",
		"state_name":"state_name",
		"permanent_address":"permanent_address",
		"present_address":"present_address",
		"email_id":"email_id",
		"education_qualifications":"education_qualifications",
		"countries_visited":"countries_visited",
		"other_info":"other_info",
		"positions_held":"positions_held",
	}, inplace= True
)

engine = sqlalchemy.create_engine('postgres+psycopg2://<USER>:<PASSWORD>@<HOST>:<PORT>/<DATABASE>')

df2.to_sql(
	"mp_data",
	engine,
	index = False,
	if_exists= "replace"
)

