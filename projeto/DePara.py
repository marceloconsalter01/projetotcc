from projeto.models import UpdateMongo, getdata


def translatedb(consulta):
    try:
        # -------------------- checking_status
        if consulta["checking_status"] == "<0":
            consulta["checking_status"] = 'Menor que zero'
        elif consulta["checking_status"] == "0<=X<200":
            consulta["checking_status"] = 'Entre zero e duzentos'
        elif consulta["checking_status"] == "'no checking'":
            consulta["checking_status"] = 'Não possui conta'
        elif consulta["checking_status"] == ">=200":
            consulta["checking_status"] = 'Maior ou igual a duzentos'
        print(consulta["checking_status"])

        # -------------------- credit_history
        if consulta["credit_history"] == "'critical/other existing credit'":
            consulta["credit_history"] = 'Conta crítica em outros bancos'
        elif consulta["credit_history"] == "'existing paid'":
            consulta["credit_history"] = 'Créditos existentes, porém pagos'
        elif consulta["credit_history"] == "'no credits/all paid'":
            consulta["credit_history"] = 'Empréstimos nessa instuição pagos'
        elif consulta["credit_history"] == "'all paid'":
            consulta["credit_history"] = 'Sem empréstimos atualmente'
        elif consulta["credit_history"] == "'delayed previously'":
            consulta["credit_history"] = 'Adiado anteriormente'
        print(consulta["credit_history"])

        # -------------------- purpose
        if consulta["purpose"] == "radio/tv":
            consulta["purpose"] = 'Televisão'
        elif consulta["purpose"] == "education":
            consulta["purpose"] = 'Educação'
        elif consulta["purpose"] == "furniture/equipment":
            consulta["purpose"] = 'Móveis/Equipamentos'
        elif consulta["purpose"] == "'new car'":
            consulta["purpose"] = 'Carro novo'
        elif consulta["purpose"] == "'used car'":
            consulta["purpose"] = 'Carro usado'
        elif consulta["purpose"] == "business":
            consulta["purpose"] = 'Negócios'
        elif consulta["purpose"] == "'domestic appliance'":
            consulta["purpose"] = 'Mobília'
        elif consulta["purpose"] == "repairs":
            consulta["purpose"] = 'Reparos'
        elif consulta["purpose"] == "other":
            consulta["purpose"] = 'Outros'
        elif consulta["purpose"] == "retraining":
            consulta["purpose"] = 'Reciclagem'
        print(consulta["purpose"])

        # -------------------- savings_status
        if consulta["savings_status"] == "'no known savings'":
            consulta["savings_status"] = "'Nenhuma conta corrente'"
        elif consulta["savings_status"] == "<100":
            consulta["savings_status"] = 'Menos que R$100,00'
        elif consulta["savings_status"] == "500<=X<1000":
            consulta["savings_status"] = 'Entre R$500,00 e R$1.000,00'
        elif consulta["savings_status"] == ">=1000":
            consulta["savings_status"] = 'Mais que R$1.000,00'
        elif consulta["savings_status"] == "100<=X<500":
            consulta["savings_status"] = 'Entre R$100 e R$500,00 '
        print(consulta["savings_status"])

        # -------------------- employment
        if consulta["employment"] == ">=7":
            consulta["employment"] = 'Mais que 7 anos'
        elif consulta["employment"] == "1<=X<4":
            consulta["employment"] = 'Entre 1 à 4 anos'
        elif consulta["employment"] == "4<=X<7":
            consulta["employment"] = 'Entre 4 à 7 anos'
        elif consulta["employment"] == "unemployed":
            consulta["employment"] = 'Desempregado'
        elif consulta["employment"] == "<1":
            consulta["employment"] = 'Menos que 1 ano'
        print(consulta["employment"])

        # -------------------- personal_status
        if consulta["personal_status"] == "'male single'":
            consulta["personal_status"] = "'Masculino e solteiro'"
        elif consulta["personal_status"] == "'female div/dep/mar'":
            consulta["personal_status"] = 'Feminino e Divorciado/Separado/Casado'
        elif consulta["personal_status"] == "'male div/sep'":
            consulta["personal_status"] = 'Masculino e Divorciado/Separado'
        elif consulta["personal_status"] == "'male mar/wid'":
            consulta["personal_status"] = 'Masculino e Casado/Viúvo'
        elif consulta["personal_status"] == "'female single'":
            consulta["personal_status"] = 'Feminino e Solteiro'
        print(consulta["personal_status"])

        # -------------------- other_parties
        if consulta["other_parties"] == "none":
            consulta["other_parties"] = 'Nenhum'
        elif consulta["other_parties"] == "guarantor":
            consulta["other_parties"] = 'Fiador'
        elif consulta["other_parties"] == "'co applicant'":
            consulta["other_parties"] = 'Cofiador'
        print(consulta["other_parties"])

        # -------------------- residence_since
        if consulta["residence_since"] == "1":
            consulta["residence_since"] = '1 Ano'
        elif consulta["residence_since"] == "2":
            consulta["residence_since"] = '2 Anos'
        elif consulta["residence_since"] == "3":
            consulta["residence_since"] = '3 Anos'
        elif consulta["residence_since"] == "4":
            consulta["residence_since"] = '4 Anos ou mais'
        print(consulta["residence_since"])

        # -------------------- property_magnitude
        if consulta["property_magnitude"] == "'real estate'":
            consulta["property_magnitude"] = 'Imovéis'
        elif consulta["property_magnitude"] == "'life insurance'":
            consulta["property_magnitude"] = 'Seguro de vida'
        elif consulta["property_magnitude"] == "'no known property'":
            consulta["property_magnitude"] = 'Sem propriedades'
        elif consulta["property_magnitude"] == "car":
            consulta["property_magnitude"] = 'Carro'
        print(consulta["property_magnitude"])

        # -------------------- other_payment_plans
        if consulta["other_payment_plans"] == "none":
            consulta["other_payment_plans"] = 'Nenhum'
        elif consulta["other_payment_plans"] == "bank":
            consulta["other_payment_plans"] = 'Bancos'
        elif consulta["other_payment_plans"] == "stores":
            consulta["other_payment_plans"] = 'Lojas'
        print(consulta["other_payment_plans"])

        # -------------------- housing
        if consulta["housing"] == "own":
            consulta["housing"] = 'Próprio'
        elif consulta["housing"] == "'for free'":
            consulta["housing"] = 'De graça'
        elif consulta["housing"] == "rent":
            consulta["housing"] = 'Alugada'
        print(consulta["housing"])

        # -------------------- existing_credits
        if consulta["existing_credits"] == "0":
            consulta["existing_credits"] = 'Nenhum'
        elif consulta["existing_credits"] == "1":
            consulta["existing_credits"] = '1'
        elif consulta["existing_credits"] == "2":
            consulta["existing_credits"] = '2'
        elif consulta["existing_credits"] == "3":
            consulta["existing_credits"] = '3'
        elif consulta["existing_credits"] == "4":
            consulta["existing_credits"] = '4 ou mais'
        print(consulta["existing_credits"])

        # -------------------- job
        if consulta["job"] == "skilled":
            consulta["job"] = 'Funcionário'
        elif consulta["job"] == "'unskilled resident'":
            consulta["job"] = 'Não qualificado'
        elif consulta["job"] == "'high qualif/self emp/mgmt'":
            consulta["job"] = 'Administrador / autônomo'
        elif consulta["job"] == "'unemp/unskilled non res'":
            consulta["job"] = 'Desempregado'
        print(consulta["job"])

        # -------------------- num_dependents
        if consulta["num_dependents"] == "0":
            consulta["num_dependents"] = 'Nenhum'
        elif consulta["num_dependents"] == "1":
            consulta["num_dependents"] = '1'
        elif consulta["num_dependents"] == "2":
            consulta["num_dependents"] = '2 ou mais'
        print(consulta["num_dependents"])

        # -------------------- own_telephone
        if consulta["own_telephone"] == "yes":
            consulta["own_telephone"] = 'Sim'
        elif consulta["own_telephone"] == "none":
            consulta["own_telephone"] = 'Nenhum'
        print(consulta["num_dependents"])

        # -------------------- foreign_worker
        if consulta["foreign_worker"] == "yes":
            consulta["foreign_worker"] = 'Sim'
        elif consulta["foreign_worker"] == "no":
            consulta["foreign_worker"] = 'Não'
        print(consulta["foreign_worker"])

        return consulta
    except:
        erro = "CPF não cadastrado"

        return erro


def translateupdate(selecao_nome, selecao_cpf, selecao_email, selecao_1,
                    selecao_2, selecao_3, selecao_4, selecao_5, selecao_6, selecao_7, selecao_8, selecao_9, selecao_10,
                    selecao_11, selecao_12, selecao_13, selecao_14, selecao_15, selecao_16, selecao_17, selecao_18,
                    selecao_19, selecao_20):
    # --------- Status da Conta Corrente
    if selecao_1 == 'Menor que zero':
        selecao_1 = "<0"
    elif selecao_1 == 'Entre zero e duzentos':
        selecao_1 = "0<=X<200"
    elif selecao_1 == 'Não possui conta':
        selecao_1 = "'no checking'"
    elif selecao_1 == 'Maior ou igual a duzentos':
        selecao_1 = ">=200"

    # --------- Histórico de crédito
    if selecao_3 == 'Conta crítica em outros bancos':
        selecao_3 = "'critical/other existing credit'"
    elif selecao_3 == 'Créditos existentes, porém pagos':
        selecao_3 = "'existing paid'"
    elif selecao_3 == 'Empréstimos nessa instuição pagos':
        selecao_3 = "'no credits/all paid'"
    elif selecao_3 == 'Sem empréstimos atualmente':
        selecao_3 = "'all paid'"
    elif selecao_3 == 'Adiado anteriormente':
        selecao_3 = "'delayed previously'"

    # --------- Objetivos
    if selecao_4 == 'Televisão':
        selecao_4 = "radio/tv"
    elif selecao_4 == 'Educação':
        selecao_4 = "education"
    elif selecao_4 == 'Móveis/Equipamentos':
        selecao_4 = "furniture/equipment"
    elif selecao_4 == 'Carro novo':
        selecao_4 = "'new car'"
    elif selecao_4 == 'Carro Usado':
        selecao_4 = "'used car'"
    elif selecao_4 == 'Negócios':
        selecao_4 = "business"
    elif selecao_4 == 'Mobília':
        selecao_4 = "'domestic appliance'"
    elif selecao_4 == 'Reparos':
        selecao_4 = "repairs"
    elif selecao_4 == 'Outros':
        selecao_4 = "other"
    elif selecao_4 == 'Reciclagem':
        selecao_4 = "retraining"

    # --------- Valor em conta poupança
    if selecao_6 == "'Nenhuma conta corrente'":
        selecao_6 = "'no known savings'"
    elif selecao_6 == "'Menos que R$100,00'":
        selecao_6 = "<100"
    elif selecao_6 == "'Entre R$500,00 e R$1.000,00'":
        selecao_6 = "500<=X<1000"
    elif selecao_6 == "'Mais que R$1.000,00'":
        selecao_6 = ">=1000"
    elif selecao_6 == "'Entre R$100 e R$500,00'":
        selecao_6 = "100<=X<500"

    # --------- Tempo de trabalho no emprego atual
    if selecao_7 == 'Entre 1 à 4 anos':
        selecao_7 = "1<=X<4"
    elif selecao_7 == 'Entre 4 à 7 anos':
        selecao_7 = "4<=X<7"
    elif selecao_7 == 'Desempregado':
        selecao_7 = "unemployed"
    elif selecao_7 == 'Menos que 1 ano':
        selecao_7 = "<1"
    elif selecao_7 == 'Mais que 7 anos':
        selecao_7 = ">=7"

    # --------- Estado civil e gênero
    if selecao_9 == "'Masculino e solteiro'":
        selecao_9 = "'male single'"
    elif selecao_9 == "'Feminino e Divorciado/Separado/Casado'":
        selecao_9 = "'female div/dep/mar'"
    elif selecao_9 == "'Masculino e Divorciado/Separado'":
        selecao_9 = "'male div/sep'"
    elif selecao_9 =="'Masculino e Casado/Viúvo'":
        selecao_9 = "'male mar/wid'"
    elif selecao_9 == "'Feminino e Solteiro'":
        selecao_9 = "'female single'"

    # --------- Fiador/Outras partes envolvidas
    if selecao_10 == 'Nenhum':
        selecao_10 = "none"
    elif selecao_10 == 'Fiador':
        selecao_10 = "guarantor"
    elif selecao_10 == 'Cofiador':
        selecao_10 = "'co applicant'"

    # --------- Reside no mesmo lugar desde
    if selecao_11 == '1 Ano':
        selecao_11 = "1"
    elif selecao_11 == '2 Anos':
        selecao_11 = "2"
    elif selecao_11 == '3 Anos':
        selecao_11 = "3"
    elif selecao_11 == '4 Anos ou mais':
        selecao_11 = "4"

    # --------- Propriedades
    if selecao_12 == 'Imovéis':
        selecao_12 = "'real estate'"
    elif selecao_12 == 'Seguro de vida':
        selecao_12 = "'life insurance'"
    elif selecao_12 == 'Sem propriedades':
        selecao_12 = "'no known property'"
    elif selecao_12 == 'Carro':
        selecao_12 = "car"

    # --------- Outros parcelamentos
    if selecao_14 == 'Nenhum':
        selecao_14 = "none"
    elif selecao_14 == 'Bancos':
        selecao_14 = "bank"
    elif selecao_14 == 'Lojas':
        selecao_14 = "stores"

    # --------- Habitação
    if selecao_15 == 'Próprio':
        selecao_15 = "own"
    elif selecao_15 == 'De graça':
        selecao_15 = "'for free'"
    elif selecao_15 == 'Alugada':
        selecao_15 = "rent"

    # --------- Nº de créditos existentes nesse banco
    if selecao_16 == '1':
        selecao_16 = "1"
    elif selecao_16 == '2':
        selecao_16 = "3"
    elif selecao_16 == '3':
        selecao_16 = "rent"
    elif selecao_16 == '4 ou mais':
        selecao_16 = "4"
    elif selecao_16 == 'Nenhum':
        selecao_16 = "0"

    # --------- Trabalho
    if selecao_17 == 'Funcionário':
        selecao_17 = "skilled"
    elif selecao_17 == 'Não qualificado':
        selecao_17 = "'unskilled resident'"
    elif selecao_17 == 'Administrador/autônomo':
        selecao_17 = "'high qualif/self emp/mgmt'"
    elif selecao_17 == "Desempregado":
        selecao_17 = "'unemp/unskilled non res'"

    # --------- Quantidade de dependentes
    if selecao_18 == '1':
        selecao_18 = "1"
    elif selecao_18 == '2 ou mais':
        selecao_18 = "2"
    elif selecao_18 == 'Nenhum':
        selecao_18 = "0"

    # --------- Telefone registrado em nome próprio
    if selecao_19 == 'Sim':
        selecao_19 = "yes"
    elif selecao_19 == 'Nenhum':
        selecao_19 = "none"

    # --------- Trabalhador estrageiro
    if selecao_20 == 'Sim':
        selecao_20 = "yes"
    elif selecao_20 == 'Não':
        selecao_20 = "no"


    UpdateMongo(selecao_nome, selecao_cpf,getdata(), selecao_email, selecao_1,
            selecao_2, selecao_3, selecao_4, selecao_5, selecao_6, selecao_7, selecao_8, selecao_9, selecao_10,
            selecao_11, selecao_12, selecao_13, selecao_14, selecao_15, selecao_16, selecao_17, selecao_18,
            selecao_19, selecao_20)
