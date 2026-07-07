import streamlit as st
import pandas as pd
import base64
import os
import glob

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

# --- TEXTO ESTRUTURADO DO SEU CURRÍCULO ANEXADO ---
TEXTO_CURRICULO = """MATHEUS ALEIXO
Várzea Paulista/SP | matheus.aleixo2020@gmail.com | (11) 97478-0590
LinkedIn: https://www.linkedin.com/in/matheus-aleixo-299a05247

OBJETIVO ESTRATÉGICO:
Atuar de forma analítica e consultiva na área de Tecnologia da Informação como Analista de Sistemas, Desenvolvedor ou Analista de Dados / Power BI. Foco em aplicar competências analíticas refinadas e estratégias tecnológicas modernas para estruturar dados, desenhar dashboards inteligentes e garantir a governança corporativa de ponta a ponta.

FORMAÇÃO ACADÊMICA:
- Bacharelado em Tecnologia da Informação - UNIVESP (Ensino Superior Completo / Graduado)

HISTÓRICO PROFISSIONAL:
1. Professor de Tecnologia e Matemática - Secretaria da Educação | Campo Limpo Paulista - SP (Outubro 2025 – Fevereiro 2026)
   • Condução e liderança de turmas focando no raciocínio lógico, abstração e competências digitais.
   • Mediação activa de cronogramas digitais de ensino e uso estratégico de ferramentas de TI aplicadas à educação.

2. Consultor SAP Jr - Stefanini | Atuação Remota (Escopo de Projeto)
   • Fornecimento de Suporte Funcional de Nível I e II em SAP S/4HANA para usuários finais nos módulos FI, CO e SD.
   • Tratamento de dados mestres de clientes/fornecedores via IDocs, parametrizações customizadas (customizing) e requests.

3. Estagiário de Tecnologia da Informação - Continental Automotive | Várzea Paulista - SP (Junho 2023 – Fevereiro 2025)
   • Atuação direta em suporte funcional SAP ECC nos módulos Basis, MM, FI, CO e SD, atendendo fluxos de Procure-to-Pay (P2P).
   • Projeto SPIRIT: Participação activa na iniciativa global da Continental de harmonização dos ambientes e consolidação de servidores SAP do grupo.
   • Atuação analítica com a solução fiscal Guepardo (extração de relatórios, análises em debug do sistema e transporte de requests).

COMPETÊNCIAS TÉCNICAS:
- BI & Dados: Power BI Avançado (Dashboards Gerenciais e Modelagem DAX), Bancos de Dados Relacionais (PostgreSQL), Pipelines ETL & Manipulação de Dados (JSON, XML, HTML).
- Automação (RPA): Python Avançado (Scrapy, Playwright, BeautifulSoup), Plataforma de Robótica UiPath.
- ERP Integrado: Suporte Funcional SAP (ECC e S/4HANA), Módulos FI, CO, SD, MM, Basis, ABAP debug e Solução Fiscal Guepardo.
- Práticas de Nuvem: Controle de versão distribuído via Git/GitHub, noções de escalabilidade serverless em nuvem (AWS Lambda / EventBridge) e orquestradores de fluxo (Apache Airflow)."""

# --- INJEÇÃO DE ESTILOS CSS PREMIUM ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background-color: #0F172A;
        color: #E2E8F0;
    }
    
    .avatar-container {
        display: flex;
        justify-content: center;
        margin-bottom: 15px;
    }
    .avatar-img {
        width: 155px;
        height: 155px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid #38BDF8;
        box-shadow: 0 4px 20px rgba(56, 189, 248, 0.4);
    }
    
    h1 {
        color: #F8FAFC !important;
        font-weight: 700 !important;
        letter-spacing: -0.05em;
    }
    h2, h3 {
        color: #38BDF8 !important;
        font-weight: 600 !important;
    }
    
    .focus-card {
        background: #1E293B;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 24px;
        height: 100%;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .project-card {
        background: #1E293B;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 20px;
        transition: transform 0.3s ease, border-color 0.3s ease;
    }
    .project-card:hover {
        transform: translateY(-4px);
        border-color: #38BDF8;
        box-shadow: 0 10px 20px -10px rgba(56, 189, 248, 0.2);
    }
    
    .timeline-item {
        border-left: 2px solid #38BDF8;
        padding-left: 20px;
        margin-bottom: 30px;
        position: relative;
    }
    .timeline-item::before {
        content: '';
        position: absolute;
        width: 14px;
        height: 14px;
        background: #0F172A;
        border: 3px solid #38BDF8;
        border-radius: 50%;
        left: -9px;
        top: 4px;
    }
    
    .skill-section-card {
        background: #1E293B;
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 24px;
    }
    .skill-item {
        margin-bottom: 15px;
    }
    .skill-name-percentage {
        display: flex;
        justify-content: space-between;
        font-size: 0.9rem;
        font-weight: 500;
        margin-bottom: 6px;
    }
    .skill-bar-bg {
        background: #334155;
        border-radius: 8px;
        height: 8px;
        width: 100%;
        overflow: hidden;
    }
    .skill-bar-fill {
        background: linear-gradient(90deg, #0EA5E9 0%, #38BDF8 100%);
        height: 100%;
    }
    
    .course-card {
        background: #1E293B;
        border: 1px solid #334155;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 12px;
    }
</style>
""", unsafe_allow_html=True)

# --- CARREGAMENTO REATIVO DAS TRÊS BASES ---
df_dados = pd.read_csv(ARQUIVO_DADOS)
df_vagas = pd.read_csv(ARQUIVO_VAGAS)
df_skills = pd.read_csv(ARQUIVO_SKILLS)

# --- 4. BARRA LATERAL (Sidebar) ---
with st.sidebar:
    if foto_base64:
        st.markdown(f"""
        <div class="avatar-container">
            <img class="avatar-img" src="data:image/jpeg;base64,{foto_base64}" alt="Matheus Aleixo">
        </div>
        """, unsafe_allow_html=True)
    else:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=130)
        st.caption("⚠️ Use a área de configurações de sistema abaixo para carregar sua foto de perfil via site.")
        
    st.markdown("<h2 style='text-align: center; color: white !important;'>Matheus Aleixo</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #38BDF8; margin-top:-10px; font-weight: 500;'>TI & Data Analytics</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    # --- ÁREA INTERATIVA DO CURRÍCULO COMPLETO ---
    with st.expander("📄 Visualizar Currículo Completo", expanded=False):
        st.text(TEXTO_CURRICULO)
        
    st.download_button(
        label="📥 Baixar Currículo PDF/TXT",
        data=TEXTO_CURRICULO,
        file_name="Curriculo_Matheus_Aleixo.txt",
        mime="text/plain",
        use_container_width=True
    )
    st.markdown("---")
    
    st.markdown("### 📋 Informações Pessoais")
    st.markdown("**📅 Nascimento:** 20/02/1996")
    st.markdown("**📍 Localização:** Várzea Paulista - SP")
    st.markdown("**💼 Disponibilidade:** Remoto / Híbrido / Presencial")
    st.markdown("**🌐 Idiomas:** Inglês (Básico)")
    st.markdown("**✉️ E-mail:** [matheus.aleixo2020@gmail.com](mailto:matheus.aleixo2020@gmail.com)")
    st.markdown("**🔗 LinkedIn:** [Acessar Perfil](https://www.linkedin.com/in/matheus-aleixo-299a05247)")
    
    # --- EASTER EGG: BOTÃO SECRETO DE SISTEMA ADMINISTRATIVO ---
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)
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
st.markdown("<p style='font-size: 1.2rem; color: #94A3B8; max-width: 900px;'>Especialista no desenvolvimento de automações (RPA), engenharia de pipelines de dados ETL, análises corporativas em Power BI e suporte técnico/funcional a ecossistemas ERP SAP (ECC e S/4HANA).</p>", unsafe_allow_html=True)
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
    st.markdown(
        "Atuar de forma analítica e consultiva na área de **Tecnologia da Informação como Analista de Sistemas, Desenvolvedor ou Analista de Dados / Power BI**. "
        "Foco em aplicar competências analíticas refinadas e estratégias tecnológicas modernas para estruturar dados, desenho de relatórios visuais inteligentes, "
        "automatizar rotinas operacionais e garantir a produtividade e governança corporativa de ponta a ponta."
    )
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Renderização dinâmica dos Cards de Objetivos/Vagas a partir do arquivo local
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

# --- ABA: TRAJETÓRIA PROFISSIONAL ---
with aba_experiencias:
    st.markdown("## Histórico de Carreira")
    st.markdown("""
    <div class="timeline-item">
        <h3 style="margin:0; color:#F8FAFC;">Professor de Tecnologia e Matemática</h3>
        <span style="color:#38BDF8; font-size:0.95rem; font-weight:600;">Secretaria da Educação | Campo Limpo Paulista - SP</span><br>
        <span style="color:#64748B; font-size:0.85rem; font-weight:500;">Outubro 2025 – Fevereiro 2026</span>
        <p style="color:#94A3B8; font-size:0.95rem; margin-top:8px; line-height:1.6;">
            • Condução e liderança de turmas focando no raciocínio lógico, abstraction e competências digitais.<br>
            • Mediação ativa de cronogramas digitais de ensino e uso estratégico de ferramentas de TI aplicadas à educação.
        </p>
    </div>
    
    <div class="timeline-item">
        <h3 style="margin:0; color:#F8FAFC;">Consultor SAP Jr</h3>
        <span style="color:#38BDF8; font-size:0.95rem; font-weight:600;">Stefanini | Atuação Remota</span><br>
        <span style="color:#64748B; font-size:0.85rem; font-weight:500;">Alocação por Escopo de Projeto</span>
        <p style="color:#94A3B8; font-size:0.95rem; margin-top:8px; line-height:1.6;">
            • Fornecimento de Suporte Funcional de Nível I e II em SAP S/4HANA para usuários finais nos módulos FI, CO e SD.<br>
            • Tratamento de dados mestres de clientes/fornecedores via IDocs, parametrizações customizadas (customizing) e transporte de requests.
        </p>
    </div>
    
    <div class="timeline-item">
        <h3 style="margin:0; color:#F8FAFC;">Estagiário de Tecnologia da Informação</h3>
        <span style="color:#38BDF8; font-size:0.95rem; font-weight:600;">Continental Automotive | Várzea Paulista - SP</span><br>
        <span style="color:#64748B; font-size:0.85rem; font-weight:500;">Junho 2023 – Fevereiro 2025</span>
        <p style="color:#94A3B8; font-size:0.95rem; margin-top:8px; line-height:1.6;">
            • Atuação direta em suporte funcional SAP ECC nos módulos Basis, MM, FI, CO e SD, atendendo fluxos de Procure-to-Pay (P2P).<br>
            • <strong>Projeto SPIRIT:</strong> Participação ativa na iniciativa global da Continental de harmonização dos ambientes e consolidação de servidores SAP do grupo.<br>
            • Atuação analítica com a solução fiscal <strong>Guepardo</strong> (extração de relatórios, análises em debug do sistema e transporte de requests).
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- ABA: CONHECIMENTOS TÉCNICOS ---
with aba_conhecimentos:
    st.markdown("## Hard Skills & Matriz de Competências")
    col_k1, col_k2 = st.columns(2)
    
    with col_k1:
        st.markdown('<div class="skill-section-card">', unsafe_allow_html=True)
        st.markdown("### 📊 BI, Engenharia & Ciência de Dados")
        df_k_dados = df_skills[df_skills["Categoria"] == "Dados"]
        for _, row in df_k_dados.iterrows():
            st.markdown(f'<div class="skill-item"><div class="skill-name-percentage"><span>{row["Nome"]}</span><span>{row["Porcentagem"]}%</span></div><div class="skill-bar-bg"><div class="skill-bar-fill" style="width: {row["Porcentagem"]}%;"></div></div></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="skill-section-card">', unsafe_allow_html=True)
        st.markdown("### 🐍 Engenharia de Automação (RPA)")
        df_k_rpa = df_skills[df_skills["Categoria"] == "RPA"]
        for _, row in df_k_rpa.iterrows():
            st.markdown(f'<div class="skill-item"><div class="skill-name-percentage"><span>{row["Nome"]}</span><span>{row["Porcentagem"]}%</span></div><div class="skill-bar-bg"><div class="skill-bar-fill" style="width: {row["Porcentagem"]}%;"></div></div></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_k2:
        st.markdown('<div class="skill-section-card">', unsafe_allow_html=True)
        st.markdown("### 🏢 Ecossistema ERP SAP & Corporativo")
        df_k_sap = df_skills[df_skills["Categoria"] == "SAP"]
        for _, row in df_k_sap.iterrows():
            st.markdown(f'<div class="skill-item"><div class="skill-name-percentage"><span>{row["Nome"]}</span><span>{row["Porcentagem"]}%</span></div><div class="skill-bar-bg"><div class="skill-bar-fill" style="width: {row["Porcentagem"]}%;"></div></div></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- ABA: MEUS PROJETOS ---
with aba_projetos:
    st.markdown("## Repositório Dinâmico de Projetos")
    st.write("Projetos inseridos e atualizados através do painel restrito administrativo.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    if not df_dados.empty:
        for index, row in df_dados.iterrows():
            st.markdown(f"""
            <div class="project-card">
                <h4 style="margin:0 0 10px 0; color:#38BDF8 !important;">🚀 {row['Título']} <small style='color:#64748B; font-size:0.8rem;'>({row['Categoria']})</small></h4>
                <p style="color:#94A3B8; font-size:0.95rem; margin-bottom:15px;">{row['Descrição']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            c_btn, c_vid = st.columns([1, 1.5])
            with c_btn:
                if pd.notna(row['Link do Processo']) and str(row['Link do Processo']).strip() != "":
                    st.link_button("🌐 Ver Repositório / Código", str(row['Link do Processo']), key=f"pub_btn_{index}")
            with c_vid:
                if pd.notna(row['Link do Vídeo']) and str(row['Link do Vídeo']).strip() != "":
                    try: st.video(str(row['Link do Vídeo']))
                    except: st.markdown(f"🎥 [Assistir Demonstração]({row['Link do Vídeo']})")
            st.markdown("<br>", unsafe_allow_html=True)
    else:
        st.info("Nenhum projeto dinâmico publicado.")

# --- ABA: CURSOS E FORMAÇÃO ---
with aba_formacao:
    st.markdown("## Formação Acadêmica Regular")
    st.markdown("""
    <div style="background:#1E293B; padding:24px; border-radius:12px; border-left:5px solid #38BDF8; margin-bottom: 25px;">
        <h4 style="margin:0; color:white; font-size:1.2rem;">Bacharelado em Tecnologia da Informação</h4>
        <span style="color:#38BDF8; font-weight:500;">Universidade Virtual do Estado de São Paulo (UNIVESP)</span>
        <p style="margin:8px 0 0 0; color:#94A3B8;">Status: <strong>Ensino Superior Completo / Graduado</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("## Certificações & Especializações de Mercado")
    cursos = [
        ("📊 Power BI Avançado", "Plataforma Udemy", "Conclusão: 31/07/2025", "Construção de arquiteturas corporativas de BI e dashboards estratégicos."),
        ("🐍 Python Avançado", "Plataforma Udemy", "Conclusão: 30/12/2025", "Estruturas de algoritmos, raspagem complexa e pipelines ETL."),
        ("🤖 Formação Profissional em Automação", "UiPath Academy de Automação e Desenvolvimento", "Conclusão: 21/04/2024", "Modelagem, testes e governança de robôs (RPA) industriais."),
        ("🏢 Fundamentos Básicos do SAP S/4HANA", "KA Solutions", "Carga Horária: 8 horas", "Arquitetura estrutural base de sistemas integrados ERP.")
    ]
    for titulo, emissor, data, desc in cursos:
        st.markdown(f"""
        <div class="course-card">
            <strong style="color:#F8FAFC; font-size:1.05rem;">{titulo}</strong><br>
            <span style="color:#38BDF8; font-size:0.9rem;">{emissor} — <small style="color:#64748B;">{data}</small></span>
            <p style="margin:6px 0 0 0; color:#94A3B8; font-size:0.9rem;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# --- PANEL CENTRAL DE ADMINISTRAÇÃO PROTEGIDO (EXIBIDO APENAS SE AUTENTICADO) ---
if st.session_state["autenticado"]:
    st.markdown("---")
    st.markdown("## 🔒 Terminal do Administrador — Gerenciamento Total")
    
    menu_adm = st.selectbox("Escolha a Base para Modificar", [
        "Projetos e Automações", 
        "Focos de Vagas (Objetivo)", 
        "Novos Conhecimentos Técnicos",
        "🖼️ Atualizar Foto de Perfil"
    ])
    
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
                nl = pd.DataFrame([{"Categoria": p_cat, "Título": p_tit, "Descrição": p_des, "Link do Processo": p_l1, "Link do Vídeo": p_l2}])
                pd.concat([df_dados, nl], ignore_index=True).to_csv(ARQUIVO_DADOS, index=False)
                st.success("Salvo com sucesso!")
                st.rerun()
                
        st.subheader("🗑️ Exclusão de Projetos")
        if not df_dados.empty:
            st.dataframe(df_dados)
            idx_ex = st.number_input("Índice para apagar:", min_value=0, max_value=len(df_dados)-1, step=1)
            if st.button("❌ Apagar Registro"):
                df_dados.drop(idx_ex).reset_index(drop=True).to_csv(ARQUIVO_DADOS, index=False)
                st.rerun()

    # 2. GERENCIAR VAGAS / FOCOS
    elif menu_adm == "Focos de Vagas (Objetivo)":
        st.subheader("📝 Inserir Novo Foco de Vaga")
        v_tit = st.text_input("Área/Vaga (Ex: Analista de Negócios)")
        v_des = st.text_area("Descrição Estratégica do Foco")
        
        if st.button("🚀 Gravar Novo Foco"):
            if v_tit and v_des:
                nl = pd.DataFrame([{"Título": v_tit, "Descrição": v_des}])
                pd.concat([df_vagas, nl], ignore_index=True).to_csv(ARQUIVO_VAGAS, index=False)
                st.success("Foco Adicionado!")
                st.rerun()
                
        st.subheader("🗑️ Remover Focos Existentes")
        st.dataframe(df_vagas)
        idx_ex = st.number_input("Índice do foco para apagar:", min_value=0, max_value=len(df_vagas)-1, step=1)
        if st.button("❌ Apagar Foco"):
            df_vagas.drop(idx_ex).reset_index(drop=True).to_csv(ARQUIVO_VAGAS, index=False)
            st.rerun()

    # 3. GERENCIAR CONHECIMENTOS
    elif menu_adm == "Novos Conhecimentos Técnicos":
        st.subheader("📝 Inserir Nova Skill")
        s_cat = st.selectbox("Categoria", ["Dados", "RPA", "SAP"])
        s_nom = st.text_input("Nome do Conhecimento (Ex: Apache Airflow)")
        s_pct = st.slider("Porcentagem de Domínio", 0, 100, 80)
        
        if st.button("🚀 Gravar Skill"):
            if s_nom:
                nl = pd.DataFrame([{"Categoria": s_cat, "Nome": s_nom, "Porcentagem": s_pct}])
                pd.concat([df_skills, nl], ignore_index=True).to_csv(ARQUIVO_SKILLS, index=False)
                st.success("Skill Adicionada!")
                st.rerun()
                
        st.subheader("🗑️ Remover Skills")
        st.dataframe(df_skills)
        idx_ex = st.number_input("Índice da skill para apagar:", min_value=0, max_value=len(df_skills)-1, step=1)
        if st.button("❌ Apagar Skill"):
            df_skills.drop(idx_ex).reset_index(drop=True).to_csv(ARQUIVO_SKILLS, index=False)
            st.rerun()

    # 4. ATUALIZAR FOTO DE PERFIL DIRETO PELO SITE
    elif menu_adm == "🖼️ Atualizar Foto de Perfil":
        st.subheader("Substituir Imagem do Perfil")
        st.write("Selecione sua foto profissional do computador. Ela será renomeada e configurada automaticamente.")
        
        foto_carregada = st.file_uploader("Escolha um arquivo de imagem", type=["jpg", "jpeg", "png"])
        
        if foto_carregada is not None:
            # Mostra um preview temporário para referência
            st.image(foto_carregada, width=200, caption="Pré-visualização do arquivo selecionado")
            
            if st.button("💾 Aplicar Nova Imagem ao Perfil", type="primary"):
                try:
                    # Remove arquivos antigos de imagens para evitar conflito com glob
                    extensoes_limpar = ["*.jpg", "*.jpeg", "*.png"]
                    for ext in extensoes_limpar:
                        for arq_antigo in glob.glob(ext):
                            if arq_antigo != "dados_portfolio.csv" and arq_antigo != "dados_vagas.csv" and arq_antigo != "dados_skills.csv":
                                os.remove(arq_antigo)
                                
                    # Salva o novo arquivo
                    nome_padrao_foto = "Foto perfil Matheus.jpg"
                    with open(nome_padrao_foto, "wb") as f:
                        f.write(foto_carregada.getbuffer())
                        
                    st.success("✨ Imagem atualizada com sucesso! Recarregando a interface...")
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao salvar arquivo: {e}")
