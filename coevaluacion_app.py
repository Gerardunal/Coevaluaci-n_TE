import streamlit as st
import pandas as pd
import numpy as np

# Descripción de los niveles
levels_description = {
    1: "Muy deficiente: No cumplió con el criterio o mostró actitudes negativas.",
    2: "Insuficiente: Participación o desempeño mínimo; muy por debajo del grupo.",
    3: "Aceptable: Cumplió con lo mínimo esperado, pero con limitaciones evidentes.",
    4: "Bueno: Participación activa y constructiva, con pequeños aspectos por mejorar.",
    5: "Excelente: Participación destacada, colaborativa y comprometida en todo momento."
}

# Retroalimentación y sugerencia por rango
feedback_matrix = [
    (1.0, 1.9, "Participación muy limitada o negativa.", "Debes involucrarte más y respetar las decisiones grupales."),
    (2.0, 2.9, "Participación limitada y poco colaborativa.", "Intenta apoyar más a tus compañeros y comunicarte mejor."),
    (3.0, 3.9, "Participación aceptable, pero con debilidades.", "Mejora tu organización y disposición para colaborar."),
    (4.0, 4.4, "Participación buena, aunque hay pequeños aspectos por pulir.", "Refuerza tu liderazgo o apoyo constante al grupo."),
    (4.5, 5.0, "Participación destacada y muy valorada por el grupo.", "Sigue así y ayuda a mantener la motivación grupal.")
]

# Criterios de coevaluación
criteria = [
    "C1. ¿Participó activamente en la realización del trabajo de grupo?",
    "C2. ¿Interactuó con todos los miembros del grupo?",
    "C3. ¿Trabajó por igual, colaborando con unos y recibiendo apoyo de otros?",
    "C4. ¿Tuvo algo que ver con los logros alcanzados?",
    "C5. ¿Trató de dividir al grupo con discrepancias o malos entendidos?",
    "C6. ¿Aportó con materiales de apoyo para mejorar el trabajo de grupo?",
    "C7. ¿Comprende todo lo avanzado con este trabajo?"
]

st.title("Formulario de Coevaluación de Trabajo en Equipo")

with st.form("coevaluation_form"):
    st.write("Seleccione una calificación de 1 a 5 para cada criterio")
    ratings = []
    for crit in criteria:
        val = st.slider(crit, 1, 5, 3, format="%d")
        st.caption(f"{levels_description[val]}")
        ratings.append(val)

    submit = st.form_submit_button("Enviar Evaluación")

if submit:
    df = pd.DataFrame({"Criterio": criteria, "Calificación": ratings})
    df["Retroalimentación"] = ""
    df["Sugerencia"] = ""

    for i, row in df.iterrows():
        for rng in feedback_matrix:
            if rng[0] <= row["Calificación"] <= rng[1]:
                df.at[i, "Retroalimentación"] = rng[2]
                df.at[i, "Sugerencia"] = rng[3]
                break

    promedio = np.mean(ratings)
    st.subheader("Resumen de Evaluación")
    st.write(df)
    st.success(f"Nota Final por Coevaluación: {promedio:.2f}")

    # Mostrar observaciones generales
    st.subheader("Observaciones Generales")
    for i, row in df.iterrows():
        st.markdown(f"**{row['Criterio']}**\n- Retroalimentación: {row['Retroalimentación']}\n- Sugerencia: {row['Sugerencia']}")
