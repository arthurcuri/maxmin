# Projeto - Algoritmo de Seleção Simultânea MaxMin Select

## Descrição do Projeto

O **Algoritmo de Seleção Simultânea MaxMin Select** é uma técnica eficiente para encontrar simultaneamente o maior e o menor elementos de uma sequência de números. Este projeto implementa o algoritmo em Python, demonstrando a estratégia "dividir para conquistar" para reduzir o número de comparações necessárias em comparação com uma abordagem ingênua.

### Lógica do Algoritmo Implementado

O algoritmo utiliza a estratégia "dividir para conquistar" seguindo a seguinte lógica linha a linha:

```python
def max_min_select(arr, left, right):
    # Linha 1: Caso base - apenas um elemento
    if left == right:
        return arr[left], arr[left]  # O único elemento é tanto min quanto max
    
    # Linha 2-6: Caso base - dois elementos
    if right == left + 1:
        if arr[left] < arr[right]:
            return arr[left], arr[right]  # left é menor, right é maior
        else:
            return arr[right], arr[left]  # right é menor, left é maior
    
    # Linha 7: Divide o problema no ponto médio
    mid = (left + right) // 2
    
    # Linha 8-9: Resolve recursivamente as duas metades
    min_left, max_left = max_min_select(arr, left, mid)      # Metade esquerda
    min_right, max_right = max_min_select(arr, mid + 1, right)  # Metade direita
    
    # Linha 10: Combina os resultados com duas comparações
    return min(min_left, min_right), max(max_left, max_right)
```

**Explicação da Estratégia:**
- Para uma sequência de tamanho n, divide-se em duas subsequências de tamanho ⌊n/2⌋
- Resolve-se recursivamente cada metade para obter (min, max) de cada parte
- Combina os resultados comparando os mínimos entre si e os máximos entre si
- Reduz significativamente o número de comparações em relação à busca sequencial

## Como Executar o Projeto

### Pré-requisitos
- Python 3.6 ou superior
- Nenhuma biblioteca externa necessária

### Passos para Execução

1. **Clone o repositório:**
```bash
git clone https://github.com/arthurcuri/maxmin.git
cd maxmin
```

2. **Execute o programa principal:**
```bash
python main.py
```

3. **Saída esperada:**
```
Min: -9
Max: 9
```

## Relatório Técnico

### 1. Análise da Complexidade Assintótica pelo Método de Contagem de Operações

#### Contagem Detalhada de Comparações

Vamos analisar o número de comparações realizadas pelo algoritmo MaxMin Select:

**Casos Base:**
- **n = 1**: 0 comparações (retorna o elemento diretamente)
- **n = 2**: 1 comparação (para determinar qual é menor e qual é maior)

**Caso Geral (n > 2):**
- Divide o problema em duas partes de tamanho ⌊n/2⌋ e ⌈n/2⌉
- Duas chamadas recursivas: T(⌊n/2⌋) + T(⌈n/2⌉) comparações
- Combinação dos resultados: 2 comparações (uma para min, uma para max)

**Função de Recorrência:**
```
T(1) = 0
T(2) = 1
T(n) = T(⌊n/2⌋) + T(⌈n/2⌉) + 2, para n > 2
```

**Resolução da Recorrência:**

Para simplificar, assumindo n = 2^k:
```
T(n) = 2T(n/2) + 2
```

Expandindo:
```
T(n) = 2T(n/2) + 2
     = 2[2T(n/4) + 2] + 2
     = 4T(n/4) + 4 + 2
     = 4T(n/4) + 6
     = 4[2T(n/8) + 2] + 6
     = 8T(n/8) + 8 + 6
     = 8T(n/8) + 14
```

Generalizando para k níveis:
```
T(n) = 2^k × T(n/2^k) + 2(2^k - 1)
```

Quando n/2^k = 2 (chegamos ao caso base), temos k = log₂(n) - 1:
```
T(n) = (n/2) × T(2) + 2(n/2 - 1)
     = (n/2) × 1 + 2(n/2 - 1)
     = n/2 + n - 2
     = 3n/2 - 2
```

**Resultado:** O algoritmo realiza **3n/2 - 2** comparações, resultando em complexidade temporal **O(n)**.

**Comparação com Abordagem Ingênua:**
- Busca sequencial: 2n - 2 comparações (n-1 para min + n-1 para max)
- MaxMin Select: 3n/2 - 2 comparações
- **Redução de aproximadamente 25% nas comparações**

### 2. Análise da Complexidade Assintótica pela Aplicação do Teorema Mestre

#### Identificação dos Parâmetros

Considerando a recorrência do MaxMin Select:
**T(n) = 2T(n/2) + O(1)**

Na fórmula padrão **T(n) = a·T(n/b) + f(n)**:

**1. Identificação dos valores:**
- **a = 2** (número de subproblemas recursivos)
- **b = 2** (fator de redução do tamanho)
- **f(n) = O(1)** (tempo de combinação - constante)

**2. Cálculo de log_b(a):**
```
log_b(a) = log₂(2) = 1
Portanto, p = 1
```

**3. Determinação do caso do Teorema Mestre:**

Temos f(n) = O(1) = O(n⁰)

Comparando com n^p = n¹:
- f(n) = O(n⁰) 
- n^p = n¹

Como f(n) = O(n^(p-ε)) onde ε = 1 > 0, estamos no **Caso 1** do Teorema Mestre.

**4. Solução assintótica:**

Pelo Caso 1 do Teorema Mestre:
**T(n) = Θ(n^p) = Θ(n¹) = Θ(n)**

#### Análise por Casos

**1. Melhor Caso: Θ(n)**
- Ocorre independentemente dos valores de entrada
- O algoritmo sempre realiza o mesmo padrão de divisões

**2. Caso Médio: Θ(n)**
- Comportamento consistente devido à natureza determinística
- Não há variação baseada na distribuição dos valores

**3. Pior Caso: Θ(n)**
- Mantém a mesma complexidade em qualquer cenário
- Superior à busca sequencial que realiza O(n) com constante maior

#### Complexidade Espacial

**Análise do Espaço:**
- **Pilha de recursão:** O(log n) níveis de profundidade
- **Variáveis por chamada:** O(1) espaço constante
- **Complexidade Espacial Total: O(log n)**

#### Comparação com Outras Abordagens

| Abordagem | Complexidade Temporal | Comparações | Complexidade Espacial |
|-----------|----------------------|-------------|----------------------|
| **Busca Sequencial** | O(n) | 2n - 2 | O(1) |
| **MaxMin Select** | O(n) | 3n/2 - 2 | O(log n) |
| **Eficiência** | Igual | **25% menos** | Maior |

## Autor

- **Nome**: Arthur Kramberger
- **Repositório**: https://github.com/arthurcuri/maxmin
- **Disciplina**: Fundamentos de Projeto e Análise de Algoritmos
- **Data**: Setembro de 2025
