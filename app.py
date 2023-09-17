from flask import Flask, Response, request

projetos = [
    {"id": 1, "nome": "Registro Brasileiro de Transplantes 2.0", "descricao": "A STEMIS, em parceria com a Magnus Tecnologia e com a Associação Brasileira de Transplante de Órgãos (ABTO), está desenvolvendo o segundo sistema do RBT (Registro Brasileiro de Transplantes). Nosso principal objetivo é criar uma ferramenta de gestão e armazenamento de dados para modernizar o processo de transplante no Brasil."},

    {"id": 2, "nome": "Vitrine Urbana", "descricao": "A STEMIS atua nas seguintes atividades em parceria empresa Vitrine Urbana Ltda. Desenvolvimento de Front-end, definição de modelos de inteligência artificial em aplicações de reconhecimento de imagens e previsão de preços de aluguel (comercial e residencial e ciência de dados para gestão de informação estratégica, como mapa de calor e etc)"},

    {"id": 3, "nome": "Automação aplicada a equipamentos industriais", "descricao":"A Stemis atua executando projetos de automação desde a sua concepção inicial até a implementação final em cenário industrial. Uma das nossas atividades hoje é a concepção, desenvolvimento, engenharia e fabricação de equipamentos fabris para confecção de estojos para joias em parceria com a Estojos Baldi que visa aumentar a produtividade na confecção de estojos, com estimativa de reduzir o tempo de produção atual em até 6x."},

    {"id": 4, "nome": "Automação aplicada a plantas de energia solar", "descricao":"A STEMIS desenvolve de forma eficaz o projeto de automação para Tracker. Os Trackers, também conhecidos como seguidores solares, possibilitam a movimentação dos módulos fotovoltaicos de forma a acompanhar o sol e otimizar o ângulo de incidência dos raios solares. O uso desta tecnologia é capaz de aumentar em até 50 a geração em comparação aos sistemas de estrutura fixa."}
]
tarefas = [
    #projeto 1
    {"id": 1, "projeto_id": 1, "titulo":"Cadastro de Pacientes","descricao": "Desenvolver um módulo para registrar informações detalhadas sobre os pacientes que necessitam de transplantes, incluindo nome, idade, histórico médico, tipo sanguíneo e informações de contato.", "observações":"", "concluida": True},

    {"id": 2, "projeto_id": 1, "titulo":"Cadastro de Doadores", "descricao": "Criar uma funcionalidade para cadastrar doadores de órgãos, coletando informações como nome, tipo sanguíneo, idade, histórico médico e informações de contato.", "observações":"", "concluida": True},

    {"id": 3, "projeto_id": 1, "titulo":"Gerenciamento de Listas de Espera", "descricao": "Desenvolver uma lista de espera para diferentes tipos de órgãos, garantindo que os pacientes sejam colocados na lista apropriada com base em critérios médicos.", "observações":"Módulo ainda necessita ajustes", "concluida": False },

    {"id": 4, "projeto_id": 1, "titulo":"Registro de Doações", "descricao": "Implementar um sistema para registrar doações de órgãos, incluindo informações sobre o órgão doado, data e local da doação e detalhes do doador.", "observações":"", "concluida": True },
    
    {"id": 5, "projeto_id": 1, "titulo":"Notificação Automática", "descricao": "Configurar um sistema de notificação automatizada para alertar os pacientes e equipes médicas sobre possíveis correspondências de doadores e procedimentos de transplante agendados.", "observações":"Módulo em desenvolvimento", "concluida": False },

    #projeto 2
    {"id": 6, "projeto_id": 2, "titulo":"Coleta e Pré-processamento de Dados", "descricao": "Coletar um grande conjunto de dados de imagens relevantes para a tarefa de reconhecimento. Realizar pré-processamento nas imagens, incluindo redimensionamento, normalização de cores e eliminação de ruídos.", "observações":"", "concluida": True },

    {"id": 7, "projeto_id": 2, "titulo":"Anotação de Dados", "descricao": "Anotar manualmente as imagens com rótulos precisos que descrevam o que está representado em cada imagem.", "observações":"Anotação manual feita até a imagem 576", "concluida": False},

    {"id": 8, "projeto_id": 2, "titulo":"Avaliação e Validação do Modelo", "descricao": "Avaliar o modelo usando métricas apropriadas, como precisão, recall, F1-score, e matriz de confusão.", "observações":"", "concluida": False },

    #projeto 3
    {"id": 9, "projeto_id": 3, "titulo":"Identificação de Necessidades e Requisitos", "descricao": "Realizar reuniões com os stakeholders para identificar as necessidades de automação e os requisitos específicos do projeto.", "observações":"", "concluida": True },
    
    {"id": 10, "projeto_id": 3, "titulo":"Análise de Viabilidade Técnica e Econômica", "descricao": "Realizar uma análise de viabilidade para determinar se a automação é apropriada para o processo industrial em questão, levando em consideração aspectos técnicos e econômicos.", "observações":"", "concluida": True },

    {"id": 11, "projeto_id": 3, "titulo":"Design Conceitual", "descricao": "Criar um design conceitual do sistema de automação, incluindo os principais componentes, como sensores, atuadores, controladores e interfaces de usuário.", "observações":"Design em fase inicial", "concluida": False },

    #projeto 4
    {"id": 12, "projeto_id": 4, "titulo":"Levantamento de Requisitos", "descricao": "Realizar um levantamento detalhado dos requisitos específicos da planta de energia solar, considerando a capacidade, a localização, os tipos de painéis solares, os sistemas de rastreamento solar, a topografia do terreno e outros fatores relevantes.", "observações":"", "concluida": True },

    {"id": 13, "projeto_id": 4, "titulo":"Design do Sistema de Monitoramento", "descricao": "Projetar o sistema de monitoramento que coletará dados das estações meteorológicas, inversores, sensores de irradiância solar e outros dispositivos relevantes.", "observações":"", "concluida": True },

    {"id": 14, "projeto_id": 4, "titulo":"Seleção de Sensores e Equipamentos", "descricao": "Escolher sensores adequados para medir a radiação solar, a temperatura dos painéis, a produção de energia, a direção e a intensidade do vento, entre outros parâmetros.", "observações":"", "concluida": True },

    {"id": 15, "projeto_id": 4, "titulo":"Desenvolvimento de Interface de Controle", "descricao": "Criar uma interface de controle que permita aos operadores monitorar o desempenho do sistema e tomar decisões informadas.", "observações":"", "concluida": True },
    
    {"id": 16, "projeto_id": 4, "titulo":"Desenvolvimento de Algoritmos de Previsão de Energia Solar", "descricao": "Desenvolver algoritmos de previsão que estimem a geração futura de energia com base nas condições meteorológicas previstas.", "observações":"", "concluida": False },
]
app = Flask(__name__)

app.run()





