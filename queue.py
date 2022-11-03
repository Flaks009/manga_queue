from generate_creds import main
import pandas as pd
import numpy as np

SPREADSHEET_ID = '1yD5XUKdx1YjLLcZw3oGgZU0Fyv8BcNMrHtE5tH4RL3o'

def get_queue():
    
    service = main()
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range='A1:E60').execute()
    df = pd.DataFrame(result['values'][1:], columns=result['values'][0])
    df['cell'] = np.arange(len(df))
    df['cell'] = df['cell'] + 2
    df = df.loc[df['Status'] == 'NA FILA']

    df.to_csv('/home/flaks/projects/mangadex_downloader/queue.csv', index=False)

def write_sheet(cell_number):

    service = main()
    result = service.spreadsheets().values().update(
            spreadsheetId=SPREADSHEET_ID, range='E{}'.format(cell_number),
            valueInputOption="USER_ENTERED", body={'values':[['BAIXADO']]}).execute()

def change_status():

    queue = pd.read_csv('/home/flaks/projects/mangadex_downloader/queue.csv')

    for index, row in queue.iterrows():
        write_sheet(row['cell'])
