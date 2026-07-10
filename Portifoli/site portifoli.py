import streamlit as st
import pandas as pd
import base64
import os

# Configurações de Layout da Página
st.set_page_config(
    page_title="M. Aleixo TI",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estado de sessão (login/logoff)
if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

# Credenciais administrativas
USUARIO_ADMIN = "matheus"
SENHA_ADMIN = "@Kayle2023"

# Arquivos locais
ARQUIVO_DADOS = "dados_portfolio.csv"
ARQUIVO_VAGAS = "dados_vagas.csv"
ARQUIVO_SKILLS = "dados_skills.csv"
NOME_ESTÁTICO_FOTO = "Foto_Perfil_Matheus_Upload.jpg"

# Inicialização de bases CSV
if not os.path.exists(ARQUIVO_DADOS):
    pd.DataFrame(columns=["Categoria", "Título", "Descrição", "Link do Processo", "Link do Vídeo"]).to_csv(ARQUIVO_DADOS, index=False)

if not os.path.exists(ARQUIVO_VAGAS):
    df_vagas_init = pd.DataFrame([
        {"Título": "📊 Power BI & Data Analytics", "Descrição": "Foco no desenvolvimento de soluções de inteligência de negócios."},
        {"Título": "⚙️ Automação (RPA) & Scraping", "Descrição": "Arquitetura de robôs estáveis utilizando Python e UiPath."},
        {"Título": "🏢 ERP & Soluções SAP", "Descrição": "Suporte técnico e funcional aos ambientes SAP ECC e S/4HANA."}
    ])
    df_vagas_init.to_csv(ARQUIVO_VAGAS, index=False)

if not os.path.exists(ARQUIVO_SKILLS):
    df_skills_init = pd.DataFrame([
        {"Categoria": "Dados", "Nome": "Power BI (Dashboards & DAX)", "Porcentagem": 90},
        {"Categoria": "RPA", "Nome": "Python Avançado (Scrapy, Playwright)", "Porcentagem": 95},
        {"Categoria": "SAP", "Nome": "Suporte Funcional SAP (ECC e S/4HANA)", "Porcentagem": 90}
    ])
    df_skills_init.to_csv(ARQUIVO_SKILLS, index=False)

# Função auxiliar para imagem
def obter_imagem_base64_flexivel():
    if os.path.exists(NOME_ESTÁTICO_FOTO):
        try:
            with open(NOME_ESTÁTICO_FOTO, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode()
        except:
            return None
    return None

foto_base64 = obter_imagem_base64_flexivel()

# Texto do currículo
TEXTO_CURRICULO = """MATHEUS ALEIXO
Várzea Paulista/SP | matheus.aleixo2020@gmail.com | (11) 97478-0590
LinkedIn: www.linkedin.com/in/matheus-aleixo-299a05247

OBJETIVO:
Atuar de forma analítica e consultiva na área de TI como Analista de Sistemas, Desenvolvedor ou Analista de Dados / Power BI.

FORMAÇÃO:
- Bacharelado em Tecnologia da Informação - UNIVESP

EXPERIÊNCIA:
1. Professor de Tecnologia e Matemática - Secretaria da Educação | Campo Limpo Paulista - SP (Outubro 2025 – Fevereiro 2026)
2. Consultor SAP Jr - Stefanini | Atuação Remota
3. Estagiário de TI - Continental Automotive | Várzea Paulista - SP (Junho 2023 – Fevereiro 2025)
"""

# CSS Premium
st.markdown("""
<style>
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background-color: #0F172A;
        color: #E2E8F0;
    }
    .avatar-img { width: 155px; height: 155px; border-radius: 50%; border: 3px solid #38BDF8; }
    h1 { color: #F8FAFC !important; font-weight: 700 !important; }
    h2, h3 { color: #38BDF8 !important; font-weight: 600 !important; }
</style>
""", unsafe_allow_html=True)

# Carregamento das bases
df_dados = pd.read_csv(ARQUIVO_DADOS)
df_vagas = pd.read_csv(ARQUIVO_VAGAS)
df_skills = pd.read_csv(ARQUIVO_SKILLS)

# Sidebar
with st.sidebar:
    if foto_base64:
        st.markdown(f'<img class="avatar-img" src="data:image/jpeg;base64,{foto_base64}" alt="Matheus Aleixo">', unsafe_allow_html=True)
    else:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=130)
        st.caption("⚠️ Nenhuma foto carregada.")

    st.markdown("### 📋 Informações Pessoais")
    st.markdown("**📍 Localização:** Várzea Paulista - SP")
    st.markdown("**✉️ E-mail:** [matheus.aleixo2020@gmail.com](mailto:matheus.aleixo2020@gmail.com)")
    st.markdown("**🔗 LinkedIn:** [Perfil](https://www.linkedin.com/in/matheus-aleixo-299a05247/)")

    with st.expander("🛠️ Configurações de Sistema", expanded=False):
        if not st.session_state["autenticado"]:
            input_user = st.text_input("User ID", key="adm_user")
            input_pass = st.text_input("Senha", type="password", key="adm_pass")
            if st.button("🔑 Autenticar"):
                if input_user == USUARIO_ADMIN and input_pass == SENHA_ADMIN:
                    st.session_state["autenticado"] = True
                    st.rerun()
                else:
                    st.error("Acesso negado.")
        else:
            st.write("🟢 Modo Editor Ativo")
            if st.button("🔒 Logoff", type="primary"):
                st.session_state["autenticado"] = False
                st.rerun()

# Cabeçalho
st.title("💻 M. Aleixo TI")
st.markdown("Especialista em RPA, ETL, Power BI e suporte SAP.")

# Tabs
aba_sobre, aba_experiencias, aba_conhecimentos, aba_projetos, aba_formacao = st.tabs([
    "👤 Objetivo & Foco", "💼 Experiências", "🧠 Conhecimentos", "🚀 Projetos", "📚 Formação"
])

with aba_sobre:
    st.markdown("## Objetivo Estratégico")
    st.text(TEXTO_CURRICULO)

with aba_experiencias:
    st.markdown("## Histórico Profissional")
    st.markdown("- Professor de Tecnologia e Matemática (2025–2026)")
    st.markdown("- Consultor SAP Jr (Stefanini)")
    st.markdown("- Estagiário de TI (Continental Automotive)")

with aba_conhecimentos:
    st.markdown("## Hard Skills")
    st.dataframe(df_skills)

with aba_projetos:
    st.markdown("## Projetos")
    if not df_dados.empty:
        st.dataframe(df_dados)
    else:
        st.info("Nenhum projeto publicado.")

with aba_formacao:
    st.markdown("## Formação Acadêmica")
    st.markdown("Bacharelado em Tecnologia da Informação — UNIVESP")

# Painel Administrativo
if st.session_state["autenticado"]:
    st.markdown("---")
    st.markdown("## 🔒 Terminal do Administrador")
    menu_adm = st.selectbox("Escolha a Base", ["Projetos", "Vagas", "Skills", "🖼️ Foto de Perfil"])

    if menu_adm == "🖼️ Foto de Perfil":
        foto_carregada = st.file_uploader("Escolha uma imagem", type=["jpg", "jpeg", "png"])
        if foto_carregada is not None:
            st.image(foto_carregada, width=200)
            if st.button("💾 Aplicar Nova Imagem", type="primary"):
                try:
                    if os.path.exists(NOME_ESTÁTICO_FOTO):
                        os.remove(NOME_ESTÁTICO_FOTO)
                    with open(NOME_ESTÁTICO_FOTO, "wb") as f:
                        f.write(foto_carregada.getbuffer())
                    st.success("Imagem atualizada com sucesso!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao salvar: {e}")

