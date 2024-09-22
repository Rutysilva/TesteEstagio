from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

def q3_tratar_datas(datas):
    
    formatadas = []
    
    for data in datas:
        try:
            
            if '/' in data:
                formatada = datetime.strptime(data, '%d/%m/%Y' )
                formatadas.append(formatada.strftime('%Y-%m-%d'))
            elif 'de' in data:
                formatada = datetime.strptime(data, '%d de %B de %Y')
                formatadas.append(formatada.strftime('%Y-%m-%d'))
            elif '' in data:
                formatada = datetime.strptime(data, '%d %b %Y')
                formatadas.append(formatada.strftime('%Y-%m-%d'))
            else:
                formatadas.append("Formato de data não identificado")
        except ValueError:
            formatadas.append("Data inválida")
            
    return formatadas
            
    
    
datas_para_tratar = ['30/02/2022', '01 Dez 2022', '25/12/2022', '31 de dezembro de 2022']

formatadas = q3_tratar_datas( datas_para_tratar)
print(formatadas)
    