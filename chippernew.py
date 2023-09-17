import streamlit as st
import pyrebase
from datetime import datetime
from streamlit_option_menu import option_menu
from PIL import Image as imgget
import requests
import streamlit.components.v1 as components
import random
import json
from io import BytesIO
import feedparser
import urllib.request
from datetime import datetime,timedelta
import uuid
import ast 
from streamlit_lottie import st_lottie
from googleapiclient.discovery import build

#streamlit=1.24.0
#on streamlit cloud streamlit=1.16.0
#now on streamit cloud streamlit==1.26.0
#current version changed to streamlit=1.26.0from streamlit=1.24.0











logot=imgget.open("logo.png")

st.set_page_config(page_title="Chipper",page_icon=logot)





hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            #GithubIcon{visiblity:hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)





button_style = '''
    <style>
        .stButton button {
            background: linear-gradient(to left,#3CCBF4,#2DB4EC,#20A2E6);
            color: #FFFFFF; 
            border-color:#2DB4EC; 
        }
    </style>
'''


st.markdown(button_style, unsafe_allow_html=True)
st.markdown('<style>.stButton>button { margin-left: auto; margin-right: auto; display: block; }</style>', unsafe_allow_html=True)




textcolor= """
    <style>
    .textlogin{
        background: linear-gradient(to left,#3CCBF4,#2DB4EC,#20A2E6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family:serif;font-style:italic;color:#1A6DFF;text-align:left;font-size:30px;
    }
    </style>
    """
st.markdown(textcolor,unsafe_allow_html=True)


textcolor= """
    <style>
    .text{
        background: linear-gradient(to left,#3CCBF4,#2DB4EC,#20A2E6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family:serif;font-style:italic;color:#1A6DFF;text-align:center;font-size:30px;
    }
    </style>
    """
st.markdown(textcolor,unsafe_allow_html=True)





firebaseConfig = {
  "apiKey": "AIzaSyDQkowU9ElUDooKZKb-b-g6beWBF30glv0",
  "authDomain": "chipper1-2980f.firebaseapp.com",
  "databaseURL": "https://chipper1-2980f-default-rtdb.firebaseio.com",
  "projectId": "chipper1-2980f",
  "storageBucket": "chipper1-2980f.appspot.com",
  "messagingSenderId": "276274547796",
  "appId": "1:276274547796:web:9593e0f6fdd3afba8471c1",
  "measurementId": "G-2NPS52N6ZX"
}
firebase= pyrebase.initialize_app(firebaseConfig)

auth=firebase.auth()

data=firebase.database()
storage=firebase.storage()


textcolor= """
    <style>
    .holdertext{
        background: linear-gradient(to left,#3CCBF4,#2DB4EC,#20A2E6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family:serif;font-style:italic;color:#1A6DFF;text-align:left;font-size:30px;
    }
    </style>
    """
st.markdown(textcolor,unsafe_allow_html=True)
       

textcolor= """
    <style>
    .holdertexts{
        background: linear-gradient(to left,#3CCBF4,#2DB4EC,#20A2E6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family:serif;font-style:italic;color:#1A6DFF;text-align:center;font-size:25px;
    }
    </style>
    """
st.markdown(textcolor,unsafe_allow_html=True)


textcolor= """
    <style>
    .gradienttext{
        background: linear-gradient(to left,#3CCBF4,#2DB4EC,#20A2E6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family:serif;font-weight: 600;font-style:italic;color:#1A6DFF;text-align:left;font-size:30px;
    }
    </style>
    """
st.markdown(textcolor,unsafe_allow_html=True)
# st.markdown("<p class='holdertext'>Login or Register :</p>", unsafe_allow_html=True)
button_style = '''
    <style>
        .stButton button {
            background: linear-gradient(to left,#3CCBF4,#2DB4EC,#20A2E6);
            color: #FFFFFF; 
            border-color:#2DB4EC; 
        }
    </style>
'''


st.markdown(button_style, unsafe_allow_html=True)
st.markdown('<style>.stButton>button { margin-left: auto; margin-right: auto; display: block; }</style>', unsafe_allow_html=True)


# css for st.tabs 
font_css = """
<style>
button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
  font-size: 20px;
  padding:10px
}
</style>
"""
st.write(font_css, unsafe_allow_html=True)

placeholder=st.empty()
with placeholder.container():
     st.markdown("<center><img src=https://img.icons8.com/fluency/500/soulseek.png; alt=centered imgget; height=150; width=150> </center>",unsafe_allow_html=True)
     textcolor= """
    <style>
    .gradient-text{
        background: linear-gradient(to left,#3CCBF4,#2DB4EC,#20A2E6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family:serif;font-weight: 600;font-style:italic;color:#1A6DFF;text-align:center;font-size:30px;
    }
    </style>
    """
     st.markdown(textcolor,unsafe_allow_html=True)
     st.markdown('<p class="gradient-text">ℂ𝕙𝕚𝕡𝕡𝕖𝕣</p>', unsafe_allow_html=True)
     streamlitstyle = """
			<style>
			sidebar,body,[class*="css"]{background-image: url("https://64.media.tumblr.com/0282981b3d64c161dfee6db1fcba9b2e/c6c844929d40597e-5c/s500x750/68afbb70ac6ec01b1c2819383b7bedd09fd1da7a.gif");
                        background-attachment: fixed;
                        background-size: cover 
			
			
                       
			
			
                        }
			</style>
			"""
     st.markdown(streamlitstyle, unsafe_allow_html=True)
#https://www.threads.net/images/barcelona/ribbons/english-dark.webp
#https://media0.giphy.com/media/dAWZiSMbMvObDWP3aA/200w.gif?cid=82a1493b49jwnewzhlc0m7rh0d76uaigmivehf0zefpbx8ih&ep=v1_gifs_related&rid=200w.gif&ct=g
#https://devforum-uploads.s3.dualstack.us-east-2.amazonaws.com/uploads/optimized/4X/b/5/d/b5df22212253eda5f0cebe857cc84dd9a874a478_2_1035x582.jpeg
 
    # st.markdown("<p class='holdertext'>Login or Register :</p>", unsafe_allow_html=True)
   
     st.markdown('<p class="gradienttext">Log in :</p>', unsafe_allow_html=True)
     email=st.text_input("",placeholder="Email")
     passw=st.text_input("",placeholder="Password",type="password")
     st.write("[Forgot password?](https://chipperforgotpassword.streamlit.app)")
     
     signin=st.checkbox("Log in")

     

     st.markdown(f"___")

    
     st.write('<div style="text-align: center;">New to Chipper? <a href="https://chipperregister.streamlit.app">Register now</a></div>', unsafe_allow_html=True)
     #http://localhost:8502/

         
     
      




if signin:
            if not email or not passw :
                st.markdown(f"___")
                st.error("Please enter your full credentials !")
            else:
               try:
                    placeholder.empty()
                    user=auth.sign_in_with_email_and_password(email,passw)
                    nav = option_menu(menu_title=None,   options=["", " ","  ", "   "],icons=["house-fill","search","pencil-square","person-fill"],menu_icon="cast",default_index=0,orientation="horizontal",styles={
        "container": {"padding": "10!important" ,"background":"linear-gradient(to left,#3CCBF4,#2DB4EC,#20A2E6)"},
        "icon": {"color": "black", "font-size": "20px"},
        "nav-link": {"text-align":"left", "margin":"1px", "--hover-color": "#1c1c1c"},
        "nav-link-selected": {"background-color": "lightblue","color":"#1c1c1c"},})
                    nimg=data.child(user["localId"]).child("Images").get().val()
                    if nimg is not None:
                          imgg=data.child(user["localId"]).child("Images").get()
                          for img in imgg.each():
                               imgc=img.val()
                          st.sidebar.markdown(f'<div style="display: flex; justify-content: center;"><img src="{imgc}" width="200" height="200" style="border-radius:50%;"></div>', unsafe_allow_html=True)
                          expa=st.sidebar.expander("👤 Change your profile pic")
                          with expa:
                             
                               newimgp=st.file_uploader("",type=["jpg", "jpeg", "png","gif"])
                               upbt=st.button("Upload profile pic")
                               
                               if upbt:
                                    uid=user["localId"]
                                    dataup=storage.child(uid).put(newimgp,user["idToken"])
                                    aimgdata=storage.child(uid).get_url(dataup["downloadTokens"])

                                    data.child(user["localId"]).child("Images").push(aimgdata)
                                    
                                    
                               

                                   
                               if st.button("🗑 Double tap to remove profile pic"):
                                         data.child(user["localId"]).child("Images").remove()
                               
                                 
                    else:
                                #st.sidebar.markdown(f'<div style="display: flex; justify-content: center;"><img src="https://img.icons8.com/fluency/500/user-male-circle.png" width="200" height="200"  style="border-radius:50%;"></div>', unsafe_allow_html=True)
                                with st.sidebar:
                                     st_lottie("https://lottie.host/9839c16f-ad3d-43b0-ba7d-f5399cced728/6459NXwpZO.json",width="200",height="200")
                                expand=st.sidebar.expander("📷 Choose your profile pic :")
                                with expand:
                                     newimgp=st.file_uploader("",type=["jpg", "jpeg", "png","gif"])
                                     upbt=st.button("Upload profile pic")
                                     if upbt:
                                         
                                               uid=user["localId"]
                                               dataup=storage.child(uid).put(newimgp,user["idToken"])
                                               aimgdata=storage.child(uid).get_url(dataup["downloadTokens"])
                                               data.child(user["localId"]).child("Images").push(aimgdata)
                    st.sidebar.markdown(f"___")
                    expanderbio=st.sidebar.expander("🪪 Update your Bio ")
                    bio=data.child(user["localId"]).child("Bio").get().val()
                    with expanderbio:
                         if bio is not None:
                              bio=data.child(user["localId"]).child("Bio").get()
                              for bio in bio.each():
                                   bioc=bio.val()
                              st.text(bioc)
                              bioin=st.text_area("",placeholder="Enter your Bio to be uploaded eg: name,date of birth etc")
                              upbtn=st.button("Upload Bio")
                              if upbtn:
                                   data.child(user["localId"]).child("Bio").push(bioin)
                                   st.info("Bio set successfully !")
                         else:
                              st.info("No Bio till now !")
                              bioin=st.text_area("",placeholder="Enter your Bio to be uploaded eg: name,date of birth etc")
                              upbtn=st.button("Upload Bio")
                              if upbtn:
                                   data.child(user["localId"]).child("Bio").push(bioin)
                                   st.info("Bio set successfully !")
                    
                           


                   




                    if nav=="   ":
                          
                          nimg=data.child(user["localId"]).child("Images").get().val()
                          if nimg is not None:
                               v=data.child(user["localId"]).child("Images").get()
                               for img in v.each():
                                    imgc=img.val()
                               st.markdown(f'<div style="display: flex; justify-content: center;"><img src="{imgc}" width="200" height="200" style="border-radius:50%;"></div>', unsafe_allow_html=True)
                               userdata=data.child(user['localId']).child("Handle").get().val()
                               st.markdown(f'<div style="display: flex; justify-content: center;"><h2>{userdata}</h2></div>',unsafe_allow_html=True)
                          else:

                               #st.markdown(f'<div style="display: flex; justify-content: center;"><img src="https://img.icons8.com/fluency/500/user-male-circle.png" width="200" height="200"  style="border-radius:50%;"></div>', unsafe_allow_html=True)
                               st_lottie("https://lottie.host/9839c16f-ad3d-43b0-ba7d-f5399cced728/6459NXwpZO.json",width="200",height="200")
                               userdata=data.child(user['localId']).child("Handle").get().val()
                               #st.header(userdata)
                               st.markdown(f'<div style="display: flex; justify-content: center;"><h2>{userdata}</h2></div>',unsafe_allow_html=True)

                          st.subheader("Bio :")
                          bio=data.child(user["localId"]).child("Bio").get().val()
                          if bio is not None:
                              bio=data.child(user["localId"]).child("Bio").get()
                              for bio in bio.each():
                                   bioc=bio.val()
                              st.text(bioc)
                          else:
                              st.info("No Bio  till now !")
                          joined=data.child(user['localId']).child("date").get().val()
                          if joined is not None:
                               joined=data.child(user['localId']).child("date").get()
                               for joined in joined.each():
                                    joic=joined.val()
                                    
                                    st.markdown(f'<div style="display: flex; justify-content: left;"><h5>{joic}</h5></div>',unsafe_allow_html=True)

                          tab3,tab4=st.tabs(["Thought's","Pic's"])
                          with tab3:
                              all_posts=data.child(user['localId']).child("Posts").get()
                              if all_posts.val() is not None:
                                   for Posts in reversed(all_posts.each()):
                                       
                                        message = st.chat_message("user")
                                        message.write(Posts.val())
                                      
                                        
                                        st.markdown(f"___")
                              else:
                                   st.info("No thought's  till now !")
                                   st.markdown(f"___")
                          with tab4:
                              posts=data.child(user['localId']).child("posts").get()
                              if  posts.val() is not None:
                                   for Posts in posts.each():
                                        caption = Posts.val()["caption"]
                                        image_url = Posts.val()["image_url"]
                                        message = st.chat_message("user")
                                        message.write(caption)
                                        response = requests.get(image_url)
                                        img = imgget.open(BytesIO(response.content))
                                        st.image(img, use_column_width=True)
                                        st.markdown(f"___")
                              else:
                                   #st_lottie("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")

                                   st.info("No pic's  till now !")
                                   st.markdown(f"___")


                    elif nav=="  ":
                                   st.subheader("Share a Thought or Pic :")
                                  
                                   tab1,tab2 = st.tabs(["Share a thought","Share a pic "])
                                   with tab1:
                                      
                                        post=st.text_input("",placeholder="Share your thought with the world",max_chars=400)
                                        expander=st.expander("Share your thought")
                                        with expander:
                                             add_post=st.button("Share your thought")
                                             if add_post:
                                                  if not post:
                                                       st.error("Please enter your thought")
                                                  else:
                                                       now=datetime.now()
                                                       dt=now.strftime("%d / %m / %y")
                                                       dtt=now.strftime("%I:%M %p")
                                                       userdata=data.child(user['localId']).child("Handle").get().val()
                                                        


                                                       post=f'''{userdata}  \n {post} \n  shared on : {dt}  at  {dtt}'''
                                                       results=data.child(user["localId"]).child("Posts").push(post)
                                                       st.toast("Thought shared successfully")
                                   with tab2:
                                         
                                         caption = st.text_input("",placeholder="Add a caption to your pic")
                                         expan=st.expander("Share your pic")
                                         with expan:
                                              imgex = st.file_uploader("", type=["jpg", "jpeg", "png"])
                                              if imgex is None:
                                                   st.warning("Please select a pic")
                                              upbta=st.button("Share the pic and caption")
                                              if upbta:
                                                  with st.spinner("Uploading image..."):
                                                       storage.child("images/" + imgex.name).put(imgex)
                                                       userdata=data.child(user['localId']).child("Handle").get().val()

                                                       now=datetime.now()
                                                       dt=now.strftime("%d / %m / %y")
                                                       dtt=now.strftime("%I:%M %p")
                                                       captiondata="Posted by \n"+userdata + "/n"+caption + " ; "  +  "\n  shared on :" + dt + "  at  " + dtt
                                                       post_data = {"caption": captiondata,"image_url": storage.child("images/" + imgex.name).get_url(None) }
                                                       data.child(user["localId"]).child("posts").push(post_data)
                                                       st.toast("Pic shared successfully")
                    elif nav==" ":
                         allu=data.get()
                         resa=[]
                         for ush in allu.each():
                              k=ush.val().get("Handle")
                              resa.append(k)
                         n = len(resa)
                         st.subheader("🔍 Search :")
                         cho = st.selectbox('',resa)
                         pusha = st.button('Show Profile')
                         news=st.empty()
                         with news.container():
                             #st.markdown(f"___")
                             tab7,tab8=st.tabs(["New's","Music"])

                             with tab7:
                                  #st.subheader("Have a look at todays news")
                                  #st.markdown(f"___")
                                  NEWS_API_KEY = "5a2401032c9d48e9a1ae511bbfa6efb9"
                                  NEWS_SOURCE = "bbc-news"  # You can change this to your preferred news source
                                  NEWS_ENDPOINT = f"https://newsapi.org/v2/top-headlines?sources={NEWS_SOURCE}&apiKey={NEWS_API_KEY}"
                                  response = requests.get(NEWS_ENDPOINT)
                                  da = response.json()
                                  if da.get("status") == "ok":
                                      articles = da["articles"][:5]  # Get the first 5 articles
                                      for idx, article in enumerate(articles):
                                          st.subheader(f"Article {idx + 1}: {article['title']}")
                                          st.image(article["urlToImage"], caption=article["title"], use_column_width=True)
                                          st.write(article["description"])
                                          st.write(f"Source: {article['source']['name']}")
                                          st.write(f"Published: {article['publishedAt']}")
                                          st.write(f"Read more: [Link]({article['url']})")
                                          st.markdown(f"___")
                                  else:
                                      st.error("Failed to fetch news data. Please check your API key or try again later.")
                             with  tab8:
                              
                                api_key = "AIzaSyAjXob46DfOJ4EmDSxlzaOeMu2vFNMG3iE"
                                youtube = build("youtube", "v3", developerKey=api_key)
                                song_query=st.text_input("",placeholder="Write a song name  and hit enter")
                                song=st.empty()
                                with song:
                                     st_lottie("https://lottie.host/19b40b9a-5537-4b06-a316-19ad6d7f2db1/HEnD5GLrPh.json",width="200",height="200")
                                if song_query:
                                    song.empty()
                                    search_response = youtube.search().list(part="snippet",q=song_query, type="video", maxResults=2).execute()
                                    for search_result in search_response.get("items", []):
                                        video_id = search_result["id"]["videoId"]
                                        video_title = search_result["snippet"]["title"]
                                        video_url = f"https://www.youtube.com/watch?v={video_id}"
                                       
                                        video_url = f"https://www.youtube.com/watch?v={video_id}"
                                        st.video(video_url)

     
                                        st.markdown("---")
                                
                                 

                            
                             #5a2401032c9d48e9a1ae511bbfa6efb9
                         if pusha:
                          for ush in allu.each():
                              k=ush.val().get("Handle")
                              if k==cho:
                                   news.empty()
                                   l=ush.val().get("ID")
                                   
                              
                                   userdata=data.child(l).child("Handle").get().val()
                                  
                                   
                         
                                   st.markdown(f"___")
                           
                                   nimg=data.child(l).child("Images").get().val()
                                   if nimg is not None:
                                        v=data.child(l).child("Images").get()
                                        for img in v.each():
                                             imgc=img.val()
                                    
                                        st.markdown(f'<div style="display: flex; justify-content: center;"><img src="{imgc}" width="200" height="200" style="border-radius:50%;"></div>', unsafe_allow_html=True)
                       
                                   else:
                                        st_lottie("https://lottie.host/9839c16f-ad3d-43b0-ba7d-f5399cced728/6459NXwpZO.json",width="200",height="200")

                                        #st.markdown(f'<div style="display: flex; justify-content: center;"><img src="https://img.icons8.com/fluency/500/user-male-circle.png" width="200" height="200"  style="border-radius:50%;"></div>', unsafe_allow_html=True)
                                   st.markdown(f'<div style="display: flex; justify-content: center;"><h2>{userdata}</h2></div>',unsafe_allow_html=True)


                                   #followers_count = 0
                                  # followers_query = data.child("followers").child(l).get()
                                  # if followers_query:
                                   #     for follower in followers_query.each():
                                        
                                    #         followers_count += 1
                                  
                                   
                                  # st.markdown(f'<div style="display: flex; justify-content: center;"><h5>{followers_count}</h5></div>',unsafe_allow_html=True)
                                  
                                   st.subheader("Bio :")
                                   
                                   bio=data.child(l).child("Bio").get().val()
                                   if bio is not None:
                                        bioinfo=data.child(l).child("Bio").get()
                                        for bio in bioinfo.each():
                                             bioc=bio.val()
                                        st.text(bioc)
                                             
                                   else:
                                        st.info("No Bio  till now !")

                                   joined=data.child(l).child("date").get().val()
                                   if joined is not None:
                                         joined=data.child(l).child("date").get()
                                         for joined in joined.each():
                                              joic=joined.val()
                                              st.markdown(f'<div style="display: flex; justify-content: left;"><h5>{joic}</h5></div>',unsafe_allow_html=True)



                                   tab5,tab6=st.tabs(["Thought's","Pic's"])

                                   with tab5:
                                        all_posts=data.child(l).child("Posts").get()
                                        if all_posts.val() is not None:
                                             for Posts in reversed(all_posts.each()):
                                                 
                                                   message = st.chat_message("user")
                                                   message.write(Posts.val())
                                      
                                        else:
                                             st.info("No thought's  till now !")
                                   with tab6:
                                        posts=data.child(l).child("posts").get()
                                        if  posts.val() is not None:
                                             for Posts in posts.each():
                                                  caption = Posts.val()["caption"]
                                                  image_url = Posts.val()["image_url"]
                                                  st.success(caption)
                                                  response = requests.get(image_url)
                                                  img = imgget.open(BytesIO(response.content))
                                                  st.image(img, use_column_width=True)
                                                  st.markdown(f"___")
                                        else:
                                             st.info("No pic's  till now !")
                                   
                                        
                                            
                                


                                   

                                    
                                
                           
                          
                         
                         
                          
                     
                              
                     
                         
                        
                         
                      
                        
                         
                         
                          
                 #["chat-left-fill","camera-fill"]
                 #AIzaSyAjXob46DfOJ4EmDSxlzaOeMu2vFNMG3iE
                     
                     
                    
                         

                            
                         
               
               except:
                    st.markdown("<center><img src=https://img.icons8.com/fluency/500/soulseek.png; alt=centered imgget; height=150; width=150> </center>",unsafe_allow_html=True)
                    textcolor= """ <style>.gradient-text{background: linear-gradient(to left,#3CCBF4,#2DB4EC,#20A2E6);-webkit-background-clip: text;-webkit-text-fill-color: transparent;font-family:serif;font-weight: 600;font-style:italic;color:#1A6DFF;text-align:center;font-size:30px; }  </style>"""
                    st.markdown(textcolor,unsafe_allow_html=True)
                    st.markdown('<p class="gradient-text">ℂ𝕙𝕚𝕡𝕡𝕖𝕣</p>', unsafe_allow_html=True)

                    st.error("Invalid Email address or Password !")
                    
                     
                    st.write("[Forgot password?](https://chipperforgotpassword.streamlit.app)")

                    st.markdown(f"___")
                   
                    st.write('<div style="text-align: center;">🔙<a href="https://chipper.streamlit.app">Return back to Log in page</a></div>', unsafe_allow_html=True)
                    #http://localhost:8501/
                     
                    
               
                  
      
    
               

        
        
         


