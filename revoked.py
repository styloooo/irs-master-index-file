import utils
import agate
import csv
import agatesql
import os

def generate_header():
    return [
        'ein',
        'legal_name',
        'doing_business_as_name',
        'organization_address',
        'city',
        'state',
        'zip_code',
        'country',
        'exemption_type',
        'revocation_date',
        'revocation_posting_date',
        'exemption_reinstatement_date',
        'year'
    ]


# @TODO: check for existing records?
def process_revoked_eos(url):
    print('Downloading file')
    utils.download_file(url)
    # remove file
    fileName = 'data-download-revocation.txt'
    filePath = os.path.join(utils.EXTRACTED_FILE_DIR, fileName)

    data = []

    print('Reading file on disk')
    with open(filePath, 'r') as f:
        reader = csv.reader(f, delimiter="|")
        print('Proccessing rows')
        for row in reader:
            print(row)
            if not row:
                continue
            procRow = row
            procRow.append(row[9][7:])
            data.append(procRow)

    header = generate_header()
    colTypes = [agate.Text() for column in range(len(header))]

    print('Inserting into database')
    table = agate.Table(data, header, colTypes)
    table.to_sql(utils.DB_URL, 'revoked_eos')
