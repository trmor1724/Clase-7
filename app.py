import streamlit as st
import os
import pandas as pd
import re
from PIL import Image
from textblob import TextBlob
from googletrans import Translator

# ✅ `st.set_page_config()` debe ser el primer comando de Streamlit
st.set_page_config(
    page_title="Analizador de Sentimiento",
    page_icon="📊",
    layout="wide"
)

# Título principal
st.title("🔍 Análisis de Sentimiento con TextBlob")

# Sidebar con explicación
with st.sidebar:
    st.subheader("📌 ¿Qué significa el análisis de sentimiento?")
    st.markdown("""
    - **Polaridad**: Rango de -1 (muy negativo) a 1 (muy positivo).
    - **Subjetividad**: Rango de 0 (objetivo) a 1 (subjetivo).
    """)

# Cargar imagen de portada
try:
    image = Image.open("cliente.jpg")
    st.image(image, caption="Cliente")
except:
    st.warning("⚠️ No se encontró la imagen 'cliente.jpg'.")

# Inicializar traductor
translator = Translator()

# Sección de análisis de sentimiento
with st.expander('💬 Analizar Sentimiento de un Texto'):
    text1 = st.text_area('✍️ Escribe una frase:', placeholder="Ejemplo: Me encanta este producto")
    
    if text1:
        try:
            # Traducir al inglés para mejorar análisis
            translation = translator.translate(text1, src="es", dest="en")
            trans_text = translation.text

            # Analizar con TextBlob
            blob = TextBlob(trans_text)
            polarity = round(blob.sentiment.polarity, 2)
            subjectivity = round(blob.sentiment.subjectivity, 2)

            # Mostrar resultados
            st.write('📊 **Polaridad:**', polarity)
            st.write('🧐 **Subjetividad:**', subjectivity)

            # Interacción basada en el sentimiento
            if polarity >= 0.5:
                st.success('😊 ¡El sentimiento es positivo! ¡Sigue disfrutando!')
            elif polarity <= -0.5:
                st.error('😔 El sentimiento es negativo. ¿Podemos mejorar algo?')
            else:
                st.warning('😐 Es un sentimiento neutral. ¿Algo más que quieras compartir?')
        except Exception as e:
            st.error(f"❌ Error al traducir o analizar el texto: {e}")

# Sección de corrección de texto en inglés
with st.expander('📝 Corrección de Texto en Inglés'):
    text2 = st.text_area('✍️ Escribe un texto para corregir:', key='correction')
    if text2:
        blob2 = TextBlob(text2)
        corrected_text = blob2.correct()
        st.write('✅ **Texto corregido:**', corrected_text)

# Pie de página
st.markdown("---")
st.markdown("Desarrollado con ❤️ usando Streamlit y TextBlob")

    """)

# Pie de página
st.markdown("---")
st.markdown("Desarrollado con ❤️ usando Streamlit y TextBlob")

