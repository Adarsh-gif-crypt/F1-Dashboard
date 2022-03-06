import pandas as pd
import streamlit as st
import numpy as np
import altair as alt

st.set_page_config(layout='wide')

dfcont = pd.read_csv('D:\DS\Streamlit\Formula 1\Circuit Data\CircuitcontdataUpdated.csv')
dfloc = pd.read_csv('D:\DS\Streamlit\Formula 1\Circuit Data\circuitlocation.csv')

#df operations
dfcont.fillna('North America',inplace=True)
dfcontdata = pd.DataFrame({'Continent':['Europe','Asia','North America','South America','Africa','Australia'],
'Count':[14,14,3,2,1,1]})




image_spacer0, image1, image_spacer2 = st.columns((2,6,2))
image1.image('https://www.boip.int/uploads/inline/FORMULE1_0.gif')
title_spacer0, title1, tilte_space2 = st.columns((5,5,3))
title1.title('FORMULA ONE 🏎️')

row0c1, row0c2 = st.columns(2)
row0c1.markdown("""This webapp is designed and curated for Formula ONE, The pinnacle of motorsports around the whole world
. It showcases the historical statistics of Formula 1 since it started back in the 1950s. Feel free to learn more 
about it [here](https://en.wikipedia.org/wiki/Formula_One)""")
row0c2.markdown(""" Formula One (also known as Formula 1 or F1) is the highest class of international racing for 
open-wheel single-seater formula racing cars sanctioned by the Fédération Internationale de l'Automobile (FIA).
 The World Drivers' Championship, which became the FIA Formula One World Championship in 1981.
 For checking out the world of Formula One, check out its [website](https://www.formula1.com/).
 For more information about FIA [click here](https://en.wikipedia.org/wiki/F%C3%A9d%C3%A9ration_Internationale_de_l%27Automobile)""")

begins0,begin,begins1 = st.columns((1,5,1))
begin.markdown(""" ### To begin, please select one of the categories mentioned below """)

category = begin.selectbox('',('Categories','Circuits','Constructors', 'Drivers','Races','Seasons'))
#st.write('you selected :', category)
if(category =='Circuits'):
    row1titles0, row1title, row1titles1 = st.columns((4.5,5,2))
    row1title.title('Circuit Data')
    c1,c2,c3 = st.columns(3)
    c2.markdown("""This section showcases the information about the circuits and their locations. A detailed list of the information about the circuits can be found here.""")
    row2c1,row2c2 = st.columns(2)
    row2c1.subheader('Circuit distribution by countries')
    countpie = alt.Chart(dfcont).mark_arc().encode(
        theta = alt.Theta(field = 'value',type = 'quantitative'),
        color = alt.Color(field = 'countryname', type = 'nominal'), tooltip=['value', 'countryname']
    )
    row2c1.altair_chart(countpie,use_container_width = True)
    row2c2.subheader('Circuit distribution by Continents')
    contpie = alt.Chart(dfcontdata).mark_arc().encode(
        theta = alt.Theta(field = 'Count', type = 'quantitative'), color = alt.Color(field = 'Continent',type = 'nominal'),
        tooltip = ['Count','Continent']
    )
    row2c2.altair_chart(contpie, use_container_width = True)
    #st.write(dfcont)
    #st.write(dfloc)
    row3s0, row3, row3s1 = st.columns((5,6,4))
    row3.subheader('The Circuits on the Map of the World')
    st.map(dfloc,zoom = 1)
    note = st.expander('Please Note 👉 ')
    with note:
        st.markdown(""" All the circuits are shown in this map i.e. All the cicuits where there has been a Formula 1 Race""")
    row4s0, row4, row4s1 = st.columns((5,6,4))
    #choroplethcont = alt.Chart(dfcontdata).mark_geoshape().encode(
    #    color = 'Count'
    #).project('equirectangular')
        #st.altair_chart(choroplethcont)