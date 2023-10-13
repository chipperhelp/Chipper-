import streamlit as st
import pyrebase
import datetime
from streamlit_option_menu import option_menu
from PIL import Image as imgget
import requests
import streamlit.components.v1 as components
import random
import json
from io import BytesIO
import feedparser
import urllib.request
import uuid
import ast 
from streamlit_lottie import st_lottie
from googleapiclient.discovery import build
import hydralit_components as hc#new 
import extra_streamlit_components as stx#new

#new
#streamlit=1.24.0
#on streamlit cloud streamlit=1.16.0
#now on streamit cloud streamlit==1.26.0
#current version changed to streamlit=1.26.0from streamlit=1.24.0




logot=imgget.open("logo.png")

st.set_page_config(page_title="Chipper",page_icon=logot,layout='wide',initial_sidebar_state='auto')





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





streamlitstyle = """
			<style>
			sidebar,body,form,[class*="css"]{background-image: url("https://media.tenor.com/SpNcK_OnyC0AAAAC/water-wave.gif");
                        background-attachment: fixed;
                        background-size: cover 
			
			
                       
			
			
                        }
			</style>
			"""
#st.markdown(streamlitstyle, unsafe_allow_html=True)
        



        
def get_manager():
    return stx.CookieManager()
cookie_manager = get_manager()
def main():
    user_id=cookie_manager.get("user_id")

    if user_id:
        
         userdata=data.child(user_id).child("Handle").get().val()
         menu_data = [{'id':'house','icon': "bi bi-house-fill", 'label':"Home"},{'id':'search','icon': "bi bi-search", 'label':"Search"},{'id':'write','icon': "bi bi-pencil-square", 'label':"Share"},{'id':'account','icon': "bi bi-person-fill", 'label':f"{userdata}"}]
         over_theme = {'txc_inactive': 'lightblue','menu_background':'#20A2E6','txc_active':'lightblue'}
         nav= hc.nav_bar(menu_definition=menu_data, override_theme=over_theme, sticky_mode='stickey')


         if nav=="search":
                         allu=data.get()
                         resa=[]
                         for ush in allu.each():
                              user_data=ush.val()
                              if isinstance(user_data,dict):
                                   k=ush.val().get("Handle")
                                   if k:
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
                                      st.error("Failed to fetch news data. Please try again later.")
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
                                        #data.child(user["localId"]).child("songs").push(video_url)

     
                                        st.markdown("---")
                                                                         
                                
                                 

                            
                             #5a2401032c9d48e9a1ae511bbfa6efb9
                         if pusha:
                          for ush in allu.each():
                               user_data = ush.val()
                               if isinstance(user_data, dict):
                                    k = user_data.get("Handle")
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

                                         tab5,tab6,tab7=st.tabs(["Thought's","Pic's","Video's"])
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
                                                  for Posts in reversed(posts.each()):
                                                       caption = Posts.val()["caption"]
                                                       image_url = Posts.val()["image_url"]
                                                       message = st.chat_message("user")
                                                       message.write(caption)
                                                       #st.success(caption)
                                                       response = requests.get(image_url)
                                                       img = imgget.open(BytesIO(response.content))
                                                       #st.image(img, use_column_width=True)
                                                       st.markdown(f'<div style="display: flex; justify-content: center"><img src="{image_url}" width="400" height="400" style="border-radius:10%; border: 2px solid #555"></div>', unsafe_allow_html=True)
                                                       st.markdown(f"___")
                                             else:
                                                  st.info("No pic's  till now !")
                                         with tab7:
                                              posts=data.child(l).child("videosdata").get()
                                              if  posts.val() is not None:
                                                   for Posts in reversed(posts.each()):
                                                        caption = Posts.val()["caption"]
                                                        image_url = Posts.val()["image_url"]
                                                        message = st.chat_message("user")
                                                        message.write(caption)
                                             
                                                        st.video(image_url)
                                                        st.markdown(f"___")
                                              else:
                                                  st.info("No Video's  till now !")
                                                 

                                        

             

         if nav=="house":
             all_user_posts_response = data.get("Posts")
             all_user_posts = all_user_posts_response.val()
             st.markdown("""<style>.like-button {margin-left: 10px;}</style>""",unsafe_allow_html=True)
             if all_user_posts is not None:
                 reversed_users = reversed(all_user_posts.items())
                 for post_id, post_content in all_user_posts.items():
                     if isinstance(post_content, dict) and "Posts" in post_content:
                         posts_data = post_content.get("Posts")
                         if posts_data is not None:
                             for post_id, post_info in reversed(list(posts_data.items())):
                                 message = st.chat_message("user")
                                 message.write(post_info)
                                 
                                 like_button_key = f"like_button_{post_id}"

                                 liked = data.child("likes_data").child(user_id).child(post_id).get().val()
                                 like_count = data.child("Posts").child(post_id).child("likes").get().val()

                                 if liked:
                                     st.button(f"👍 Like's:{like_count}", key=like_button_key,disabled=True)
                                 else:
                                    if st.button("👍 Double tap to like", key=like_button_key):
                                        current_likes = data.child("Posts").child(post_id).child("likes").get().val()
                                        if current_likes is None:
                                            current_likes = 0
                                            current_likes += 1
                                            data.child("Posts").child(post_id).child("likes").set(current_likes)
                                            data.child("likes_data").child(user_id).child(post_id).set(True)
                                 st.markdown(f"___")
         if nav=="account":
                          nimg=data.child(user_id).child("Images").get().val()
                          if nimg is not None:
                               v=data.child(user_id).child("Images").get()
                               for img in v.each():
                                    imgc=img.val()
                               st.markdown(f'<div style="display: flex; justify-content: center;"><img src="{imgc}" width="200" height="200" style="border-radius:50%;"></div>', unsafe_allow_html=True)
                               userdata=data.child(user_id).child("Handle").get().val()
                               st.markdown(f'<div style="display: flex; justify-content: center;"><h2>{userdata}</h2></div>',unsafe_allow_html=True)
                          else:

                               #st.markdown(f'<div style="display: flex; justify-content: center;"><img src="https://img.icons8.com/fluency/500/user-male-circle.png" width="200" height="200"  style="border-radius:50%;"></div>', unsafe_allow_html=True)
                               st_lottie("https://lottie.host/9839c16f-ad3d-43b0-ba7d-f5399cced728/6459NXwpZO.json",width="200",height="200")
                               userdata=data.child(user_id).child("Handle").get().val()
                               #st.header(userdata)
                               st.markdown(f'<div style="display: flex; justify-content: center;"><h2>{userdata}</h2></div>',unsafe_allow_html=True)

                          st.subheader("Bio :")
                          bio=data.child(user_id).child("Bio").get().val()
                          if bio is not None:
                              bio=data.child(user_id).child("Bio").get()
                              for bio in bio.each():
                                   bioc=bio.val()
                              st.text(bioc)
                          else:
                              st.info("No Bio  till now !")
                          joined=data.child(user_id).child("date").get().val()
                          if joined is not None:
                               joined=data.child(user_id).child("date").get()
                               for joined in joined.each():
                                    joic=joined.val()
                                    
                                    st.markdown(f'<div style="display: flex; justify-content: left;"><h5>{joic}</h5></div>',unsafe_allow_html=True)

                          tab3,tab4,tab5=st.tabs(["Thought's","Pic's","Video's"])
                          with tab3:
                              all_posts=data.child(user_id).child("Posts").get()
                              if all_posts.val() is not None:
                                   for Posts in reversed(all_posts.each()):
                                       
                                        message = st.chat_message("user")
                                        message.write(Posts.val())
                                      
                                        
                                        st.markdown(f"___")
                              else:
                                   st.info("No thought's  till now !")
                                   st.markdown(f"___")
                          with tab4:
                              posts=data.child(user_id).child("posts").get()
                              if  posts.val() is not None:
                                   for Posts in reversed(posts.each()):
                                        caption = Posts.val()["caption"]
                                        image_url = Posts.val()["image_url"]
                                        message = st.chat_message("user")
                                        message.write(caption)
                                        response = requests.get(image_url)
                                        img= imgget.open(BytesIO(response.content))
                                        #st.image(img, use_column_width=True)
                                        st.markdown(f'<div style="display: flex; justify-content: center"><img src="{image_url}" width="400" height="400" style="border-radius:10%; border: 2px solid #555"></div>', unsafe_allow_html=True)

                                        st.markdown(f"___")
                              else:
                                   #st_lottie("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")

                                   st.info("No pic's  till now !")
                                   st.markdown(f"___")
                              with tab5:
                                   posts=data.child(user_id).child("videosdata").get()
                                   if  posts.val() is not None:
                                        for Posts in reversed(posts.each()):
                                             caption = Posts.val()["caption"]
                                             image_url = Posts.val()["image_url"]
                                             message = st.chat_message("user")
                                             message.write(caption)
                                             
                                             st.video(image_url)
                                             #st.markdown(f'<div style="display: flex; justify-content: center"><img src="{image_url}" width="400" height="400" style="border-radius:10%; border: 2px solid #555"></div>', unsafe_allow_html=True)

                                        st.markdown(f"___")
                                   else:
                                   #st_lottie("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
                                        st.info("No Video's  till now !")
                                        st.markdown(f"___")

             
         if nav=="write":
                                   st.subheader("Share a Thought or Pic :")
                                  
                                   tab1,tab2,tab3 = st.tabs(["Share a thought","Share a pic ","Share a video"])
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
                                                       userdata=data.child(user_id).child("Handle").get().val()
                                                        


                                                       post=f'''{userdata}  \n {post} \n\n  shared on : {dt}  at  {dtt}'''
                                                       results=data.child(user_id).child("Posts").push(post)
                                                       st.toast("Thought shared successfully")
                                   with tab2:
                                         
                                         caption = st.text_input("",placeholder="Add a caption to your pic ")
                                         expan=st.expander("Share your pic")
                                         with expan:
                                              imgex = st.file_uploader("", type=["jpg", "jpeg", "png","gif"],key="none")
                                              #if imgex is None:
                                                   #st.warning("Please select a pic")
                                              upbta=st.button("Share your pic")
                                              if upbta:
                                                  with st.spinner("Uploading image..."):
                                                       storage.child("images/" + imgex.name).put(imgex)
                                                       userdata=data.child(user_id).child("Handle").get().val()

                                                       now=datetime.now()
                                                       dt=now.strftime("%d / %m / %y")
                                                       dtt=now.strftime("%I:%M %p")
                                                       captiondata=f'''{userdata} \n\n  {caption} \n\n shared on : {dt} at  {dtt}'''
                                                       post_data = {"caption": captiondata,"image_url": storage.child("images/" + imgex.name).get_url(None) }
                                                       data.child(user_id).child("posts").push(post_data)
                                                       st.toast("Pic shared successfully")
                                   with tab3:
                                        cap=st.text_input("",placeholder="Add a caption to your video")
                                        expn=st.expander("Share your video")
                                        with expn:
                                             vidx=st.file_uploader("",type=["mp4"])
                                             up=st.button("Share your video")
                                             if up:
                                                  with st.spinner("Uploading your video..."):
                                                       storage.child("videos/"+vidx.name).put(vidx)
                                                       userd=data.child(user_id).child("Handle").get().val()
                                                       now=datetime.now()
                                                       dt=now.strftime("%d / %m / %y")
                                                       dtt=now.strftime("%I:%M %p")
                                                       captiondata=f'''{userd} \n\n  {cap} \n\n shared on : {dt} at  {dtt}'''
                                                       post_data = {"caption": captiondata,"image_url": storage.child("videos/" + vidx.name).get_url(None) }
                                                       data.child(user_id).child("videosdata").push(post_data)
                                                       st.toast("Video shared successfully")
                                                       
                                                 
                                                  
            
             
         nimg=data.child(user_id).child("Images").get().val()
         if nimg is not None:
             imgg=data.child(user_id).child("Images").get()
             for img in imgg.each():
                 imgc=img.val()
             st.sidebar.markdown(f'<div style="display: flex; justify-content: center;"><img src="{imgc}" width="200" height="200" style="border-radius:50%;"></div>', unsafe_allow_html=True)
             expa=st.sidebar.expander("👤 Change your profile pic")
             with expa:
                 newimgp=st.file_uploader("",type=["jpg", "jpeg", "png","gif"])
                 upbt=st.button("Upload profile pic")
                               
                 if upbt:
                     
                    
                     dataup=storage.child(user_id).put(newimgp)
                     aimgdata=storage.child(user_id).get_url(dataup["downloadTokens"])

                     data.child(user_id).child("Images").push(aimgdata)
                                    
                 if st.button("🗑 Double tap to remove profile pic"):
                         data.child(user_id).child("Images").remove()
                               
                                 
         else:
                                #st.sidebar.markdown(f'<div style="display: flex; justify-content: center;"><img src="https://img.icons8.com/fluency/500/user-male-circle.png" width="200" height="200"  style="border-radius:50%;"></div>', unsafe_allow_html=True)
             with st.sidebar:
                 st_lottie("https://lottie.host/9839c16f-ad3d-43b0-ba7d-f5399cced728/6459NXwpZO.json",width="200",height="200")
             expand=st.sidebar.expander("📷 Choose your profile pic :")
             with expand:
                 newimgp=st.file_uploader("",type=["jpg", "jpeg", "png","gif"])
                 upbt=st.button("Upload profile pic")
                 if upbt:
                     
                     
                     dataup=storage.child(user_id).put(newimgp)
                     aimgdata=storage.child(user_id).get_url(dataup["downloadTokens"])
                     data.child(user_id).child("Images").push(aimgdata)
         st.sidebar.markdown(f"___")
         expanderbio=st.sidebar.expander("🪪 Update your Bio ")
         bio=data.child(user_id).child("Bio").get().val()
         with expanderbio:
            if bio is not None:
                bio=data.child(user_id).child("Bio").get()
                for bio in bio.each():
                    bioc=bio.val()
                st.text(bioc)
                bioin=st.text_area("",placeholder="Enter your Bio to be uploaded eg: name,date of birth etc")
                upbtn=st.button("Upload Bio")
                if upbtn:
                    data.child(user_id).child("Bio").push(bioin)
                    st.info("Bio set successfully !")
            else:
                    st.info("No Bio till now !")
                    bioin=st.text_area("",placeholder="Enter your Bio to be uploaded eg: name,date of birth etc")
                    upbtn=st.button("Upload Bio")
                    if upbtn:
                        data.child(user_id).child("Bio").push(bioin)
                        st.info("Bio set successfully !")
         st.sidebar.markdown(f"___")
         log=st.sidebar.expander("Log out of chipper?")
         with log:
             st.write("You can always log back in at any time.")
             abc=st.button("Log out")
             if abc:
                 cookie_manager.delete("user_id")
        
         
    else:
        login()
def login():
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
    st.markdown('<p class="gradienttext">Log in :</p>', unsafe_allow_html=True)
    with st.form("login"):


        



        
        
        
        email = st.text_input("",placeholder="Email")
        password = st.text_input("",placeholder="Password", type="password")
        st.write("[Forgot password?](https://chipperforgotpassword.streamlit.app)")

        login = st.form_submit_button("Log in")
        if login:
            if not email or not password :
               
                st.toast("⚠️ Please enter your full credentials !")
            else:
                try:
                    user = auth.sign_in_with_email_and_password(email, password)
                    user_id = user['localId']
                    cookie_manager.set("user_id", user_id,expires_at=datetime(year=3000,month=1,day=1))
                    st.info("Tap again to log in")
                except:
                    st.toast("🚫 Invalid Email address or Password !")
            
        
    st.write('<div style="text-align: center;">New to Chipper? <a href="https://chipperregister.streamlit.app">Register now</a></div>', unsafe_allow_html=True)
   



    
if __name__=="__main__":
    main()
    
