// Esse desafio consiste em criar uma função capaz de filtrar uma lista e retirar as strings que ela possui
// Para isso criei uma nova lista, que sempre iniciará vazia
// Depois usei um for para percorrer a lista passada como parametro para a função
// Declarei uma variavel chamada "item" dentro do loop que irá receber o valor do indice atual de cada repetição
// Depois criei uma condição que verificia o tipo do "item" e se ele for do tipo númerico, será adicionado na nova lista
// Depois de todo o processo, a função retorna a nova lista filtrada como resultado

function Filtrando_lista(l) {
    let novaLista = []; 

    for (let i = 0; i < l.length; i++) {
        let item = l[i]; 
        
        if (typeof item === 'number') {
            novaLista.push(item); 
        }
    }

    return novaLista; 
}

console.log("--- Testes do desafio ---");
console.log("Teste 1:", Filtrando_lista([1, 2, 'a', 'b']));    
console.log("Teste 2:", Filtrando_lista([1, 'a', 'b', 0, 15]));      
console.log("Teste 3:", Filtrando_lista([1, 2, 'aasf', '1', '123', 123]));
console.log("Teste 4:", Filtrando_lista([-1, 0, 1, 15, "10", "20", "texto", true, false, null, undefined, { nome: "teste" }, 1, 2, 999, -500, " ", "0"]));