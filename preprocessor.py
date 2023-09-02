import re
import pandas as pd
def preprocess(data):

    pattern = '\[(\d{2}/\d{2}/\d{2}, \d{1,2}:\d{2}:\d{2} [AP]M)\]'
    message = re.split(pattern, data)[2::2]
    dates = re.findall(pattern, data)
    df = pd.DataFrame({'users_message': message, 'message_date': dates})
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M:%S %p')
    df.rename(columns={'message_date': 'date'}, inplace=True)
    users = []
    messages = []
    for message in df['users_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group notification ')
            messages.append(entry[0])
    df['users'] = users
    df['message'] = messages
    df.drop(columns=['users_message'], inplace=True)
    df['years'] = df['date'].dt.year
    df['days'] = df['date'].dt.day
    df['month'] = df['date'].dt.month_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    return df
