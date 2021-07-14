import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
sheet = client.open("Resource Project").sheet1

# Extract and print all of the values
# pp = pprint.PrettyPrinter()
# output = sheet.row_values("Level" == {{LevelSelection}})
# return row where the column value is equal to SubjectSelection & LevelSelection & MediumSelection
# pp.pprint(output)

x = sheet.row_count
while x > 0:
    row = sheet.row_values(x, value_render_option='UNFORMATTED_VALUE')
if row[0] == "Beginner":
    print(row[2])
    x = x - 1

