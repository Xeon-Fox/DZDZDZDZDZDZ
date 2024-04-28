//1
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
console.log(Math.max(...numbers), Math.min(...numbers))

//2
let numbersPrompt = []
let sum = 0
for(let i = 0; i < 5; i++) {
    numbersPrompt[i] = Number(prompt("число"))
    sum += numbersPrompt[i]
}
console.log(`сумма: ${sum}, сред: ${sum / numbersPrompt.length}`)

// 3
let array1 = [1, 2, 3, 4, 5, 6, 7]
let array2 = [7, 6, 5, 4, 3, 2, 1]
for(let i = 0; i < 7; i++) {
    console.log(`${i}: в 1 - ${array1[i]}, во 2 - ${array2[i]}`)
}

//4
let numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
let evenNumbers = []
for(let i = 0; i < numbers1.length; i++) {
    if(numbers1[i] % 2 === 0) {
        evenNumbers.push(numbers1[i])
    }
}
console.log(evenNumbers)
