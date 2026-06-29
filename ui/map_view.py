import folium
from streamlit_folium import st_folium


def render_map():

    m = folium.Map(
        location=[22.5,79],
        zoom_start=5,
        tiles="CartoDB dark_matter"
    )

    hospitals = [
        [19.0760,72.8777,"Mumbai Hospital"],
        [28.6139,77.2090,"Delhi Hospital"],
        [12.9716,77.5946,"Bangalore Hospital"],
        [18.5204,73.8567,"Pune Hospital"]
    ]

    rescue = [
        [22.5726,88.3639,"Kolkata Rescue"],
        [17.3850,78.4867,"Hyderabad Rescue"],
        [26.9124,75.7873,"Jaipur Rescue"]
    ]

    ngos = [
        [13.0827,80.2707,"NGO Camp Chennai"],
        [26.1445,91.7362,"NGO Camp Guwahati"]
    ]

    incidents = [
        [18.5204,73.8567,"Critical Incident"]
    ]

    for lat,lon,name in hospitals:

        folium.Marker(
            [lat,lon],
            popup=name,
            icon=folium.Icon(
                color="blue"
            )
        ).add_to(m)

    for lat,lon,name in rescue:

        folium.Marker(
            [lat,lon],
            popup=name,
            icon=folium.Icon(
                color="green"
            )
        ).add_to(m)

    for lat,lon,name in ngos:

        folium.Marker(
            [lat,lon],
            popup=name,
            icon=folium.Icon(
                color="orange"
            )
        ).add_to(m)

    for lat,lon,name in incidents:

        folium.Marker(
            [lat,lon],
            popup=name,
            icon=folium.Icon(
                color="red"
            )
        ).add_to(m)

    st_folium(
        m,
        width=1200,
        height=650
    )