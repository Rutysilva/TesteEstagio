from datetime import datetime, timedelta
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

def q5_calculo_prazo(data, prazo, tipo):
    
    formato_data = datetime.strptime(data, '%d/%m/%Y')
    dia_seguinte = formato_data + timedelta(days = 1)
    print (dia_seguinte)
    prazo = int(prazo)
    
    if tipo == 'Corridos' or tipo == 'CORRIDOS'or tipo == 'corridos':
    
        data_final = dia_seguinte + timedelta (days = prazo)
        data_final_formatada = data_final.strftime('%d/%m/%Y')
        print('Data ', formato_data.strftime('%d/%m/%Y'),', prazo de', prazo, 'dias corridos, a data final é no dia', data_final_formatada)
    
    if tipo  == 'Úteis' or tipo == 'ÚTEIS'or tipo == 'úteis':
        
        data_final = dia_seguinte + timedelta (days = prazo + 2 -1)
        data_final_formatada = data_final.strftime('%d/%m/%Y')
        print('Data ', formato_data.strftime('%d/%m/%Y'),', prazo de', prazo, 'dias úteis, a data final é no dia', data_final_formatada)
        
    
data = input('Informe a data para realizar o cálculo do prazo (dd/mm/aaaa): ')
prazo = input('Informe o prazo: ')
tipo = input('Informe o tipo, se dias CORRIDOS ou dias ÚTEIS: ')

print(q5_calculo_prazo(data,prazo,tipo))
    

    
    