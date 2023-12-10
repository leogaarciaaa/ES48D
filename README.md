# Reconhecimento de imagens através da técnica Hu Moments

## Membros do projeto

*  Sander Henrique | RA: 2053861
*  Leonardo Garcia | RA: 2170736
*  Vinicius Ferreira | RA:

## Status: Concluído 🔨

## Links

* Vídeo: https://drive.google.com/file/d/1_xPFPsh5EML7kZrCJNSscRFHrVarXjpZ/view?usp=sharing

## Sobre Hu Moments

Hu Moments refere-se a uma técnica de análise de momentos invariantes desenvolvida por M. K. Hu na década de 1960. Essa técnica é frequentemente utilizada em visão computacional e processamento de imagem para extrair características invariantes de uma imagem em relação a rotações, escalas e translações. Os momentos de Hu são derivados dos momentos estatísticos tradicionais da distribuição de intensidade de pixels em uma imagem.Eles são calculados a partir de momentos de imagem, que são estatísticas calculadas a partir da distribuição de intensidades de pixels em uma imagem. São usados para capturar informações importantes sobre a forma e a distribuição de intensidades na imagem, tornando-os robustos em relação a transformações geométricas.

## Resultados

Foram obtidos resultados bem parecidos em MLP, RF e SVM, com acurácia entre 50% e 53%, considerando todas as imagens utilizadas.

* MLP

![image](https://github.com/leogaarciaaa/ES48D/assets/37093580/c368768d-469e-4bcb-a1fe-89761e2bb3e9)

  
* RF

![image](https://github.com/leogaarciaaa/ES48D/assets/37093580/0aee76bc-c084-43d5-ae1b-0969839ce4b8)

  
* SVM

![image](https://github.com/leogaarciaaa/ES48D/assets/37093580/a0cac3a5-c80d-4df8-a149-2e93a0fd7338)



## Passo a passo para reprodução

  * 1 - Baixe o dataset;
  * 2 - Coloque o conteúdo completo do dataset dentro da pasta "images_full"
  * 3 - Execute data_splitting.py
  * 4 - Renomeie o folder val para test, em: images_split/val
  * 5 - Execute huMoments_FeatureExtraction.py e run_all_classifiers.py.


