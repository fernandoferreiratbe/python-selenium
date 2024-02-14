# Python & Selenium
Repositório criado para proporcionar um teste utilizando [Python](https://pypi.org/project/selenium/) & [Selenium](https://www.selenium.dev/)

## Objetivo
O objetivo é criar um script que solicite um cep para o usuário e vá de modo interativo até o site dos [Correios](https://buscacepinter.correios.com.br/app/endereco/index.php)
e traga o endereço completo para o cep indicado como parâmetro.

### Execução no MacOS

```
python3 -m vevn .venv 
source .venv/bin/activate
pip install --upgrade pip 
pip install -r requirements.txt
python main.py
```

### Notas

- O script inicial foi gerado via chat gpt 3.5
- Foram feitas correções na identificação do campo cep na pagina inicial
- Foram feitas correções na extração dos dados da tabela
- Foi feito ajuste na chamado do método find_element_by_xpath para **_find_element(By.Resource, value)_**
- Versão do Python utilizada 3.11.7
- É necessário instalar o chromedriver (pressuponho que utilizará o Google Chrome para realizar o teste). A versão do meu navegador durante o teste foi a 121.0.6167.160. 
  * ```$ curl -o chromedriver.zip https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/121.0.6167.85/mac-x64/chromedriver-mac-x64.zip ```
