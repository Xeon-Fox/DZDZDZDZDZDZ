// 1
let age = prompt("ваш возраст");
if (age >= 0 && age <= 2){
    alert("ребенок");
}
else if (age >= 12 && age <= 18){
    alert("подросток");
}
else if (age >= 18 && age <= 60){
    alert("взрослый");
}
else if (age > 60) {
    alert("старина");
}

// 2
let num = prompt("число от 0 до 9");
switch (num) {
    case '1':
        alert("!");
        break;
    case '2':
        alert("@");
        break;
    case '3':
        alert("#");
        break;
    // дальше мне лень ну там понятно да
}

// 3
let num = prompt("трехзначное число");
let digits = num.split("");
if(digits[0] == digits[1] || digits[0] == digits[2] || digits[1] == digits[2]){
    alert("одинаковые цифры");
}
else {
    alert("нет одинаковых цифр");
}

// 4
let year = prompt("введите год");
if((year % 400 == 0) || (year % 4 == 0 && year % 100 != 0)){
    alert(" високосный");
}
else {
    alert("эне високосный");
}

//5
let num = prompt(" число");
let digits = num.split("");
if(digits[0] == digits[4] && digits[1] == digits[3]){
    alert("палиндромом");
}
else {
    alert("не палиндромом");
}

let amount = prompt("деньги");
let currency = prompt("выберите валюту");
let result;
switch (currency) {
    case 'EUR':
        result = amount * 1; 
        break;
    case 'UAN':
        result = amount * 2;
        break;
    case 'AZN':
        result = amount * 3; 
        break;
}
alert(`сумма в ${currency}: ${result}`);

//7
let sum = prompt("Введите сумму покупки");
let discount;
if (sum >= 200 && sum < 300) {
    discount = 0.03;
} else if (sum >= 300 && sum < 500) {
    discount = 0.05;
} else if (sum >= 500) {
    discount = 0.07;
}
let total = sum - sum * discount;
alert(`Сумма к оплате сс скидкой: ${total}`);

// 8
let circleLength = prompt("Введите длину окружности");
let squarePerimeter = prompt("Введите периметр квадрата");
let circleDiameter = circleLength / Math.PI;
let squareSide = squarePerimeter / 4;
if (circleDiameter <= squareSide) {
    alert("Окружность может поместиться в квадрат")
}
else {
    alert("Окружность не может поместиться в квадрат")
}

//9
let score = 0;
let question1 = prompt("вопрос!@!!");
if (question1 == '2') {
    score += 2;
}
// тоже самое 2 раза
alert(`Вы набрали ${score} баллов`);

//10
let date = new Date(prompt("Введите дату (день, месяц, год)"));
date.setDate(date.getDate() + 1);
alert(`Следующая дата: ${date.getDate()}.${date.getMonth() + 1}.${date.getFullYear()}`);

/1
function compareNumbers(a, b) {
    if (a < b) {
        return -1;
    } else if (a > b) {
        return 1;
    } else {
        return 0;
    }
}


//2

function factorial(n) {
    let result = 1;
    for (let i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}


//3
function digitsToNumber(a, b, c) {
    return a * 100 + b * 10 + c;
}

//4
function rectangleArea(length, width = length) {
    return length * width;
}
//5
function isPerfectNumber(n) {
    let sum = 0;
    for (let i = 1; i <= n / 2; i++) {
        if (n % i === 0) {
            sum += i;
        }
    }
    return sum === n;
}

//6
function perfectNumbersInRange(min, max) {
    let result = [];
    for (let i = min; i <= max; i++) {
        if (isPerfectNumber(i)) {
            result.push(i);
        }
    }
    return result;
}

//7и8
function formatTime(hours, minutes = "00", seconds = "00") {
    return `${hours}:${minutes}:${seconds}`;
}

//9
function timeToSeconds(hours, minutes, seconds) {
    return hours * 3600 + minutes * 60 + seconds;
}
//10
function secondsToTime(seconds) {
    let hours = Math.floor(seconds / 3600);
    seconds %= 3600;
    let minutes = Math.floor(seconds / 60);
    seconds %= 60;
    return formatTime(hours, minutes, seconds);
}

//11
function timeDifference(year1, month1, day1, year2, month2, day2) {
    let date1 = new Date(year1, month1 - 1, day1);
    let date2 = new Date(year2, month2 - 1, day2);
    let differenceInSeconds = Math.abs(date1 - date2) / 1000;
    return secondsToTime(differenceInSeconds);
}


