import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv("data/ventas.csv", parse_dates=["fecha"])
df["total"] = df["precio"] * df["cantidad"]
df["mes"] = df["fecha"].dt.to_period("M").astype(str)

st.title("📊 Dashboard de Ventas - Supermercado")

# Filtro por producto
producto = st.selectbox("Selecciona un producto:", df["producto"].unique())
df_producto = df[df["producto"] == producto]

# Gráfico ventas por mes
st.subheader(f"Ventas mensuales de {producto}")
ventas_mes = df_producto.groupby("mes")["total"].sum().reset_index()

fig, ax = plt.subplots(figsize=(6,4))
sns.barplot(data=ventas_mes, x="mes", y="total", ax=ax, palette="Blues")
plt.ylabel("Ventas ($)")
st.pyplot(fig)

# Gráfico participación por categoría
st.subheader("Participación por categoría")
ventas_categoria = df.groupby("categoria")["total"].sum().reset_index()

fig2, ax2 = plt.subplots(figsize=(5,5))
ax2.pie(ventas_categoria["total"], labels=ventas_categoria["categoria"], autopct="%1.1f%%", startangle=90)
ax2.axis("equal")
st.pyplot(fig2)

st.success("Dashboard generado con datos ficticios para práctica.")
