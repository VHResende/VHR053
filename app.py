import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Definindo os resultados das métricas
metrics = {
    "Métrica": ["Acurácia", "KS", "Gini"],
    "Base de Validação": [0.9133, 0.3798, 0.5071],
    "Base Out-of-Time": [0.9130, 0.3866, 0.5119]
}

# Criando um DataFrame para exibir as métricas
df_metrics = pd.DataFrame(metrics)

# Configurando a página do Streamlit
st.set_page_config(page_title="Avaliação do Modelo", layout="wide")

# Título da aplicação
st.title("📊 Avaliação do Modelo de Regressão Logística")
st.markdown("Este dashboard apresenta as métricas de avaliação do modelo, incluindo Acurácia, KS e Gini, para as bases de validação e out-of-time.")

# Exibindo a tabela de métricas
st.subheader("Tabela de Métricas")
st.dataframe(df_metrics, use_container_width=True)

# Gráfico de Acurácia, KS e Gini
st.subheader("Gráficos Comparativos das Métricas")

# Função para criar gráficos de barras comparativos
def create_comparison_chart(metric_name, validation_values, oot_values, title, y_title):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=metric_name,
        y=validation_values,
        name="Base de Validação",
        marker_color='blue'
    ))
    fig.add_trace(go.Bar(
        x=metric_name,
        y=oot_values,
        name="Base Out-of-Time",
        marker_color='orange'
    ))
    fig.update_layout(
        title=title,
        xaxis_title="Métrica",
        yaxis_title=y_title,
        barmode="group",
        template="plotly_white",
        legend=dict(title="Bases")
    )
    return fig

# Criando gráficos para cada métrica
st.plotly_chart(create_comparison_chart(
    df_metrics["Métrica"], 
    df_metrics["Base de Validação"], 
    df_metrics["Base Out-of-Time"], 
    "Comparação de Acurácia", 
    "Acurácia"
), use_container_width=True)

st.plotly_chart(create_comparison_chart(
    df_metrics["Métrica"], 
    df_metrics["Base de Validação"], 
    df_metrics["Base Out-of-Time"], 
    "Comparação de KS", 
    "KS"
), use_container_width=True)

st.plotly_chart(create_comparison_chart(
    df_metrics["Métrica"], 
    df_metrics["Base de Validação"], 
    df_metrics["Base Out-of-Time"], 
    "Comparação de Gini", 
    "Gini"
), use_container_width=True)

# Conclusão
st.markdown("""
### Conclusão
- Os gráficos e a tabela acima permitem comparar as métricas de desempenho do modelo nas bases de validação e out-of-time. Isso auxilia na avaliação da robustez e estabilidade do modelo.
- O modelo parece ser bem calibrado, com boa performance nas duas bases (treinamento/validação e out-of-time). Ele tem um bom poder discriminante (com KS e Gini em torno de 0.4-0.5) e está performando consistentemente em diferentes subconjuntos dos dados. Os resultados são muito sólidos.
- Com as variáveis selecionadas podemos calcular, com mais previsibilidade, os riscos de inadimplência.
- Com isso, podemos sugerir outras abordagens e possibilidades para diminuir o risco de inandimplência e trazer mais clientes com maior poder de crédito.
""")

# by Victor Resende
st.markdown("---")
st.write("by 📊 **Victor Resende**")