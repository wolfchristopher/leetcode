"""
273. Integer To English Words
Convert a non-negative integer num to its English words representation.



Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"


Constraints:

0 <= num <= 231 - 1

Explanation of the Code:
below_20 and tens Arrays:
- below_20 contains English words for numbers from 1 to 19.
- tens contains English words for tens multiples (like Twenty, Thirty, etc.).

helper(n) Function:
- This function converts numbers less than 1000 to their English words representation.
- It handles numbers:
  - Less than 20 by directly mapping to below_20.
  - Between 20 and 99 by taking the tens part from the tens array and recursively converting the units part.
  - Greater than or equal to 100 by recursively calling helper on the remaining part after dividing by 100.

Main Loop:
- We loop through the thousands array (["", "Thousand", "Million", "Billion"]) and process each chunk of the number.
- We extract the last three digits (using num % 1000), convert them to English words, and append the corresponding place value (like "Thousand", "Million", etc.).
- After processing each chunk, we reduce the number by dividing it by 1000.

Return Result:
- After processing all chunks, we remove any leading or trailing spaces with strip() and return the result.

Time Complexity:
The time complexity is O(log n) because we divide the number by 1000 at each step, and there are only a few place values (Billions, Millions, Thousands, etc.).

Space Complexity:
The space complexity is O(1), as we use only a constant amount of extra space to store strings for tens, below 20, and the place values.

Edge Cases:
- Zero: If num is 0, return "Zero".
- Numbers with trailing zeros: Properly handle cases like 1000, 1000000, etc.
- Large numbers: The solution handles large numbers up to 2^31 - 1.

"""

def numberToWords(num: int) -> str:
        if num == 0:
            return "Zero"

        # Words for numbers 1-19
        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                    "Twelve",
                    "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

        # Words for tens (20, 30, ..., 90)
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        # Place values
        thousands = ["", "Thousand", "Million", "Billion"]

        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return below_20[n]
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10) if n % 10 != 0 else tens[n // 10]
            else:
                return below_20[n // 100] + " Hundred " + helper(n % 100) if n % 100 != 0 else below_20[
                                                                                                   n // 100] + " Hundred"

        res = ""
        for i in range(len(thousands)):
            if num % 1000 != 0:
                res = helper(num % 1000) + " " + thousands[i] + " " + res
            num //= 1000

        return res.strip()

numberToWords(123) # "One Hundred Twenty Three"
numberToWords(12345) # "Twelve Thousand Three Hundred Forty Five
numberToWords(123456) # "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"