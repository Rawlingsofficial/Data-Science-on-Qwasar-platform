# Welcome to My Roman Numerals Converter
Roman Numerals Converter
This is a Python function that converts normal numbers to Roman numerals. The Romans used letters such as I, V, X, L, C, D, and M to represent numbers.
 The function provides a way to convert a given number to its equivalent Roman numeral representation.

## Task
Write a function to convert normal numbers to Roman Numerals.
The Romans wrote numbers using letters - I, V, X, L, C, D, M. 
(notice these letters have lots of straight lines and are hence easy to carve into stone tablets).
 1  => I
10  => X
 7  => VII

## Description
How have you solved the problem?
To solve the problem of converting normal numbers to Roman numerals, the my_roman_numerals_converter function follows these steps:
Define a dictionary roman_numerals that maps the decimal values to their corresponding Roman numeral symbols. The dictionary includes the symbols for numbers from 1 to 1000, as well as special cases for subtractive notation like 4 (IV), 9 (IX), 40 (XL), etc.
Initialize an empty string variable roman_numeral to store the resulting Roman numeral.
Iterate through the roman_numerals dictionary in descending order of decimal values.
Within each iteration, check if the input number is greater than or equal to the current decimal value. If so, append the corresponding Roman numeral symbol to the roman_numeral string, and subtract the decimal value from the input number.
Repeat the previous step until the input number becomes less than the current decimal value.
Once all the decimal values have been processed, the roman_numeral string will contain the Roman numeral representation of the original number.
Return the roman_numeral string as the result.
For example, let's say we want to convert the number 14 to a Roman numeral:
Start with an empty roman_numeral string.
Iterate through the roman_numerals dictionary:
The first iteration checks if 14 is greater than or equal to 10. Since it is, we append 'X' to the roman_numeral string and subtract 10 from 14, resulting in a remaining value of 4.
The second iteration checks if 4 is greater than or equal to 4. Since it is, we append 'IV' to the roman_numeral string and subtract 4 from 4, resulting in a remaining value of 0.
The iterations end because the remaining value is 0.
The resulting roman_numeral string is 'XIV', which is the Roman numeral representation of 14.
This process is repeated for any given number, providing the corresponding Roman numeral representation as the output.

## Installation
 How to install your project? npm install? make? make re?
there was no installation for this project
## Usage
 How does it work?
 The my_roman_numerals_converter function accepts an integer as input and returns a string containing the
Roman numeral representation of the number.
python
result = my_roman_numerals_converter(number)
Example
python
result = my_roman_numerals_converter(14)
print(result)  # Output: XIV
```
./my_project argument1 argument2
```

### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px'></span>
