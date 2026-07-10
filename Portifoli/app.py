import streamlit as st
import pandas as pd
import base64
import os
import glob
import subprocess

# 1. Configurações de Layout da Página
st.set_page_config(
    page_title="M. Aleixo TI",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DO ESTADO DE SESSÃO CORPORATIVO (LOGIN/LOGOFF) ---
if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

# Credenciais Administrativas Restritas
USUARIO_ADMIN = "matheus"
SENHA_ADMIN = "@Kayle2023"

# --- ARQUIVOS LOCAIS DE PERSISTÊNCIA DE DADOS ---
ARQUIVO_DADOS = "dados_portfolio.csv"
ARQUIVO_VAGAS = "dados_vagas.csv"
ARQUIVO_SKILLS = "dados_skills.csv"
ARQUIVO_CURSOS = "dados_cursos.csv"

# Inicialização de bases CSV caso não existam
if not os.path.exists(ARQUIVO_DADOS):
    pd.DataFrame(columns=["Categoria", "Título", "Descrição", "Link do Processo", "Link do Vídeo"]).to_csv(ARQUIVO_DADOS, index=False)

if not os.path.exists(ARQUIVO_VAGAS):
    df_vagas_init = pd.DataFrame([
        {"Título": "📊 Power BI & Data Analytics", "Descrição": "Foco no desenvolvimento de soluções de inteligência de negócios. Modelagem analítica de dados estruturados, criação de dashboards dinâmicos avançados no Power BI para suporte à tomada de decisão."},
        {"Título": "⚙️ Automação (RPA) & Scraping", "Descrição": "Arquitetura de robôs estáveis utilizando Python (Scrapy, Playwright) e plataforma UiPath. Desenvolvimento de bots robustos focados em otimização de fluxos operacionais."},
        {"Título": "🏢 ERP & Soluções SAP", "Descrição": "Sustentação técnica e funcional aos ambientes SAP ECC e S/4HANA. Atendimento consultivo Níveis I e II focado nos módulos FI, CO, SD e MM."}
    ])
    df_vagas_init.to_csv(ARQUIVO_VAGAS, index=False)

if not os.path.exists(ARQUIVO_SKILLS):
    df_skills_init = pd.DataFrame([
        {"Categoria": "Dados", "Nome": "Power BI (Dashboards Gerenciais & Modelagem DAX)", "Porcentagem": 90},
        {"Categoria": "Dados", "Nome": "Bancos de Dados Relacionais (PostgreSQL)", "Porcentagem": 75},
        {"Categoria": "Dados", "Nome": "Pipelines ETL & Manipulação (JSON, XML, HTML)", "Porcentagem": 90},
        {"Categoria": "RPA", "Nome": "Python Avançado (Scrapy, Playwright, BeautifulSoup)", "Porcentagem": 95},
        {"Categoria": "RPA", "Nome": "Plataforma de Robótica UiPath", "Porcentagem": 85},
        {"Categoria": "SAP", "Nome": "Suporte Funcional SAP (ECC e S/4HANA)", "Porcentagem": 90},
        {"Categoria": "SAP", "Nome": "Módulos de Processos (FI, CO, SD, MM, Basis)", "Porcentagem": 80},
        {"Categoria": "SAP", "Nome": "Solução Fiscal Integrada Guepardo", "Porcentagem": 85}
    ])
    df_skills_init.to_csv(ARQUIVO_SKILLS, index=False)

if not os.path.exists(ARQUIVO_CURSOS):
    df_cursos_init = pd.DataFrame([
        {"Título": "📊 Power BI Avançado", "Emissor": "Plataforma Udemy", "Data": "Conclusão: 31/07/2025", "Descrição": "Construção de arquiteturas corporativas de BI e dashboards estratégicos."},
        {"Título": "🐍 Python Avançado", "Emissor": "Plataforma Udemy", "Data": "Conclusão: 30/12/2025", "Descrição": "Estruturas de algoritmos, raspagem complexa e pipelines ETL."},
        {"Título": "🤖 Formação Profissional em Automação", "Emissor": "UiPath Academy de Automação e Desenvolvimento", "Data": "Conclusão: 21/04/2024", "Descrição": "Modelagem, testes e governança de robôs (RPA) industriais."},
        {"Título": "🏢 Fundamentos Básicos do SAP S/4HANA", "Emissor": "KA Solutions", "Data": "Carga Horária: 8 horas", "Descrição": "Arquitetura estrutural base de sistemas integrados ERP."}
    ])
    df_cursos_init.to_csv(ARQUIVO_CURSOS, index=False)


# --- FUNÇÃO AUTOMÁTICA DE COMMIT E PUSH NO GIT ---
def sincronizar_com_github(mensagem_commit="Painel Admin: Sincronização automática de dados"):
    """Adiciona as alterações, commita e envia diretamente ao GitHub remoto."""
    try:
        subprocess.run(["git", "add", ARQUIVO_DADOS, ARQUIVO_VAGAS, ARQUIVO_SKILLS, ARQUIVO_CURSOS, "*.jpg", "*.png", "*.jpeg"], check=True)
        subprocess.run(["git", "commit", "-m", mensagem_commit], check=True)
        subprocess.run(["git", "push"], check=True)
        st.toast("🚀 Sincronização automatizada concluída no GitHub!", icon="🔄")
    except subprocess.CalledProcessError as e:
        st.error(f"Falha de sincronização automática com o GitHub: {e}")


# --- FUNÇÃO AUXILIAR DE RENDERIZAÇÃO DA IMAGEM ---
def obter_imagem_base64_flexivel():
    padroes = ["Foto perfil Matheus.jpg", "foto perfil matheus.jpg", "Foto perfil Matheus.jpeg", "Foto_Perfil.jpg", "*.jpg", "*.png"]
    for padrao in padroes:
        arquivos = glob.glob(padrao)
        if arquivos:
            with open(arquivos[0], "rb") as image_file:
                return base64.b64encode(image_file.read()).decode()
    return None

foto_base64 = obter_imagem_base64_flexivel()

# --- TEXTO ESTRUTURADO DO CURRÍCULO ---
TEXTO_CURRICULO = """MATHEUS ALEIXO
Várzea Paulista/SP | matheus.aleixo2020@gmail.com | (11) 97478-0590
LinkedIn: https://www.linkedin.com/in/matheus-aleixo-299a05247

OBJETIVO ESTRATÉGICO:
Atuar de forma analítica e consultiva na área de Tecnologia da Informação como Analista de Sistemas, Desenvolvedor ou Analista de Dados / Power BI."""

# --- INJEÇÃO DE ESTILOS CSS PREMIUM ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background-color: #0F172A;
        color: #E2E8F0;
    }
    .avatar-container { display: flex; justify-content: center; margin-bottom: 15px; }
    .avatar-img { width: 155px; height: 155px; border-radius: 50%; object-fit: cover; border: 3px solid #38BDF8; box-shadow: 0 4px 20px rgba(56, 189, 248, 0.4); }
    h1 { color: #F8FAFC !important; font-weight: 700 !important; letter-spacing: -0.05em; }
    h2, h3 { color: #38BDF8 !important; font-weight: 600 !important; }
    .focus-card { background: #1E293B; border: 1px solid #334155; border-radius: 12px; padding: 24px; height: 100%; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }
    .project-card { background: #1E293B; border: 1px solid #334155; border-radius: 12px; padding: 24px; margin-bottom: 20px; }
    .timeline-item { border-left: 2px solid #38BDF8; padding-left: 20px; margin-bottom: 30px; position: relative; }
    .timeline-item::before { content: ''; position: absolute; width: 14px; height: 14px; background: #0F172A; border: 3px solid #38BDF8; border-radius: 50%; left: -9px; top: 4px; }
    .skill-section-card { background: #1E293B; border: 1px solid #334155; border-radius: 16px; padding: 24px; margin-bottom: 24px; }
    .skill-item { margin-bottom: 15px; }
    .skill-name-percentage { display: flex; justify-content: space-between; font-size: 0.9rem; font-weight: 500; margin-bottom: 6px; }
    .skill-bar-bg { background: #334155; border-radius: 8px; height: 8px; width: 100%; overflow: hidden; }
    .skill-bar-fill { background: linear-gradient(90deg, #0EA5E9 0%, #38BDF8 100%); height: 100%; }
    .course-card { background: #1E293B; border: 1px solid #334155; border-radius: 8px; padding: 16px; margin-bottom: 12px; }
</style>
""", unsafe_allow_html=True)

# --- CARREGAMENTO REATIVO DAS QUATRO BASES ---
df_dados = pd.read_csv(ARQUIVO_DADOS)
df_vagas = pd.read_csv(ARQUIVO_VAGAS)
df_skills = pd.read_csv(ARQUIVO_SKILLS)
df_cursos = pd.read_csv(ARQUIVO_CURSOS)

# --- 4. BARRA LATERAL (Sidebar) ---
with st.sidebar:
    if foto_base64:
        st.markdown(f'<div class="avatar-container"><img class="avatar-img" src="data:image/jpeg;base64,{foto_base64}" alt="Matheus Aleixo"></div>', unsafe_allow_html=True)
    else:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=130)
        
    st.markdown("<h2 style='text-align: center; color: white !important;'>Matheus Aleixo</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #38BDF8; margin-top:-10px; font-weight: 500;'>TI & Data Analytics</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    with st.expander("📄 Visualizar Currículo Completo", expanded=False):
        st.text(TEXTO_CURRICULO)
        
    st.download_button(label="📥 Baixar Currículo PDF/TXT", data=TEXTO_CURRICULO, file_name="Curriculo_Matheus_Aleixo.txt", mime="text/plain", use_container_width=True)
    st.markdown("---")
    
    st.markdown("### 📋 Informações Pessoais")
    st.markdown("**📅 Nascimento:** 20/02/1996")
    st.markdown("**📍 Localização:** Várzea Paulista - SP")
    st.markdown("**💼 Disponibilidade:** Remoto / Híbrido / Presencial")
    st.markdown("**✉️ E-mail:** [matheus.aleixo2020@gmail.com](mailto:matheus.aleixo2020@gmail.com)")
    st.markdown("**🔗 LinkedIn:** [Acessar Perfil](https://www.linkedin.com/in/matheus-aleixo-299a05247)")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    with st.expander("🛠️ Configurações de Sistema", expanded=False):
        if not st.session_state["autenticado"]:
            input_user = st.text_input("User ID", key="adm_user")
            input_pass = st.text_input("Chave", type="password", key="adm_pass")
            if st.button("🔑 Autenticar"):
                if input_user == USUARIO_ADMIN and input_pass == SENHA_ADMIN:
                    st.session_state["autenticado"] = True
                    st.rerun()
                else:
                    st.error("Acesso negado.")
        else:
            st.write("🟢 Modo Editor Ativo")
            if st.button("🔒 Efetuar Logoff / Sair", type="primary"):
                st.session_state["autenticado"] = False
                st.rerun()

# --- 5. CABEÇALHO DO SITE ---
st.title("💻 M. Aleixo TI")
st.markdown("<p style='font-size: 1.2rem; color: #94A3B8; max-width: 900px;'>Especialista no desenvolvimento de automações (RPA), engenharia de pipelines de dados ETL, análises corporativas em Power BI e suporte técnico/funcional a ecossistemas ERP SAP.</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Configuração das Abas Principais
aba_sobre, aba_experiencias, aba_conhecimentos, aba_projetos, aba_formacao = st.tabs([
    "👤 Objetivo & Foco", 
    "💼 Trajetória Profissional", 
    "🧠 Conhecimentos Técnicos",
    "🚀 Meus Projetos", 
    "📚 Cursos e Formação"
])

# --- ABA: OBJETIVO & FOCO ---
with aba_sobre:
    st.markdown("## Perfil e Objetivo Estratégico")
    st.markdown("Atuar de forma analítica e consultiva na área de **Tecnologia da Informação como Analista de Sistemas, Desenvolvedor ou Analista de Dados / Power BI**.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    if not df_vagas.empty:
        colunas_vagas = st.columns(len(df_vagas))
        for idx, row in df_vagas.iterrows():
            with colunas_vagas[idx % len(df_vagas)]:
                st.markdown(f"""
                <div class="focus-card">
                    <h3 style="margin-top:0;">{row['Título']}</h3>
                    <p style="font-size:0.95rem; color:#94A3B8; line-height:1.5;">{row['Descrição']}</p>
                </div>
                """, unsafe_allow_html=True)

    # SUB-PAINEL ADMINISTRATIVO DIRETAMENTE NA ABA
    if st.session_state["autenticado"]:
        st.markdown("<br><hr><h3>🔒 Gerenciar Focos de Vagas</h3>", unsafe_allow_html=True)
        v_tit = st.text_input("Área/Vaga (Ex: Analista de Negócios)", key="add_vaga_tit")
        v_des = st.text_area("Descrição Estratégica do Foco", key="add_vaga_des")
        if st.button("🚀 Gravar Novo Foco", key="btn_vaga"):
            if v_tit and v_des:
                nl = pd.DataFrame([{"Título": v_tit, "Descrição": v_des}])
                pd.concat([df_vagas, nl], ignore_index=True).to_csv(ARQUIVO_VAGAS, index=False)
                sincronizar_com_github(f"Painel Admin: Adicionado foco de vaga '{v_tit}'")
                st.rerun()

        st.markdown("#### 🗑️ Remover Focos Existentes")
        if not df_vagas.empty:
            idx_excluir = None
            for idx, row in df_vagas.iterrows():
                if st.checkbox(f"Excluir linha: **{row['Título']}**", key=f"del_vaga_{idx}"):
                    idx_excluir = idx
            if idx_excluir is not None and st.button("❌ Confirmar e Apagar Foco", type="primary", key="btn_del_vaga"):
                df_vagas.drop(idx_excluir).reset_index(drop=True).to_csv(ARQUIVO_VAGAS, index=False)
                sincronizar_com_github("Painel Admin: Removido foco de vaga")
                st.rerun()

# --- ABA: TRAJETÓRIA PROFISSIONAL ---
with aba_experiencias:
    st.markdown("## Histórico de Carreira")
    st.markdown("""
    <div class="timeline-item">
        <h3 style="margin:0; color:#F8FAFC;">Professor de Tecnologia e Matemática</h3>
        <span style="color:#38BDF8; font-size:0.95rem; font-weight:600;">Secretaria da Educação</span><br>
        <span style="color:#64748B; font-size:0.85rem; font-weight:500;">Outubro 2025 – Fevereiro 2026</span>
    </div>
    <div class="timeline-item">
        <h3 style="margin:0; color:#F8FAFC;">Consultor SAP Jr</h3>
        <span style="color:#38BDF8; font-size:0.95rem; font-weight:600;">Stefanini</span><br>
    </div>
    """, unsafe_allow_html=True)

# --- ABA: CONHECIMENTOS TÉCNICOS ---
with aba_conhecimentos:
    st.markdown("## Hard Skills & Matriz de Competências")
    col_k1, col_k2 = st.columns(2)
    with col_k1:
        st.markdown('<div class="skill-section-card">### 📊 BI & Dados</div>', unsafe_allow_html=True)
        df_k_dados = df_skills[df_skills["Categoria"] == "Dados"]
        for _, row in df_k_dados.iterrows():
            st.markdown(f'{row["Nome"]} - {row["Porcentagem"]}%')
            
    # SUB-PAINEL ADMINISTRATIVO DIRETAMENTE NA ABA
    if st.session_state["autenticado"]:
        st.markdown("<br><hr><h3>🔒 Gerenciar Skills</h3>", unsafe_allow_html=True)
        s_cat = st.selectbox("Categoria", ["Dados", "RPA", "SAP"], key="add_skill_cat")
        s_nom = st.text_input("Nome da Skill", key="add_skill_nom")
        s_pct = st.slider("Domínio %", 0, 100, 80, key="add_skill_pct")
        if st.button("🚀 Gravar Skill", key="btn_skill"):
            if s_nom:
                nl = pd.DataFrame([{"Categoria": s_cat, "Nome": s_nom, "Porcentagem": s_pct}])
                pd.concat([df_skills, nl], ignore_index=True).to_csv(ARQUIVO_SKILLS, index=False)
                sincronizar_com_github(f"Painel Admin: Adicionada skill '{s_nom}'")
                st.rerun()

        st.markdown("#### 🗑️ Remover Skills")
        if not df_skills.empty:
            idx_excluir = None
            for idx, row in df_skills.iterrows():
                if st.checkbox(f"Excluir linha: **{row['Nome']}** ({row['Categoria']})", key=f"del_skill_{idx}"):
                    idx_excluir = idx
            if idx_excluir is not None and st.button("❌ Confirmar e Apagar Skill", type="primary", key="btn_del_skill"):
                df_skills.drop(idx_excluir).reset_index(drop=True).to_csv(ARQUIVO_SKILLS, index=False)
                sincronizar_com_github("Painel Admin: Removida skill")
                st.rerun()

# --- ABA: MEUS PROJETOS ---
with aba_projetos:
    st.markdown("## Repositório Dinâmico de Projetos")
    if not df_dados.empty:
        for index, row in df_dados.iterrows():
            st.markdown(f"#### 🚀 {row['Título']} ({row['Categoria']})")
            st.write(row['Descrição'])
    else:
        st.info("Nenhum projeto dinâmico publicado.")

    # SUB-PAINEL ADMINISTRATIVO DIRETAMENTE NA ABA
    if st.session_state["autenticado"]:
        st.markdown("<br><hr><h3>🔒 Gerenciar Projetos e Automações</h3>", unsafe_allow_html=True)
        p_cat = st.selectbox("Categoria", ["Projeto", "Automação"], key="add_proj_cat")
        p_tit = st.text_input("Título", key="add_proj_tit")
        p_des = st.text_area("Descrição", key="add_proj_des")
        p_l1 = st.text_input("Link do Repositório (GitHub)", key="add_proj_l1")
        p_l2 = st.text_input("Link do Vídeo", key="add_proj_l2")
        
        if st.button("🚀 Gravar Projeto", key="btn_proj"):
            if p_tit and p_des:
                nl = pd.DataFrame([{"Categoria": p_cat, "Título": p_tit, "Descrição": p_des, "Link do Processo": p_l1, "Link do Vídeo": p_l2}])
                pd.concat([df_dados, nl], ignore_index=True).to_csv(ARQUIVO_DADOS, index=False)
                sincronizar_com_github(f"Painel Admin: Adicionado projeto '{p_tit}'")
                st.rerun()
                
        st.markdown("#### 🗑️ Exclusão de Projetos")
        if not df_dados.empty:
            idx_excluir = None
            for idx, row in df_dados.iterrows():
                if st.checkbox(f"Excluir linha: **{row['Título']}** [{row['Categoria']}]", key=f"del_proj_{idx}"):
                    idx_excluir = idx
            
            if idx_excluir is not None and st.button("❌ Confirmar e Apagar Registro", type="primary", key="btn_del_proj"):
                df_dados.drop(idx_excluir).reset_index(drop=True).to_csv(ARQUIVO_DADOS, index=False)
                sincronizar_com_github("Painel Admin: Removido projeto")
                st.rerun()

# --- ABA: CURSOS E FORMAÇÃO ---
with aba_formacao:
    st.markdown("## Certificações & Especializações de Mercado")
    if not df_cursos.empty:
        for _, row in df_cursos.iterrows():
            st.markdown(f"**{row['Título']}** — {row['Emissor']}")
    else:
        st.info("Nenhuma certificação cadastrada.")

    # SUB-PAINEL ADMINISTRATIVO DIRETAMENTE NA ABA
    if st.session_state["autenticado"]:
        st.markdown("<br><hr><h3>🔒 Gerenciar Especializações e Cursos</h3>", unsafe_allow_html=True)
        c_tit = st.text_input("Título do Curso", key="add_curso_tit")
        c_emi = st.text_input("Emissor / Instituição", key="add_curso_emi")
        c_dat = st.text_input("Data de Conclusão / Carga Horária", key="add_curso_dat")
        c_des = st.text_area("Breve Descrição do Aprendizado", key="add_curso_des")
        
        if st.button("🚀 Gravar Novo Curso", key="btn_curso"):
            if c_tit and c_emi:
                nl = pd.DataFrame([{"Título": c_tit, "Emissor": c_emi, "Data": c_dat, "Descrição": c_des}])
                pd.concat([df_cursos, nl], ignore_index=True).to_csv(ARQUIVO_CURSOS, index=False)
                sincronizar_com_github(f"Painel Admin: Adicionado curso '{c_tit}'")
                st.rerun()
                
        st.markdown("#### 🗑️ Remover Cursos Existentes")
        if not df_cursos.empty:
            idx_excluir = None
            for idx, row in df_cursos.iterrows():
                if st.checkbox(f"Excluir linha: **{row['Título']}** ({row['Emissor']})", key=f"del_curso_{idx}"):
                    idx_excluir = idx
            if idx_excluir is not None and st.button("❌ Confirmar e Apagar Curso", type="primary", key="btn_del_curso"):
                df_cursos.drop(idx_excluir).reset_index(drop=True).to_csv(ARQUIVO_CURSOS, index=False)
                sincronizar_com_github("Painel Admin: Removido curso")
                st.rerun()
