# PI2-Vending-Machine

Repositório para os artefatos de software do grupo 6 na disciplina Projeto Integrador 2 - 2021.2

## Clonar repositório
`git clone git@github.com:Fealps/PI2-Vending-Machine.git && cd PI2-Vending-Machine`

## Criar arquivo .env 

![DeepinScreenshot_select-area_20220422215934](https://user-images.githubusercontent.com/12221656/164844926-dd6e9bfb-710c-41b4-a8fd-496ce57505ce.png)


Na raiz do projeto onde se encontra os arquivos de Docker crie um arquivo chamado `.env`. Dentro desse arquivo escreva:

`export POSTGRES_PASSWORD= 'suasenha' `

Substitua suasenha por uma senha que ache apropriada e salve o arquivo.

## Subir aplicação pela primeira vez 
`docker-compose up --build`

## Subir aplicação 
`docker-compose up`

## Acessar aplicação
 No navegador digite `http://localhost:8000/`
