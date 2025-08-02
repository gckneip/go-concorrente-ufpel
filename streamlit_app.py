import streamlit as st
import streamlit.components.v1 as components

# Page settings
st.set_page_config(
    page_title="GO - Concorrente",
    page_icon="assets/go-icon.png",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "This app generates scripts for data clean rooms!"
    }
)

# Top of the page: title and logo
col1, col2 = st.columns((6, 1))
with col1:
    st.title("GO Concorrente")
with col2:
    st.image("assets/golang-goper-logo.png", width=1000)

# Sidebar: logo + links úteis
st.sidebar.image("assets/go-logo.png")
st.sidebar.image("assets/GOLANG.png")

# Menu items: (label, url, icon path)
menu_items = [
    ("Documentação oficial", "https://golang.org/doc/", "assets/documentation-gopher.png"),
    ("Tour do Go", "https://tour.golang.org/", "assets/tour-gopher.png"),
    ("Go Playground", "https://play.golang.org/", "assets/playground-gopher.png"),
    ("Pacotes (pkg.go.dev)", "https://pkg.go.dev/", "assets/pacotes-gopher.png"),
    ("Blog oficial do Go", "https://blog.golang.org/", "assets/blog-gopher.png"),
    ("Crie seu mascote", "https://gopherize.me/", "assets/mascote-gopher.png"),
]

st.sidebar.title("Recursos do Go")

for label, url, icon_path in menu_items:
    col1,  col2 = st.sidebar.columns([6, 10])
    
    with col1:
        st.image(icon_path, width=100)
    
    with col2:
        components.html(f"""
        <div style="height: 100px; display: flex; align-items: center;">
            <a href="{url}" target="_blank" style="
                color: white;
                text-decoration: none;
                padding: 8px 16px;
                border-radius: 6px;
                font-weight: bold;
                font-size: 16px;
                display: inline-block;
                font-family: sans-serif
            ">{label}</a>
        </div>
        """, height=100)

# Tabs de conteúdo principal
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Porque usar GO para concorrência?",
    "Goroutines",
    "Channels",
    "Runtime do GO",
    "Experimente no Playground"
])

with tab1:
    st.subheader("Porque usar GO para concorrência?")
    st.write("""
    Go foi projetado com concorrência em mente desde o início.
    Suas goroutines são leves, simples de usar, e a linguagem oferece suporte nativo a paralelismo eficiente.
    Isso torna Go uma excelente escolha para aplicações de alta performance e sistemas distribuídos.
    """)

with tab2:
    st.subheader("Goroutines")
    st.write("""
    Goroutines são funções que rodam concorrentemente com outras funções.
    Elas são muito mais leves que threads tradicionais e são gerenciadas pela runtime do Go.
    
    Exemplo:
    ```go
    go func() {
        fmt.Println("Olá de uma goroutine!")
    }()
    ```
    """)

with tab3:
    st.subheader("Channels")
    st.write("""
    Channels são a forma como goroutines se comunicam em Go.
    Eles permitem o envio e recebimento de valores entre goroutines de forma segura.

    Exemplo:
    ```go
    ch := make(chan int)
    go func() {
        ch <- 42
    }()
    fmt.Println(<-ch)
    ```
    """)

with tab4:
    st.subheader("Runtime do GO")
    st.write("""
    A runtime do Go gerencia o agendamento de goroutines, coleta de lixo, e muito mais.
    Ela é otimizada para escalabilidade, permitindo que milhares de goroutines rodem eficientemente mesmo em poucas threads do sistema operacional.
    """)

with tab5:
    st.subheader("Playground")
    st.write("Experimente escrever e executar código Go diretamente aqui:")
    # Go Playground via iframe
    st.components.v1.iframe("https://go.dev/play/", height=600, scrolling=True)
