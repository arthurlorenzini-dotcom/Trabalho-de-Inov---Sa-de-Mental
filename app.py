import streamlit as st
import random
from datetime import datetime

if "porta_aberta" not in st.session_state:
    st.session_state.porta_aberta = False
if "tela_atual" not in st.session_state:
    st.session_state.tela_atual = "inicio"
if "nome_usuario" not in st.session_state:
    st.session_state.nome_usuario = "Usuário Anônimo"
if "email_usuario" not in st.session_state:
    st.session_state.email_usuario = "anonimo@acolhemente.org"
if "idioma" not in st.session_state:
    st.session_state.idioma = "Português"
if "tema_escuro" not in st.session_state:
    st.session_state.tema_escuro = False
if "diario" not in st.session_state:
    st.session_state.diario = []
if "atividades" not in st.session_state:
    st.session_state.atividades = []

TEXTOS = {
    "Português": {
        "titulo": "💛 AcolheMente",
        "sub": "Seu espaço seguro de acolhimento e suporte emocional",
        "aviso": "⚠️ **AVISO IMPORTANTE:** O AcolheMente é um suporte complementar. Não substitui atendimento profissional.",
        "diario": "📖 Diário", "atividades": "🎯 Atividades", "progresso": "📈 Progresso", "perfil": "👤 Perfil",
        "escrever": "Escrever", "historico": "Histórico", "dias": "Dias Registrados",
        "salvar": "Salvar Registro", "sucesso": "Registro salvo com sucesso!"
    },
    "Inglês": {
        "titulo": "💛 AcolheMente",
        "sub": "Your safe space for welcoming and emotional support",
        "aviso": "⚠️ **IMPORTANT NOTICE:** AcolheMente is a complementary support. It does not replace professional care.",
        "diario": "📖 Diary", "atividades": "🎯 Activities", "progresso": "📈 Progress", "perfil": "👤 Profile",
        "escrever": "Write", "historico": "History", "dias": "Registered Days",
        "salvar": "Save Record", "sucesso": "Record saved successfully!"
    },
    "Espanhol": {
        "titulo": "💛 AcolheMente",
        "sub": "Tu espacio seguro de acogida y soporte emocional",
        "aviso": "⚠️ **AVISO IMPORTANTE:** AcolheMente es un soporte complementario. No sustituye la atención profesional.",
        "diario": "📖 Diario", "atividades": "🎯 Actividades", "progresso": "📈 Progreso", "perfil": "👤 Perfil",
        "escrever": "Escribir", "historico": "Historial", "dias": "Días Registrados",
        "salvar": "Guardar Registro", "sucesso": "¡Registro guardado con éxito!"
    }
}

txt = TEXTOS[st.session_state.idioma]

st.set_page_config(page_title="AcolheMente", page_icon="💛", layout="centered")

cor_fundo = "#222222" if st.session_state.tema_escuro else "#fdfbf7"
cor_texto = "#ffffff" if st.session_state.tema_escuro else "#333333"

st.markdown(f"""
    <style>
    .stApp {{ background-color: {cor_fundo} !important; color: {cor_texto} !important; }}
    h1, h2, h3, h4, p, span, label {{ color: {cor_texto} !important; }}
    .disclaimer-box {{
        background-color: #fff3cd !important;
        color: #856404 !important;
        padding: 15px !important;
        border-radius: 10px !important;
        border-left: 5px solid #ffeeba !important;
        font-size: 0.9rem !important;
        margin-bottom: 20px !important;
    }}
    .stButton>button {{
        background-color: #ffd700 !important;
        color: #333333 !important;
        font-weight: bold !important;
        border-radius: 20px !important;
    }}
    </style>
""", unsafe_allow_html=True)

st.markdown(f'<div class="disclaimer-box">{txt["aviso"]}</div>', unsafe_allow_html=True)

if st.session_state.tela_atual == "inicio":
    st.markdown("<h1 style='text-align: center;'>Bem-vindo ao AcolheMente</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 1.2rem;'>{txt['sub']}</p>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 6rem; margin: 20px 0;'>🚪</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col2:
        if st.button("Abrir Porta (Entrar no Espaço Seguro)", use_container_width=True):
            st.session_state.tela_atual = "cadastro"
            st.rerun()

elif st.session_state.tela_atual == "cadastro":
    st.markdown("## Cadastro de Usuário")
    st.write("Crie sua conta de forma totalmente anônima e segura.")
    nome = st.text_input("Nome ou Apelido:", value=st.session_state.nome_usuario)
    email = st.text_input("E-mail de recuperação:", value=st.session_state.email_usuario)
    st.text_input("Senha de acesso:", type="password", value="******")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Criar Conta", use_container_width=True):
            st.session_state.nome_usuario = nome if nome else "Usuário Anônimo"
            st.session_state.email_usuario = email if email else "anonimo@acolhemente.org"
            st.session_state.tela_atual = "termos"
            st.rerun()
    with col2:
        if st.button("Voltar", use_container_width=True):
            st.session_state.tela_atual = "inicio"
            st.rerun()

elif st.session_state.tela_atual == "termos":
    st.markdown("## Termos de Uso")
    st.info("O AcolheMente é uma ferramenta complementar de suporte e escuta. Este sistema automatizado não substitui em nenhuma hipótese o acompanhamento médico, psicoterapêutico ou psiquiátrico profissional. Ao prosseguir, você concorda com o caráter estritamente educativo da plataforma.")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Aceitar e Entrar", use_container_width=True):
            st.session_state.porta_aberta = True
            st.session_state.tela_atual = "app"
            st.rerun()
    with col2:
        if st.button("Recusar", use_container_width=True):
            st.session_state.tela_atual = "cadastro"
            st.rerun()

elif st.session_state.tela_atual == "app":
    st.title(txt["titulo"])
    st.caption(f"{txt['sub']} • Campanha Setembro Amarelo")
    
    aba_diario, aba_atividades, aba_progresso, aba_perfil = st.tabs([
        txt["diario"], txt["atividades"], txt["progresso"], txt["perfil"]
    ])
    
    with aba_diario:
        sub_escrever, sub_historico, sub_dias = st.tabs([txt["escrever"], txt["historico"], txt["dias"]])
        
        with sub_escrever:
            st.write("### Como você está se sentindo hoje?")
            humor = st.select_slider("Humor:", options=["😢", "🙁", "😐", "🙂", "😄"], value="😐")
            texto = st.text_area("Desabafe aqui as suas reflexões:")
            if st.button(txt["salvar"]):
                data_agora = datetime.now().strftime("%d/%m/%Y %H:%M")
                st.session_state.diario.append({"data": data_agora, "humor": humor, "texto": texto})
                st.success(txt["sucesso"])
                st.rerun()
                
        with sub_historico:
            st.write("#### Histórico do Diário")
            for item in reversed(st.session_state.diario):
                st.markdown(f"**{item['data']}** - Humor: {item['humor']}\n> {item['texto']}\n---")
                
            st.write("#### Histórico de Atividades")
            for item in reversed(st.session_state.atividades):
                st.markdown(f"✅ Concluído: {item['nome']} em {item['data']}")
                
            st.write("#### Histórico de Frequência")
            st.write(f"Total de interações nesta sessão: {len(st.session_state.diario) + len(st.session_state.atividades)} registros.")
            
        with sub_dias:
            dias_unicos = len(st.session_state.diario)
            st.metric("Dias Acompanhados", dias_unicos)

    with aba_atividades:
        sub_mental, sub_fisico = st.tabs(["Exec. Mental", "Exec. Físico"])
        data_atv = datetime.now().strftime("%d/%m/%Y %H:%M")
        with sub_mental:
            st.write("### Exercício Mental: Respiração Quadrada")
            st.write("Inspirar por 4s, reter por 4s, expirar por 4s, manter vazio por 4s.")
            if st.button("Concluir Exercício Mental"):
                st.session_state.atividades.append({"data": data_atv, "nome": "Exercício Mental (Respiração)"})
                st.success("Atividade registrada!")
        with sub_fisico:
            st.write("### Exercício Físico: Alongamento Rápido")
            st.write("Alongue os braços e o pescoço por 5 minutos para aliviar o estresse corporal.")
            if st.button("Concluir Exercício Físico"):
                st.session_state.atividades.append({"data": data_atv, "nome": "Exercício Físico (Alongamento)"})
                st.success("Atividade registrada!")

    with aba_progresso:
        st.write("## Seu Progresso")
        total_feitos = len(st.session_state.diario) + len(st.session_state.atividades)
        porcentagem = min(total_feitos * 20, 100)
        st.progress(porcentagem / 100)
        st.write(f"Você já completou {porcentagem}% da meta de bem-estar dessa semana!")

    with aba_perfil:
        st.write("## Painel de Perfil")
        
        with st.expander("⚙️ Configuração"):
            st.write("#### Alterar Dados da Conta")
            novo_nome = st.text_input("Editar Apelido:", value=st.session_state.nome_usuario)
            novo_email = st.text_input("Editar E-mail:", value=st.session_state.email_usuario)
            if st.button("Atualizar Dados"):
                st.session_state.nome_usuario = novo_nome
                st.session_state.email_usuario = novo_email
                st.success("Dados atualizados!")
                st.rerun()
            
            st.write("---")
            st.write("#### Idioma do Sistema")
            novo_idioma = st.selectbox("Selecione o Idioma:", ["Português", "Inglês", "Espanhol"], index=["Português", "Inglês", "Espanhol"].index(st.session_state.idioma))
            if st.button("Mudar Idioma"):
                st.session_state.idioma = novo_idioma
                st.success("Idioma alterado!")
                st.rerun()
                
            st.write("---")
            st.write("#### Visual do Aplicativo")
            label_botao_tema = "Ativar Modo Claro ☀️" if st.session_state.tema_escuro else "Ativar Modo Escuro 🌙"
            if st.button(label_botao_tema):
                st.session_state.tema_escuro = not st.session_state.tema_escuro
                st.rerun()
            with st.expander("👤 Conta"):
                st.write(f"Usuário Conectado: {st.session_state.nome_usuario}")
                st.write(f"E-mail: {st.session_state.email_usuario}")
            if st.button("Trocar de Conta"):
                st.session_state.tela_atual = "cadastro"
                st.rerun()
            if st.button("Sair do Aplicativo"):
                st.session_state.porta_aberta = False
                st.session_state.tela_atual = "inicio"
                st.rerun()
            with st.expander("🛠️ Suporte"):
                st.write("#### Central de Ajuda Técnica")
                problema = st.text_area("Descreva o erro ou dúvida sobre o app:")
            if st.button("Enviar para o Suporte"):
                if problema:
                    st.success(f"Chamado aberto com sucesso! Protocolo: #{random.randint(1000, 9999)}")
            else:
                st.warning("Por favor, digite o problema antes de enviar.")