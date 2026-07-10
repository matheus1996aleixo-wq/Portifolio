import streamlit as st
import pandas as pd
import base64
import os

# Configuração da página
st.set_page_config(
    page_title="M. Aleixo TI",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estado de sessão
if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

# Credenciais
USUARIO_ADMIN = "matheus"
SENHA_ADMIN = "@Kayle2023"

# Arquivos locais
ARQUIVO_DADOS = "dados_portfolio.csv"
ARQUIVO_VAGAS = "dados_vagas.csv"
ARQUIVO_SKILLS = "dados_skills.csv"
NOME_FOTO = "Foto_Perfil_Matheus.jpg"

# Inicialização de bases
for arquivo, cols in [
    (ARQUIVO_DADOS, ["Categoria", "Título", "Descrição", "Link do Processo", "Link do Vídeo"]),
    (ARQUIVO_VAGAS, ["Título", "Descrição"]),
    (ARQUIVO_SKILLS, ["Categoria", "Nome", "Porcentagem"])
]:
    if not os.path.exists(arquivo):
        pd.DataFrame(columns=cols).to_csv(arquivo, index=False)

# Função imagem
def obter_imagem_base64():
    if os.path.exists(NOME_FOTO):
        try:
            with open(NOME_FOTO, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode()
        except:
            return None
    return None

foto_base64 = obter_imagem_base64()

# CSS Premium
st.markdown("""
<style>
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background-color: #0F172A;
        color: #E2E8F0;
    }
    .avatar-img {
        width: 160px; height: 160px;
        border-radius: 50%;
        border: 4px solid #38BDF8;
        box-shadow: 0 4px 20px rgba(56,189,248,0.4);
        margin-bottom: 15px;
    }
    .info-card {
        background: #1E293B;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 12px;
        margin-bottom: 10px;
    }
    h1 { color: #F8FAFC !important; font-weight: 700; text-align: center; }
    h2, h3 { color: #38BDF8 !important; font-weight: 600; }
    .section-card {
        background: #1E293B;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    if foto_base64:
        st.markdown(f'<img class="avatar-img" src="data:image/jpeg;base64,{foto_base64}" alt="Matheus Aleixo">', unsafe_allow_html=True)
    else:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=130)
        st.caption("⚠️ Nenhuma foto carregada.")

    st.markdown("### 📋 Informações Pessoais")
    st.markdown('<div class="info-card">👤 <b>Nome:</b> Matheus Aleixo</div>', unsafe_allow_html=True)
    st.markdown('<div class="info-card">📅 <b>Nascimento:</b> 20/02/1996</div>', unsafe_allow_html=True)
    st.markdown('<div class="info-card">📍 <b>Localização:</b> Várzea Paulista - SP</div>', unsafe_allow_html=True)
    st.markdown('<div class="info-card">✉️ <b>E-mail:</b> <a href="mailto:matheus.aleixo2020@gmail.com">matheus.aleixo2020@gmail.com</a></div>', unsafe_allow_html=True)
    st.markdown('<div class="info-card">🔗 <b>LinkedIn:</b> <a href="https://www.linkedin.com/in/matheus-aleixo-299a05247/">Perfil</a></div>', unsafe_allow_html=True)

    st.markdown("---")
    with st.expander("🛠️ Painel de Acesso", expanded=False):
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
st.markdown("<p style='font-size: 1.2rem; color: #94A3B8; text-align:center;'>Especialista em RPA, ETL, Power BI e suporte SAP.</p>", unsafe_allow_html=True)

# Tabs
aba_objetivo, aba_experiencias, aba_conhecimentos, aba_projetos, aba_formacao = st.tabs([
    "👤 Objetivo & Foco", "💼 Experiências", "🧠 Conhecimentos", "🚀 Projetos", "📚 Formação"
])

# Objetivo
with aba_objetivo:
    st.markdown('<div class="section-card"><h2>🎯 Objetivo e Foco</h2>', unsafe_allow_html=True)
    st.markdown("""
    Atuar na área de Tecnologia da Informação como Analista de Sistemas ou Desenvolvedor, 
    visando evoluir profissionalmente, desenvolver novas competências e agregar valor à organização.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Experiências
with aba_experiencias:
    st.markdown('<div class="section-card"><h2>💼 Experiências Profissionais</h2>', unsafe_allow_html=True)
    st.markdown("""
    **Professor de Tecnologia e Matemática — Secretaria da Educação (2025–2026)**  
    Ensino Fundamental II e Médio, foco em competências digitais e matemáticas.

    **Consultor SAP Jr — Stefanini (Remoto)**  
    Suporte SAP S/4HANA nos módulos FI, CO e SD.

    **Estagiário de TI — Continental Automotive (2023–2025)**  
    Suporte SAP ECC, participação no projeto global SPIRIT e solução fiscal Guepardo.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Conhecimentos
with aba_conhecimentos:
    st.markdown('<div class="section-card"><h2>🧠 Conhecimentos Técnicos</h2>', unsafe_allow_html=True)
    st.markdown("""
    - SAP ECC e S/4HANA (FI, CO, SD, MM, Basis, ABAP)  
    - Automação em Python, UiPath, Scrapy, Playwright  
    - Pipelines ETL, HTML, XML, JSON  
    - PostgreSQL, APIs, AWS Lambda, Airflow  
    - Soft Skills: organização, resolução de problemas, comunicação assertiva
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Projetos
with aba_projetos:
    st.markdown('<div class="section-card"><h2>🚀 Meus Projetos</h2>', unsafe_allow_html=True)
    st.info("Os projetos serão adicionados e gerenciados pelo painel administrativo.")
    st.markdown('</div>', unsafe_allow_html=True)

# Formação
with aba_formacao:
    st.markdown('<div class="section-card"><h2>📚 Formação Acadêmica</h2>', unsafe_allow_html=True)
    st.markdown("""
    **Bacharelado em Tecnologia da Informação — UNIVESP**  
    Status: Ensino Superior Completo / Graduado

    **Certificações e Cursos:**
    - UiPath Academy — Automação (2024)
    - KA Solutions — SAP S/4HANA (8h)
    - Udemy — Power BI Avançado (2025)
    - Udemy — Python Avançado (2025)
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Painel Administrativo
if st.session_state["autenticado"]:
    st.markdown("---")
    st.markdown("## 🔒 Terminal do Administrador — Gerenciamento Total")

    menu_adm = st.selectbox(
        "Escolha a Base para Modificar",
        ["Projetos e Automações", "Focos de Vagas (Objetivo)", "Novos Conhecimentos Técnicos", "🖼️ Atualizar Foto de Perfil"]
    )

    if menu_adm == "🖼️ Atual"
    # --- PAINEL ADMINISTRATIVO ---
if st.session_state["autenticado"]:
    st.markdown("---")
    st.markdown("## 🔒 Terminal do Administrador — Gerenciamento Total")

    menu_adm = st.selectbox(
        "Escolha a Base para Modificar",
        ["Projetos e Automações", "Focos de Vagas (Objetivo)", "Novos Conhecimentos Técnicos", "🖼️ Atualizar Foto de Perfil"]
    )

    # 1. GERENCIAR PROJETOS
    if menu_adm == "Projetos e Automações":
        st.subheader("📝 Adicionar Novo Projeto")
        p_cat = st.selectbox("Categoria", ["Projeto", "Automação"])
        p_tit = st.text_input("Título")
        p_des = st.text_area("Descrição")
        p_l1 = st.text_input("Link do Repositório (GitHub)")
        p_l2 = st.text_input("Link do Vídeo")

        if st.button("🚀 Gravar Projeto"):
            if p_tit and p_des:
                nl = pd.DataFrame([{
                    "Categoria": p_cat,
                    "Título": p_tit,
                    "Descrição": p_des,
                    "Link do Processo": p_l1,
                    "Link do Vídeo": p_l2
                }])
                pd.concat([pd.read_csv(ARQUIVO_DADOS), nl], ignore_index=True).to_csv(ARQUIVO_DADOS, index=False)
                st.success("Projeto salvo com sucesso!")
                st.rerun()

        st.subheader("🗑️ Exclusão de Projetos")
        df_dados = pd.read_csv(ARQUIVO_DADOS)
        if not df_dados.empty:
            st.dataframe(df_dados)
            idx_ex = st.number_input("Índice para apagar:", min_value=0, max_value=len(df_dados)-1, step=1)
            confirmar_exclusao = st.checkbox("⚠️ Confirmar exclusão do registro", key="conf_ex_dados")
            if st.button("❌ Apagar Registro"):
                if confirmar_exclusao:
                    df_dados.drop(idx_ex).reset_index(drop=True).to_csv(ARQUIVO_DADOS, index=False)
                    st.success("Registro removido com sucesso!")
                    st.rerun()
                else:
                    st.warning("Marque a caixa de verificação para confirmar.")
        else:
            st.info("Nenhum projeto cadastrado.")

    # 2. GERENCIAR VAGAS (OBJETIVO)
    elif menu_adm == "Focos de Vagas (Objetivo)":
        st.subheader("📝 Inserir Novo Foco de Vaga")
        v_tit = st.text_input("Área/Vaga (Ex: Analista de Negócios)")
        v_des = st.text_area("Descrição Estratégica do Foco")

        if st.button("🚀 Gravar Novo Foco"):
            if v_tit and v_des:
                nl = pd.DataFrame([{"Título": v_tit, "Descrição": v_des}])
                pd.concat([pd.read_csv(ARQUIVO_VAGAS), nl], ignore_index=True).to_csv(ARQUIVO_VAGAS, index=False)
                st.success("Foco adicionado com sucesso!")
                st.rerun()

        st.subheader("🗑️ Remover Focos Existentes")
        df_vagas = pd.read_csv(ARQUIVO_VAGAS)
        if not df_vagas.empty:
            st.dataframe(df_vagas)
            idx_ex = st.number_input("Índice do foco para apagar:", min_value=0, max_value=len(df_vagas)-1, step=1)
            confirmar_exclusao = st.checkbox("⚠️ Confirmar exclusão deste foco", key="conf_ex_vagas")
            if st.button("❌ Apagar Foco"):
                if confirmar_exclusao:
                    df_vagas.drop(idx_ex).reset_index(drop=True).to_csv(ARQUIVO_VAGAS, index=False)
                    st.success("Foco removido com sucesso!")
                    st.rerun()
                else:
                    st.warning("Marque a caixa de verificação para confirmar.")
        else:
            st.info("Nenhum foco cadastrado.")

    # 3. GERENCIAR CONHECIMENTOS
    elif menu_adm == "Novos Conhecimentos Técnicos":
        st.subheader("📝 Inserir Nova Skill")
        s_cat = st.selectbox("Categoria", ["Dados", "RPA", "SAP"])
        s_nom = st.text_input("Nome do Conhecimento (Ex: Apache Airflow)")
        s_pct = st.slider("Porcentagem de Domínio", 0, 100, 80)

        if st.button("🚀 Gravar Skill"):
            if s_nom:
                nl = pd.DataFrame([{"Categoria": s_cat, "Nome": s_nom, "Porcentagem": s_pct}])
                pd.concat([pd.read_csv(ARQUIVO_SKILLS), nl], ignore_index=True).to_csv(ARQUIVO_SKILLS, index=False)
                st.success("Skill adicionada com sucesso!")
                st.rerun()

        st.subheader("🗑️ Remover Skills")
        df_skills = pd.read_csv(ARQUIVO_SKILLS)
        if not df_skills.empty:
            st.dataframe(df_skills)
            idx_ex = st.number_input("Índice da skill para apagar:", min_value=0, max_value=len(df_skills)-1, step=1)
            confirmar_exclusao = st.checkbox("⚠️ Confirmar exclusão desta skill", key="conf_ex_skills")
            if st.button("❌ Apagar Skill"):
                if confirmar_exclusao:
                    df_skills.drop(idx_ex).reset_index(drop=True).to_csv(ARQUIVO_SKILLS, index=False)
                    st.success("Skill removida com sucesso!")
                    st.rerun()
                else:
                    st.warning("Marque a caixa de verificação para confirmar.")
        else:
            st.info("Nenhuma skill cadastrada.")

    # 4. ATUALIZAR FOTO DE PERFIL
    elif menu_adm == "🖼️ Atualizar Foto de Perfil":
        st.subheader("Substituir Imagem do Perfil")
        foto_carregada = st.file_uploader("Escolha uma imagem", type=["jpg", "jpeg", "png"])
        if foto_carregada is not None:
            st.image(foto_carregada, width=200, caption="Pré-visualização")
            if st.button("💾 Aplicar Nova Imagem", type="primary"):
                try:
                    if os.path.exists(NOME_FOTO):
                        os.remove(NOME_FOTO)
                    with open(NOME_FOTO, "wb") as f:
                        f.write(foto_carregada.getbuffer())
                    st.success("Imagem atualizada com sucesso!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao salvar: {e}")


