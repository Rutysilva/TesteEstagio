def q4_converter_arrays_em_dics (chaves, valores):
    meu_dicionario = dict(zip(chaves, valores))
    print(meu_dicionario)
    
chaves = ['data_distribuicao', 'valor_da_causa', 'classe_judicial', 'assunto']
valores = ['14/04/2024', 'R$ 810,26', 'EXECUÇÃO DE TÍTULO EXTRAJUDICIAL (12154)', 'Nota Promissória (4980)']

print (q4_converter_arrays_em_dics(chaves, valores))