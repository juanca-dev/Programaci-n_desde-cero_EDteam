// Condiciones dobles
//  
// if (5 > 3) {
//     console.log('La condicion es verdadera')
// } else {
//     console.log('La condicion es falsa')
// }
// console.log('Yo siempre me voy a ejecutar')

// Condicionales múltiples
// if (5 > 6) {
//     console.log('a')
// } else if(8 > 10 ){
//     console.log('b')
// } else if(5 > 7) {
//     console.log('c')
// } else {
//     console.log('d')
// }
 
// let edad = 29 
// if (edad >= 18 && edad < 20) {
//     console.log ('a')
// } else {
//     console.log('b')    
// }

//ejemplo 2

// let  pension  = 65
// if (pension >= 60 && pension < 62) {
//     console.log ('c')
// } else {
//     console.log('d')
// }
// el o  en javascript
// let  pension  = 65
// if (pension >= 60 || pension < 62) {
//     console.log ('c')
// } else {
//     console.log('d')
// }


//Condiciones anidadas


let edad = 29 
let  mayorDeEdad = edad >= 18 || edad < 20
if (mayorDeEdad) {
    console.log ('a')
    if (5>3) {
        console.log('b')
    }else{
        console.log('b2')  
    }
} else {
    console.log('c')    
}