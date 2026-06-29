import random
import urllib.parse
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import streamlit as st

try:
    EMAIL_SUPORTE = st.secrets.get("EMAIL_SUPORTE", "automacao.teste.2026@outlook.com")
    SENHA_SUPORTE = st.secrets.get("SENHA_SUPORTE", "@Daniel2022") 
except Exception:
    EMAIL_SUPORTE = "automacao.teste.2026@outlook.com"
    SENHA_SUPORTE = "@Daniel2022"

def notificar_problema_sistema(detalhes_erro):
    smtp_server = "smtp.office365.com"
    porto_smtp = 587
    msg = MIMEMultipart()
    msg['From'] = EMAIL_SUPORTE
    msg['To'] = EMAIL_SUPORTE
    msg['Subject'] = "🚨 ALERTA: Erro Crítico na Inicialização de Dados de Viagem"
    corpo = f"Falha reportada na geração de relatórios:\n\n{detalhes_erro}"
    msg.attach(MIMEText(corpo, 'plain'))
    
    try:
        servidor = smtplib.SMTP(smtp_server, porto_smtp, timeout=5)
        servidor.ehlo()
        servidor.starttls()
        servidor.ehlo()
        servidor.login(EMAIL_SUPORTE, SENHA_SUPORTE)
        servidor.sendmail(EMAIL_SUPORTE, EMAIL_SUPORTE, msg.as_string())
        servidor.quit()
    except Exception as e:
        print(f"Não foi possível notificar o suporte via SMTP: {e}")

def buscar_imagem_postal_exata(destino):
    destino_busca = destino.strip().lower()
    mapa_postais = {
        "brasil": "https://images.unsplash.com/photo-1516306580629-468a6e7de10d?auto=format&fit=crop&w=1200&q=80",
        "frança": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=1200&q=80",
        "canadá": "https://images.unsplash.com/photo-1487621167305-5d248087c724?auto=format&fit=crop&w=1200&q=80",
        "canada": "https://images.unsplash.com/photo-1487621167305-5d248087c724?auto=format&fit=crop&w=1200&q=80",
        "japão": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?auto=format&fit=crop&w=1200&q=80",
        "estados unidos": "https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?auto=format&fit=crop&w=1200&q=80"
    }
    if destino_busca in mapa_postais: return mapa_postais[destino_busca]
    termo_ingles = urllib.parse.quote(f"{destino_busca} landmark famous tourism")
    return f"https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1200&q=80&sig={termo_ingles}"

def buscar_fuso_horario(destino):
    cabeçalho = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    termo = f"fuso horario de {destino} em relacao ao brasil brasilia"
    url = f"https://www.google.com/search?q={urllib.parse.quote(termo)}"
    try:
        resposta = requests.get(url, headers=cabeçalho, timeout=5)
        if resposta.status_code == 200:
            sopa = BeautifulSoup(resposta.text, 'html.parser')
            bloco = sopa.select_one("div.BNeawe")
            if bloco: return bloco.text.strip().split("\n")[0]
    except Exception as e:
        notificar_problema_sistema(f"Fuso horário indisponível: {e}")
    return "Fuso horário variável conforme o Estado selecionado"

def buscar_cotacao_moeda(destino):
    cabeçalho = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    termo = f"qual a moeda oficial de {destino} e valor em real para compra hoje"
    url = f"https://www.google.com/search?q={urllib.parse.quote(termo)}"
    try:
        resposta = requests.get(url, headers=cabeçalho, timeout=5)
        if resposta.status_code == 200:
            sopa = BeautifulSoup(resposta.text, 'html.parser')
            bloco = sopa.select_one("span.DFlfde, div.BNeawe")
            if bloco: return bloco.text.strip().split("\n")[0]
    except: pass
    return "5.45 (Valor Comercial Estimado)"

def gerar_roteiro_turismo(destino):
    dest_ajustado = destino.lower().strip()
    
    if "canadá" in dest_ajustado or "canada" in dest_ajustado:
        return (
            "Dia 1: Eixo Urbano e Modernidade\n"
            "  - Manhã: Chegada e subida à famosa CN Tower para reconhecimento panorâmico.\n"
            "  - Tarde: Caminhada cultural pelas ruas históricas do Distillery District.\n"
            "  - Noite: Jantar na movimentada Dundas Square.\n\n"
            "Dia 2: Maravilhas Naturais Imperdíveis\n"
            "  - Manhã: Deslocamento para o espetáculo visual das Cataratas do Niágara.\n"
            "  - Tarde: Passeio de barco 'Maid of the Mist' e visita às vinícolas locais.\n"
            "  - Noite: Retorno à base hoteleira central.\n\n"
            "Dia 3: Parques e Imersão Local\n"
            "  - Manhã: Visita ao Casa Loma, o icônico castelo urbano canadense.\n"
            "  - Tarde: Piquenique e caminhada relaxante no High Park.\n"
            "  - Noite: Despedida gastronômica no St. Lawrence Market."
        )
    elif "frança" in dest_ajustado or "franca" in dest_ajustado:
        return (
            "Dia 1: O Coração Histórico de Paris\n"
            "  - Manhã: Visita à icônica Torre Eiffel e fotos nos Jardins do Trocadéro.\n"
            "  - Tarde: Caminhada guiada pela Avenida Champs-Élysées até o Arco do Triunfo.\n"
            "  - Noite: Cruzeiro romântico com jantar pelo Rio Sena.\n\n"
            "Dia 2: Arte, Boemia e Cultura\n"
            "  - Manhã: Entrada prioritária no Museu do Louvre para apreciar grandes obras.\n"
            "  - Tarde: Caminhada pelas ladeiras charmosas e cafés de Montmartre.\n"
            "  - Noite: Visita à belíssima Basílica de Sacré-Cœur ao pôr do sol.\n\n"
            "Dia 3: Realeza e Jardins Clássicos\n"
            "  - Manhã: Bate-volta de train até o imponente Palácio de Versalhes.\n"
            "  - Tarde: Exploração detalhada dos extensos labirintos e fontes dos Jardins Reais.\n"
            "  - Noite: Retorno a Paris para jantar no Quartier Latin."
        )
    else:
        return (
            f"Dia 1: Reconhecimento e Principais Cartões-Postais de {destino}\n"
            "  - Manhã: Tour panorâmico pelos principais pontos de referência centrais.\n"
            "  - Tarde: Visita guiada ao monumento ou museum de maior relevância histórica.\n"
            "  - Noite: Jantar de boas-vindas focado na culinária típica regional.\n\n"
            "Dia 2: Natureza, Parques e Mirantes\n"
            "  - Manhã: Atividade ao ar livre no parque ecológico ou local de maior destaque.\n"
            "  - Tarde: Parada para fotos em mirantes exclusivos e compra de artesanato.\n"
            "  - Noite: Passeio a pé pelo centro comercial histórico."
        )

def gerar_calendario_temperaturas(destino):
    destino_ajustado = destino.lower().strip()
    if "canadá" in destino_ajustado or "canada" in destino_ajustado:
        temps = [-10, -8, -2, 6, 13, 18, 22, 21, 16, 9, 2, -5]
    elif "frança" in destino_ajustado or "franca" in destino_ajustado:
        temps = [5, 6, 9, 12, 16, 20, 23, 22, 19, 14, 9, 6]
    elif "japão" in destino_ajustado or "japao" in destino_ajustado:
        temps = [5, 6, 9, 14, 19, 22, 26, 27, 23, 18, 12, 7]
    else:
        temps = [26, 27, 26, 24, 22, 20, 20, 21, 23, 24, 25, 26]

    meses_nomes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
                   "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    
    tabela_clima = []
    for i, nome_mes in enumerate(meses_nomes):
        t = temps[i]
        if nome_mes in ["Dezembro", "Janeiro", "Fevereiro", "Julho"]:
            sazonalidade = "🚀 Alta Temporada"
            condicao = "Fluxo Máximo / Clima Extremo" if t < 5 else "Fluxo Máximo / Verão Dinâmico"
        elif nome_mes in ["Junho", "Agosto", "Novembro"]:
            sazonalidade = "📉 Baixa Temporada"
            condicao = "Período Chuvoso / Instável" if t > 15 else "Frio Intenso / Baixo Fluxo"
        else:
            sazonalidade = "⚖️ Média Temporada"
            condicao = "Clima Ameno / Condições Ideais"
            
        tabela_clima.append({
            "Mês": nome_mes,
            "Temperatura Média": f"{t}°C",
            "Sazonalidade": sazonalidade,
            "Condição Operacional": condicao
        })
    return tabela_clima

def rodar_busca_geral(destino, mes):
    destino_limpo = destino.strip().title()
    try:
        foto_unica = buscar_imagem_postal_exata(destino_limpo)
        roteiro_formatado = gerar_roteiro_turismo(destino_limpo)
        valor_cambio = buscar_cotacao_moeda(destino_limpo)
        fuso_local = buscar_fuso_horario(destino_limpo)
        cronograma_clima = gerar_calendario_temperaturas(destino_limpo)
        
        return {
            "destino": destino_limpo,
            "mes_planejado": mes,
            "imagem_capa": foto_unica,
            "roteiro": roteiro_formatado,
            "fuso_horario": fuso_local,
            "valor_moeda_compra": valor_cambio,
            "tabela_valores": cronograma_clima
        }
    except Exception as erro:
        notificar_problema_sistema(f"Erro ao processar mapeamento para {destino_limpo}: {erro}")
        return None