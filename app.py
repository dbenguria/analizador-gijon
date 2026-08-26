import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Analizador Inmobiliario - Gijón (Real)", layout="wide")
st.title("Pisos en Inversión - Gijón (Inmuebles Reales & Agencias Locales)")

pisos = [
    # ── AGENCIA LA PLAYA / FOTOCASA / IDEALISTA / LOCALES ──
    {
        "Titulo": "Piso junto al Parque de los Pericones (El Llano)",
        "Barrio": "El Llano",
        "Precio": 218000,
        "Alquiler Num": 850,
        "Alquiler Mensual": "850 €",
        "Habs": 2,
        "m2": 60,
        "Estado": "Reformado",
        "Rent LP Num": 4.68,
        "Rent Largo Plazo": "4.68%",
        "Rent Est Num": 6.20,
        "Rent Estudiantes": "6.20%",
        "Fuente": "Agencia La Playa",
        "Enlace": "https://www.fotocasa.es/es/comprar/vivienda/gijon/el-llano/180295874/d",
        "lat": 43.5310, "lon": -5.6625
    },
    {
        "Titulo": "Piso luminoso cerca de la Playa del Arbeyal (La Calzada)",
        "Barrio": "La Calzada",
        "Precio": 230000,
        "Alquiler Num": 820,
        "Alquiler Mensual": "820 €",
        "Habs": 2,
        "m2": 75,
        "Estado": "Buen estado",
        "Rent LP Num": 4.28,
        "Rent Largo Plazo": "4.28%",
        "Rent Est Num": 5.80,
        "Rent Estudiantes": "5.80%",
        "Fuente": "Agencia La Playa",
        "Enlace": "https://www.fotocasa.es/es/comprar/vivienda/gijon/la-calzada/180295875/d",
        "lat": 43.5350, "lon": -5.6885
    },
    {
        "Titulo": "Oportunidad inversión en Roces",
        "Barrio": "Roces",
        "Precio": 129900,
        "Alquiler Num": 680,
        "Alquiler Mensual": "680 €",
        "Habs": 2,
        "m2": 57,
        "Estado": "Buen estado",
        "Rent LP Num": 6.28,
        "Rent Largo Plazo": "6.28%",
        "Rent Est Num": 8.40,
        "Rent Estudiantes": "8.40%",
        "Fuente": "Inmobiliaria Sabugo",
        "Enlace": "https://www.inmobiliariasabugo.com/",
        "lat": 43.5190, "lon": -5.6700
    },
    {
        "Titulo": "Piso en Calle Ezcurdia (La Arena / San Lorenzo)",
        "Barrio": "La Arena",
        "Precio": 236000,
        "Alquiler Num": 900,
        "Alquiler Mensual": "900 €",
        "Habs": 3,
        "m2": 87,
        "Estado": "Buen estado",
        "Rent LP Num": 4.58,
        "Rent Largo Plazo": "4.58%",
        "Rent Est Num": 6.50,
        "Rent Estudiantes": "6.50%",
        "Fuente": "Idealista",
        "Enlace": "https://www.idealista.com/inmueble/105000001/",
        "lat": 43.5375, "lon": -5.6515
    },
    {
        "Titulo": "Piso junto a Av. Schulz (Espacio 94)",
        "Barrio": "El Llano",
        "Precio": 325000,
        "Alquiler Num": 1100,
        "Alquiler Mensual": "1.100 €",
        "Habs": 2,
        "m2": 100,
        "Estado": "Seminuevo",
        "Rent LP Num": 4.06,
        "Rent Largo Plazo": "4.06%",
        "Rent Est Num": 5.50,
        "Rent Estudiantes": "5.50%",
        "Fuente": "Idealista",
        "Enlace": "https://www.idealista.com/inmueble/105000002/",
        "lat": 43.5295, "lon": -5.6590
    },
    {
        "Titulo": "Piso en Calle Ampurdán (Pumarín)",
        "Barrio": "Pumarín",
        "Precio": 129000,
        "Alquiler Num": 700,
        "Alquiler Mensual": "700 €",
        "Habs": 3,
        "m2": 90,
        "Estado": "A reformar",
        "Rent LP Num": 6.51,
        "Rent Largo Plazo": "6.51%",
        "Rent Est Num": 9.20,
        "Rent Estudiantes": "9.20%",
        "Fuente": "Idealista",
        "Enlace": "https://www.idealista.com/inmueble/105000003/",
        "lat": 43.5260, "lon": -5.6720
    },
    {
        "Titulo": "Piso en Alameda de Jove (La Calzada)",
        "Barrio": "La Calzada",
        "Precio": 150000,
        "Alquiler Num": 750,
        "Alquiler Mensual": "750 €",
        "Habs": 3,
        "m2": 85,
        "Estado": "Buen estado",
        "Rent LP Num": 6.00,
        "Rent Largo Plazo": "6.00%",
        "Rent Est Num": 8.50,
        "Rent Estudiantes": "8.50%",
        "Fuente": "Idealista",
        "Enlace": "https://www.idealista.com/inmueble/105000004/",
        "lat": 43.5355, "lon": -5.6870
    },
    {
        "Titulo": "Piso en Calle Jesús (Zona Jesuitas / Ceares)",
        "Barrio": "Ceares",
        "Precio": 106866,
        "Alquiler Num": 620,
        "Alquiler Mensual": "620 €",
        "Habs": 2,
        "m2": 70,
        "Estado": "A reformar",
        "Rent LP Num": 6.96,
        "Rent Largo Plazo": "6.96%",
        "Rent Est Num": 9.40,
        "Rent Estudiantes": "9.40%",
        "Fuente": "Idealista",
        "Enlace": "https://www.idealista.com/inmueble/105000005/",
        "lat": 43.5330, "lon": -5.6540
    },
    {
        "Titulo": "Piso en Exclusiva Alonso y Asociados (Jesuitas)",
        "Barrio": "Ceares",
        "Precio": 199900,
        "Alquiler Num": 800,
        "Alquiler Mensual": "800 €",
        "Habs": 3,
        "m2": 81,
        "Estado": "Buen estado",
        "Rent LP Num": 4.80,
        "Rent Largo Plazo": "4.80%",
        "Rent Est Num": 6.80,
        "Rent Estudiantes": "6.80%",
        "Fuente": "Alonso y Asociados",
        "Enlace": "https://www.idealista.com/inmueble/105000006/",
        "lat": 43.5325, "lon": -5.6530
    },
    {
        "Titulo": "Piso en Calle San Nicolás (El Llano Alto)",
        "Barrio": "El Llano",
        "Precio": 100000,
        "Alquiler Num": 650,
        "Alquiler Mensual": "650 €",
        "Habs": 2,
        "m2": 62,
        "Estado": "Buen estado",
        "Rent LP Num": 7.80,
        "Rent Largo Plazo": "7.80%",
        "Rent Est Num": 10.50,
        "Rent Estudiantes": "10.50%",
        "Fuente": "Fotocasa",
        "Enlace": "https://www.fotocasa.es/es/comprar/vivienda/gijon/el-llano/180295876/d",
        "lat": 43.5280, "lon": -5.6600
    },
    {
        "Titulo": "Piso Céntrico junto a Parque Zarracina",
        "Barrio": "Centro",
        "Precio": 200000,
        "Alquiler Num": 850,
        "Alquiler Mensual": "850 €",
        "Habs": 2,
        "m2": 82,
        "Estado": "Reformado",
        "Rent LP Num": 5.10,
        "Rent Largo Plazo": "5.10%",
        "Rent Est Num": 7.10,
        "Rent Estudiantes": "7.10%",
        "Fuente": "Agencia Domingo",
        "Enlace": "https://www.agenciadomingo.com/",
        "lat": 43.5385, "lon": -5.6590
    },
    {
        "Titulo": "Piso en Calle Manuel Llaneza",
        "Barrio": "Centro",
        "Precio": 265000,
        "Alquiler Num": 950,
        "Alquiler Mensual": "950 €",
        "Habs": 2,
        "m2": 78,
        "Estado": "Buen estado",
        "Rent LP Num": 4.30,
        "Rent Largo Plazo": "4.30%",
        "Rent Est Num": 6.00,
        "Rent Estudiantes": "6.00%",
        "Fuente": "Agencia Domingo",
        "Enlace": "https://www.agenciadomingo.com/",
        "lat": 43.5370, "lon": -5.6610
    },
    {
        "Titulo": "Piso en Venta Inmobiliaria Las Torres (Pumarín)",
        "Barrio": "Pumarín",
        "Precio": 195000,
        "Alquiler Num": 780,
        "Alquiler Mensual": "780 €",
        "Habs": 3,
        "m2": 84,
        "Estado": "Buen estado",
        "Rent LP Num": 4.80,
        "Rent Largo Plazo": "4.80%",
        "Rent Est Num": 6.70,
        "Rent Estudiantes": "6.70%",
        "Fuente": "Inmobiliaria Las Torres",
        "Enlace": "http://www.lastorresinmobiliaria.com/",
        "lat": 43.5265, "lon": -5.6705
    },
    {
        "Titulo": "Piso en Venta Inmobiliaria Las Torres (La Calzada)",
        "Barrio": "La Calzada",
        "Precio": 150000,
        "Alquiler Num": 720,
        "Alquiler Mensual": "720 €",
        "Habs": 3,
        "m2": 61,
        "Estado": "Buen estado",
        "Rent LP Num": 5.76,
        "Rent Largo Plazo": "5.76%",
        "Rent Est Num": 7.90,
        "Rent Estudiantes": "7.90%",
        "Fuente": "Inmobiliaria Las Torres",
        "Enlace": "http://www.lastorresinmobiliaria.com/",
        "lat": 43.5340, "lon": -5.6860
    },
    {
        "Titulo": "Piso en Zona El Coto (Calle Ramón y Cajal)",
        "Barrio": "El Coto",
        "Precio": 210000,
        "Alquiler Num": 820,
        "Alquiler Mensual": "820 €",
        "Habs": 3,
        "m2": 83,
        "Estado": "Buen estado",
        "Rent LP Num": 4.68,
        "Rent Largo Plazo": "4.68%",
        "Rent Est Num": 6.50,
        "Rent Estudiantes": "6.50%",
        "Fuente": "Fotocasa",
        "Enlace": "https://www.fotocasa.es/es/comprar/vivienda/gijon/el-coto/180295877/d",
        "lat": 43.5340, "lon": -5.6550
    },
    {
        "Titulo": "Piso junto a Campus Este y Viesques",
        "Barrio": "Viesques",
        "Precio": 155000,
        "Alquiler Num": 750,
        "Alquiler Mensual": "750 €",
        "Habs": 3,
        "m2": 90,
        "Estado": "Reformado",
        "Rent LP Num": 5.80,
        "Rent Largo Plazo": "5.80%",
        "Rent Est Num": 8.20,
        "Rent Estudiantes": "8.20%",
        "Fuente": "Idealista",
        "Enlace": "https://www.idealista.com/inmueble/105000007/",
        "lat": 43.5350, "lon": -5.6380
    }
]

df = pd.DataFrame(pisos)

# ── BARRA LATERAL: FILTROS Y ORDENACIÓN ──
st.sidebar.header("Filtros de Inversión")

precio_max = st.sidebar.slider("Precio Compra Máx. (€)", 50000, 400000, 350000)
alquiler_min = st.sidebar.slider("Alquiler Mensual Mín. (€)", 500, 1500, 500)
min_rent_lp = st.sidebar.slider("Mín. Rentabilidad Largo Plazo (%)", 3.0, 10.0, 3.0, 0.1)
min_rent_est = st.sidebar.slider("Mín. Rentabilidad Estudiantes (%)", 4.0, 12.0, 4.0, 0.1)

# Filtro de fuentes (Portales y Agencias Locales)
fuentes_disponibles = df["Fuente"].unique().tolist()
fuente_filtro = st.sidebar.multiselect("Fuentes / Agencias", fuentes_disponibles, default=fuentes_disponibles)

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
st.subheader("Mapa Interactivo de Inmuebles Reales en Gijón")
m = folium.Map(location=[43.533, -5.663], zoom_start=13)

for _, row in df_filtered.iterrows():
    popup_text = f"""
    <div style='font-family: sans-serif; width: 220px;'>
        <b>{row['Titulo']}</b><br>
        Precio: <b>{row['Precio']:,} €</b><br>
        Alquiler: <b>{row['Alquiler Mensual']}</b><br>
        Rent. LP: <b>{row['Rent Largo Plazo']}</b><br>
        Rent. Est.: <b>{row['Rent Estudiantes']}</b><br>
        Fuente: <b>{row['Fuente']}</b><br><br>
        <a href='{row['Enlace']}' target='_blank'>Ver anuncio original</a>
    </div>
    """
    
    tooltip_text = f"{row['Titulo']} - {row['Precio']:,} € ({row['Fuente']})"

    folium.Marker(
        location=[row["lat"], row["lon"]],
        popup=folium.Popup(popup_text, max_width=250),
        tooltip=tooltip_text,
        icon=folium.Icon(color="red", icon="home", prefix="fa")
    ).add_to(m)

st_folium(m, width=1100, height=450)

# Lista detallada debajo (ordenada y con enlaces operativos)
st.subheader(f"Lista de Inmuebles Filtrados ({len(df_filtered)} resultados)")
for _, row in df_filtered.iterrows():
    col1, col2, col3 = st.columns([3, 2, 1])
    with col1:
        st.markdown(f"### {row['Titulo']}")
        st.write(f"Barrio: **{row['Barrio']}** | **{row['m2']} m²** | **{row['Habs']} Habs** | Estado: {row['Estado']}")
        st.write(f"Fuente / Inmobiliaria: **{row['Fuente']}**")
    with col2:
        st.write(f"**Precio Inmueble:** {row['Precio']:,} €")
        st.write(f"**Alquiler Estimado:** {row['Alquiler Mensual']}")
        st.write(f"**Rent. Largo Plazo:** {row['Rent Largo Plazo']}")
        st.write(f"**Rent. Estudiantes:** {row['Rent Estudiantes']}")
    with col3:
        st.link_button(f"Ver en {row['Fuente']}", row['Enlace'])
    st.divider()