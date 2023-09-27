# Uma nova loja de cosméticos abriu no seu bairro e pediram para você elaborar um sistema que imprime na tela na frente da loja os novos
# produtos que chegaram. O sistema da loja já tem um array com os produtos, você precisa apenas imprimir eles no terminal, um por um.


lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']
for i in range(len(lista_produtos)):
  print('Temos ' + (lista_produtos[i]) + ' à venda!')


# Dessa vez, eles precisam que você atualize o array de produtos. Agora, eles estão vendendo rímel ao invés de batons, e cremes 
# hidratantes no lugar de loções. Além disso, ficaram sem delineadores, então precisam que você remova ele da lista de produtos. 
# Imprima a nova lista no terminal para verificar que as alterações foram realizadas corretamente.
# Como desafio, adicione dois novos produtos da sua escolha à lista.

lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']
print('Lista antiga: ', lista_produtos)
lista_produtos[1], lista_produtos[4] = 'rímel', 'cremes hidratantes'
lista_produtos.pop()
lista_produtos.append('creme barbear')
lista_produtos.append('gel de cabelo')
print('Lista atualizada:', lista_produtos)

