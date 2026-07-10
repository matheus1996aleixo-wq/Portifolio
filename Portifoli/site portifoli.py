import streamlit as st
import pandas as pd
import base64
import os

# Configuração da página
st.set_page_config(
    page_title="M. Aleixo TI - Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTADO DE SESSÃO E ARQUIVOS ---
if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

USUARIO_ADMIN = "matheus"
SENHA_ADMIN = "@Kayle2023"

ARQUIVO_PROJETOS = "dados_portfolio.csv"
ARQUIVO_VAGAS = "dados_vagas.csv"
ARQUIVO_SKILLS = "dados_skills.csv"
ARQUIVO_EDU = "dados_educacao.csv"
NOME_FOTO = "Foto_Perfil_Matheus.jpg"

# Inicialização de bases de dados (CSV)
bases = [
    (ARQUIVO_PROJETOS, ["Categoria", "Título", "Descrição", "Link do Processo", "Link do Vídeo"]),
    (ARQUIVO_VAGAS, ["Título", "Descrição"]),
    (ARQUIVO_SKILLS, ["Categoria", "Nome", "Porcentagem"]),
    (ARQUIVO_EDU, ["Tipo", "Instituição", "Ano", "Descrição"])
]

for arquivo, cols in bases:
    if not os.path.exists(arquivo):
        pd.DataFrame(columns=cols).to_csv(arquivo, index=False)

# --- FUNÇÕES DE APOIO ---
def obter_imagem_base64():
    if os.path.exists(NOME_FOTO):
        try:
            with open(NOME_FOTO, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode()
        except: return None
    return None

foto_base64 = obter_imagem_base64()

# --- CSS PERSONALIZADO (CORES DIVERTIDAS E CHAMATIVAS) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #0F172A;
        color: #E2E8F0;
        font-family: 'Inter', sans-serif;
    }
    
    /* Cards com bordas coloridas */
    .skill-card {
        background: #1E293B;
        border-radius: 15px;
        padding: 20px;
        border: 1px solid #334155;
        margin-bottom: 15px;
        transition: transform 0.3s;
    }
    .skill-card:hover {
        transform: translateY(-5px);
        border-color: #38BDF8;
    }
    
    /* Cores das categorias */
    .cat-sap { color: #FACC15; } /* Amarelo */
    .cat-rpa { color: #4ADE80; } /* Verde */
    .cat-dados { color: #F87171; } /* Vermelho/Coral */
    
    .avatar-img {
        width: 160px; height: 160px;
        border-radius: 50%;
        border: 4px solid #38BDF8;
        box-shadow: 0 4px 25px rgba(56,189,248,0.5);
    }

    .info-card {
        background: #1E293B;
        border: 1px solid #334155;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 8px;
    }
    
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #38BDF8, #818CF8);
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    if foto_base64:
        st.markdown(f'<center><img class="avatar-img" src="data:image/jpeg;base64,{foto_base64}"></center>', unsafe_allow_html=True)
    else:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150)
    
    st.markdown("<h2 style='text-align: center; color: white;'>Matheus Aleixo</h2>", unsafe_allow_html=True)
    
    with st.expander("🛠️ Acesso Restrito", expanded=False):
        if not st.session_state["autenticado"]:
            u = st.text_input("Usuário")
            p = st.text_input("Senha", type="password")
            if st.button("Entrar"):
                if u == USUARIO_ADMIN and p == SENHA_ADMIN:
                    st.session_state["autenticado"] = True
                    st.rerun()
                else: st.error("Incorreto")
        else:
            if st.button("Sair"):
                st.session_state["autenticado"] = False
                st.rerun()

# --- CONTEÚDO PRINCIPAL ---
st.title("💻 Portfólio M. Aleixo TI")

tab_obj, tab_exp, tab_skills, tab_proj, tab_edu = st.tabs([
    "🎯 Objetivo", "💼 Experiências", "🧠 Conhecimentos", "🚀 Projetos", "📚 Formação"
])

# 1. OBJETIVO
with tab_obj:
    st.markdown("### 🎯 Foco Profissional")
    st.info("Especialista focado em otimização de processos, integração SAP e arquitetura de dados.")
    df_v = pd.read_csv(ARQUIVO_VAGAS)
    for _, r in df_v.iterrows():
        st.markdown(f"<div class='skill-card'><h4>✨ {r['Título']}</h4><p>{r['Descrição']}</p></div>", unsafe_allow_html=True)

# 2. EXPERIÊNCIAS (Resumo fixo ou dinâmico)
with tab_exp:
    st.markdown("### 💼 Trajetória")
    exps = [
        ("Consultor SAP Jr", "Stefanini", "Suporte S/4HANA FI/CO/SD"),
        ("Estagiário TI", "Continental", "SAP ECC & Projeto SPIRIT"),
    ]
    for cargo, emp, desc in exps:
        st.markdown(f"<div class='skill-card'><b>{cargo}</b> @ {emp}<br><small>{desc}</small></div>", unsafe_allow_html=True)

# 3. CONHECIMENTOS (LAYOUT CHAMATIVO COM ÍCONES)
with tab_skills:
    st.markdown("### 🧠 Hard Skills & Nível de Domínio")
    df_s = pd.read_csv(ARQUIVO_SKILLS)
    
    # Mapeamento de Cores e Ícones
    icones = {"SAP": "⚙️", "RPA": "🤖", "Dados": "📊"}
    cores = {"SAP": "cat-sap", "RPA": "cat-rpa", "Dados": "cat-dados"}

    if not df_s.empty:
        cats = df_s["Categoria"].unique()
        for c in cats:
            st.markdown(f"<h3 class='{cores.get(c, '')}'>{icones.get(c, '🔹')} Categoria: {c}</h3>", unsafe_allow_html=True)
            df_f = df_s[df_s["Categoria"] == c]
            
            c1, c2 = st.columns(2)
            for i, row in enumerate(df_f.iterrows()):
                alvo = c1 if i % 2 == 0 else c2
                with alvo:
                    st.write(f"**{row[1]['Nome']}**")
                    st.progress(int(row[1]['Porcentagem']))
            st.write("---")

# 4. PROJETOS
with tab_proj:
    st.markdown("### 🚀 Projetos e Automações")
    df_p = pd.read_csv(ARQUIVO_PROJETOS)
    for _, r in df_p.iterrows():
        with st.container():
            st.markdown(f"<div class='skill-card'><h4>{r['Título']}</h4><p>{r['Descrição']}</p></div>", unsafe_allow_html=True)
            if r['Link do Processo']: st.link_button("📂 Ver Código", r['Link do Processo'])

# 5. FORMAÇÃO (DINÂMICA)
with tab_edu:
    st.markdown("### 📚 Educação e Cursos")
    df_e = pd.read_csv(ARQUIVO_EDU)
    if not df_e.empty:
        for _, r in df_e.iterrows():
            st.markdown(f"""
            <div class='skill-card' style='border-left: 5px solid #38BDF8;'>
                <h4 style='margin:0;'>🎓 {r['Instituição']}</h4>
                <p style='color:#38BDF8; margin:0;'><b>{r['Tipo']}</b> | {r['Ano']}</p>
                <p style='font-size:0.9rem; color:#94A3B8;'>{r['Descrição']}</p>
            </div>
            """, unsafe_allow_html=True)
    else: st.info("Nenhuma formação cadastrada.")

# --- PAINEL ADMINISTRATIVO ---
if st.session_state["autenticado"]:
    st.divider()
    st.header("🔒 Painel de Controle")
    
    opcao = st.selectbox("O que deseja gerenciar?", ["Projetos", "Skills", "Formação/Cursos", "Foco/Vagas", "Foto"])

    # GERENCIAR FORMAÇÃO (NOVO)
    if opcao == "Formação/Cursos":
        st.subheader("📝 Adicionar Formação/Curso")
        with st.form("form_edu"):
            f_tipo = st.text_input("Tipo (Ex: Bacharelado, Curso Online, Certificação)")
            f_inst = st.text_input("Instituição")
            f_ano = st.text_input("Ano/Período")
            f_desc = st.text_area("Breve descrição")
            if st.form_submit_button("Salvar Formação"):
                nova_f = pd.DataFrame([{"Tipo": f_tipo, "Instituição": f_inst, "Ano": f_ano, "Descrição": f_desc}])
                pd.concat([pd.read_csv(ARQUIVO_EDU), nova_f], ignore_index=True).to_csv(ARQUIVO_EDU, index=False)
                st.success("Salvo!")
                st.rerun()
        
        st.subheader("🗑️ Remover")
        df_edit_e = pd.read_csv(ARQUIVO_EDU)
        if not df_edit_e.empty:
            it_rem = st.selectbox("Selecione para excluir", df_edit_e.index, format_func=lambda x: df_edit_e.iloc[x]['Instituição'])
            if st.button("Excluir Formação"):
                df_edit_e.drop(it_rem).to_csv(ARQUIVO_EDU, index=False)
                st.rerun()

    # GERENCIAR SKILLS (CORES/ICONES)
    elif opcao == "Skills":
        st.subheader("Adicionar Conhecimento")
        with st.form("form_s"):
            s_cat = st.selectbox("Categoria", ["SAP", "RPA", "Dados"])
            s_nom = st.text_input("Nome da Skill")
            s_per = st.slider("Nível (%)", 0, 100, 80)
            if st.form_submit_button("Gravar"):
                ns = pd.DataFrame([{"Categoria": s_cat, "Nome": s_nom, "Porcentagem": s_per}])
                pd.concat([pd.read_csv(ARQUIVO_SKILLS), ns], ignore_index=True).to_csv(ARQUIVO_SKILLS, index=False)
                st.rerun()
        
        df_edit_s = pd.read_csv(ARQUIVO_SKILLS)
        st.dataframe(df_edit_s)
        idx_s = st.number_input("Index para excluir", 0, 100)
        if st.button("Remover Skill"):
            df_edit_s.drop(idx_s).to_csv(ARQUIVO_SKILLS, index=False)
            st.rerun()

    # (As outras opções como Projetos e Foto seguem a mesma lógica CRUD anterior...)
    elif opcao == "Foto":
        uploaded_file = st.file_uploader("Escolha a foto de perfil", type=["jpg", "png", "jpeg"])
        if uploaded_file and st.button("Substituir Foto"):
            with open(NOME_FOTO, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success("Foto atualizada!")
            st.rerun()

    elif opcao == "Projetos":
        with st.form("f_p"):
            t = st.text_input("Título")
            d = st.text_area("Descrição")
            cat = st.text_input("Categoria")
            l = st.text_input("Link")
            if st.form_submit_button("Salvar Projeto"):
                np = pd.DataFrame([{"Categoria": cat, "Título": t, "Descrição": d, "Link do Processo": l, "Link do Vídeo": ""}])
                pd.concat([pd.read_csv(ARQUIVO_PROJETOS), np], ignore_index=True).to_csv(ARQUIVO_PROJETOS, index=False)
                st.rerun()
