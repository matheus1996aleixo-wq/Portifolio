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

# Credenciais administrativas seguras (Conforme o seu GitHub/Streamlit Secrets)
try:
    USUARIO_ADMIN = st.secrets["USUARIO_ADMINPORT"]
    SENHA_ADMIN = st.secrets["MINHA_SENHAPORT"]
except Exception:
    # Caso rode localmente (Localhost), usará estas credenciais padrão:
    USUARIO_ADMIN = "matheus"
    SENHA_ADMIN = "sua_senha_aqui"

# Arquivos locais
ARQUIVO_DADOS = "dados_portfolio.csv"
ARQUIVO_VAGAS = "dados_vagas.csv"
ARQUIVO_SKILLS = "dados_skills.csv"
ARQUIVO_EDU = "dados_educacao.csv"
NOME_FOTO = "Foto_Perfil_Matheus.jpg"

# Inicialização de bases com as colunas adequadas
for arquivo, cols in [
    (ARQUIVO_DADOS, ["Categoria", "Título", "Descrição", "Link do Processo", "Link do Vídeo"]),
    (ARQUIVO_VAGAS, ["Título", "Descrição"]),
    (ARQUIVO_SKILLS, ["Categoria", "Nome", "Porcentagem"]),
    (ARQUIVO_EDU, ["Instituição", "Curso_Formacao", "Status", "Conhecimentos"])
]:
    if not os.path.exists(arquivo):
        pd.DataFrame(columns=cols).to_csv(arquivo, index=False)

# Função imagem
def obter_imagem_base64():
    if os.path.exists(NOME_FOTO):
        try:
            with open(NOME_FOTO, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode()
        except Exception:
            return None
    return None

foto_base64 = obter_imagem_base64()

# CSS Premium Customizado
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
    h2, h3 { color: #38BDF8 !important; font-weight: 600; margin-bottom: 15px; }
    
    .custom-card {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
        border: 1px solid #334155;
        border-left: 5px solid #38BDF8;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
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
                # Validação corrigida utilizando as variáveis globais padronizadas
                if input_user == USUARIO_ADMIN and input_pass == SENHA_ADMIN:
                    st.session_state["autenticado"] = True
                    st.rerun()
                else:
                    st.error("Acesso negado. Verifique os dados introduzidos.")
        else:
            st.write("🟢 Modo Editor Ativo")
            if st.button("🔒 Logoff", type="primary"):
                st.session_state["autenticado"] = False
                st.rerun()

# Cabeçalho principal
st.title("💻 M. Aleixo TI")
st.markdown("<p style='font-size: 1.2rem; color: #94A3B8; text-align:center;'>Especialista em RPA, ETL, Power BI e suporte SAP.</p>", unsafe_allow_html=True)

# Tabs / Abas
aba_objetivo, aba_experiencias, aba_conhecimentos, aba_projetos, aba_formacao = st.tabs([
    "👤 Objetivo & Foco", "💼 Experiências", "🧠 Conhecimentos", "🚀 Projetos", "📚 Formação"
])

# 1. ABA OBJETIVO & FOCO
with aba_objetivo:
    st.markdown("### 🎯 Objetivo Profissional")
    st.markdown("""
    <div class="custom-card">
        <p style='font-size:1.15rem; margin:0; line-height:1.6;'>
            Atuar na área de Tecnologia da Informação como <b>Analista de Sistemas</b> ou <b>Desenvolvedor</b>, 
            visando evoluir profissionalmente, desenvolver novas competências e agregar valor estratégico à organização.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    df_vagas = pd.read_csv(ARQUIVO_VAGAS)
    if not df_vagas.empty:
        st.markdown("#### 🎯 Alvos de Atuação Cadastrados")
        for idx, row in df_vagas.iterrows():
            st.markdown(f"""
            <div class="custom-card" style="border-left-color: #A855F7;">
                <h4 style="margin:0 0 8px 0; color:#38BDF8;">✨ {row['Título']}</h4>
                <p style="margin:0; color:#94A3B8;">{row['Descrição']}</p>
            </div>
            """, unsafe_allow_html=True)

# 2. ABA EXPERIÊNCIAS
with aba_experiencias:
    st.markdown("### 💼 Trajetória Profissional")
    experiencias = [
        {"cargo": "Professor de Tecnologia e Matemática", "empresa": "Secretaria da Educação", "periodo": "2025–2026", "desc": "Ensino Fundamental II e Médio, foco em desenvolvimento de competências digitais, raciocínio lógico e resolução de problemas matemáticos utilizando ferramentas tecnológicas."},
        {"cargo": "Consultor SAP Jr", "empresa": "Stefanini", "periodo": "Remoto", "desc": "Atuação no suporte funcional do sistema SAP S/4HANA focado diretamente na resolução de chamados e melhorias nos módulos FI, CO e SD."},
        {"cargo": "Estagiário de TI", "empresa": "Continental Automotive", "periodo": "2023–2025", "desc": "Suporte a usuários no ecossistema SAP ECC, participação direta no projeto global de migração SPIRIT e manutenção de regras da solução fiscal complementar Guepardo."}
    ]
    
    for exp in experiencias:
        st.markdown(f"""
        <div class="custom-card">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                <h4 style="margin: 0; color: #F8FAFC;">🚀 {exp['cargo']}</h4>
                <span style="background: #334155; padding: 4px 10px; border-radius: 20px; font-size: 0.85rem; color: #38BDF8; font-weight: bold;">⏱️ {exp['periodo']}</span>
            </div>
            <p style="margin: 5px 0 10px 0; font-weight: 500; color: #38BDF8;">🏢 {exp['empresa']}</p>
            <p style="margin: 0; color: #94A3B8; font-size: 0.95rem; line-height: 1.5;">{exp['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

# 3. ABA CONHECIMENTOS
with aba_conhecimentos:
    st.markdown("### 🧠 Hard Skills & Nível de Domínio")
    
    df_skills = pd.read_csv(ARQUIVO_SKILLS)
    if df_skills.empty:
        skills_padrao = [
            {"Categoria": "Dados", "Nome": "Power BI (Dashboards Gerenciais & Modelagem DAX)", "Porcentagem": 90},
            {"Categoria": "Dados", "Nome": "Bancos de Dados Relacionais (PostgreSQL)", "Porcentagem": 75},
            {"Categoria": "Dados", "Nome": "Pipelines ETL & Manipulação (JSON, XML, HTML)", "Porcentagem": 90},
            {"Categoria": "RPA", "Nome": "Python Avançado (Scrapy, Playwright, BeautifulSoup)", "Porcentagem": 95},
            {"Categoria": "RPA", "Nome": "Plataforma de Robótica UiPath", "Porcentagem": 85},
            {"Categoria": "SAP", "Nome": "Suporte Funcional SAP (ECC e S/4HANA)", "Porcentagem": 90},
            {"Categoria": "SAP", "Nome": "Módulos de Processos (FI, CO, SD, MM, Basis)", "Porcentagem": 80},
            {"Categoria": "SAP", "Nome": "Solução Fiscal Integrada Guepardo", "Porcentagem": 85}
        ]
        df_skills = pd.DataFrame(skills_padrao)
        df_skills.to_csv(ARQUIVO_SKILLS, index=False)
        
    categorias = df_skills["Categoria"].unique()
    for cat in categorias:
        st.markdown(f"#### 🛠️ Categoria: {cat}")
        df_filtrado = df_skills[df_skills["Categoria"] == cat]
        
        cols_skill = st.columns(2)
        for idx, (_, row) in enumerate(df_filtrado.iterrows()):
            col_alvo = cols_skill[idx % 2]
            with col_alvo:
                nome_skill = row['Nome']
                
                emoji_adicional = ""
                if "python" in nome_skill.lower():
                    emoji_adicional = " 🐍"
                elif "banco de dados" in nome_skill.lower() or "power bi" in nome_skill.lower():
                    emoji_adicional = " 📊"
                elif "rpa" in nome_skill.lower() or "automação" in nome_skill.lower() or "automacao" in nome_skill.lower():
                    emoji_adicional = " 🤖"
                
                st.markdown(f"**{nome_skill}{emoji_adicional}** ({row['Porcentagem']}%)")
                st.progress(int(row['Porcentagem']) / 100)
        st.markdown("<br>", unsafe_allow_html=True)

# 4. ABA PROJETOS
with aba_projetos:
    st.markdown("### 🚀 Projetos e Portfólio Técnico")
    df_dados = pd.read_csv(ARQUIVO_DADOS)
    
    if not df_dados.empty:
        for idx, row in df_dados.iterrows():
            st.markdown(f"""
            <div class="custom-card" style="border-left-color: #10B981;">
                <span style="background: #065F46; color: #34D399; padding: 2px 8px; border-radius: 4px; font-size: 0.8rem; font-weight: bold;">{row['Categoria']}</span>
                <h4 style="margin: 8px 0; color: #F8FAFC;">{row['Título']}</h4>
                <p style="color: #94A3B8; font-size: 0.95rem;">{row['Descrição']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            col_btn1, col_btn2, _ = st.columns([1, 1, 4])
            if pd.notna(row['Link do Processo']) and row['Link do Processo']:
                col_btn1.link_button("📂 Ver Repositório", row['Link do Processo'], use_container_width=True)
            if pd.notna(row['Link do Vídeo']) and row['Link do Vídeo']:
                col_btn2.link_button("🎥 Assistir Demonstração", row['Link do Vídeo'], use_container_width=True)
            st.markdown("<hr style='border-color: #334155; margin: 15px 0;'>", unsafe_allow_html=True)
    else:
        st.info("Nenhum projeto foi publicado ainda. Utilize o Painel de Controle para adicionar novos itens.")

# 5. ABA FORMAÇÃO E CURSOS
with aba_formacao:
    st.markdown("### 📚 Histórico Acadêmico e Certificações")
    df_edu = pd.read_csv(ARQUIVO_EDU)
    
    if df_edu.empty:
        exemplo_edu = [
            {"Instituição": "UNIVESP", "Curso_Formacao": "Bacharelado em Tecnologia da Informação", "Status": "Concluído", "Conhecimentos": "Desenvolvimento de Software, Banco de Dados, Engenharia de Requisitos"},
            {"Instituição": "UiPath Academy", "Curso_Formacao": "Especialização em Automação RPA", "Status": "Concluído", "Conhecimentos": "Orchestrator, Studio, REFrameWork, Atividades Avançadas"},
            {"Instituição": "KA Solutions", "Curso_Formacao": "Fundamentos básicos do Sap S/4Hana", "Status": "Concluído", "Conhecimentos": "Carga horária: 8 horas"},
            {"Instituição": "Udemy", "Curso_Formacao": "Power BI Avançado", "Status": "Concluído", "Conhecimentos": "Conclusão: 31/07/2025"},
            {"Instituição": "Udemy", "Curso_Formacao": "Python Avançado", "Status": "Concluído", "Conhecimentos": "Conclusão: 30/12/2025"}
        ]
        df_edu = pd.DataFrame(exemplo_edu)
        df_edu.to_csv(ARQUIVO_EDU, index=False)

    cols_edu = st.columns(2)
    for idx, row in df_edu.iterrows():
        col_alvo = cols_edu[idx % 2]
        with col_alvo:
            status_color = "#10B981" if row['Status'] == "Concluído" else "#F59E0B"
            st.markdown(f"""
            <div class="custom-card" style="border-left-color: #38BDF8;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <span style="background: #1E293B; border: 1px solid #334155; color: #38BDF8; padding: 2px 8px; border-radius: 4px; font-size: 0.8rem; font-weight: bold;">🏫 {row['Instituição']}</span>
                    <span style="color: {status_color}; font-size: 0.85rem; font-weight: bold;">⚡ {row['Status']}</span>
                </div>
                <h4 style="margin: 0 0 8px 0; color: #F8FAFC;">{row['Curso_Formacao']}</h4>
                <p style="margin: 0; color: #94A3B8; font-size: 0.9rem;"><b>🧠 Conhecimentos:</b> {row['Conhecimentos']}</p>
            </div>
            """, unsafe_allow_html=True)


# --- PAINEL ADMINISTRATIVO ---
if st.session_state["autenticado"]:
    st.markdown("---")
    st.markdown("## 🔒 Terminal do Administrador — Gerenciamento Total")
    st.info("💾 **Nota de Persistência:** Todas as modificações feitas neste painel salvam diretamente nos bancos de dados locais (`.csv`).")

    menu_adm = st.selectbox(
        "Escolha a Base para Modificar",
        ["Projetos e Automações", "Focos de Vagas (Objetivo)", "Novos Conhecimentos Técnicos", "📚 Formações e Cursos", "🖼️ @Atualizar Foto de Perfil"]
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
                nl = pd.DataFrame([{"Categoria": p_cat, "Título": p_tit, "Descrição": p_des, "Link do Processo": p_l1, "Link do Vídeo": p_l2}])
                pd.concat([pd.read_csv(ARQUIVO_DADOS), nl], ignore_index=True).to_csv(ARQUIVO_DADOS, index=False)
                st.success("Projeto salvo com sucesso!")
                st.rerun()

        st.subheader("🗑️ Exclusão de Projetos")
        df_dados = pd.read_csv(ARQUIVO_DADOS)
        if not df_dados.empty:
            st.dataframe(df_dados)
            idx_ex = st.number_input("Índice para apagar:", min_value=0, max_value=len(df_dados)-1, step=1)
            linha_selecionada = df_dados.iloc[[idx_ex]]
            st.markdown("**Item que será apagado:**")
            st.dataframe(linha_selecionada)
            confirmar_exclusao = st.checkbox("✅ Confirmo que selecionei a linha correta para a exclusão", key="conf_ex_dados")
            
            if st.button("❌ Apagar Registro"):
                if confirmar_exclusao:
                    df_dados.drop(idx_ex).reset_index(drop=True).to_csv(ARQUIVO_DADOS, index=False)
                    st.success("Registro removido com sucesso!")
                    st.rerun()
                else:
                    st.warning("Precisa marcar a caixa de seleção acima antes de excluir.")

    # 2. GERENCIAR VAGAS
    elif menu_adm == "Focos de Vagas (Objetivo)":
        st.subheader("📝 Inserir Novo Foco de Vaga")
        v_tit = st.text_input("Área/Vaga")
        v_des = st.text_area("Descrição Estratégica")

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
            linha_selecionada = df_vagas.iloc[[idx_ex]]
            st.markdown("**Foco que será apagado:**")
            st.dataframe(linha_selecionada)
            confirmar_exclusao = st.checkbox("✅ Confirmo que selecionei a linha correta para a exclusão", key="conf_ex_vagas")
            
            if st.button("❌ Apagar Foco"):
                if confirmar_exclusao:
                    df_vagas.drop(idx_ex).reset_index(drop=True).to_csv(ARQUIVO_VAGAS, index=False)
                    st.success("Foco removido com sucesso!")
                    st.rerun()
                else:
                    st.warning("Precisa marcar a caixa de seleção acima antes de excluir.")

    # 3. GERENCIAR CONHECIMENTOS
    elif menu_adm == "Novos Conhecimentos Técnicos":
        st.subheader("📝 Inserir Nova Skill")
        s_cat = st.selectbox("Categoria", ["Dados", "RPA", "SAP"])
        s_nom = st.text_input("Nome do Conhecimento")
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
            linha_selecionada = df_skills.iloc[[idx_ex]]
            st.markdown("**Skill que será apagada:**")
            st.dataframe(linha_selecionada)
            confirmar_exclusao = st.checkbox("✅ Confirmo que selecionei a linha correta para a exclusão", key="conf_ex_skills")
            
            if st.button("❌ Apagar Skill"):
                if confirmar_exclusao:
                    df_skills.drop(idx_ex).reset_index(drop=True).to_csv(ARQUIVO_SKILLS, index=False)
                    st.success("Skill removida com sucesso!")
                    st.rerun()
                else:
                    st.warning("Precisa marcar a caixa de seleção acima antes de excluir.")

    # 4. GERENCIAR FORMAÇÕES E CURSOS
    elif menu_adm == "📚 Formações e Cursos":
        st.subheader("📝 Cadastrar Nova Formação Acadêmica ou Curso")
        e_inst = st.text_input("Nome da instituição")
        e_nome = st.text_input("Curso ou Formação")
        e_status = st.selectbox("Status", ["Concluído", "Cursando"])
        e_conhecimentos = st.text_area("Conhecimentos do curso")

        if st.button("🚀 Gravar Formação/Curso"):
            if e_inst and e_nome:
                nl = pd.DataFrame([{"Instituição": e_inst, "Curso_Formacao": e_nome, "Status": e_status, "Conhecimentos": e_conhecimentos}])
                pd.concat([pd.read_csv(ARQUIVO_EDU), nl], ignore_index=True).to_csv(ARQUIVO_EDU, index=False)
                st.success("Histórico educacional salvo com sucesso!")
                st.rerun()

        st.subheader("🗑️ Remover Histórico Educacional")
        df_edu = pd.read_csv(ARQUIVO_EDU)
        if not df_edu.empty:
            st.dataframe(df_edu)
            idx_ex = st.number_input("Índice do item para apagar:", min_value=0, max_value=len(df_edu)-1, step=1)
            linha_selecionada = df_edu.iloc[[idx_ex]]
            st.markdown("**Histórico educacional que será apagado:**")
            st.dataframe(linha_selecionada)
            confirmar_exclusao = st.checkbox("✅ Confirmo que selecionei a linha correta para a exclusão", key="conf_ex_edu")
            
            if st.button("❌ Apagar Registro"):
                if confirmar_exclusao:
                    df_edu.drop(idx_ex).reset_index(drop=True).to_csv(ARQUIVO_EDU, index=False)
                    st.success("Item educacional removido com sucesso!")
                    st.rerun()
                else:
                    st.warning("Precisa marcar a caixa de seleção acima antes de excluir.")

    # 5. ATUALIZAR FOTO DE PERFIL
    elif menu_adm == "🖼️ @Atualizar Foto de Perfil":
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
