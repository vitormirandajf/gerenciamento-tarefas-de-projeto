from flask import Flask, Response, request, jsonify

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
projetos = [
    {"id": 1, "nome": "Registro Brasileiro de Transplantes 2.0", "descricao": "A STEMIS, em parceria com a Magnus Tecnologia e com a Associação Brasileira de Transplante de Órgãos (ABTO), está desenvolvendo o segundo sistema do RBT (Registro Brasileiro de Transplantes). Nosso principal objetivo é criar uma ferramenta de gestão e armazenamento de dados para modernizar o processo de transplante no Brasil."},

    {"id": 2, "nome": "Vitrine Urbana", "descricao": "A STEMIS atua nas seguintes atividades em parceria empresa Vitrine Urbana Ltda. Desenvolvimento de Front-end, definição de modelos de inteligência artificial em aplicações de reconhecimento de imagens e previsão de preços de aluguel (comercial e residencial e ciência de dados para gestão de informação estratégica, como mapa de calor e etc)"},

    {"id": 3, "nome": "Automação aplicada a equipamentos industriais", "descricao":"A Stemis atua executando projetos de automação desde a sua concepção inicial até a implementação final em cenário industrial. Uma das nossas atividades hoje é a concepção, desenvolvimento, engenharia e fabricação de equipamentos fabris para confecção de estojos para joias em parceria com a Estojos Baldi que visa aumentar a produtividade na confecção de estojos, com estimativa de reduzir o tempo de produção atual em até 6x."},

    {"id": 4, "nome": "Automação aplicada a plantas de energia solar", "descricao":"A STEMIS desenvolve de forma eficaz o projeto de automação para Tracker. Os Trackers, também conhecidos como seguidores solares, possibilitam a movimentação dos módulos fotovoltaicos de forma a acompanhar o sol e otimizar o ângulo de incidência dos raios solares. O uso desta tecnologia é capaz de aumentar em até 50 a geração em comparação aos sistemas de estrutura fixa."}
]
tarefas = [
    #projeto 1
    {"id": 1, "projeto_id": 1, "titulo":"Cadastro de Pacientes","descricao": "Desenvolver um módulo para registrar informações detalhadas sobre os pacientes que necessitam de transplantes, incluindo nome, idade, histórico médico, tipo sanguíneo e informações de contato.", "observacoes":"", "concluida": "True"},

    {"id": 2, "projeto_id": 1, "titulo":"Cadastro de Doadores", "descricao": "Criar uma funcionalidade para cadastrar doadores de órgãos, coletando informações como nome, tipo sanguíneo, idade, histórico médico e informações de contato.", "observacoes":"", "concluida": "True"},

    {"id": 3, "projeto_id": 1, "titulo":"Gerenciamento de Listas de Espera", "descricao": "Desenvolver uma lista de espera para diferentes tipos de órgãos, garantindo que os pacientes sejam colocados na lista apropriada com base em critérios médicos.", "observacoes":"Módulo ainda necessita ajustes", "concluida": "False" },

    {"id": 4, "projeto_id": 1, "titulo":"Registro de Doações", "descricao": "Implementar um sistema para registrar doações de órgãos, incluindo informações sobre o órgão doado, data e local da doação e detalhes do doador.", "observacoes":"", "concluida": "True" },
    
    {"id": 5, "projeto_id": 1, "titulo":"Notificação Automática", "descricao": "Configurar um sistema de notificação automatizada para alertar os pacientes e equipes médicas sobre possíveis correspondências de doadores e procedimentos de transplante agendados.", "observacoes":"Módulo em desenvolvimento", "concluida": "False" },

    #projeto 2
    {"id": 6, "projeto_id": 2, "titulo":"Coleta e Pré-processamento de Dados", "descricao": "Coletar um grande conjunto de dados de imagens relevantes para a tarefa de reconhecimento. Realizar pré-processamento nas imagens, incluindo redimensionamento, normalização de cores e eliminação de ruídos.", "observacoes":"", "concluida": "True" },

    {"id": 7, "projeto_id": 2, "titulo":"Anotação de Dados", "descricao": "Anotar manualmente as imagens com rótulos precisos que descrevam o que está representado em cada imagem.", "observacoes":"Anotação manual feita até a imagem 576", "concluida": "False"},

    {"id": 8, "projeto_id": 2, "titulo":"Avaliação e Validação do Modelo", "descricao": "Avaliar o modelo usando métricas apropriadas, como precisão, recall, F1-score, e matriz de confusão.", "observacoes":"", "concluida": "False" },

    #projeto 3
    {"id": 9, "projeto_id": 3, "titulo":"Identificação de Necessidades e Requisitos", "descricao": "Realizar reuniões com os stakeholders para identificar as necessidades de automação e os requisitos específicos do projeto.", "observacoes":"", "concluida": "True" },
    
    {"id": 10, "projeto_id": 3, "titulo":"Análise de Viabilidade Técnica e Econômica", "descricao": "Realizar uma análise de viabilidade para determinar se a automação é apropriada para o processo industrial em questão, levando em consideração aspectos técnicos e econômicos.", "observacoes":"", "concluida": "True" },

    {"id": 11, "projeto_id": 3, "titulo":"Design Conceitual", "descricao": "Criar um design conceitual do sistema de automação, incluindo os principais componentes, como sensores, atuadores, controladores e interfaces de usuário.", "observacoes":"Design em fase inicial", "concluida": "False" },

    #projeto 4
    {"id": 12, "projeto_id": 4, "titulo":"Levantamento de Requisitos", "descricao": "Realizar um levantamento detalhado dos requisitos específicos da planta de energia solar, considerando a capacidade, a localização, os tipos de painéis solares, os sistemas de rastreamento solar, a topografia do terreno e outros fatores relevantes.", "observacoes":"", "concluida": "True" },

    {"id": 13, "projeto_id": 4, "titulo":"Design do Sistema de Monitoramento", "descricao": "Projetar o sistema de monitoramento que coletará dados das estações meteorológicas, inversores, sensores de irradiância solar e outros dispositivos relevantes.", "observacoes":"", "concluida": "True" },

    {"id": 14, "projeto_id": 4, "titulo":"Seleção de Sensores e Equipamentos", "descricao": "Escolher sensores adequados para medir a radiação solar, a temperatura dos painéis, a produção de energia, a direção e a intensidade do vento, entre outros parâmetros.", "observacoes":"", "concluida": "True" },

    {"id": 15, "projeto_id": 4, "titulo":"Desenvolvimento de Interface de Controle", "descricao": "Criar uma interface de controle que permita aos operadores monitorar o desempenho do sistema e tomar decisões informadas.", "observacoes":"", "concluida": "True" },
    
    {"id": 16, "projeto_id": 4, "titulo":"Desenvolvimento de Algoritmos de Previsão de Energia Solar", "descricao": "Desenvolver algoritmos de previsão que estimem a geração futura de energia com base nas condições meteorológicas previstas.", "observacoes":"", "concluida": "False" },
]

# Lista todos projetos
@app.route('/projetos', methods=['GET'])
def listar_projetos():
    return jsonify(projetos)

# Retorna um único projeto através de seu ID.
@app.route('/projetos/<int:id>', methods=['GET'])
def obter_projeto(id):
    projeto = next((projeto for projeto in projetos if projeto['id'] == id), None)
    if projeto is None:
        return jsonify({"mensagem": "Projeto não encontrado"}), 404
    return jsonify(projeto), 200

# Cria um novo projeto
@app.route('/projetos', methods=['POST'])
def criar_projeto():
    novo_projeto = request.get_json()
    if not novo_projeto or 'nome' not in novo_projeto or 'descricao' not in novo_projeto :
        return jsonify({"mensagem": "Dados incompletos"}), 400

    novo_projeto['id'] = len(projetos) + 1
    projetos.append(novo_projeto)
    return jsonify(novo_projeto), 201

#Atualiza o projeto a partir do seu ID
@app.route('/projetos/<int:id>', methods=['PUT'])
def atualizar_projeto(id):
    projeto = next((projeto for projeto in projetos if projeto['id'] == id), None)
    if projeto is None:
        return jsonify({"mensagem": "Projeto não encontrado"}), 404

    dados_atualizados = request.get_json()
    if not dados_atualizados or 'nome' not in dados_atualizados or 'descricao' not in dados_atualizados:
        return jsonify({"mensagem": "Dados incompletos"}), 400

    projeto['id'] = id
    projeto['nome'] = dados_atualizados['nome']
    projeto['descricao'] = dados_atualizados['descricao']

    return jsonify(projeto), 200

#Exclui um projeto apartir de seu ID
@app.route('/projetos/<int:id>', methods=['DELETE'])
def excluir_projeto(id):
    projeto = next((projeto for projeto in projetos if projeto['id'] == id), None)
    if projeto is None:
        return jsonify({"mensagem": "Projeto não encontrado"}), 404

    projetos.remove(projeto)
    return jsonify({"mensagem": "Projeto excluído com sucesso"})

# Cria uma tarefa a partir do id do projeto
@app.route('/projetos/<int:projeto_id>/tarefas', methods=['POST'])
def criar_tarefa_em_projeto(projeto_id):
    projeto = next((projeto for projeto in projetos if projeto['id'] == projeto_id), None)
    if projeto is None:
        return jsonify({"mensagem": "Projeto não encontrado"}), 404

    dados_tarefa = request.get_json()
    if not dados_tarefa or 'descricao' not in dados_tarefa or 'concluida' not in dados_tarefa:
        return jsonify({"mensagem": "Dados incompletos"}), 400

    nova_tarefa = {
        "id": len(tarefas) + 1,
        "titulo": dados_tarefa['titulo'],
        "projeto_id": projeto_id,
        "descricao": dados_tarefa['descricao'],
        "concluida": dados_tarefa['concluida']
    }

    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201, {'Content-Type': 'application/json; charset=utf-8'}

# Retorna todas as tarefas do projeto pelo ID do projeto.
@app.route('/projetos/<int:id>/tarefas', methods=['GET'])
def listar_tarefas_do_projeto(id):
    tarefas_do_projeto = [tarefa for tarefa in tarefas if tarefa['projeto_id'] == id]
    return jsonify(tarefas_do_projeto), 200

# Retorna uma apenas uma tarefa específica de um projeto pelo ID do projeto + ID da tarefa.
@app.route('/projetos/<int:projeto_id>/tarefas/<int:tarefa_id>', methods=['GET'])
def obter_tarefa_do_projeto(projeto_id, tarefa_id):
    projeto = next((projeto for projeto in projetos if projeto['id'] == projeto_id), None)
    if projeto is None:
        return jsonify({"mensagem": "Projeto não encontrado"}), 404

    tarefa = next((tarefa for tarefa in tarefas if tarefa['projeto_id'] == projeto_id and tarefa['id'] == tarefa_id), None)
    if tarefa is None:
        return jsonify({"mensagem": "Tarefa não encontrada"}), 404

    return jsonify(tarefa)

# Atualiza uma tarefa específica pelo ID
@app.route('/projetos/<int:projeto_id>/tarefas/<int:tarefa_id>', methods=['PUT'])
def atualizar_tarefa(projeto_id, tarefa_id):
    projeto = next((projeto for projeto in projetos if projeto['id'] == projeto_id), None)
    if projeto is None:
        return jsonify({"mensagem": "Projeto não encontrado"}), 404
    
    tarefa = next((tarefa for tarefa in tarefas if tarefa['projeto_id'] == projeto_id and tarefa['id'] == tarefa_id), None)
    if tarefa is None:
        return jsonify({"mensagem": "Tarefa não encontrada"}), 404

    dados_atualizados = request.get_json()
    if not dados_atualizados or 'descricao' not in dados_atualizados or 'concluida' not in dados_atualizados:
        return jsonify({"mensagem": "Dados incompletos"}), 400

    tarefa['descricao'] = dados_atualizados['descricao']
    tarefa['concluida'] = dados_atualizados['concluida']
    tarefa['titulo'] = dados_atualizados.get('titulo', tarefa.get('titulo'))
    tarefa['observacoes'] = dados_atualizados.get('observacoes', tarefa.get('observacoes'))

    return jsonify(tarefa), 200

# Deleta uma tarefa específica pelo ID
@app.route('/projetos/<int:projeto_id>/tarefas/<int:tarefa_id>', methods=['DELETE'])
def excluir_tarefa(projeto_id, tarefa_id):
    projeto = next((projeto for projeto in projetos if projeto['id'] == projeto_id), None)
    if projeto is None:
        return jsonify({"mensagem": "Projeto não encontrado"}), 404
    
    tarefa = next((tarefa for tarefa in tarefas if tarefa['projeto_id'] == projeto_id and tarefa['id'] == tarefa_id), None)
    if tarefa is None:
        return jsonify({"mensagem": "Tarefa não encontrada"}), 404

    tarefas.remove(tarefa)
    return jsonify({"mensagem": "Tarefa excluída com sucesso"}), 200

app.run()





