import streamlit as st
from buscador import rodar_busca_geral

st.set_page_config(page_title="Plataforma de Viagens Inteligente", page_icon="✈️", layout="wide")

st.markdown("""
<style>
    .cartao-info {
        background-color: #ffffff !important;
        color: #212529 !important;
        padding: 22px;
        border-radius: 12px;
        border-left: 6px solid #007AFF;
        margin-bottom: 20px;
        box-shadow: 0px 4px 14px rgba(0, 0, 0, 0.05);
    }
    .titulo-cartao { color: #007AFF; font-weight: bold; font-size: 18px; margin-bottom: 12px; }
    .header-resultado { font-size: 28px; font-weight: bold; color: #1C1C1E; }
    .caixa-turismo {
        background-color: #f8f9fa !important;
        border-left: 5px solid #28a745 !important;
        padding: 25px !important;
        border-radius: 8px;
        color: #333333 !important;
        font-family: Arial, sans-serif !important;
        line-height: 1.6 !important;
        margin-top: 15px;
    }
    .ponto-destaque {
        font-weight: bold;
        color: #28a745;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.image("https://images.unsplash.com/photo-1488646953014-85cb44e25828?auto=format&fit=crop&w=300&q=80", use_column_width=True)
    st.markdown("### 🔍 Configuração do Planejamento")
    
    destino_usuario = st.text_input("📍 Digite o destino (Cidade/Estado/País):", value="Canadá")
    mes_usuario = st.selectbox(
        "📅 Mês de Foco Inicial:",
        ["Independente do mês", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    )
    
    botao_pesquisar = st.button("🔎 Atualizar Listagem", use_container_width=True, type="primary")

st.title("✈️ Portal de Inteligência Turística Local")
st.write("Consolide relatórios geográficos, cenários visuais exclusivos, fuso horário e tabelas climatológicas.")

if 'dados_site' not in st.session_state:
    st.session_state['last_dest'] = destino_usuario
    st.session_state['last_month'] = mes_usuario
    with st.spinner(f"Inicializando dados automáticos para {destino_usuario}..."):
        retorno_inicial = rodar_busca_geral(destino_usuario, mes_usuario)
        if retorno_inicial:
            st.session_state['dados_site'] = retorno_inicial

if botao_pesquisar or (destino_usuario and st.session_state.get('last_dest') != destino_usuario) or (mes_usuario and st.session_state.get('last_month') != mes_usuario):
    st.session_state['last_dest'] = destino_usuario
    st.session_state['last_month'] = mes_usuario
    
    with st.spinner(f"Processando novas informações para {destino_usuario}..."):
        retorno_api = rodar_busca_geral(destino_usuario, mes_usuario)
        if retorno_api:
            st.session_state['dados_site'] = retorno_api

if 'dados_site' in st.session_state:
    dados = st.session_state['dados_site']
    
    st.markdown("---")
    st.markdown(f"<div class='header-resultado'>🗺️ Destino Analisado: {dados['destino']}</div>", unsafe_allow_html=True)
    st.caption(f"🗓️ Período de Referência em Análise: **{dados['mes_planejado']}**")
    
    col_esquerda, col_direita = st.columns([1.2, 1])
    
    with col_esquerda:
        st.image(dados['imagem_capa'], caption=f"Região de Destaque Turístico em {dados['destino']}", use_container_width=True)
        
    with col_direita:
        st.markdown(f"<div class='cartao-info'><div class='titulo-cartao'>🗺️ Sugestão de Roteiro Prático</div></div>", unsafe_allow_html=True)
        st.write(dados['roteiro'])
        
        st.markdown(f"""
        <div class='cartao-info' style='margin-top: -15px;'>
            <p><b>🕐 Sistema de Fusos Horários (Ref. Horário de Brasília):</b><br>{dados['fuso_horario']}</p>
            <hr>
            <p><b>💱 Cotação da Moeda Local (Compra):</b><br>{dados['valor_moeda_compra']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 📊 Indicadores Meteorológicos Médios e Sazonalidade (Mês a Mês)")
    st.table(dados['tabela_valores'])

    st.markdown("---")
    st.markdown("### 📍 Resumo dos Pontos Turísticos e Lugares para Conhecer")
    
    # As strings HTML abaixo foram "coladas" na parede esquerda (sem espaços no começo) para o Streamlit não criar caixas pretas
    if "canadá" in dados['destino'].lower() or "canada" in dados['destino'].lower():
        info_local = """<ul>
<li><span class='ponto-destaque'>Parque Nacional de Banff (Alberta):</span> Famoso pelas suas impressionantes montanhas rochosas, florestas densas e os icônicos lagos de água azul-turquesa alimentados por geleiras, como o Lake Louise e o Moraine Lake.</li>
<li><span class='ponto-destaque'>Torre CN (Toronto):</span> Uma das estruturas mais altas do mundo, definindo a linha de horizonte de Toronto com mirantes panorâmicos incríveis e o famoso piso de vidro.</li>
<li><span class='ponto-destaque'>Cataratas do Niágara (Ontário):</span> Três imensas quedas d'água localizadas na fronteira com os EUA, atraindo milhões de visitantes anualmente para passeios de barco bem próximos à névoa.</li>
<li><span class='ponto-destaque'>Vancouver e Stanley Park (Colúmbia Britânica):</span> Uma metrópole urbana perfeitamente integrada à natureza costeira, ostentando um parque urbano gigante com florestas temperadas e vista para o oceano Pacifico.</li>
</ul>"""
    elif "frança" in dados['destino'].lower() or "franca" in dados['destino'].lower():
        info_local = """<ul>
<li><span class='ponto-destaque'>Torre Eiffel e Rio Sena (Paris):</span> O monumento pago mais visitado do mundo, cercado por jardins e passeios de barco românticos que cruzam os principais pontos históricos da capital.</li>
<li><span class='ponto-destaque'>Museu do Louvre (Paris):</span> O maior museum de arte do planeta, lar da icônica Mona Lisa e de uma imensa coleção de antiguidades reais e esculturas clássicas.</li>
<li><span class='ponto-destaque'>Palácio de Versalhes:</span> Símbolo histórico da monarquia absoluta francesa com seus imponentes salões espelhados e labirintos verdes milimetricamente desenhados.</li>
</ul>"""
    else:
        info_local = f"""<ul>
<li><span class='ponto-destaque'>Centro Histórico e Monumentos Locais:</span> Espaços ideais para explorar a herança cultural, arquiteturas típicas e mercados tradicionais da região de {dados['destino']}.</li>
<li><span class='ponto-destaque'>Parques e Mirantes Naturais:</span> Áreas de preservação ecológica ou pontos elevados perfeitos para fotografias panorâmicas e atividades ao ar livre.</li>
<li><span class='ponto-destaque'>Rotas Gastronômicas Nacionais:</span> Restaurantes e distritos culinários focados na experimentação dos pratos mais emblemáticos da cultura local.</li>
</ul>"""

    # Montando o HTML final totalmente encostado à esquerda para evitar a interpretação de código do Markdown
    html_final = f"""<div class='caixa-turismo'>
<h4 style='margin-top: 0; color: #28a745;'>🗺️ Informações Relevantes sobre {dados['destino']}</h4>
<p>O destino selecionado oferece uma rica gama de atrações que mesclam modernidade, traços culturais marcantes e paisagens naturais preservadas. Abaixo estão os locais mais recomendados e de maior prestígio para inclusão imediata em seu roteiro de viagem:</p>
{info_local}
<p style='font-size: 13px; color: #666; margin-bottom: 0; margin-top: 15px;'><i>Mapeamento de Pontos de Interesse Turístico Comercial — Atualizado 2026</i></p>
</div>"""

    st.markdown(html_final, unsafe_allow_html=True)