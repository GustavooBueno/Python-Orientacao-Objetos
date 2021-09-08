class Produto:
    def __init__(self, codigo, descricao, valorUni):
        self.codigo = codigo
        self.descricao = descricao
        self.valorUni = valorUni

class NotaFiscal:
    def __init__(self, nroNF, nomeCliente, itensNF):
        self.nroNF = nroNF
        self.nomeCliente = nomeCliente
        self.itensNF = itensNF

class CompraParcialmenteRealizada(Exception):
    pass
class CompraInvalida(Exception):
    pass

if __name__ == '__main__':
    calça = Produto(101, 'calça', 150)
    meia = Produto(102, 'meia', 10)
    tenis = Produto(103, 'tenis', 500)
    colar = Produto(104, 'colar', 100)
    pulseira = Produto(105, 'pulseira', 100)
    brinco = Produto(106, 'brinco', 50)

    listaProdutos = [calça.descricao, meia.descricao, tenis.descricao, colar.descricao, pulseira.descricao, brinco.descricao]  
    estoque = {calça.descricao:5, meia.descricao:10, tenis.descricao:3, colar.descricao:10, pulseira.descricao:6, brinco.descricao:2}
    compra1 = {calça.descricao:2, meia.descricao:3, tenis.descricao:3, colar.descricao:2, pulseira.descricao:1, brinco.descricao:0}
    novoEstoque = {calça.descricao: estoque[calça.descricao] - compra1[calça.descricao],meia.descricao: estoque[meia.descricao] - compra1[meia.descricao], tenis.descricao:estoque[tenis.descricao] - compra1[tenis.descricao], colar.descricao:estoque[colar.descricao] - compra1[colar.descricao], pulseira.descricao:estoque[pulseira.descricao] - compra1[pulseira.descricao], brinco.descricao:estoque[brinco.descricao] - compra1[brinco.descricao]}
    valorFinal = (compra1[calça.descricao] * calça.valorUni) + (compra1[meia.descricao] * meia.valorUni) + (compra1[tenis.descricao] * tenis.valorUni) + (compra1[colar.descricao] * colar.valorUni) + (compra1[pulseira.descricao] * pulseira.valorUni) + (compra1[brinco.descricao] * brinco.valorUni) 

    cliente1 = NotaFiscal(1, 'Gustavo', compra1)


    print(f'Estoque inicial: {estoque}')
    print(f'Carrinho de compras: {compra1}')
    print(f'Estoque pós compras: {novoEstoque}')
    print('======================================')
    print(f'Número da nota:{cliente1.nroNF}\nNome do Cliente: {cliente1.nomeCliente}, Produto: {calça.descricao} - {calça.valorUni} reais - {compra1[calça.descricao]} vendidos')
    print(f'Produto: {meia.descricao} - {meia.valorUni} reais - {compra1[meia.descricao]} vendidos')
    print(f'Produto: {tenis.descricao} - {tenis.valorUni} reais - {compra1[tenis.descricao]} vendidos')
    print(f'Produto: {colar.descricao} - {colar.valorUni} reais - {compra1[colar.descricao]} vendidos')
    print(f'Produto: {pulseira.descricao} - {pulseira.valorUni} reais - {compra1[pulseira.descricao]} vendidos')
    print(f'Produto: {brinco.descricao} - {brinco.valorUni} reais - {compra1[brinco.descricao]} vendidos')
    print(f'VALOR DA COMPRA : {valorFinal}')
    print('==========================================')


    try:
        if compra1[calça.descricao] < estoque[calça.descricao] and compra1[meia.descricao] < estoque[meia.descricao] and compra1[tenis.descricao] < estoque[tenis.descricao]and compra1[colar.descricao] < estoque[colar.descricao]and compra1[pulseira.descricao] < estoque[pulseira.descricao] and compra1[brinco.descricao] < estoque[brinco.descricao]:
            raise CompraParcialmenteRealizada()
        if compra1[calça.descricao] > estoque[calça.descricao] and compra1[meia.descricao] > estoque[meia.descricao] and compra1[tenis.descricao] > estoque[tenis.descricao]and compra1[colar.descricao] > estoque[colar.descricao]and compra1[pulseira.descricao] > estoque[pulseira.descricao] and compra1[brinco.descricao] > estoque[brinco.descricao]:
            raise CompraInvalida()
    except CompraParcialmenteRealizada:
        print('Nota Fiscal parcialmente criada')
    except CompraInvalida:
        print('Nota fiscal não criada')
    else:
        print('Nota fiscal criada')

