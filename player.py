import streamlit as st
import requests
 
res=requests.get("https://openwhyd.org/hot/electro?format=json")
 
if res.status_code == 200:
    res=res.json()
    tracks=res["tracks"]
 
 
    col=st.columns([0.3,3,0.3])
 
 
   
    with col[1]:
      st.subheader("Music Always")
      search_pharse=st.text_input("serach text",placeholder="🔍search here",label_visibility="collapsed")
   
      for track in tracks:
          if search_pharse in track["name"]:
            with st.container(border=True):
              col1=st.columns([3,2])
    # with st.container(border=True):
            with col1[0]:
               title=track["name"]
               st.write(title[:35]+"....")
               st.write(f"🧑‍🎤{track['uNm']}")
               url=track["trackUrl"]
               st.link_button("Play",f"https:{url}",type="tertiary")
            with col1[1]:
               st.image(track["img"])
