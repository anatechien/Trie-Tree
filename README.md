## Complexidade
- buscar um prefixo de tamanho m custa O(m). E esse custo não depende de quantas palavras existem no dicionário.
- Depois de chegar ao nó do prefixo, coletar as sugestões custa o tamanho do que você percorrer abaixo dele.
- A referência para cada nó filho é em estrutura de dicionário porque dessa forma a busca pelo char dentro das referências é O(1).
-  