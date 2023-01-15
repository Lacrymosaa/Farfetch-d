# PokeAutoFarm
 Auto farm for pokemon

 STEP BY STEP HOW FARM:
 - Andar para direta
 - Andar para esquerda
 - Se encontrar lute
 - Se encontrar raro pare
 - Após fechar batalha continue
Diagram. 

O programa tende a falhar e deve ser configurado diferentemente de jogo pra jogo e de tamanho de tela para outro diferente.

ESTE PROGRAMA É FEITO UNICO E EXCLUSIVAMENTE PARA ESTUDOS

Patch Notes 1.1:
- Tentativa de melhora na identificação faz com que a linha 34 precise ser ajustada para uso. Por isso,
será incluso nesta pasta o "where.py" que mostrada a posição do seu mouse para dar ao programa as devidas
informações de coordenada. 
Quando tiver 2 coordenadas: é necessario apenas o ponto central de um botão ou espaço.
Quando houver 4: é necessario um ponto inicial (DEVE SER o ponto superior direito) e o X e Y seguintes mostrarão quantos pixels para o lado e para baixo, respectivamente, serão usado na imagem. Isso aumenta consideravelmente a precisão do programa mas ainda é necessario um ajuste dependendo do pokémon escolhido.

Patch Notes 1.2:
- Melhorias na função de andar, que antes concluia um ciclo de direita e esquerda e depois verificava. Agora faz apenas 1 direção e verifica. 
- Retirada função if de batalha, que causava um delay consideravel para verificação, sendo agora uma chamada de função. 
- Testes estão sendo realizados no reconhecimento de pokemon utilizando cores agora. No momento utilize where.py e pegue R G ou B no valor correspondente. Explicações dentro do código.

Patch Note 15/01/23:
- Melhoria na manutenção do programa e reformulação do passe.
 
