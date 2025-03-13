import streamlit as st
import os
from streamlit_lottie import json
from PIL import Image
from textblob import TextBlob
from googletrans import Translator

translator = Translator()
st.title('Analisis de satifaccion')
image = Image.open("cliente.jpg")
st.image(image, caption="cliente")

st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")
with st.sidebar:
               st.subheader("Polaridad y Subjetividad")
               ("""
                Polaridad: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
                Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.
                
               Subjetividad: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
               (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.

                 """
               ) 


with st.expander('Analizar Polaridad y Subjetividad en un texto'):
    text1 = st.text_area('Escribe por favor: ')
    if text1:

        #translation = translator.translate(text1, src="es", dest="en")
        #trans_text = translation.text
        #blob = TextBlob(trans_text)
        blob = TextBlob(text1)
       
        
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
        x=round(blob.sentiment.polarity,2)
        if x >= 0.5:
            st.write( 'Es un sentimiento Positivo 😊')
        elif x <= -0.5:
            st.write( 'Es un sentimiento Negativo 😔')
        else:
            st.write( 'Es un sentimiento Neutral 😐')

with st.expander('Corrección en inglés'):
       text2 = st.text_area('Escribe por favor: ',key='4')
       if text2:
          blob2=TextBlob(text2)
          st.write((blob2.correct()))  


# Inicializar traductor
translator = Translator()

# Título de la app
st.title('🔍 Análisis de Sentimiento')

# Cargar imagen
image = Image.open("cliente.jpg")
st.image(image, caption="Cliente")

# Sidebar con explicación
with st.sidebar:
    st.subheader("📌 ¿Qué significa el análisis de sentimiento?")
    st.markdown(
        """
        - **Polaridad**: Rango de -1 (muy negativo) a 1 (muy positivo).
        - **Subjetividad**: Rango de 0 (objetivo) a 1 (subjetivo).
        """
    )

# Sección de análisis de sentimiento
with st.expander('💬 Analizar Sentimiento de un Texto'):
    text1 = st.text_area('✍️ Escribe una frase:', placeholder="Ejemplo: Me encanta este producto")
    if text1:
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

# Sección de corrección de texto en inglés
with st.expander('📝 Corrección de Texto en Inglés'):
    text2 = st.text_area('✍️ Escribe un texto para corregir:', key='correction')
    if text2:
        blob2 = TextBlob(text2)
        corrected_text = blob2.correct()
        st.write('✅ **Texto corregido:**', corrected_text)


with open("Animation.json", "r") as f:
    animacion = json.load(f)

st_lottie(animacion, height=300, key="lottie_animacion")
