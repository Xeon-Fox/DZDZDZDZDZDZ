// 1
let name = prompt("ваше имя");
alert(name);

// 2
const CURRENT_YEAR = 2024;
let birthYear = prompt("год вашего рождения");
let age = CURRENT_YEAR - birthYear;
alert(age);

// 3
let side = prompt("сторона");
let perimeter = 4 * side;
alert(perimeter);

// 4
let radius = prompt("радиус");
let area = Math.PI * Math.pow(radius, 2);
alert(area);

// 5
let distance = prompt("расстояние");
let time = prompt("сколько часов");
let speed = distance / time;
alert(speed);

// 6
const EXCHANGE_RATE = 0.85;
let dollars = prompt("сумма");
let euros = dollars * EXCHANGE_RATE;
alert(euros);

// 7
let flashDriveSize = prompt("объем флешки");
let fileSize = 820; 
let filesAmount = (flashDriveSize * 1024) / fileSize; 
alert(Math.floor(filesAmount));

// 8
let moneyAmount = prompt("сумма");
let chocolatePrice = prompt("цена");
let chocolatesAmount = Math.floor(moneyAmount / chocolatePrice);
let change = moneyAmount % chocolatePrice;
alert(chocolates, change);

// 9
let number = prompt("число");
let reversedNumber = number.split('').reverse().join('');
alert(reversedNumber);

// 10
let number = prompt("число");
let isEven = number % 2 === 0;
alert(isEven);
