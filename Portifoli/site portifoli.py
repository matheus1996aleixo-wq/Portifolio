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

# --- 5. CABEÇALHO DO SITE ---
st.title("💻 M. Aleixo TI")
st.markdown("<p style='font-size: 1.2rem; color: #94A3B8; max-width: 900px;'>Especialista no desenvolvimento de automações (RPA), engenharia de pipelines de dados ETL, análises corporativas em Power BI e suporte técnico/funcional a ecossistemas ERP SAP.</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

aba_sobre, aba_experiencias, aba_conhecimentos, aba_projetos, aba_formacao = st.tabs([
    "👤 Objetivo & Foco", "💼 Trajetória Profissional", "🧠 Conhecimentos Técnicos", "🚀 Meus Projetos", "📚 Cursos e Formação"
])

# (Rederizações das abas normais omitidas aqui para manter o foco no painel, continuam iguais no seu sistema)

# --- PAINEL CENTRAL DE ADMINISTRAÇÃO PROTEGIDO ---
if st.session_state["autenticado"]:
    st.markdown("---")
    st.markdown("## 🔒 Terminal do Administrador — Gerenciamento Total")
    
    menu_adm = st.selectbox("Escolha a Base para Modificar", [
        "Projetos e Automações", 
        "Focos de Vagas (Objetivo)", 
        "Novos Conhecimentos Técnicos",
        "Especializações e Cursos",
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
                sincronizar_com_github(f"Painel Admin: Adicionado projeto '{p_tit}'")
                st.success("Salvo com sucesso!")
                st.rerun()
                
        st.subheader("🗑️ Exclusão de Projetos")
        if not df_dados.empty:
            item_selecionado = None
            st.write("Marque o item abaixo na lista que deseja excluir:")
            
            # Cria caixas de seleção na frente do nome de cada item
            for idx, row in df_dados.iterrows():
                if st.checkbox(f"Apagar: **{row['Título']}** ({row['Categoria']})", key=f"del_proj_{idx}"):
                    item_selecionado = idx
            
            if item_selecionado is not None:
                if st.button("❌ Confirmar e Apagar Projeto", type="primary"):
                    titulo_removido = df_dados.loc[item_selecionado, 'Título']
                    df_dados.drop(item_selecionado).reset_index(drop=True).to_csv(ARQUIVO_DADOS, index=False)
                    sincronizar_com_github(f"Painel Admin: Removido projeto '{titulo_removido}'")
                    st.success(f"'{titulo_removido}' apagado com sucesso!")
                    st.rerun()
            else:
                st.info("Selecione uma caixa acima para liberar o botão de exclusão.")

    # 2. GERENCIAR VAGAS / FOCOS
    elif menu_adm == "Focos de Vagas (Objetivo)":
        st.subheader("📝 Inserir Novo Foco de Vaga")
        v_tit = st.text_input("Área/Vaga")
        v_des = st.text_area("Descrição Estratégica")
        
        if st.button("🚀 Gravar Novo Foco"):
            if v_tit and v_des:
                nl = pd.DataFrame([{"Título": v_tit, "Descrição": v_des}])
                pd.concat([df_vagas, nl], ignore_index=True).to_csv(ARQUIVO_VAGAS, index=False)
                sincronizar_com_github(f"Painel Admin: Adicionado foco de vaga '{v_tit}'")
                st.success("Foco Adicionado!")
                st.rerun()
                
        st.subheader("🗑️ Remover Focos Existentes")
        if not df_vagas.empty:
            item_selecionado = None
            for idx, row in df_vagas.iterrows():
                if st.checkbox(f"Apagar: **{row['Título']}**", key=f"del_vaga_{idx}"):
                    item_selecionado = idx
                    
            if item_selecionado is not None:
                if st.button("❌ Confirmar e Apagar Foco", type="primary"):
                    foco_removido = df_vagas.loc[item_selecionado, 'Título']
                    df_vagas.drop(item_selecionado).reset_index(drop=True).to_csv(ARQUIVO_VAGAS, index=False)
                    sincronizar_com_github(f"Painel Admin: Removido foco de vaga '{foco_removido}'")
                    st.success(f"'{foco_removido}' apagado!")
                    st.rerun()
            else:
                st.info("Selecione uma vaga acima para excluir.")

    # 3. GERENCIAR CONHECIMENTOS
    elif menu_adm == "Novos Conhecimentos Técnicos":
        st.subheader("📝 Inserir Nova Skill")
        s_cat = st.selectbox("Categoria", ["Dados", "RPA", "SAP"])
        s_nom = st.text_input("Nome do Conhecimento")
        s_pct = st.slider("Porcentagem de Domínio", 0, 100, 80)
        
        if st.button("🚀 Gravar Skill"):
            if s_nom:
                nl = pd.DataFrame([{"Categoria": s_cat, "Nome": s_nom, "Porcentagem": s_pct}])
                pd.concat([df_skills, nl], ignore_index=True).to_csv(ARQUIVO_SKILLS, index=False)
                sincronizar_com_github(f"Painel Admin: Adicionada skill '{s_nom}'")
                st.success("Skill Adicionada!")
                st.rerun()
                
        st.subheader("🗑️ Remover Skills")
        if not df_skills.empty:
            item_selecionado = None
            for idx, row in df_skills.iterrows():
                if st.checkbox(f"Apagar: **{row['Nome']}** ({row['Categoria']} - {row['Porcentagem']}%)", key=f"del_skill_{idx}"):
                    item_selecionado = idx
                    
            if item_selecionado is not None:
                if st.button("❌ Confirmar e Apagar Skill", type="primary"):
                    skill_removida = df_skills.loc[item_selecionado, 'Nome']
                    df_skills.drop(item_selecionado).reset_index(drop=True).to_csv(ARQUIVO_SKILLS, index=False)
                    sincronizar_com_github(f"Painel Admin: Removida skill '{skill_removida}'")
                    st.success(f"'{skill_removida}' apagada!")
                    st.rerun()
            else:
                st.info("Selecione uma skill acima para excluir.")

    # 4. GERENCIAR CURSOS E CERTIFICAÇÕES
    elif menu_adm == "Especializações e Cursos":
        st.subheader("📝 Adicionar Novo Curso")
        c_tit = st.text_input("Título do Curso")
        c_emi = st.text_input("Emissor / Instituição")
        c_dat = st.text_input("Data de Conclusão")
        c_des = st.text_area("Descrição")
        
        if st.button("🚀 Gravar Novo Curso"):
            if c_tit and c_emi:
                nl = pd.DataFrame([{"Título": c_tit, "Emissor": c_emi, "Data": c_dat, "Descrição": c_des}])
                pd.concat([df_cursos, nl], ignore_index=True).to_csv(ARQUIVO_CURSOS, index=False)
                sincronizar_com_github(f"Painel Admin: Adicionado curso '{c_tit}'")
                st.success("Curso salvo!")
                st.rerun()
                
        st.subheader("🗑️ Remover Cursos Existentes")
        if not df_cursos.empty:
            item_selecionado = None
            for idx, row in df_cursos.iterrows():
                if st.checkbox(f"Apagar: **{row['Título']}** ({row['Emissor']})", key=f"del_curso_{idx}"):
                    item_selecionado = idx
                    
            if item_selecionado is not None:
                if st.button("❌ Confirmar e Apagar Curso", type="primary"):
                    curso_removido = df_cursos.loc[item_selecionado, 'Título']
                    df_cursos.drop(item_selecionado).reset_index(drop=True).to_csv(ARQUIVO_CURSOS, index=False)
                    sincronizar_com_github(f"Painel Admin: Removido curso '{curso_removido}'")
                    st.success(f"'{curso_removido}' apagado!")
                    st.rerun()
            else:
                st.info("Selecione um curso acima para excluir.")

    # 5. ATUALIZAR FOTO DE PERFIL
    elif menu_adm == "🖼️ Atualizar Foto de Perfil":
        st.subheader("Substituir Imagem do Perfil")
        foto_carregada = st.file_uploader("Escolha um arquivo de imagem", type=["jpg", "jpeg", "png"])
        if foto_carregada is not None:
            st.image(foto_carregada, width=200)
            if st.button("💾 Aplicar Nova Imagem ao Perfil", type="primary"):
                try:
                    extensoes_limpar = ["*.jpg", "*.jpeg", "*.png"]
                    for ext in extensoes_limpar:
                        for arq_antigo in glob.glob(ext):
                            if arq_antigo not in [ARQUIVO_DADOS, ARQUIVO_VAGAS, ARQUIVO_SKILLS, ARQUIVO_CURSOS]:
                                os.remove(arq_antigo)
                    nome_padrao_foto = "Foto perfil Matheus.jpg"
                    with open(nome_padrao_foto, "wb") as f:
                        f.write(foto_carregada.getbuffer())
                    sincronizar_com_github("Painel Admin: Atualização da foto de perfil profissional")
                    st.success("Imagem atualizada!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao salvar arquivo: {e}")
