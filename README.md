# cifra-de-cesar
Segundo o Wikipedia, criptografia ou criptologia (em grego: kryptós, “escondido”, e gráphein, “escrita”) é o estudo e prática de princípios e técnicas para comunicação segura na presença de terceiros, chamados “adversários”. Mas geralmente, a criptografia refere-se à construção e análise de protocolos que impedem terceiros, ou o público, de lerem mensagens privadas. Muitos aspectos em segurança da informação, como confidencialidade, integridade de dados, autenticação e não-repúdio são centrais à criptografia moderna. Aplicações de criptografia incluem comércio eletrônico, cartões de pagamento baseados em chip, moedas digitais, senhas de computadores e comunicações militares. Das Criptografias mais curiosas na história da humanidade podemos citar a criptografia utilizada pelo grande líder militar romano Júlio César para comunicar com os seus generais. Essa criptografia se baseia na substituição da letra do alfabeto avançado um determinado número de casas. Por exemplo, considerando o número de casas = 3:

Normal: a ligeira raposa marrom saltou sobre o cachorro cansado

Cifrado: d oljhlud udsrvd pduurp vdowrx vreuh r fdfkruur fdqvdgr

--------------------------
# Pré-requisitos
Todas as bobliotecas utilizadas no projeto, normalmente já vem incluída no python, mas caso sua instalação seja "anormal", instale as seguintes bibliotecas:
- hashlib
- requests
- json

Detalhe, esse código não vai funcionar porque é necessario o endereço correto da API do Codenation

# Sobre
Esse script simples em Python decifra uma criptografia de Cesar com base na quantidade de casas passadas. Esse script foi utilizado em um desafio da codenation "http://codenation.dev/", onde é passado um Json por API com o seguinte formato:


{
	"numero_casas": 10,
	"token":"token_do_usuario",
	"cifrado": "texto criptografado",
	"decifrado": "aqui vai o texto decifrado",
	"resumo_criptografico": "aqui vai o resumo"
}

e com base nessas informações, é necessario decifrar o texto e gerar uma Hash sha1, em seguida, atualizar o Json e enviar para API do Codenation, a partir dai é gerado uma nota com base nesse trabalho.

Só para constar, fiquei com 100% hehe

Foi um trabalho que não será muito útil no dia a dia, mas serve para documentar meu aprendizado. Outra coisa que é importante ressaultar, é a primeira vez que utilizo o GitHub, então se não estiver bem organizado, documentado ou algo do tipo, peço que relevem, irem melhorar com a pratica!

Ate mais!
