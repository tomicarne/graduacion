import streamlit as st
import joblib
import numpy as np

# Cargar el modelo entrenado
modelo = joblib.load("primermillon.joblib")

# Título
st.title("Predictor de Éxito Académico")

# Autor
st.markdown("**Autor:** Tomas Vasquez")

# Imagen
st.image(
    "https://buscacarrera.com.co/public/content/articulos/la-clave-del-exito-academico-como-crear-un-plan-de-estudio-efectivo.jpg",
    caption="La clave del éxito académico"
)

# Introducción
st.write("""
Bienvenido a la aplicación **Predictor de Éxito Académico**.  
Aquí podrás ingresar tus calificaciones y conocer si, según nuestro modelo, 
tienes altas probabilidades de graduarte con éxito en la universidad.

**Instrucciones:**
1. Ajusta los valores de **Nota IA** y **GPA** con los deslizadores.
2. Presiona el botón de predicción.
3. Observa el resultado con su mensaje correspondiente.
""")

# Entradas con slider
nota_ia = st.slider("Nota IA", 0.0, 1.0, 0.5, step=0.1)
gpa = st.slider("GPA", 0.0, 1.0, 0.5, step=0.1)

# Botón de predicción
if st.button("Predecir"):
    # Preparar los datos
    entrada = np.array([[nota_ia, gpa]])
    prediccion = modelo.predict(entrada)[0]

    # Mostrar resultado
    if prediccion == 0:
        st.markdown(
            "<h3 style='color:red;'>❌ No se graduará</h3>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<h3 style='color:green;'>🎓 Felicitaciones, te vas a graduar con honores</h3>",
            unsafe_allow_html=True
        )

# Pie de página
st.markdown("---")
st.markdown("Unab © 2025")
