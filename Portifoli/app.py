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
NOME_FOTO = "Foto_Perfil_Matheus.jpg"

# Inicialização de bases CSV
if not os.path.exists(ARQUIVO_DADOS):
    pd.DataFrame(columns=["Categoria", "Título", "Descrição", "Link do Processo", "Link do Vídeo"]).to_csv(ARQUIVO_DADOS, index=False)
if not os.path.exists(ARQUIVO_VAGAS):
    pd.DataFrame(columns=["Título", "Descrição"]).to_csv(ARQUIVO_VAGAS, index=False)
if not os.path.exists(ARQUIVO_SKILLS):
    pd.DataFrame(columns=["Categoria", "Nome", "Porcentagem"]).to_csv(ARQUIVO_SKILLS, index=False)

# Função auxiliar para imagem
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
    .avatar-img { width: 155px; height: 155px; border-radius: 50%; border: 3px solid #38BDF8; }
    h1 { color: #F8FAFC !important; font-weight: 700 !important; }
    h2, h3 { color: #38BDF8 !important; font-weight: 600 !important; }
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
    st.markdown("**👤 Nome:** Matheus Aleixo")
    st.markdown("**📅 Nascimento:** 20/02/1996")
    st.markdown("**📍 Localização:** Várzea Paulista - SP")
    st.markdown("**✉️ E-mail:** [matheus.aleixo2020@gmail.com](mailto:matheus.aleixo2020@gmail.com)")
    st.markdown("**🔗 LinkedIn:** [www.linkedin.com/in/matheus-aleixo-299a05247](https://www.linkedin.com/in/matheus-aleixo-299a05247)")

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
st.markdown("<p style='font-size: 1.2rem; color: #94A3B8;'>Especialista em RPA, ETL, Power BI e suporte SAP.</p>", unsafe_allow_html=True)

# Tabs
aba_objetivo, aba_experiencias, aba_conhecimentos, aba_projetos, aba_formacao = st.tabs([
    "👤 Objetivo & Foco", "💼 Trajetória Profissional", "🧠 Conhecimentos Técnicos", "🚀 Meus Projetos", "📚 Cursos e Formação"
])

# --- ABA: OBJETIVO & FOCO ---
with aba_objetivo:
    st.markdown("## Objetivo e Foco")
    st.markdown("""
    Atuar na área de Tecnologia da Informação como Analista de Sistemas ou Desenvolvedor, 
    visando evoluir profissionalmente, desenvolver novas competências e agregar valor à organização 
    através das seguintes frentes:
    - **Sistemas e Infraestrutura:** suporte técnico, desenvolvimento de sistemas e execução de testes funcionais.
    - **Automação e Engenharia de Dados:** desenvolvimento de soluções em Python, pipelines ETL e integração de APIs.
    - **Governança e Processos:** gerenciamento de repositórios Git/GitHub e aplicação de visão analítica para segurança e produtividade.
    """)

# --- ABA: EXPERIÊNCIAS ---
with aba_experiencias:
    st.markdown("## Experiências Profissionais")
    st.markdown("""
    **Professor de Tecnologia e Matemática — Secretaria da Educação | Campo Limpo Paulista - SP (Outubro 2025 – Fevereiro 2026)**  
    Ensino Fundamental II e Médio, com foco em competências lógicas, digitais e matemáticas.  
    Uso de ferramentas de TI e materiais digitais para facilitar a compreensão de conceitos abstratos.

    **Consultor SAP Jr — Stefanini | Remoto (Projeto Temporário)**  
    Suporte Funcional SAP S/4HANA (Nível I e II) nos módulos FI, CO e SD.  
    Monitoramento de IDocs, execução de parametrizações (customizing) e aplicação de notas SAP.

    **Estagiário de Tecnologia da Informação — Continental Automotive | Várzea Paulista - SP (Junho 2023 – Fevereiro 2025)**  
    Suporte funcional SAP ECC (Basis, FI, CO, SD e MM).  
    Participação no projeto global SPIRIT e atuação na solução fiscal Guepardo.
    """)

# --- ABA: CONHECIMENTOS ---
with aba_conhecimentos:
    st.markdown("## Conhecimentos Técnicos")
    st.markdown("""
    - **Sistemas & ERP:** SAP ECC e S/4HANA (FI, CO, SD, MM, Basis, ABAP).  
    - **Localização Fiscal:** Ferramenta Guepardo, monitoramento e tratamento de IDocs.  
    - **Automação & Web Scraping (RPA):** Python, UiPath, Scrapy, Playwright, BeautifulSoup.  
    - **Engenharia de Dados & ETL:** pipelines de dados, extração e modelagem (HTML, XML, JSON).  
    - **Bancos de Dados & APIs:** PostgreSQL, integração e consumo de APIs.  
    - **Cloud & Testes:** AWS Lambda, EventBridge, Apache Airflow, Git, testes funcionais.  
    - **Processos & Segurança:** suporte ao usuário, conferência de notas fiscais e boas práticas anti-bot.  
    - **Soft Skills:** organização, resolução de problemas, mediação de conflitos e comunicação assertiva.  
    - **Linguagens:** Python (Avançado), Java (Básico), C (Básico).
    """)

# --- ABA: PROJETOS ---
with aba_projetos:
    st.markdown("## Meus Projetos")
    st.info("Os projetos serão adicionados e gerenciados pelo painel administrativo abaixo.")

# --- ABA: FORMAÇÃO ---
with aba_formacao:
    st.markdown("## Formação Acadêmica")
    st.markdown("""
    **Bacharelado em Tecnologia da Informação — UNIVESP**  
    Status: Ensino Superior Completo / Graduado

    **Certificações e Cursos:**
    - UiPath Academy — Formação Profissional em Automação (Conclusão: 21/04/2024)
    - KA Solutions — Fundamentos Básicos do SAP S/4HANA (Carga Horária: 8h)
    - Udemy — Power BI Avançado (Conclusão: 31/07/2025)
    - Udemy — Python Avançado (Conclusão: 30/12/2025)
    """)

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
