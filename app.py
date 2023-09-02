import streamlit as st
import helper
import preprocessor
import matplotlib.pyplot as plt
st.sidebar.title("Whatsapp chat analyzer")
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)
    st.dataframe(df)
    user_list = df['users'].unique().tolist()
    # user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, 'Group')
    selected_user = st.sidebar.selectbox("show analysis wrt",user_list)
    if st.sidebar.button("show analysis"):
        num_messages,words,media_messages,links = helper.fetch_stats(selected_user, df)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Total messages")
            st.title(num_messages)
        with col2:
            st.header("Total words")
            st.title(words)
        with col3:
            st.header("media message")
            st.title(media_messages)
        with col4:
            st.header("links shared")
            st.title(links)

        #finding the busiest user -- ploting a bar chart 

        if selected_user=='Group':
            st.title('Most busy users')
            x=helper.most_busy_user(df)
            fig,ax=plt.subplots()
            col1,col2=st.columns(2)
            with col1:
                ax.bar(x.index, x.values)
                st.pyplot(fig)


