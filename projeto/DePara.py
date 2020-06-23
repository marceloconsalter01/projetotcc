

def translatedb(consulta):
#-----checking_status
    if consulta["checking_status"] == "<0":
         consulta["checking_status"] = 'Menor que zero'
    elif consulta["checking_status"] == "0<=X<200":
         consulta["checking_status"] = 'Entre zero e duzentos'
    elif consulta["checking_status"] == "'no checking'":
         consulta["checking_status"] = 'Não possui conta'
    elif consulta["checking_status"] == '">=200"':
         consulta["checking_status"] =  'Maior ou igual a duzentos '
#--------------------
    
    print(consulta["checking_status"])
    return consulta

