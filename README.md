# Hackathon IDP 2023

Bem vindos, bem vindas ao HACKATHON IDP 2023!

Esse espaço é para o mentor prof Álvaro Campos Ferreira compartilhar seus pensamentos e código para ajudar os alunos que participarem desse evento! 

A princípio, quero apenas ter um lugar onde compartilhar minha contribuição para o evento.

Para início de conversa, vocês já devem conhecer os desafios e suas APIs associadas. Aqui estão para sua conveniência:

Informações sobre as APIs:

 - Desafio Restaurante

API: https://hackarestaurante-2023.azurewebsites.net/swagger/index.html 

 - Desafio Reserva

API: https://hackareservaespaco-2023.azurewebsites.net/swagger/index.html

Essas duas APIs devem ser utilizadas para criar soluções para os desafios apresentados. Você pode criar um Frontend, um aplicativo de linha de comando, internet das coisas, o céu é o limite. Mas sua aplicação deve ser capaz de interagir com essa API. Deixo aqui nesse repositório alguns scripts para ajudar nessa tarefa. 

Os scripts estão em Python, mas não é difícil encontrar scripts equivalentes em outras linguagens de programação.

Primeiro, para acessar uma API, vamos precisar fazer um request. Para isso, vamos usar a biblioteca requests:

```python
import requests
```

Antes de lidar com as APIs diretamente, vou mostrar como obter todos os end points de cada API usando a documentação delas. Cada API tem um link com as informações de cada end point. Os end points são os pontos onde vamos realizar nossos pedidos para API, seja para receber (GET) ou enviar (POST) recursos. Vamos obter os end points fazendo um request para a seguinte API:

```python
end_points = 'https://hackarestaurante-2023.azurewebsites.net/swagger/v1/swagger.json'
```

Para obter nossa resposta, vamos usar a função get() da biblioteca requests, atribuir a saída a uma variável chamada response, ou r. As informações sobre os end points estão no arquivo json que veio na resposta do nosso request.

```python
r = requests.get(end_points)
end_points = r.json()
paths = end_points['paths']
```

Agora temos uma nova variável que contém todos os end points para a nossa API do restaurante. 

As URLs das APIs em si, são as seguintes:

 - Desafio Restaurante

API: https://hackarestaurante-2023.azurewebsites.net/

 - Desafio Reserva

API: https://hackareservaespaco-2023.azurewebsites.net/

Podemos usar outrta variável para representar a URL da API do restaurante:

```python
restaurante = 'https://hackarestaurante-2023.azurewebsites.net'
```

Agora podemos usar nossa lista de caminhos para os end points (variável paths) para acessar os end points da nossa API:

```python
r = requests.get(rest+list(paths.keys())[0])
resposta = r.json()
print(resposta)
```

Essa é uma forma de interagir com uma API usando Python. Explore a variável end_points, ou vá direto aos sites com os end points abaixo para descobrir como o backend de nossa aplicação funciona, quais end points são GET ou POST. Para fazer requests de POST usando a biblioteca requests, use a função post(). 

Boa sorte!
