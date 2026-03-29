📉 Visualizador de Decaimento Exponencial

Este projeto foi criado para transformar a matemática do decaimento exponencial ($f(x) = e^{-x}$) em algo visual e fácil de entender. Ele inclui um script de automação que prepara todo o seu computador para rodar o código sem complicação.

🌟 O que este projeto faz?

Configuração Automática: O script cria um ambiente virtual para que as bibliotecas do projeto não entrem em conflito com outras coisas no seu sistema.

Instalação de Dependências: Baixa e instala o Numpy, Matplotlib e PyQt5.

Geração de Gráfico: Cria uma imagem profissional com anotações automáticas e notação científica.

🛠️ Configuração do Ambiente (Linux/macOS)

Para facilitar a sua vida, use o script setup_venv.sh.

Dê permissão de execução:

chmod +x setup_venv.sh


Rode o script:

./setup_venv.sh


Ative o ambiente:

Bash/Zsh: source .venv/bin/activate

Fish: source .venv/bin/activate.fish

Dica para Arch Linux / CachyOS: Se você usa o shell Fish, o script sugerirá uma abreviação (abbr) para que você não precise digitar o caminho todo da próxima vez!

🚀 Como gerar o gráfico

Com o ambiente ativado, execute o comando:

python grafico_decaimento.py


O programa vai gerar um arquivo chamado grafico_decaimento.png e abrir uma janela interativa na sua tela.

📚 Dicionário para Iniciantes

Ambiente Virtual (.venv): É como criar um "computador dentro do computador" só para este projeto. Isso evita que você instale coisas que podem quebrar outros programas.

PyQt5: É a ferramenta que permite ao Python "desenhar" a janela do gráfico no seu sistema operacional.

Notação Científica: Você verá números como 1.83e-02. Isso é apenas 0.0183. O e-02 diz para você "pular" a vírgula duas casas para a esquerda.


⚠️ Isenção de Responsabilidade

O uso dos scripts incluídos neste repositório é de sua inteira responsabilidade. Embora o código tenha sido desenvolvido para fins educativos e testado em ambientes controlados, não garantimos que ele seja isento de erros ou compatível com todas as configurações de sistema. Não nos responsabilizamos por quaisquer danos, instabilidades no sistema operacional ou perda de dados resultantes da execução dos scripts de automação ou da instalação de dependências de terceiros. Recomenda-se sempre revisar scripts de terminal antes da execução.
