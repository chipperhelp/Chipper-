import streamlit as st
import pyrebase
from datetime import datetime
from streamlit_option_menu import option_menu
from PIL import Image
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

#streamlit=1.24.0
#on streamlit cloud streamlit=1.16.0
#now on streamit cloud streamlit==1.26.0
#current version changed to streamlit=1.26.0from streamlit=1.24.0











logot=Image.open("logo.png")

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

streamlitstyle = """
			<style>
			sidebar,body,[class*="css"]{background-image: url("https://cdn.theatlantic.com/thumbor/Sy0CJqDYC9tkLmlM1XA4GgksyYo=/0x0:3500x1969/960x540/media/img/mt/2023/02/yo_yo_economy/original.gif");
                        background-attachment: fixed;
                        background-size: cover 
			
			
                       
			
			
                        }
			</style>
			"""



#st.markdown(streamlitstyle, unsafe_allow_html=True)



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
     st.markdown("<center><img src=https://img.icons8.com/fluency/500/soulseek.png; alt=centered image; height=150; width=150> </center>",unsafe_allow_html=True)
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
                          Image=data.child(user["localId"]).child("Images").get()
                          for img in Image.each():
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
                                st.sidebar.markdown(f'<div style="display: flex; justify-content: center;"><img src="https://img.icons8.com/fluency/500/user-male-circle.png" width="200" height="200"  style="border-radius:50%;"></div>', unsafe_allow_html=True)
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
                    st.sidebar.subheader("🪪 Update your Bio :")
                    bio=data.child(user["localId"]).child("Bio").get().val()
                    if bio is not None:
                        bio=data.child(user["localId"]).child("Bio").get()
                        for bio in bio.each():
                            bioc=bio.val()
                        st.sidebar.info(bioc)
                        
                        bioin=st.sidebar.text_area("",placeholder="Enter your Bio to be uploaded eg: name,date of birth etc")
                        upbtn=st.sidebar.button("Upload Bio")

                        if upbtn:
                           
                            

                            data.child(user["localId"]).child("Bio").push(bioin)

                            st.sidebar.info("Bio set successfully !")
                            
                    else:
                        st.sidebar.info("No Bio till now !")
                        bioin=st.sidebar.text_area("",placeholder="Enter your Bio to be uploaded eg: name,date of birth etc")
                        upbtn=st.sidebar.button("Upload Bio")

                        if upbtn:
                           
                           
                            data.child(user["localId"]).child("Bio").push(bioin)

                            st.sidebar.info("Bio set successfully !")
                    
                           


                   



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

                               st.markdown(f'<div style="display: flex; justify-content: center;"><img src="https://img.icons8.com/fluency/500/user-male-circle.png" width="200" height="200"  style="border-radius:50%;"></div>', unsafe_allow_html=True)
                               userdata=data.child(user['localId']).child("Handle").get().val()
                               #st.header(userdata)
                               st.markdown(f'<div style="display: flex; justify-content: center;"><h2>{userdata}</h2></div>',unsafe_allow_html=True)

                          st.subheader("Bio :")
                          bio=data.child(user["localId"]).child("Bio").get().val()
                          if bio is not None:
                              bio=data.child(user["localId"]).child("Bio").get()
                              for bio in bio.each():
                                   bioc=bio.val()
                                   st.info(bioc)
                          else:
                              st.info("No Bio  till now !")
                          joined=data.child(user['localId']).child("date").get().val()
                          if joined is not None:
                               joined=data.child(user['localId']).child("date").get()
                               for joined in joined.each():
                                    joic=joined.val()
                                    
                                    st.markdown(f'<div style="display: flex; justify-content: left;"><h5>{joic}</h5></div>',unsafe_allow_html=True)

                          tab3,tab4=st.tabs(["💭 Thought's","📷 Pic's"])
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
                                        img = Image.open(BytesIO(response.content))
                                        st.image(img, use_column_width=True)
                                        st.markdown(f"___")
                              else:
                                   st.info("No pic's  till now !")
                                   st.markdown(f"___")


                    elif nav=="  ":
                                   st.subheader("Share a Thought or Pic :")
                                  
                                   tab1,tab2 = st.tabs(["📝 Share a thought","📷 Share a pic "])
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
                                              image = st.file_uploader("", type=["jpg", "jpeg", "png","mp3"])
                                              if image is None:
                                                   st.warning("Please select a pic")
                                              upbta=st.button("Share the pic and caption")
                                              if upbta:
                                                  with st.spinner("Uploading image..."):
                                                       storage.child("images/" + image.name).put(image)
                                                       userdata=data.child(user['localId']).child("Handle").get().val()

                                                       now=datetime.now()
                                                       dt=now.strftime("%d / %m / %y")
                                                       dtt=now.strftime("%I:%M %p")
                                                       captiondata="Posted by \n"+userdata + "/n"+caption + " ; "  +  "\n  shared on :" + dt + "  at  " + dtt
                                                       post_data = {"caption": captiondata,"image_url": storage.child("images/" + image.name).get_url(None) }
                                                       data.child(user["localId"]).child("posts").push(post_data)
                                                       st.toast("Pic shared successfully")
                                   

                                    
                                
                           
                          
                         
                         
                          
                     
                              
                     
                         
                        
                         
                      
                        
                         
                         
                          
                 #["chat-left-fill","camera-fill"]
                     
                     
                    
                         

                            
                         
               
                except:
                    st.markdown("<center><img src=https://img.icons8.com/fluency/500/soulseek.png; alt=centered image; height=150; width=150> </center>",unsafe_allow_html=True)
                    textcolor= """ <style>.gradient-text{background: linear-gradient(to left,#3CCBF4,#2DB4EC,#20A2E6);-webkit-background-clip: text;-webkit-text-fill-color: transparent;font-family:serif;font-weight: 600;font-style:italic;color:#1A6DFF;text-align:center;font-size:30px; }  </style>"""
                    st.markdown(textcolor,unsafe_allow_html=True)
                    st.markdown('<p class="gradient-text">ℂ𝕙𝕚𝕡𝕡𝕖𝕣</p>', unsafe_allow_html=True)

                    st.error("Invalid Email address or Password !")
                    
                     
                    st.write("[Forgot password?](https://chipperforgotpassword.streamlit.app)")

                    st.markdown(f"___")
                   
                    st.write('<div style="text-align: center;">🔙<a href="https://chippermain.streamlit.app">Return back to Log in page</a></div>', unsafe_allow_html=True)
                    #http://localhost:8501/
                     
                    
               
                  
      
    
               

        
        
         


