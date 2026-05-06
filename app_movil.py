import streamlit as st
import time

# Configuración de página
st.set_page_config(page_title="Simulador de Reloj - VIZCARRA", layout="centered")

# Estilos de alto contraste (Azul Petróleo y Amarillo)
st.markdown("""
    <style>
    .main { background-color: #1B2631; color: white; }
    .stNumberInput label { color: #F1C40F !important; }
    .time-display { 
        font-size: 85px !important; 
        font-weight: bold; 
        color: #F1C40F; 
        text-align: center; 
        padding: 20px;
        border: 2px solid #273746;
        border-radius: 15px;
        margin: 10px 0;
    }
    h1, h3 { text-align: center; margin-bottom: 0px; }
    .footer-text { color: #85929E; text-align: center; font-style: italic; margin-top: 50px; }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE ESTADO ---
if 'tiempo_actual' not in st.session_state:
    st.session_state.tiempo_actual = 0
if 'corriendo' not in st.session_state:
    st.session_state.corriendo = False

# TÍTULOS
st.title("⏱️ SIMULADOR DE RELOJ")
st.markdown("<h3 style='color: white;'>EJERCICIO 12</h3>", unsafe_allow_html=True)
st.write("")

# 1. ÁREA DE INPUT
col1, col2, col3 = st.columns(3)
with col1: h_in = st.number_input("H", 0, 23, 23)
with col2: m_in = st.number_input("M", 0, 59, 59)
with col3: s_in = st.number_input("S", 0, 59, 45)

if st.button("Cargar Tiempo", use_container_width=True):
    st.session_state.tiempo_actual = (h_in * 3600 + m_in * 60 + s_in) % 86400
    st.session_state.corriendo = False

# 2. DISPLAY (Visualización con lógica de 24h)
def formatear_tiempo(segundos):
    # El operador % 86400 asegura que después de 23:59:59 vuelva a 00:00:00
    segundos_normalizados = segundos % 86400
    m, s = divmod(segundos_normalizados, 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"

display_placeholder = st.empty()
display_placeholder.markdown(f"<p class='time-display'>{formatear_tiempo(st.session_state.tiempo_actual)}</p>", unsafe_allow_html=True)

# 3. PANEL DE CONTROL
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("Inicio", type="primary", use_container_width=True): 
        st.session_state.corriendo = True
with c2:
    if st.button("Pausa", use_container_width=True): 
        st.session_state.corriendo = False
with c3:
    if st.button("Resetear", use_container_width=True): 
        st.session_state.tiempo_actual = 0
        st.session_state.corriendo = False
        st.rerun()

# --- BUCLE DE FUNCIONAMIENTO ---
if st.session_state.corriendo:
    while st.session_state.corriendo:
        time.sleep(1)
        # Incrementamos y aplicamos el módulo de un día completo (86400 segundos)
        st.session_state.tiempo_actual = (st.session_state.tiempo_actual + 1) % 86400
        display_placeholder.markdown(f"<p class='time-display'>{formatear_tiempo(st.session_state.tiempo_actual)}</p>", unsafe_allow_html=True)

st.markdown("<p class='footer-text'>Estudiante: Derian Vizcarra</p>", unsafe_allow_html=True)