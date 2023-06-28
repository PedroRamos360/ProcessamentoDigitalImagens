# Trabalho final Processamento Digital de Imagens
## Detector de porta trancada

### Tentativa 1 - Detectar bordas da imagem
A primeira tentativa para detectar se a porta estava trancada ou não foi usar um gaussian blur
e em seguida o algoritmo de detecção de bordas de canny do cv2 para verificar se era possível
identificar a tranca da porta na imagem trancada que não existia na imagem destrancada. Pode
ser até que essa alternativa seria possível, mas logo percebi que provavelmente não seria tão
preciso e seria mais complexo de implementar

### Tentativa 2 - Filtrar a cor da tranca da porta
A segunda tentativa foi mais eficiente, agora é filtrado a variação de rgbs de cinza que tem maior
concentração na tranca da porta, em seguida é contado a quantidade de pixels a partir dessa filtragem
e comparado com a imagem destrancada, como na porta destrancada a tranca não será visível, é esperado
que a porta trancada tenha mais pixeis que a destrancada. O problema desta tentativa se dá por conta
da variação de cor pela iluminação diferente.

### Tentativa 3 - Detectar tranca da porta por machine learning