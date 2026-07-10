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
ARQUIVO_EXPERIENCIAS = "dados_experiencias.csv"

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

if not os.path.exists(ARQUIVO_EXPERIENCIAS):
    df_exp_init = pd.DataFrame([
        {"Cargo": "Professor de Tecnologia e Matemática", "Empresa": "Secretaria da Educação | Campo Limpo Paulista - SP", "Periodo": "Outubro 2025 – Fevereiro 2026"},
        {"Cargo": "Consultor SAP Jr", "Empresa": "Stefanini | Atuação Remota", "Periodo": "Escopo de Projeto"},
        {"Cargo": "Estagiário de Tecnologia da Informação", "Empresa": "Continental Automotive | Várzea Paulista - SP", "Periodo": "Junho 2023 – Fevereiro 2025"}
    ])
    df_exp_init.to_csv(ARQUIVO_EXPERIENCIAS, index=False)


# --- FUNÇÃO AUTOMÁTICA DE COMMIT E PUSH NO GIT ---
def sincronizar_com_github(mensagem_commit="Painel Admin: Sincronização automática de dados"):
    """Adiciona as alterações, commita e envia diretamente ao GitHub remoto."""
    try:
        subprocess.run(["git", "add", ARQUIVO_DADOS, ARQUIVO_VAGAS, ARQUIVO_SKILLS, ARQUIVO_CURSOS, ARQUIVO_EXPERIENCIAS, "*.jpg", "*.png", "*.jpeg"], check=True)
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
2. Consultor SAP Jr - Stefanini | Atuação Remota (Escopo de Projeto)
3. Estagiário de Tecnologia da Informação - Continental Automotive | Várzea Paulista - SP (Junho 2023 – Fevereiro 2025)"""

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
    .project-card { background: #1E293B; border: 1px solid #334155; border-radius: 12px; padding: 24px; margin-bottom: 20px; transition: transform 0.3s ease, border-color 0.3s ease; }
    .project-card:hover { transform: translateY(-4px); border-color: #38BDF8; box-shadow: 0 10px 20px -10px rgba(56, 189, 248, 0.2); }
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

# --- CARREGAMENTO REATIVO DAS CINCO BASES ---
df_dados = pd.read_csv(ARQUIVO_DADOS)
df_vagas = pd.read_csv(ARQUIVO_VAGAS)
df_skills = pd.read_csv(ARQUIVO_SKILLS)
df_cursos = pd.read_csv(ARQUIVO_CURSOS)
df_experiencias = pd.read_csv(ARQUIVO_EXPERIENCIAS)

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
    st.markdown("**📍 Localização:** Várzea Paulista - SP")
    st.markdown("**✉️ E-mail:** [matheus.aleixo2020@gmail.com](mailto:matheus.aleixo2020@gmail.com)")
    st.markdown("**🔗 LinkedIn:** [Acessar Perfil](https://www.linkedin.com/in/matheus-aleixo-299a05247)")
    
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
            
            st.markdown("---")
            st.markdown("### 🖼️ Foto de Perfil")
            foto_carregada = st.file_uploader("Substituir imagem", type=["jpg", "jpeg", "png"], key="side_upload_foto")
            if foto_carregada is not None:
                st.image(foto_carregada, width=100)
                if st.button("💾 Aplicar Foto", type="primary", key="btn_save_photo"):
                    try:
                        for ext in ["*.jpg", "*.jpeg", "*.png"]:
                            for arq_antigo in glob.glob(ext):
                                if arq_antigo not in [ARQUIVO_DADOS, ARQUIVO_VAGAS, ARQUIVO_SKILLS, ARQUIVO_CURSOS, ARQUIVO_EXPERIENCIAS]:
                                    os.remove(arq_antigo)
                        nome_padrao_foto = "Foto perfil Matheus.jpg"
                        with open(nome_padrao_foto, "wb") as f:
                            f.write(foto_carregada.getbuffer())
                        sincronizar_com_github("Painel Admin: Atualização da foto de perfil profissional")
                        st.success("Imagem updated!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Erro: {e}")

# --- 5. CABEÇALHO DO SITE ---
st.title("💻 M. Aleixo TI")
st.markdown("<p style='font-size: 1.2rem; color: #94A3B8; max-width: 900px;'>Especialista no desenvolvimento de automações (RPA), engenharia de pipelines de dados ETL, análises corporativas em Power BI e suporte técnico/funcional a ecossistemas ERP SAP.</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

aba_sobre, aba_experiencias, aba_conhecimentos, aba_projetos, aba_formacao = st.tabs([
    "👤 Objetivo & Foco", "💼 Trajetória Profissional", "🧠 Conhecimentos Técnicos", "🚀 Meus Projetos", "📚 Cursos e Formação"
])

# ==========================================
# --- ABA 1: OBJETIVO & FOCO ---
# ==========================================
with aba_sobre:
    st.markdown("## Perfil e Objetivo Estratégico")
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

    if st.session_state["autenticado"]:
        st.markdown("<br><hr><h2>🔒 Gerenciar Focos de Vagas (Objetivo)</h2>", unsafe_allow_html=True)
        col_v1, col_v2 = st.columns([1, 2])
        with col_v1:
            st.subheader("📝 Inserir Novo Foco")
            v_tit = st.text_input("Área/Vaga", key="aba_vaga_tit")
            v_des = st.text_area("Descrição Estratégica", key="aba_vaga_des")
            if st.button("🚀 Gravar Novo Foco", key="aba_vaga_save"):
                if v_tit and v_des:
                    nl = pd.DataFrame([{"Título": v_tit, "Descrição": v_des}])
                    pd.concat([df_vagas, nl], ignore_index=True).to_csv(ARQUIVO_VAGAS, index=False)
                    sincronizar_com_github(f"Painel Admin: Adicionado foco de vaga '{v_tit}'")
                    st.success("Foco Adicionado!")
                    st.rerun()
        with col_v2:
            st.subheader("🗑️ Remover Focos Existentes")
            if not df_vagas.empty:
                item_vaga_sel = None
                for idx, row in df_vagas.iterrows():
                    if st.checkbox(f"Apagar Foco: **{row['Título']}**", key=f"aba_del_vaga_{idx}"):
                        item_vaga_sel = idx
                if item_vaga_sel is not None:
                    if st.button("❌ Confirmar Exclusão de Foco", type="primary", key="aba_vaga_del_btn"):
                        foco_removido = df_vagas.loc[item_vaga_sel, 'Título']
                        df_vagas.drop(item_vaga_sel).reset_index(drop=True).to_csv(ARQUIVO_VAGAS, index=False)
                        sincronizar_com_github(f"Painel Admin: Removido foco de vaga '{foco_removido}'")
                        st.success("Foco excluído!")
                        st.rerun()

# ==========================================
# --- ABA 2: TRAJETÓRIA PROFISSIONAL ---
# ==========================================
with aba_experiencias:
    st.markdown("## Histórico de Carreira")
    
    if not df_experiencias.empty:
        for idx, row in df_experiencias.iterrows():
            st.markdown(f"""
            <div class="timeline-item">
                <h3 style="margin:0; color:#F8FAFC;">{row['Cargo']}</h3>
                <span style="color:#38BDF8; font-size:0.95rem; font-weight:600;">{row['Empresa']}</span><br>
                <span style="color:#64748B; font-size:0.85rem; font-weight:500;">{row['Periodo']}</span>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Nenhuma experiência profissional cadastrada.")

    # CONTEXTO GERENCIAL PARA EXPERIÊNCIAS
    if st.session_state["autenticado"]:
        st.markdown("<br><hr><h2>🔒 Gerenciar Histórico de Carreira</h2>", unsafe_allow_html=True)
        col_e1, col_e2 = st.columns([1, 2])
        with col_e1:
            st.subheader("📝 Inserir Nova Experiência")
            e_car = st.text_input("Cargo", key="aba_exp_car")
            e_emp = st.text_input("Empresa / Instituição", key="aba_exp_emp")
            e_per = st.text_input("Período (Ex: Junho 2023 – Atual)", key="aba_exp_per")
            if st.button("🚀 Gravar Experiência", key="aba_exp_save"):
                if e_car and e_emp:
                    nl = pd.DataFrame([{"Cargo": e_car, "Empresa": e_emp, "Periodo": e_per}])
                    pd.concat([df_experiencias, nl], ignore_index=True).to_csv(ARQUIVO_EXPERIENCIAS, index=False)
                    sincronizar_com_github(f"Painel Admin: Adicionada experiência '{e_car}' na '{e_emp}'")
                    st.success("Experiência cadastrada!")
                    st.rerun()
        with col_e2:
            st.subheader("🗑️ Remover Experiências")
            if not df_experiencias.empty:
                item_exp_sel = None
                for idx, row in df_experiencias.iterrows():
                    if st.checkbox(f"Apagar: **{row['Cargo']}** ({row['Empresa']})", key=f"aba_del_exp_{idx}"):
                        item_exp_sel = idx
                if item_exp_sel is not None:
                    if st.button("❌ Confirmar Exclusão de Experiência", type="primary", key="aba_exp_del_btn"):
                        cargo_removido = df_experiencias.loc[item_exp_sel, 'Cargo']
                        df_experiencias.drop(item_exp_sel).reset_index(drop=True).to_csv(ARQUIVO_EXPERIENCIAS, index=False)
                        sincronizar_com_github(f"Painel Admin: Removida experiência '{cargo_removido}'")
                        st.success("Experiência removida!")
                        st.rerun()

# ==========================================
# --- ABA 3: CONHECIMENTOS TÉCNICOS ---
# ==========================================
with aba_conhecimentos:
    st.markdown("## Hard Skills & Matriz de Competências")
    
    categorias_skills = ["Dados", "RPA", "SAP"]
    colunas_skills = st.columns(3)
    
    for i, cat in enumerate(categorias_skills):
        with colunas_skills[i]:
            st.markdown(f'<div class="skill-section-card"><h3>💡 {cat}</h3>', unsafe_allow_html=True)
            df_filtrado = df_skills[df_skills["Categoria"] == cat]
            for _, row in df_filtrado.iterrows():
                st.markdown(f"""
                <div class="skill-item">
                    <div class="skill-name-percentage">
                        <span>{row['Nome']}</span>
                        <span>{row['Porcentagem']}%</span>
                    </div>
                    <div class="skill-bar-bg">
                        <div class="skill-bar-fill" style="width: {row['Porcentagem']}%"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state["autenticado"]:
        st.markdown("<br><hr><h2>🔒 Gerenciar Novos Conhecimentos Técnicos</h2>", unsafe_allow_html=True)
        col_s1, col_s2 = st.columns([1, 2])
        with col_s1:
            st.subheader("📝 Inserir Nova Skill")
            s_cat = st.selectbox("Categoria", ["Dados", "RPA", "SAP"], key="aba_skill_cat")
            s_nom = st.text_input("Nome do Conhecimento", key="aba_skill_nom")
            s_pct = st.slider("Porcentagem de Domínio", 0, 100, 80, key="aba_skill_pct")
            if st.button("🚀 Gravar Skill", key="aba_skill_save"):
                if s_nom:
                    nl = pd.DataFrame([{"Categoria": s_cat, "Nome": s_nom, "Porcentagem": s_pct}])
                    pd.concat([df_skills, nl], ignore_index=True).to_csv(ARQUIVO_SKILLS, index=False)
                    sincronizar_com_github(f"Painel Admin: Adicionada skill '{s_nom}'")
                    st.success("Skill Adicionada!")
                    st.rerun()
        with col_s2:
            st.subheader("🗑️ Remover Skills")
            if not df_skills.empty:
                item_skill_sel = None
                for idx, row in df_skills.iterrows():
                    if st.checkbox(f"Apagar: **{row['Nome']}** ({row['Categoria']})", key=f"aba_del_skill_{idx}"):
                        item_skill_sel = idx
                if item_skill_sel is not None:
                    if st.button("❌ Confirmar Exclusão de Skill", type="primary", key="aba_skill_del_btn"):
                        skill_removida = df_skills.loc[item_skill_sel, 'Nome']
                        df_skills.drop(item_skill_sel).reset_index(drop=True).to_csv(ARQUIVO_SKILLS, index=False)
                        sincronizar_com_github(f"Painel Admin: Removida skill '{skill_removida}'")
                        st.success("Skill removida!")
                        st.rerun()

# ==========================================
# --- ABA 4: MEUS PROJETOS ---
# ==========================================
with aba_projetos:
    st.markdown("## Repositório Dinâmico de Projetos")
    if not df_dados.empty:
        for index, row in df_dados.iterrows():
            with st.container():
                st.markdown(f"""
                <div class="project-card">
                    <h3 style="margin-top:0;">🚀 {row['Título']} <span style="font-size:0.8rem; background:#0EA5E9; padding:4px 8px; border-radius:12px; color:white; vertical-align:middle; margin-left:10px;">{row['Categoria']}</span></h3>
                    <p style="color:#94A3B8; font-size:0.95rem; line-height:1.6;">{row['Descrição']}</p>
                </div>
                """, unsafe_allow_html=True)
                col_btn1, col_btn2, _ = st.columns([1, 1, 4])
                if pd.notna(row['Link do Processo']) and row['Link do Processo'] != "":
                    col_btn1.link_button("🔗 Código Fonte (GitHub)", row['Link do Processo'], use_container_width=True)
                if pd.notna(row['Link do Vídeo']) and row['Link do Vídeo'] != "":
                    col_btn2.link_button("🎥 Demonstração em Vídeo", row['Link do Vídeo'], use_container_width=True)
                st.markdown("<br>", unsafe_allow_html=True)
    else:
        st.info("Nenhum projeto cadastrado no sistema.")

    if st.session_state["autenticado"]:
        st.markdown("<br><hr><h2>🔒 Gerenciar Projetos e Automações</h2>", unsafe_allow_html=True)
        col_p1, col_p2 = st.columns([1, 2])
        with col_p1:
            st.subheader("📝 Adicionar Novo Projeto")
            p_cat = st.selectbox("Categoria", ["Projeto", "Automação"], key="aba_proj_cat")
            p_tit = st.text_input("Título", key="aba_proj_tit")
            p_des = st.text_area("Descrição", key="aba_proj_des")
            p_l1 = st.text_input("Link do Repositório (GitHub)", key="aba_proj_l1")
            p_l2 = st.text_input("Link do Vídeo", key="aba_proj_l2")
            if st.button("🚀 Gravar Projeto", key="aba_proj_save"):
                if p_tit and p_des:
                    nl = pd.DataFrame([{"Categoria": p_cat, "Título": p_tit, "Descrição": p_des, "Link do Processo": p_l1, "Link do Vídeo": p_l2}])
                    pd.concat([df_dados, nl], ignore_index=True).to_csv(ARQUIVO_DADOS, index=False)
                    sincronizar_com_github(f"Painel Admin: Adicionado projeto '{p_tit}'")
                    st.success("Projeto salvo!")
                    st.rerun()
        with col_p2:
            st.subheader("🗑️ Exclusão de Projetos")
            if not df_dados.empty:
                item_proj_sel = None
                for idx, row in df_dados.iterrows():
                    if st.checkbox(f"Apagar: **{row['Título']}** ({row['Categoria']})", key=f"aba_del_proj_{idx}"):
                        item_proj_sel = idx
                if item_proj_sel is not None:
                    if st.button("❌ Confirmar e Apagar Projeto", type="primary", key="aba_proj_del_btn"):
                        titulo_removido = df_dados.loc[item_proj_sel, 'Título']
                        df_dados.drop(item_proj_sel).reset_index(drop=True).to_csv(ARQUIVO_DADOS, index=False)
                        sincronizar_com_github(f"Painel Admin: Removido projeto '{titulo_removido}'")
                        st.success("Projeto removido!")
                        st.rerun()

# ==========================================
# --- ABA 5: CURSOS E FORMAÇÃO ---
# ==========================================
with aba_formacao:
    st.markdown("## Certificações & Especializações de Mercado")
    if not df_cursos.empty:
        for _, row in df_cursos.iterrows():
            st.markdown(f"""
            <div class="course-card">
                <h3 style="margin:0; font-size:1.1rem; color:#F8FAFC;">{row['Título']}</h3>
                <span style="color:#38BDF8; font-size:0.9rem; font-weight:500;">{row['Emissor']}</span> | 
                <span style="color:#64748B; font-size:0.85rem;">{row['Data']}</span>
                <p style="margin-top:8px; margin-bottom:0; color:#94A3B8; font-size:0.9rem;">{row['Descrição']}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Nenhuma certificação listada.")

    if st.session_state["autenticado"]:
        st.markdown("<br><hr><h2>🔒 Gerenciar Especializações e Cursos</h2>", unsafe_allow_html=True)
        col_c1, col_c2 = st.columns([1, 2])
        with col_c1:
            st.subheader("📝 Adicionar Novo Curso")
            c_tit = st.text_input("Título do Curso", key="aba_curso_tit")
            c_emi = st.text_input("Emissor / Instituição", key="aba_curso_emi")
            c_dat = st.text_input("Data de Conclusão", key="aba_curso_dat")
            c_des = st.text_area("Descrição", key="aba_curso_des")
            if st.button("🚀 Gravar Novo Curso", key="aba_curso_save"):
                if c_tit and c_emi:
                    nl = pd.DataFrame([{"Título": c_tit, "Emissor": c_emi, "Data": c_dat, "Descrição": c_des}])
                    pd.concat([df_cursos, nl], ignore_index=True).to_csv(ARQUIVO_CURSOS, index=False)
                    sincronizar_com_github(f"Painel Admin: Adicionado curso '{c_tit}'")
                    st.success("Curso salvo!")
                    st.rerun()
        with col_c2:
            st.subheader("🗑️ Remover Cursos Existentes")
            if not df_cursos.empty:
                item_curso_sel = None
                for idx, row in df_cursos.iterrows():
                    if st.checkbox(f"Apagar Curso: **{row['Título']}** ({row['Emissor']})", key=f"aba_del_curso_{idx}"):
                        item_curso_sel = idx
                if item_curso_sel is not None:
                    if st.button("❌ Confirmar e Apagar Curso", type="primary", key="aba_curso_del_btn"):
                        curso_removido = df_cursos.loc[item_curso_sel, 'Título']
                        df_cursos.drop(item_curso_sel).reset_index(drop=True).to_csv(ARQUIVO_CURSOS, index=False)
                        sincronizar_com_github(f"Painel Admin: Removido curso '{curso_removido}'")
                        st.success("Curso deletado!")
                        st.rerun()
