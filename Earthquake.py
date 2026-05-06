import streamlit as st
import requests

res= requests.get("https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=1990-03-01&endtime=1991-03-02&minmagnitude=5")

if res.status_code == 200:
    res=res.json()
    features=res["features"]



    col=st.columns([0.5,4,0.5])


    with col[1]:
        st.subheader("Earthquake Data")
        search_pharse=st.text_input("search text",placeholder="search here")

        for feature in features:
            props = feature["properties"]
            url = props['url']
            details = props['detail']



            if search_pharse .lower() in props ["place"].lower():
                with st.container(border=True):
                    col1=st.columns([3,2])
#with st.container(border=True):
                with col1[0]:
                    title=props["title"]
                    st.write(title)
                    st.write(f" **Magnitude:**{props['mag']}") 
                    st.write(f" **Place:**{props['place']}")
                    st.write(f" **type:**{props['type']}")
#                    url = features('featuresUrl')
                    st.link_button("More_Details",url,type="primary")
                    st.link_button("Details",f"details",type="tertiary")
                
                           
