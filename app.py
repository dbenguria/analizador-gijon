import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Analizador Inmobiliario - Gijón", layout="wide")
st.title("Pisos en Inversión - Gijón")

pisos = [
    {"Titulo": "Piso en Calle Rio de Oro", "Barrio": "El Llano", "Precio": 89000, "Habs": 3, "m2": 75, "Estado": "Buen estado", "Rent Largo Plazo": "9.89%", "Rent Estudiantes": "12.94%", "Fuente": "Idealista", "Enlace": "https://www.idealista.com/buscar/venta-viviendas/gijon/el-llano/", "lat": 43.5321, "lon": -5.6631},
    {"Titulo": "Piso en Calle Eleuterio Quintanilla", "Barrio": "El Llano", "Precio": 129900, "Habs": 2, "m2": 80, "Estado": "Reformado", "Rent Largo Plazo": "8.20%", "Rent Estudiantes": "11.10%", "Fuente": "Fotocasa", "Enlace": "https://www.fotocasa.es/es/comprar/viviendas/gijon/el-llano/l", "lat": 43.5310, "lon": -5.6645},
    {"Titulo": "Piso luminoso cerca de Begoña", "Barrio": "Centro", "Precio": 115000, "Habs": 3, "m2": 80, "Estado": "A reformar", "Rent Largo Plazo": "7.65%", "Rent Estudiantes": "10.02%", "Fuente": "Idealista", "Enlace": "https://www.idealista.com/buscar/venta-viviendas/gijon/centro/", "lat": 43.5392, "lon": -5.6601},
    {"Titulo": "Piso junto a Plaza Europa", "Barrio": "Centro", "Precio": 139000, "Habs": 2, "m2": 70, "Estado": "Buen estado", "Rent Largo Plazo": "6.80%", "Rent Estudiantes": "9.15%", "Fuente": "Pisos.com", "Enlace": "https://www.pisos.com/venta/pisos-gijon/", "lat": 43.5380, "lon": -5.6620},
    {"Titulo": "Apartamento a 2 min de la playa", "Barrio": "La Arena", "Precio": 135000, "Habs": 2, "m2": 65, "Estado": "Reformado", "Rent Largo Plazo": "6.04%", "Rent Estudiantes": "5.69%", "Fuente": "Idealista", "Enlace": "https://www.idealista.com/buscar/venta-viviendas/gijon/la-arena/", "lat": 43.5375, "lon": -5.6512},
    {"Titulo": "Piso próximo al Parque del Gas", "Barrio": "La Arena", "Precio": 158000, "Habs": 3, "m2": 85, "Estado": "Seminuevo", "Rent Largo Plazo": "5.50%", "Rent Estudiantes": "6.40%", "Fuente": "Fotocasa", "Enlace": "https://www.fotocasa.es/es/comprar/viviendas/gijon/la-arena/l", "lat": 43.5360, "lon": -5.6490},
    {"Titulo": "Piso exterior junto al parque", "Barrio": "Viesques", "Precio": 149000, "Habs": 3, "m2": 90, "Estado": "Seminuevo", "Rent Largo Plazo": "5.91%", "Rent Estudiantes": "7.73%", "Fuente": "Idealista", "Enlace": "https://www.idealista.com/buscar/venta-viviendas/gijon/viesques/", "lat": 43.5265, "lon": -5.6420},
    {"Titulo": "Piso con garaje en Av. del Llano", "Barrio": "El Llano", "Precio": 128000, "Habs": 2, "m2": 62, "Estado": "Buen estado", "Rent Largo Plazo": "7.90%", "Rent Estudiantes": "10.50%", "Fuente": "Idealista", "Enlace": "https://www.idealista.com/buscar/venta-viviendas/gijon/el-llano/", "lat": 43.5290, "lon": -5.6610},
    {"Titulo": "Piso ideal inversión La Calzada", "Barrio": "La Calzada", "Precio": 72000, "Habs": 3, "m2": 70, "Estado": "A reformar", "Rent Largo Plazo": "10.50%", "Rent Estudiantes": "13.80%", "Fuente": "Idealista", "Enlace": "https://www.idealista.com/buscar/venta-viviendas/gijon/la-calzada/", "lat": 43.5348, "lon": -5.6880},
    {"Titulo": "Oportunidad económica Pumarín", "Barrio": "Pumarín", "Precio": 79900, "Habs": 3, "m2": 72, "Estado": "Buen estado", "Rent Largo Plazo": "9.95%", "Rent Estudiantes": "13.10%", "Fuente": "Fotocasa", "Enlace": "https://www.fotocasa.es/es/comprar/viviendas/gijon/pumarin/l", "lat": 43.5270, "lon": -5.6710},
    {"Titulo": "Piso reformado cerca de Severo Ochoa", "Barrio": "Pumarín", "Precio": 95000, "Habs": 2, "m2": 65, "Estado": "Reformado", "Rent Largo Plazo": "8.84%", "Rent Estudiantes": "11.36%", "Fuente": "Pisos.com", "Enlace": "https://www.pisos.com/venta/pisos-gijon/", "lat": 43.5245, "lon": -5.6735},
    {"Titulo": "Vivienda amplia en El Coto", "Barrio": "El Coto", "Precio": 110000, "Habs": 3, "m2": 82, "Estado": "Buen estado", "Rent Largo Plazo": "8.18%", "Rent Estudiantes": "10.90%", "Fuente": "Idealista", "Enlace": "https://www.idealista.com/buscar/venta-viviendas/gijon/el-coto/", "lat": 43.5330, "lon": -5.6530},
    {"Titulo": "Piso junto a Av. Argentina", "Barrio": "La Calzada", "Precio": 84000, "Habs": 2, "m2": 68, "Estado": "Buen estado", "Rent Largo Plazo": "9.28%", "Rent Estudiantes": "11.78%", "Fuente": "Fotocasa", "Enlace": "https://www.fotocasa.es/es/comprar/viviendas/gijon/la-calzada/l", "lat": 43.5372, "lon": -5.6915},
    {"Titulo": "Piso vistas al puerto Natahoyu", "Barrio": "Natahoyu", "Precio": 105000, "Habs": 2, "m2": 64, "Estado": "Reformado", "Rent Largo Plazo": "7.42%", "Rent Estudiantes": "9.71%", "Fuente": "Idealista", "Enlace": "https://www.idealista.com/buscar/venta-viviendas/gijon/el-natahoyu/", "lat": 43.5410, "lon": -5.6780},
    {"Titulo": "Piso alto y soleado San José", "Barrio": "El Llano", "Precio": 99000, "Habs": 3, "m2": 78, "Estado": "Buen estado", "Rent Largo Plazo": "9.09%", "Rent Estudiantes": "12.12%", "Fuente": "Idealista", "Enlace": "https://www.idealista.com/buscar/venta-viviendas/gijon/el-llano/", "lat": 43.5302, "lon": -5.6655}
]

df = pd.DataFrame(pisos)

# Filtros laterales
st.sidebar.header("Filtros de Búsqueda")
precio_max = st.sidebar.slider("Presupuesto Máximo (€)", 50000, 200000, 160000)
fuente_filtro = st.sidebar.multiselect("Portal de Origen", df["Fuente"].unique(), default=df["Fuente"].unique())

df_filtered = df[(df["Precio"] <= precio_max) & (df["Fuente"].isin(fuente_filtro))]

# Mapa interactivo Folium
st.subheader("Mapa Interactivo de Inmuebles en Gijón")
m = folium.Map(location=[43.533, -5.663], zoom_start=13)

for _, row in df_filtered.iterrows():
    popup_text = f"""
    <div style='font-family: sans-serif; width: 200px;'>
        <b>{row['Titulo']}</b><br>
        Precio: <b>{row['Precio']:,} €</b><br>
        Largo Plazo: <b>{row['Rent Largo Plazo']}</b><br>
        Estudiantes: <b>{row['Rent Estudiantes']}</b><br><br>
        <a href='{row['Enlace']}' target='_blank'>Ver en {row['Fuente']}</a>
    </div>
    """
    folium.Marker(
        location=[row["lat"], row["lon"]],
        popup=folium.Popup(popup_text, max_width=250),
        tooltip=f"{row['Titulo']} - {row['Precio']:,} €",
        icon=folium.Icon(color="red", icon="home", prefix="fa")
    ).add_to(m)

st_folium(m, width=1100, height=450)

# Lista detallada debajo
st.subheader("Lista de Inmuebles Individuales")
for _, row in df_filtered.iterrows():
    col1, col2, col3 = st.columns([3, 2, 1])
    with col1:
        st.markdown(f"### {row['Titulo']}")
        st.write(f"Barrio: **{row['Barrio']}** | **{row['m2']} m²** | **{row['Habs']} Habs** | {row['Estado']}")
        st.write(f"Origen: **{row['Fuente']}**")
    with col2:
        st.write(f"**Precio:** {row['Precio']:,} €")
        st.write(f"**Rent. Largo Plazo (Tradicional):** {row['Rent Largo Plazo']}")
        st.write(f"**Rent. Estudiantes (Por Hab.):** {row['Rent Estudiantes']}")
    with col3:
        st.link_button(f"Ver en {row['Fuente']}", row['Enlace'])
    st.divider()
    st.divider()