import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Analizador Inmobiliario - Gijón", layout="wide")
st.title("Pisos en Inversión - Gijón")

pisos = [
    # ── ZONA ESTE / UNIVERSIDAD EUROPEA (La Pecuaria / Viesques / Cabueñes) ──
    {"Titulo": "Piso próximo a Parque Científico y La Pecuaria", "Barrio": "Viesques", "Precio": 142000, "Alquiler Num": 730, "Alquiler Mensual": "730 €", "Habs": 3, "m2": 86, "Estado": "Buen estado", "Rent LP Num": 6.20, "Rent Largo Plazo": "6.20%", "Rent Est Num": 8.90, "Rent Estudiantes": "8.90%", "Fuente": "Idealista", "Enlace": "https://www.idealista.com/buscar/venta-viviendas/gijon/viesques/", "lat": 43.5255, "lon": -5.6410},
    {"Titulo": "Inversión junto a La Guía y Campus Este", "Barrio": "La Guía", "Precio": 155000, "Alquiler Num": 750, "Alquiler Mensual": "750 €", "Habs": 3, "m2": 90, "Estado": "Reformado", "Rent LP Num": 5.80, "Rent Largo Plazo": "5.80%", "Rent Est Num": 8.20, "Rent Estudiantes": "8.20%", "Fuente": "Fotocasa", "Enlace": "https://www.fotocasa.es/es/comprar/viviendas/gijon/la-guia/l", "lat": 43.5350, "lon": -5.6380},
    {"Titulo": "Oportunidad camino de Cabueñes / Pecuaria", "Barrio": "Viesques", "Precio": 135000, "Alquiler Num": 780, "Alquiler Mensual": "780 €", "Habs": 2, "m2": 75, "Estado": "Buen estado", "Rent LP Num": 6.90, "Rent Largo Plazo": "6.90%", "Rent Est Num": 9.50, "Rent Estudiantes": "9.50%", "Fuente": "Pisos.com", "Enlace": "https://www.pisos.com/venta/pisos-gijon/", "lat": 43.5230, "lon": -5.6395},

    # ── RESTO DE PISOS ──
    {"Titulo": "Piso en Calle Rio de Oro", "Barrio": "El Llano", "Precio": 89000, "Alquiler Num": 734, "Alquiler Mensual": "734 €", "Habs": 3, "m2": 75, "Estado": "Buen estado", "Rent LP Num": 9.89, "Rent Largo Plazo": "9.89%", "Rent Est Num": 12.94, "Rent Estudiantes": "12.94%", "Fuente": "Idealista", "Enlace": "https://www.idealista.com/buscar/venta-viviendas/gijon/el-llano/", "lat": 43.5321, "lon": -5.6631},
    {"Titulo": "Piso en Calle Eleuterio Quintanilla", "Barrio": "El Llano", "Precio": 129900, "Alquiler Num": 888, "Alquiler Mensual": "888 €", "Habs": 2, "m2": 80, "Estado": "Reformado", "Rent LP Num": 8.20, "Rent Largo Plazo": "8.20%", "Rent Est Num": 11.10, "Rent Estudiantes": "11.10%", "Fuente": "Fotocasa", "Enlace": "https://www.fotocasa.es/es/comprar/viviendas/gijon/el-llano/l", "lat": 43.5310, "lon": -5.6645},
    {"Titulo": "Piso luminoso cerca de Begoña", "Barrio": "Centro", "Precio": 115000, "Alquiler Num": 733, "Alquiler Mensual": "733 €", "Habs": 3, "m2": 80, "Estado": "A reformar", "Rent LP Num": 7.65, "Rent Largo Plazo": "7.65%", "Rent Est Num": 10.02, "Rent Estudiantes": "10.02%", "Fuente": "Idealista", "Enlace": "https://www.idealista.com/buscar/venta-viviendas/gijon/centro/", "lat": 43.5392, "lon": -5.6601},
    {"Titulo": "Piso junto a Plaza Europa", "Barrio": "Centro", "Precio": 139000, "Alquiler Num": 787, "Alquiler Mensual": "787 €", "Habs": 2, "m2": 70, "Estado": "Buen estado", "Rent LP Num": 6.80, "Rent Largo Plazo": "6.80%", "Rent Est Num": 9.15, "Rent Estudiantes": "9.15%", "Fuente": "Pisos.com", "Enlace": "https://www.pisos.com/venta/pisos-gijon/", "lat": 43.5380, "lon": -5.6620},
    {"Titulo": "Apartamento a 2 min de la playa", "Barrio": "La Arena", "Precio": 135000, "Alquiler Num": 680, "Alquiler Mensual": "680 €", "Habs": 2, "m2": 65, "Estado": "Reformado", "Rent LP Num": 6.04, "Rent Largo Plazo": "6.04%", "Rent Est Num": 5.69, "Rent Estudiantes": "5.69%", "Fuente": "Idealista", "Enlace": "https://www.idealista.com/buscar/venta-viviendas/gijon/la-arena/", "lat": 43.5375, "lon": -5.6512},
    {"Titulo": "Piso próximo al Parque del Gas", "Barrio": "La Arena", "Precio": 158000, "Alquiler Num": 724, "Alquiler Mensual": "724 €", "Habs": 3, "m2": 85, "Estado": "Seminuevo", "Rent LP Num": 5.50, "Rent Largo Plazo": "5.50%", "Rent Est Num": 6.40, "Rent Estudiantes": "6.40%", "Fuente": "Fotocasa", "Enlace": "https://www.fotocasa.es/es/comprar/viviendas/gijon/la-arena/l", "lat": 43.5360, "lon": -5.6490},
    {"Titulo": "Piso exterior junto al parque", "Barrio": "Viesques", "Precio": 149000, "Alquiler Num": 734, "Alquiler Mensual": "734 €", "Habs": 3, "m2": 90, "Estado": "Seminuevo", "Rent LP Num": 5.91, "Rent Largo Plazo": "5.91%", "Rent Est Num": 7.73, "Rent Estudiantes": "7.73%", "Fuente": "Idealista", "Enlace": "https://www.idealista.com/buscar/venta-viviendas/gijon/viesques/", "lat": 43.5265, "lon": -5.6420},
    {"Titulo": "Piso con garaje en Av. del Llano", "Barrio": "El Llano", "Precio": 128000, "Alquiler Num": 843, "Alquiler Mensual": "843 €", "Habs": 2, "m2": 62, "Estado": "Buen estado", "Rent LP Num": 7.90, "Rent Largo Plazo": "7.90%", "Rent Est Num": 10.50, "Rent Estudiantes": "10.50%", "Fuente": "Idealista", "Enlace": "https://www.idealista.com/buscar/venta-viviendas/gijon/el-llano/", "lat": 43.5290, "lon": -5.6610},
    {"Titulo": "Piso ideal inversión La Calzada", "Barrio": "La Calzada", "Precio": 72000, "Alquiler Num": 630, "Alquiler Mensual": "630 €", "Habs": 3, "m2": 70, "Estado": "A reformar", "Rent LP Num": 10.50, "Rent Largo Plazo": "10.50%", "Rent Est Num": 13.80, "Rent Estudiantes": "13.80%", "Fuente": "Idealista", "Enlace": "https://www.idealista.com/buscar/venta-viviendas/gijon/la-calzada/", "lat": 43.5348, "lon": -5.6880},
    {"Titulo": "Oportunidad económica Pumarín", "Barrio": "Pumarín", "Precio": 79900, "Alquiler Num": 662, "Alquiler Mensual": "662 €", "Habs": 3, "m2": 72, "Estado": "Buen estado", "Rent LP Num": 9.95, "Rent Largo Plazo": "9.95%", "Rent Est Num": 13.10, "Rent Estudiantes": "13.10%", "Fuente": "Fotocasa", "Enlace": "https://www.fotocasa.es/es/comprar/viviendas/gijon/pumarin/l", "lat": 43.5270, "lon": -5.6710},
    {"Titulo": "Piso reformado cerca de Severo Ochoa", "Barrio": "Pumarín", "Precio": 95000, "Alquiler Num": 700, "Alquiler Mensual": "700 €", "Habs": 2, "m2": 65, "Estado": "Reformado", "Rent LP Num": 8.84, "Rent Largo Plazo": "8.84%", "Rent Est Num": 11.36, "Rent Estudiantes": "11.36%", "Fuente": "Pisos.com", "Enlace": "https://www.pisos.com/venta/pisos-gijon/", "lat": 43.5245, "lon": -5.6735},
    {"Titulo": "Piso junto a Av. Argentina", "Barrio": "La Calzada", "Precio": 84000, "Alquiler Num": 650, "Alquiler Mensual": "650 €", "Habs": 2, "m2": 68, "Estado": "Buen estado", "Rent LP Num": 9.28, "Rent Largo Plazo": "9.28%", "Rent Est Num": 11.78, "Rent Estudiantes": "11.78%", "Fuente": "Fotocasa", "Enlace": "https://www.fotocasa.es/es/comprar/viviendas/gijon/la-calzada/l", "lat": 43.5372, "lon": -5.6915},
    {"Titulo": "Piso vistas al puerto Natahoyu", "Barrio": "Natahoyu", "Precio": 105000, "Alquiler Num": 650, "Alquiler Mensual": "650 €", "Habs": 2, "m2": 64, "Estado": "Reformado", "Rent LP Num": 7.42, "Rent Largo Plazo": "7.42%", "Rent Est Num": 9.71, "Rent Estudiantes": "9.71%", "Fuente": "Idealista", "Enlace": "https://www.idealista.com/buscar/venta-viviendas/gijon/el-natahoyu/", "lat": 43.5410, "lon": -5.6780},
    {"Titulo": "Piso alto y soleado San José", "Barrio": "El Llano", "Precio": 99000, "Alquiler Num": 750, "Alquiler Mensual": "750 €", "Habs": 3, "m2": 78, "Estado": "Buen estado", "Rent LP Num": 9.09, "Rent Largo Plazo": "9.09%", "Rent Est Num": 12.12, "Rent Estudiantes": "12.12%", "Fuente": "Idealista", "Enlace": "https://www.idealista.com/buscar/venta-viviendas/gijon/el-llano/", "lat": 43.5302, "lon": -5.6655}
]

df = pd.DataFrame(pisos)

# ── BARRA LATERAL: FILTROS Y ORDENACIÓN ──
st.sidebar.header("Filtros de Inversión")

precio_max = st.sidebar.slider("Precio Compra Máx. (€)", 50000, 200000, 160000)
alquiler_min = st.sidebar.slider("Alquiler Mensual Mín. (€)", 500, 1000, 500)
min_rent_lp = st.sidebar.slider("Mín. Rentabilidad Largo Plazo (%)", 5.0, 12.0, 5.0, 0.1)
min_rent_est = st.sidebar.slider("Mín. Rentabilidad Estudiantes (%)", 5.0, 15.0, 5.0, 0.1)

fuente_filtro = st.sidebar.multiselect("Portal de Origen", df["Fuente"].unique(), default=df["Fuente"].unique())

st.sidebar.markdown("---")
st.sidebar.header("Ordenar por")
orden_seleccionado = st.sidebar.selectbox(
    "Criterio de ordenación",
    [
        "Mayor rentabilidad (Estudiantes)",
        "Mayor rentabilidad (Largo Plazo)",
        "Precio: más bajo primero",
        "Precio: más alto primero",
        "Mayor alquiler mensual"
    ]
)

# 1. Aplicar filtros
df_filtered = df[
    (df["Precio"] <= precio_max) & 
    (df["Alquiler Num"] >= alquiler_min) & 
    (df["Rent LP Num"] >= min_rent_lp) & 
    (df["Rent Est Num"] >= min_rent_est) & 
    (df["Fuente"].isin(fuente_filtro))
]

# 2. Aplicar ordenación estilo Idealista
if orden_seleccionado == "Mayor rentabilidad (Estudiantes)":
    df_filtered = df_filtered.sort_values(by="Rent Est Num", ascending=False)
elif orden_seleccionado == "Mayor rentabilidad (Largo Plazo)":
    df_filtered = df_filtered.sort_values(by="Rent LP Num", ascending=False)
elif orden_seleccionado == "Precio: más bajo primero":
    df_filtered = df_filtered.sort_values(by="Precio", ascending=True)
elif orden_seleccionado == "Precio: más alto primero":
    df_filtered = df_filtered.sort_values(by="Precio", ascending=False)
elif orden_seleccionado == "Mayor alquiler mensual":
    df_filtered = df_filtered.sort_values(by="Alquiler Num", ascending=False)

# Mapa interactivo Folium
st.subheader("Mapa Interactivo de Inmuebles en Gijón")
m = folium.Map(location=[43.533, -5.663], zoom_start=13)

for _, row in df_filtered.iterrows():
    popup_text = f"""
    <div style='font-family: sans-serif; width: 210px;'>
        <b>{row['Titulo']}</b><br>
        Precio: <b>{row['Precio']:,} €</b><br>
        Alquiler Esp.: <b>{row['Alquiler Mensual']}</b><br>
        Rent. Largo Plazo: <b>{row['Rent Largo Plazo']}</b><br>
        Rent. Estudiantes: <b>{row['Rent Estudiantes']}</b><br><br>
        <a href='{row['Enlace']}' target='_blank'>Ver en {row['Fuente']}</a>
    </div>
    """
    
    tooltip_text = f"{row['Titulo']} - {row['Precio']:,} € ({row['Rent Estudiantes']} est.)"

    folium.Marker(
        location=[row["lat"], row["lon"]],
        popup=folium.Popup(popup_text, max_width=250),
        tooltip=tooltip_text,
        icon=folium.Icon(color="red", icon="home", prefix="fa")
    ).add_to(m)

st_folium(m, width=1100, height=450)

# Lista detallada debajo (ordenada)
st.subheader(f"Lista de Inmuebles Filtrados ({len(df_filtered)} resultados)")
for _, row in df_filtered.iterrows():
    col1, col2, col3 = st.columns([3, 2, 1])
    with col1:
        st.markdown(f"### {row['Titulo']}")
        st.write(f"Barrio: **{row['Barrio']}** | **{row['m2']} m²** | **{row['Habs']} Habs** | {row['Estado']}")
        st.write(f"Origen: **{row['Fuente']}**")
    with col2:
        st.write(f"**Precio Inmueble:** {row['Precio']:,} €")
        st.write(f"**Alquiler Mensual Esperado:** {row['Alquiler Mensual']}")
        st.write(f"**Rent. Largo Plazo:** {row['Rent Largo Plazo']}")
        st.write(f"**Rent. Estudiantes:** {row['Rent Estudiantes']}")
    with col3:
        st.link_button(f"Ver en {row['Fuente']}", row['Enlace'])
    st.divider()