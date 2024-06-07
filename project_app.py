import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import plotly.express as px
import path



@st.cache_data
def data():
    url= "https://github.com/LilianNekesa/project/blob/main/group2x.xlsx"
    df = pd.read_excel(url)
    return df

    data = data()



st.title ('PRODUCTION PERFORMANCE')
st.write ('This app analyzes a companys production performance and how each variety and greenhouse number contributes to total production and compares to its production area in meter square')

uploaded_file = st.file_uploader("Choose a file to upload:", type=["csv", "txt", "xlsx"])
if uploaded_file is not None:
    st.write(f"File uploaded: {uploaded_file.name}")

#show raw data

if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.dataframe(data)

variety = data()['VARIETY'].unique()
Variety_filter = st.multiselect("Select variety:", variety, default=variety)
filtered_data = data()[data()['VARIETY'].isin(Variety_filter)]

#select top performing variety
st.subheader("Top Performing Variety in Area")
top = st.number_input("Select the top performing variety:", min_value=5, max_value=100, value=10, step=1)
top_variety = filtered_data.nlargest(top, "SAREA")
fig = px.bar(top_variety, x="VARIETY", y="SAREA", color="VARIETY", hover_name="VARIETY", text="SAREA")
st.plotly_chart(fig)

#select least performing variety
st.subheader("Least performing variety in Area")
top = st.number_input("Select the least performing variety:", min_value=5, max_value=100, value=10, step=1)
top_variety = filtered_data.nsmallest(top, "SAREA")
fig1 = px.bar(top_variety, x="VARIETY", y="SAREA", color="VARIETY", hover_name="VARIETY", text="SAREA")
st.plotly_chart(fig1)


#bar of total number of varieties per greenhouse in terms of total production
st.subheader("Total number of varieties per greenhouse in terms of total production")
fig2=px.bar(data(), x='VARIETY', y='GH NO', labels="TOTPRO: Total number of varieties", barmode='group', text='TOTPRO', title='TOTAL NUMBER OF VARIETIES', color='TOTPRO')
st.plotly_chart(fig2)

#Variety performance in terms of production
st.subheader("VARIETY PERFORMANCE IN TERMS OF TOTAL PRODUCTION")
variety_performance=data().groupby('VARIETY')['TOTPRO'].sum().reset_index()
fig3=px.line(variety_performance, x='VARIETY', y='TOTPRO', title='VARIETY PERFORMANCE IN TERMS OF TOTAL PRODUCTION')
st.plotly_chart(fig3)

st.write('The highest produced variet in terms of total production is Athena with 3.137252 million, followed closely with moonwalk and Madam Red. The least produced variety is Borneo! with a total of 7110')

#first quarter of the year performance
st.subheader("VARIETY PERFORMANCE IN THE FIRST QUARTER")
variety_performance=data().groupby('VARIETY')['QUARTER1'].sum().reset_index()
fig4=px.line(variety_performance, x='VARIETY', y='QUARTER1', title='VARIETY PERFORMANCE IN THE FIRST QUARTER')
st.plotly_chart(fig4)
st.write('Athena had the highest production in the firstquarter with a total of 778, 396 in production followed closely by Moonwalk with a total of 578,615. Some varieties with a production of 1 were experiencin replanting while others were being uprooted. Madam bombastic had the lowest production of 459 in quarter1')

#second quarter of the year performance
st.subheader("VARIETY PERFORMANCE IN THE SECOND QUARTER")
variety_performance=data().groupby('GH NO')['QUARTER 2'].sum().reset_index()
fig5=px.line(variety_performance, x='GH NO', y='QUARTER 2', labels= 'TOTPRO', title='GH PERFORMANCE IN Quarter3')
st.plotly_chart(fig5)

st.write('GH NO 11 had the highest produce of 557,217k in quarter3. GH NO 15 came second best with a total of 481,260. The least performing green house was GHNO 24 with 100.39k')

#Third quarter of the year performance
st.subheader("VARIETY PERFORMANCE IN THE Third QUARTER")
variety_performance=data().groupby('GH NO')['QUARTER3'].sum().reset_index()
fig6=px.line(variety_performance, x='GH NO', y='QUARTER3', labels= 'TOTPRO', title='GH PERFORMANCE IN Quarter3')
st.plotly_chart(fig6)

#FIRST half of the year performance
st.subheader("VARIETY PERFORMANCE IN THE FIRST HALF")
variety_performance=data().groupby('VARIETY')['FIRSTHA'].sum().reset_index()
fig7=px.bar(variety_performance, x='VARIETY', y='FIRSTHA', title='VARIETY PERFORMANCE IN TERMS OF TOTAL PRODUCTION')
st.plotly_chart(fig7)

st.write('Athena had the highest production in the firstquarter with a total of 778, 396 in production followed closely by Moonwalk with a total of 578,615. Some varieties with a production of 1 were experiencin replanting while others were being uprooted.Madam bombastic had the lowest production of 459 in quarter1')

#Second half of the year performance
st.subheader("VARIETY PERFORMANCE IN THE SECOND HALF")
variety_performance=data().groupby('VARIETY')['SECONDHA'].sum().reset_index()
fig8=px.bar(variety_performance, x='VARIETY', y='SECONDHA', title='VARIETY PERFORMANCE IN TERMS OF TOTAL PRODUCTION')
st.plotly_chart(fig7)
st.write('in 2022 production of Second half for the year, Athena had the largest produce of 1.687152Million. It was then followed closely by Madam Red with a production of 1.185626 million. Miss bombastic had the least production of 1 because of replanting.So, the second least produced variety in this half is Lay Bombastic with 1130')

#Which GH NO contributes the highest percentage in production during the first half of the year
st.subheader("VARIETY PERFORMANCE IN THE FIRST HALF AS A PERCENTAGE")
fig9=px.pie(data(), values='FIRSTHA', names="GH NO")
st.plotly_chart(fig9)
st.write('GH NO 15 contributes the highest production of 5.87% in the FIRSTHA. The least performing is GH NO 24 contributing only 1.01%')

#Which GH NO contributes the highest percentage in production during the second half of the year
st.subheader("VARIETY PERFORMANCE IN THE SECOND HALF AS A PERCENTAGE")
fig10=px.pie(data(), values='SECONDHA', names="GH NO")
st.plotly_chart(fig10)
st.write('The highest performing is GH NO 11 contributing 6.67% in production. The least performing is GH NO 24 which contributes 1.6% in production')

