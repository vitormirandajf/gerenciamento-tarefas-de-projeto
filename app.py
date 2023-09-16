from flask import Flask, Response, request

projetos = [
    {"id": 1, "nome": "Registro Brasileiro de Transplantes 2.0", "descricao": "A STEMIS, em parceria com a Magnus Tecnologia e com a Associação Brasileira de Transplante de Órgãos (ABTO), está desenvolvendo o segundo sistema do RBT (Registro Brasileiro de Transplantes). Nosso principal objetivo é criar uma ferramenta de gestão e armazenamento de dados para modernizar o processo de transplante no Brasil."},
    {"id": 2, "nome": "Vitrine Urbana", "descricao": "A STEMIS atua nas seguintes atividades em parceria empresa Vitrine Urbana Ltda.Desenvolvimento de Front-end, definição de modelos de inteligência artificial em aplicações de reconhecimento de imagens e previsão de preços de aluguel (comercial e residencial e ciência de dados para gestão de informação estratégica, como mapa de calor e etc)"},
    {"id": 3, "nome": "Automação aplicada a equipamentos industriais", "descricao":"A Stemis atua executando projetos de automação desde a sua concepção inicial até a implementação final em cenário industrial. Uma das nossas atividades hoje é a concepção, desenvolvimento, engenharia e fabricação de equipamentos fabris para confecção de estojos para joias em parceria com a Estojos Baldi que visa aumentar a produtividade na confecção de estojos, com estimativa de reduzir o tempo de produção atual em até 6x."},
    {"id": 4, "nome": "Automação aplicada a plantas de energia solar", "descricao":"A STEMIS desenvolve de forma eficaz o projeto de automação para Tracker. Os Trackers, também conhecidos como seguidores solares, possibilitam a movimentação dos módulos fotovoltaicos de forma a acompanhar o sol e otimizar o ângulo de incidência dos raios solares. O uso desta tecnologia é capaz de aumentar em até 50 a geração em comparação aos sistemas de estrutura fixa."}
]
tarefas = [
    {"id": 1, "projeto_id": "", "descricao": "", "concluida": False},
    {"id": 2, "projeto_id": "", "descricao": "", "concluida": False},
    {"id": 3, "projeto_id": "", "descricao": "", "concluida": True},
]
app = Flask(__name__)

app.run()





