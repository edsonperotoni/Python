import os
import matplotlib
# Configura o backend para Qt5 se houver display disponível, senão usa Agg (headless)
try:
    if 'DISPLAY' in os.environ or os.name == 'nt':
        matplotlib.use('Qt5Agg')
    else:
        matplotlib.use('Agg')
except Exception:
    matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

# 1. Gerar os dados (101 pontos: índices de 0 a 100 para corresponder a inteiros)
x = np.linspace(0, 10, 101)
y = np.exp(-x)

# 2. Configurar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x) = e^-x', color='#00ffcc', linewidth=2)

# Estilização
plt.title('Curva de Decaimento Exponencial')
plt.xlabel('Eixo X (Positivo)')
plt.ylabel('Eixo Y')
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.legend()

# Ajustar limites do eixo Y para dar espaço para as anotações
plt.ylim(-0.05, 1.15)

# 3. Adicionar Anotações
print("Gerando gráfico...")

# Escolhemos alguns índices para mostrar 
# Índices que queremos marcar (correspondentes aos inteiros 0, 2, 4, 6, 8, 10)
indices = [0, 20, 40, 60, 80, 100]

for i in indices:
    if i == 0:
        # Primeiro ponto: 2 casas decimais (ex: 1.00)
        label = f'{y[i]:.2f}'
    else:
        # Demais pontos: Notação científica com 2 casas (ex: 1.35e-01)
        label = f'{y[i]:.2e}'
    
    plt.annotate(label, 
                 (x[i], y[i]), 
                 textcoords="offset points", 
                 xytext=(0,10), 
                 ha='center',
                 fontsize=9,
                 color='blue',
                 fontweight='bold',
                 rotation=45)

# 4. Exibir e Salvar
# DICA: No Matplotlib, se você salvar DEPOIS do plt.show(), 
# a imagem pode sair em branco. Salve sempre ANTES de abrir a janela.
plt.savefig('grafico_decaimento.png')
print("Sucesso! O gráfico foi salvo como 'grafico_decaimento.png'.")

plt.show()