

def translatedb(consulta):
    try:
    #-------------------- checking_status
        if   consulta["checking_status"] == "<0":
             consulta["checking_status"] = 'Menor que zero'
        elif consulta["checking_status"] == "0<=X<200":
             consulta["checking_status"] = 'Entre zero e duzentos'
        elif consulta["checking_status"] == "'no checking'":
             consulta["checking_status"] = 'Não possui conta'
        elif consulta["checking_status"] == ">=200":
             consulta["checking_status"] = 'Maior ou igual a duzentos'
        print(consulta["checking_status"])

    #-------------------- credit_history
        if   consulta["credit_history"] == "'critical/other existing credit'":
             consulta["credit_history"] = 'Conta crítica em outros bancos'
        elif consulta["credit_history"] == "'existing paid'":
             consulta["credit_history"] = 'Créditos existentes, porém pagos'
        elif consulta["credit_history"] == "'no credits/all paid'":
             consulta["credit_history"] = 'Empréstimos nessa instuição pagos'
        elif consulta["credit_history"] == "'all paid'":
             consulta["credit_history"] =  'Sem empréstimos atualmente'
        elif consulta["credit_history"] == "'delayed previously'":
             consulta["credit_history"] =  'Adiado anteriormente'
        print(consulta["credit_history"])

    #-------------------- purpose
        if   consulta["purpose"] == "radio/tv":
             consulta["purpose"] = 'Televisão'
        elif consulta["purpose"] == "education":
             consulta["purpose"] = 'Educação'
        elif consulta["purpose"] == "furniture/equipment":
             consulta["purpose"] = 'Móveis / Equipamentos'
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

    #-------------------- savings_status
        if   consulta["savings_status"] == "'no known savings'":
             consulta["savings_status"] = 'Nenhuma conta poupança'
        elif consulta["savings_status"] == "<100":
             consulta["savings_status"] = 'Menos que R$100, 00'
        elif consulta["savings_status"] == "500<=X<1000":
             consulta["savings_status"] = 'Entre R$500, 00 e R$1.000, 00'
        elif consulta["savings_status"] == ">=1000":
             consulta["savings_status"] = 'Mais que R$1.000, 00'
        elif consulta["savings_status"] == "100<=X<500":
             consulta["savings_status"] = 'Entre R$100 e R$500, 00 '
        print(consulta["savings_status"])

    # -------------------- employment
        if   consulta["employment"] == ">=7":
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
        if   consulta["personal_status"] == "'male single'":
             consulta["personal_status"] = 'Masculino e solteiro'
        elif consulta["personal_status"] == "'female div/dep/mar'":
             consulta["personal_status"] = 'Feminino e Divorciado / Separado / Casado'
        elif consulta["personal_status"] == "'male div/sep'":
             consulta["personal_status"] = 'Masculino e Divorciado / Separado'
        elif consulta["personal_status"] == "'male mar/wid'":
             consulta["personal_status"] = 'Masculino e Casado / Viúvo'
        elif consulta["personal_status"] == "'female single'":
             consulta["personal_status"] = 'Feminino e Solteiro'
        print(consulta["personal_status"])

    # -------------------- other_parties
        if   consulta["other_parties"] == "none":
             consulta["other_parties"] = 'Nenhum'
        elif consulta["other_parties"] == "guarantor":
             consulta["other_parties"] = 'Fiador'
        elif consulta["other_parties"] == "'co applicant'":
             consulta["other_parties"] = 'Cofiador'
        print(consulta["other_parties"])

    # -------------------- residence_since
        if   consulta["residence_since"] == "1":
             consulta["residence_since"] = '1 Ano'
        elif consulta["residence_since"] == "2":
             consulta["residence_since"] = '2 Anos'
        elif consulta["residence_since"] == "3":
             consulta["residence_since"] = '3 Anos'
        elif consulta["residence_since"] == "4":
             consulta["residence_since"] = '4 Anos ou mais'
        print(consulta["residence_since"])

    # -------------------- property_magnitude
        if   consulta["property_magnitude"] == "'real estate'":
             consulta["property_magnitude"] = 'Imovéis'
        elif consulta["property_magnitude"] == "'life insurance'":
             consulta["property_magnitude"] = 'Seguro de vida'
        elif consulta["property_magnitude"] == "'no known property'":
             consulta["property_magnitude"] = 'Sem propriedades'
        elif consulta["property_magnitude"] == "car":
             consulta["property_magnitude"] = 'Carro'
        print(consulta["property_magnitude"])

    # -------------------- other_payment_plans
        if   consulta["other_payment_plans"] == "none":
             consulta["other_payment_plans"] = 'Nenhum'
        elif consulta["other_payment_plans"] == "bank":
             consulta["other_payment_plans"] = 'Bancos'
        elif consulta["other_payment_plans"] == "stores":
             consulta["other_payment_plans"] = 'Lojas'
        print(consulta["other_payment_plans"])

    # -------------------- housing
        if   consulta["housing"] == "own":
             consulta["housing"] = 'Próprio'
        elif consulta["housing"] == "'for free'":
             consulta["housing"] = 'De graça'
        elif consulta["housing"] == "rent":
             consulta["housing"] = 'Alugada'
        print(consulta["housing"])

    # -------------------- existing_credits
        if   consulta["existing_credits"] == "1":
             consulta["existing_credits"] = '1'
        elif consulta["existing_credits"] == "2":
             consulta["existing_credits"] = '2'
        elif consulta["existing_credits"] == "3":
             consulta["existing_credits"] = '3'
        elif consulta["existing_credits"] == "4":
             consulta["existing_credits"] = '4 ou mais'
        print(consulta["existing_credits"])

    # -------------------- job
        if   consulta["job"] == "skilled":
             consulta["job"] = 'Funcionário'
        elif consulta["job"] == "'unskilled resident'":
             consulta["job"] = 'Não qualificado'
        elif consulta["job"] == "'high qualif/self emp/mgmt'":
             consulta["job"] = 'Administrador / autônomo'
        elif consulta["job"] == "'unemp/unskilled non res'":
             consulta["job"] = 'Desempregado'
        print(consulta["job"])

    # -------------------- num_dependents
        if   consulta["num_dependents"] == "1":
             consulta["num_dependents"] = '1'
        elif consulta["num_dependents"] == "2":
             consulta["num_dependents"] = '2 ou mais'
        print(consulta["num_dependents"])

    # -------------------- own_telephone
        if   consulta["own_telephone"] == "yes":
             consulta["own_telephone"] = 'Sim'
        elif consulta["own_telephone"] == "none":
             consulta["own_telephone"] = 'Nenhum'
        print(consulta["num_dependents"])

    # -------------------- foreign_worker
        if   consulta["foreign_worker"] == "yes":
             consulta["foreign_worker"] = 'Sim'
        elif consulta["foreign_worker"] == "no":
             consulta["foreign_worker"] = 'Não'
        print(consulta["foreign_worker"])

        return consulta
    except:
        erro = "CPF não cadastrado"

        return erro
