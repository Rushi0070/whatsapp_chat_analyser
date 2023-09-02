from urlextract import URLExtract
extract=URLExtract()
def fetch_stats(selected_user,df):
    if selected_user !='Group':
        df=df[df['users']==selected_user]
    num_messages=df.shape[0]
    words=[]
    media_messages=0
    links=[]
    for x in df['message']:

        links.extend(extract.find_urls((x)))
        y = x.split()  # spliting on spaces
        if 'omitted' in y:
            media_messages+=1


        words.append(len(y))


    return num_messages,sum(words),media_messages,len(links)

    # if selected_user=='Group':
    #     #number of messages
    #     num_messages=df.shape[0]
    #
    #     #number of words
    #     arr = []
    #     for x in df['message']:
    #         y = x.split()       #spliting on spaces
    #
    #         arr.append(len(y))
    #     words=sum(arr)
    #     return num_messages,words
    # else:
    #     new_df=df[df['users']==selected_user]
    #     num_messages = new_df.shape[0]
    #     arr = []
    #     for x in new_df['message']:
    #         y = x.split()  # spliting on spaces
    #
    #         arr.append(len(y))
    #     words = sum(arr)
    #     return num_messages,words


def most_busy_user(df):
    x=df['users'].value_counts().head()
    return x
