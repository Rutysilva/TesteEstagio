function formatarDatas(listaDatas) {
    const mapaMeses = {
        'jan': 1, 'fev': 2, 'mar': 3, 'abr': 4, 'mai': 5, 'jun': 6,
        'jul': 7, 'ago': 8, 'set': 9, 'out': 10, 'nov': 11, 'dez': 12,
        'janeiro': 1, 'fevereiro': 2, 'março': 3, 'abril': 4, 'maio': 5,
        'junho': 6, 'julho': 7, 'agosto': 8, 'setembro': 9, 'outubro': 10,
        'novembro': 11, 'dezembro': 12
    };

    return listaDatas.map(dataString => {
        let dia, mes, ano;

        if (dataString.includes('/')) {
            [dia, mes, ano] = dataString.split('/').map(Number);
        
        } else {
          
            const partes = dataString.split(' ');
            dia = Number(partes[0]);
            const mesStr = partes[1]; 

            if (mapaMeses[mesStr]) {
                mes = mapaMeses[mesStr]; 
            } else {
                mes = mapaMeses[partes[2]];
            }
            ano = Number(partes[partes.length - 1]);
        }
        return ano + '-' + (mes < 10 ? '0' + mes : mes) + '-' + (dia < 10 ? '0' + dia : dia);
    });
}

const listaDatas = [
    '30/11/2022',
    '01 dez 2022',
    '25/12/2022',
    '31 de dezembro de 2022'
];

const datasFormatadas = formatarDatas(listaDatas);
console.log(datasFormatadas);
