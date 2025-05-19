import streamlit as st
import pandas as pd
import plotly.express as px
import json
import codecs
import ast


# Load tourism trends data
tourism_data = pd.read_csv("data/tourism_trends.csv")

# Load cultural sites JSON safely (handles BOM if present)

with codecs.open("data/cultural_sites.json", "r", encoding="utf-8-sig") as file:
    cultural_sites = json.load(file)

# Convert JSON to DataFrame
cultural_df = pd.DataFrame([{
    "Name": site["name"],
    "Category": site["category"],
    "Description": site["description"],
    "latitude": site["location"]["latitude"],
    "longitude": site["location"]["longitude"]
} for site in cultural_sites])

# Sidebar navigation
st.sidebar.title("Explore India's Culture")
page = st.sidebar.selectbox("Choose a section", ["🏠 Home", "📍 Cultural Hotspots", "📈 Tourism Trends", "🏛️ Government Initiatives"])

# Home Page
if page == "🏠 Home":
    st.title("Discover India's Art & Culture 🇮🇳")
    st.image("UNESCO.jpg", use_column_width=True)
    st.markdown("""
        India is home to a vast array of traditional art forms, sacred places, and cultural experiences.
        This interactive dashboard helps you explore these gems and promote responsible tourism.
    """)

# Cultural Hotspots Page
elif page == "📍 Cultural Hotspots":
    st.title("Cultural Hotspots in India")
    selected_category = st.selectbox("Filter by Category", ["All"] + sorted(cultural_df["Category"].unique()))
    filtered_df = cultural_df if selected_category == "All" else cultural_df[cultural_df["Category"] == selected_category]

    st.dataframe(filtered_df[["Name", "Category", "Description"]], use_container_width=True)
    st.map(filtered_df[["latitude", "longitude"]])

# Tourism Trends Page
elif page == "📈 Tourism Trends":
    st.title("Tourism Trends in India")
    if "Month" in tourism_data.columns and "Tourists" in tourism_data.columns:
        fig = px.line(
            tourism_data,
            x="Month",
            y="Tourists",
            color='State' if 'State' in tourism_data.columns else None,
            title="Seasonal Tourism Trends"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("CSV must contain 'Month' and 'Tourists' columns.")

# Government Initiatives Page
elif page == "🏛️ Government Initiatives":
    st.title("Government Support for Cultural Heritage")
    st.markdown("""
        The Government of India has launched several major schemes:

        - **HRIDAY** (Heritage City Development)
        - **PRASAD** (Pilgrimage Rejuvenation)
        - **Incredible India 2.0**

        These programs aim to:
        - Preserve cultural heritage
        - Promote spiritual and historical tourism
        - Improve infrastructure at key cultural sites
        - Encourage responsible and sustainable travel
    """)

# Footer
st.sidebar.markdown("---")
st.sidebar.text("Made with ❤️ using Streamlit")
