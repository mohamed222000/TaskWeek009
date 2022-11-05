from PIL import Image
import streamlit as st
import datetime
import requests as rq

#function to check keyword:

#import Image 
img = Image.open('ic.jpeg')
def keyCheck (string):
    return any(char.isdigit() for char in string)

#config streamlit web page 
st.set_page_config("NewsAPI Task", img ,"centered",)
#st.header("What You Want To Read Today?")
col1, mid, col2 = st.columns([30,10,20])
with col1:
    st.header("What You Want To Read Today?")
with col2:
    st.image("ic.jpeg",width=100)


#claculate The Oldest Valid Date:
od = datetime.date.today() - datetime.timedelta(days=30) 


#Take Inputs From User:

#1- Input Keyword:
key = st.text_input("Enter One Keyword:")

#2- Input The Oldest Date:
dOld= st.date_input(
    "Enter The Oldest Date:",
    min_value= od,
    max_value=datetime.date.today())

#3- Input The Newest Date:
dNew= st.date_input(
    "Enter The Newest Date:",
    max_value = datetime.date.today())

#4- Input Language:
lan= st.radio(
    "Choose Your Language:",
    ("Arabic","English"))

match lan:
    case "Arabic":
        lan = "ar"
    case "English":
        lan = "en"

#5- Input SortBy:
sort= st.selectbox(
    "The Articles Sorted By:",
    ("relevancy","popularity","publishedAt"),
    help="""relevancy = articles more closely related to Keyword come first.
    \npopularity = articles from popular sources and publishers come first.
    \npublishedAt = newest articles come first.""")

#Input of Page Size:
size= st.slider("Select A Number:",0,100)

#Button:
if st.button("OK!"):
    #check of Keyword:
    if keyCheck(key):
        st.write("Error: Keyword Must Not Have Any Numbers.")
    #check of date:
    if dOld > dNew :
        st.write("Error: Oldest date must be before than Newest date")

    else:
        url = f"https://newsapi.org/v2/everything?q={key}&from={dOld}&to={dNew}&sortBy={sort}&pageSize={size}&language={lan}&apiKey=ce58e78cc7c24508853f914825c9915f"
        print(url)
        #show Titles:
        myRequest = rq.get(url)
        print(myRequest.json()["status"])
        print(myRequest.json()["totalResults"])
        x= 0
        if myRequest.json()["totalResults"] > size:
            for i in range(size):
                st.write("TITLE",x,":")
                st.write(myRequest.json()["articles"][x]["title"])
                st.write("AUTHOR IS:")
                st.write(myRequest.json()["articles"][x]["author"])
                st.write("TO CHECK URL:")
                st.write(myRequest.json()["articles"][x]["url"])
                st.write("THIS ARTICLE PUBLISHED AT:")
                st.write(myRequest.json()["articles"][x]["publishedAt"])
                x +=1

        else:
            st.write("Please Enter Number Below",myRequest.json()["totalResults"])
        
        