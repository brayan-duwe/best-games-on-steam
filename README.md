# Best Games on Steam 👾

[[EN-US 🇺🇸]](#best-games-on-steam-) | [ [PT-BR 🇧🇷]](#best-games-on-steam--português-br-)  

Project that fetches game data from the SteamSpy API and analyzes it to find the best-rated/most popular games.

## [🌐 Project website](https://best-games-on-steam.streamlit.app)

## How to run the app 💡
1. Clone the repository
2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the app:
    ```bash
    streamlit run src/app.py
    ```


## About the project ✍🏽

- The project was built in Python using Streamlit and Pandas. 
- It consists of a list of games from Steam, with their prices, and reviews, and you can filter them to find some specific games.

The API used for this project was [SteamSpy API](https://steamspy.com/api.php?). The content from this API was fetched, and saved on [raw_data.json](/data/raw_data.json), and it makes it easier to deal with a .json file.

For this project, I used 4 types of filters:
- **Segmented control:** Filters games based on their prices "All | Free | Paid".
  <img width="236" height="98" alt="Segmented control filter" src="https://github.com/user-attachments/assets/70e31b75-d633-460e-92d7-105ce09d1995" />
- **Slider:** Filters games based on a range.
  <img width="379" height="91" alt="Slider filter" src="https://github.com/user-attachments/assets/252cb9cf-7f65-4f1a-9bb6-1964e353c693" />
- **Radio:** Filters games based on their reviews "Positive | Mostly positive | Neutral | Mostly negative".
  <img width="195" height="162" alt="Radio filter" src="https://github.com/user-attachments/assets/2bbde486-5ab7-4fdb-a127-de12fee1f241" />
- **Text input:** Filters games based on their names.
  <img width="1429" height="106" alt="Image" src="https://github.com/user-attachments/assets/2530b2eb-e18f-4a67-8a31-1496724389c3" />

****

## Best Games on Steam 👾 [Português BR 🇧🇷]

Projeto que busca os dados da API SteamSpy e analiza para encontrar os mais bem avaliados jogos.

## [🌐 Site do projeto](https://best-games-on-steam.streamlit.app)

## Como rodar o app 💡
1. Clone o repositório
2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
3. Rode o app:
    ```bash
    streamlit run src/app.py
    ```

## Sobre o projeto ✍🏽

- O projeto foi construído em Python usando os frameworks Streamlit e Pandas.
- Consiste em uma lista de jogos da Steam, com seus respectiovs preços e avaliações, e você pode filtrar à fim de encontrar jogos específicos. 

A API utilizada para esse projeto foi a [SteamSpy API](https://steamspy.com/api.php?). O conteúdo dessa API foi extraído e salvo no [raw_data.json](/data/raw_data.json), tornando mais fácil de lidar com um arquivo .json.

Para esse projeto, eu usei 4 tipos de filtros:
- **Segmented control:** Filtra jogos baseado em seus preços "All | Free | Paid".
  <img width="236" height="98" alt="Segmented control filter" src="https://github.com/user-attachments/assets/70e31b75-d633-460e-92d7-105ce09d1995" />
- **Slider:** Filtra jogos baseado em um limite de preço.
  <img width="379" height="91" alt="Slider filter" src="https://github.com/user-attachments/assets/252cb9cf-7f65-4f1a-9bb6-1964e353c693" />
- **Radio:** Filtra jogos baseado em suas avaliações "Positive | Mostly positive | Neutral | Mostly negative".
  <img width="195" height="162" alt="Radio filter" src="https://github.com/user-attachments/assets/2bbde486-5ab7-4fdb-a127-de12fee1f241" />
- **Text input:** Filtra jogos baseado em seus nomes.
  <img width="1429" height="106" alt="Image" src="https://github.com/user-attachments/assets/2530b2eb-e18f-4a67-8a31-1496724389c3" />