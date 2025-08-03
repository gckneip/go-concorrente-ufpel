import streamlit as st
import streamlit.components.v1 as components

# Page settings
st.set_page_config(
    page_title="Go para Concorrência",
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
    st.title("Go: A Escolha Inteligente para um Mundo Concorrente")
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
        
st.write("""
Explore as abas abaixo para descobrir por que a simplicidade e o poder do modelo de concorrência do Go o tornam a ferramenta ideal para construir aplicações modernas, escaláveis e de alta performance.
""")

st.markdown("---")
        
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🎯 **Por que Go para Concorrência?**",
    "💡 **Goroutines: Concorrência Leve**",
    "📡 **Channels: Comunicação Segura**",
    "🎶 **Orquestração: Select e Sync**",
    "⚙️ **O Motor: Runtime do Go**",
    "🌍 **Go no Mundo Real & Playground**"
])

with tab1:
    st.header("🎯 A Filosofia de Concorrência do Go")
    st.markdown("""
    Em um mundo onde aplicações precisam processar milhares de requisições simultaneamente, a concorrência é fundamental. Muitas linguagens abordam a concorrência com mecanismos complexos e propensos a erros, como threads e locks manuais.

    Go nasceu com uma filosofia diferente, inspirada no conceito de **CSP (Communicating Sequential Processes)**. A ideia central é:

    > **"Não comunique compartilhando memória; em vez disso, compartilhe memória comunicando."**

    Isso significa que, em vez de múltiplas threads disputando o acesso a uma mesma variável (o que exige `locks` e pode levar a *race conditions*), as Goroutines enviam mensagens umas às outras através de canais (`channels`). Esse modelo torna o código:

    -   **Mais simples de ler e raciocinar**: A lógica de comunicação é explícita.
    -   **Mais seguro**: Reduz drasticamente a chance de bugs de concorrência.
    -   **Altamente performático**: O runtime do Go foi projetado do zero para gerenciar milhões de Goroutines com eficiência.

    Go não adicionou concorrência como um recurso, **Go foi projetado em torno da concorrência**.
    """)
    
with tab2:
    st.header("💡 Goroutines: Concorrência Leve e Intuitiva")
    st.markdown("""
    **Goroutines** são a unidade fundamental de concorrência em Go. Pense nelas como threads, mas com um custo ridiculamente baixo.

    | Característica | Threads Tradicionais (SO) | Goroutines (Go) |
    | :--- | :--- | :--- |
    | **Custo de Criação** | Alto (consome muita memória e tempo de CPU) | Baixíssimo (poucos KB de stack inicial) |
    | **Gerenciamento** | Gerenciadas pelo Kernel do SO (troca de contexto lenta) | Gerenciadas pelo Runtime do Go (troca de contexto rápida) |
    | **Quantidade** | Dezenas ou centenas | Centenas de milhares ou até milhões |

    #### Como usar?
    É trivial. Basta usar a palavra-chave `go` antes de uma chamada de função. A função passará a ser executada em segundo plano, de forma concorrente, sem bloquear a execução principal.
    """)

    st.subheader("Exemplo: Disparando múltiplas tarefas")
    st.code("""
package main

import (
	"fmt"
	"time"
)

func tarefa(id int) {
	fmt.Printf("Iniciando tarefa %d...\\n", id)
	time.Sleep(2 * time.Second) // Simula um trabalho pesado
	fmt.Printf("Tarefa %d concluída!\\n", id)
}

func main() {
	// Dispara 3 goroutines concorrentemente
	go tarefa(1)
	go tarefa(2)
	go tarefa(3)

	// Espera um pouco para que as goroutines terminem antes do programa principal encerrar
	time.Sleep(3 * time.Second)
	fmt.Println("Programa principal encerrado.")
}
""", language='go')
    st.markdown("Neste exemplo, as três tarefas rodam simultaneamente. O programa não espera a primeira terminar para iniciar a segunda.")

with tab3:
    st.header("📡 Channels: Comunicação Segura e Sincronizada")
    st.markdown("""
    Se Goroutines são os "trabalhadores", **Channels** são as "esteiras" por onde eles trocam informações de forma segura. Um Channel é um canal tipado, o que significa que você só pode enviar e receber dados de um tipo específico, garantindo segurança de tipos (*type safety*).

    Operações com channels são, por padrão, **bloqueantes**:
    -   **Envio (`ch <- valor`)**: Bloqueia a Goroutine até que outra Goroutine esteja pronta para receber o valor.
    -   **Recebimento (`<-ch`)**: Bloqueia a Goroutine até que um valor seja enviado para o canal.

    Esse comportamento bloqueante é a chave para a **sincronização automática** entre Goroutines, eliminando a necessidade de `locks` manuais na maioria dos casos.

    #### Exemplo: Ping-Pong entre Goroutines
    """)
    st.code("""
package main

import (
	"fmt"
	"time"
)

// pinger envia uma mensagem e espera uma resposta
func pinger(pings chan<- string, msg string) {
	pings <- msg
}

// ponger recebe uma mensagem e a imprime
func ponger(pings <-chan string, pongs chan<- string) {
	msg := <-pings // Recebe de pings
	fmt.Println(msg, "recebido!")
	time.Sleep(1 * time.Second)
	pongs <- "Pong" // Envia para pongs
}

func main() {
	pings := make(chan string, 1) // Canal para pings
	pongs := make(chan string, 1) // Canal para pongs

	go pinger(pings, "Ping")
	go ponger(pings, pongs)

	fmt.Println("Esperando a resposta...")
	resposta := <-pongs // Recebe a resposta final
	fmt.Println("Resposta recebida:", resposta)
}
""", language='go')
    st.markdown("Este exemplo mostra como os `channels` coordenam o fluxo de execução entre duas Goroutines de forma elegante e segura.")

with tab4:
    st.header("🎶 Orquestração Avançada: `select` e `sync`")
    st.markdown("""
    Go oferece ferramentas poderosas para gerenciar cenários de concorrência mais complexos.
    """)

    st.subheader("`select`: Esperando por Múltiplos Canais")
    st.markdown("""
    O `select` permite que uma Goroutine espere por operações em múltiplos canais simultaneamente. É como um `switch` para `channels`.

    - Ele bloqueia até que um de seus `cases` (uma operação de canal) possa ser executado.
    - Se múltiplos `cases` estiverem prontos, ele escolhe um aleatoriamente.
    - Um `case default` pode ser usado para evitar o bloqueio.
    """)
    st.code("""
package main

import (
	"fmt"
	"time"
)

func main() {
	c1 := make(chan string)
	c2 := make(chan string)

	go func() {
		time.Sleep(1 * time.Second)
		c1 <- "resultado um"
	}()
	go func() {
		time.Sleep(2 * time.Second)
		c2 <- "resultado dois"
	}()

	// Espera por dois resultados, mas reage ao primeiro que chegar
	for i := 0; i < 2; i++ {
		select {
		case msg1 := <-c1:
			fmt.Println("Recebido:", msg1)
		case msg2 := <-c2:
			fmt.Println("Recebido:", msg2)
		}
	}
}
""", language='go')

    st.subheader("Pacote `sync`: Quando a Comunicação não é Suficiente")
    st.markdown("""
    Embora a comunicação via `channels` seja o ideal, às vezes você precisa de mecanismos de sincronização mais tradicionais. O pacote `sync` oferece:

    -   **`sync.WaitGroup`**: Para esperar que um grupo de Goroutines termine sua execução. É uma forma mais robusta de "esperar" do que o `time.Sleep()` que usamos nos primeiros exemplos.
    -   **`sync.Mutex`**: Um `lock` de exclusão mútua para proteger o acesso a uma variável quando várias Goroutines precisam modificá-la diretamente.
    """)
    st.code("""
package main

import (
	"fmt"
	"sync"
	"time"
)

func worker(id int, wg *sync.WaitGroup) {
	defer wg.Done() // Decrementa o contador do WaitGroup quando a função retorna
	fmt.Printf("Worker %d começando\\n", id)
	time.Sleep(time.Second)
	fmt.Printf("Worker %d terminando\\n", id)
}

func main() {
	var wg sync.WaitGroup // Cria um WaitGroup

	for i := 1; i <= 3; i++ {
		wg.Add(1) // Incrementa o contador para cada Goroutine
		go worker(i, &wg)
	}

	wg.Wait() // Bloqueia aqui até que o contador seja zero

	fmt.Println("Todos os workers terminaram.")
}
""", language='go')

with tab5:
    st.header("⚙️ O Motor por Trás de Tudo: O Runtime do Go")
    st.markdown("""
    A eficiência do modelo de concorrência do Go não é mágica, é engenharia. O **Runtime do Go** é um ambiente de execução sofisticado que gerencia recursos de forma inteligente.

    #### O Agendador (Scheduler) M:P:G
    O coração do runtime é seu agendador, que implementa um modelo conhecido como **M:P:G**:
    -   **M (Machine)**: Uma thread do sistema operacional.
    -   **P (Processor)**: Um contexto para execução, representa um recurso de processamento.
    -   **G (Goroutine)**: A sua Goroutine.

    

    O agendador do Go distribui as Goroutines (G) para serem executadas nos processadores lógicos (P), que por sua vez são executados pelas threads do SO (M).

    **Por que isso é genial?**
    1.  **Agendamento Cooperativo**: Se uma Goroutine faz uma chamada bloqueante (como ler um arquivo ou uma requisição de rede), o agendador a retira da thread do SO e coloca outra Goroutine para executar no lugar. A thread do SO nunca fica ociosa.
    2.  **Eficiência Máxima**: Ele utiliza todas as CPUs disponíveis, gerenciando um número massivo de Goroutines com um número pequeno de threads do SO, o que minimiza a sobrecarga do sistema operacional.

    #### Garbage Collector (Coletor de Lixo)
    Go possui um coletor de lixo concorrente e de baixa latência. Ele foi projetado para trabalhar em paralelo com o seu código, minimizando as pausas ("stop-the-world") e garantindo que sua aplicação de alta performance continue responsiva.
    """)

with tab6:
    st.header("🌍 Go no Mundo Real: Cases de Sucesso")
    st.markdown("""
    A simplicidade e performance da concorrência em Go não são apenas teóricas. Grandes empresas confiam em Go para construir sistemas críticos e de larga escala:

    -   **Uber**: Utiliza Go para seus serviços de geolocalização e processamento de dados de alta vazão.
    -   **Twitch**: Usa Go para partes de seu sistema de chat, que serve milhões de usuários concorrentes.
    -   **Google**: Criadora da linguagem, usa Go em inúmeros sistemas internos, incluindo partes do YouTube e da infraestrutura da nuvem.
    -   **Mercado Livre**: Empregou Go para reescrever seus principais serviços de backend, melhorando a performance e a escalabilidade.
    -   **Dropbox**: Migrou partes críticas de sua infraestrutura de Python para Go para obter melhor concorrência e uso de memória.

    Essas empresas escolheram Go porque ele entrega o que promete: **performance, simplicidade e concorrência de primeira classe.**
    """)

    st.markdown("---")

    st.header("🎮 Experimente Agora no Playground!")
    st.write("Nada melhor do que ver com os próprios olhos. Use o playground oficial do Go abaixo para testar os exemplos das abas anteriores ou escrever seus próprios códigos concorrentes. **Seja curioso!**")

    # Incorpora o Go Playground usando um iframe
    st.components.v1.iframe("https://go.dev/play/?v=gotip", height=600, scrolling=True)
