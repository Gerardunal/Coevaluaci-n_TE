
import streamlit as st

st.title("Sistema de Coevaluación de Trabajo en Equipo")
st.write("Seleccione el nivel de desempeño (1 a 5) para cada criterio:")

criterios = {
    "C1. ¿Participó activamente en la realización del trabajo de grupo?": [
        "No participó.",
        "Participación muy limitada.",
        "Participó de manera intermitente.",
        "Participó consistentemente.",
        "Participación activa y propositiva en todo momento."
    ],
    "C2. ¿Interactuó con todos los miembros del grupo?": [
        "No interactuó.",
        "Solo con algunos miembros.",
        "Interactuó parcialmente.",
        "Buena interacción general.",
        "Excelente interacción con todo el grupo."
    ],
    "C3. ¿Trabajó por igual, colaborando con unos y recibiendo apoyo de otros?": [
        "No colaboró.",
        "Colaboración muy escasa.",
        "Colaboración limitada.",
        "Buena colaboración.",
        "Alta colaboración recíproca."
    ],
    "C4. ¿Tuvo algo que ver con los logros alcanzados?": [
        "No contribuyó.",
        "Poca contribución.",
        "Contribución parcial.",
        "Buena contribución.",
        "Contribución clave para el logro grupal."
    ],
    "C5. ¿Trató de dividir al grupo con discrepancias o malos entendidos?": [
        "Sí, constantemente.",
        "Ocasionalmente.",
        "Pocas veces.",
        "Casi nunca.",
        "Nunca, mantuvo unidad del grupo."
    ],
    "C6. ¿Aportó con materiales de apoyo para mejorar el trabajo de grupo?": [
        "No aportó nada.",
        "Aportó materiales irrelevantes.",
        "Aportó lo mínimo.",
        "Aportó materiales útiles.",
        "Aportó insumos de gran valor."
    ],
    "C7. ¿Comprende todo lo avanzado con este trabajo?": [
        "No comprende el trabajo.",
        "Comprende muy poco.",
        "Comprensión parcial.",
        "Buena comprensión.",
        "Comprensión total y clara del proceso."
    ]
}

niveles = [1, 2, 3, 4, 5]
resultados = {}
total = 0

for criterio, descriptores in criterios.items():
    nivel = st.radio(criterio, niveles, key=criterio)
    retro = f"**Retroalimentación**: {descriptores[nivel-1]}"
    sugerencia = {
        1: "Mejorar compromiso y disposición.",
        2: "Incrementar la participación activa.",
        3: "Buscar mayor consistencia y colaboración.",
        4: "Mantener y fortalecer tu rol.",
        5: "Continúa siendo un referente positivo para el equipo."
    }[nivel]
    st.markdown(retro)
    st.markdown(f"**Sugerencia**: {sugerencia}")
    st.markdown("---")
    resultados[criterio] = nivel
    total += nivel

st.subheader("Resumen")
promedio = round(total / len(criterios), 2)
st.write(f"**Nota final obtenida en coevaluación:** {promedio}/5")
