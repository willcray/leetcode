/*
https://leetcode.com/problems/fizz-buzz/
time: O(N)
space: O(1)
Author: Will Cray
Date: 1/7/2020
*/

#include <string>
using namespace std;

class Solution {
public:
    vector<string> fizzBuzz(int n)
    {
        // assuming n is greater or equal to 1
        // solution 1 - iterate and modulo
        // time - O(N), space - O(1)

        // instaniate return vector of strings, preallocate space
        vector<string> ret_vector = vector<string>(n);

        // instantiate element string
        string element = "";

        int notDivisibleBy3 = 0;
        int notDivisibleBy5 = 0;

        // iterate from [1 to n]
        for (int i = 1; i <= n; ++i)
        {
            // clear string on each iteration
            element = "";
            // if divisible by 3, concat "Fizz" to element at current index
            notDivisibleBy3 = i % 3;
            notDivisibleBy5 = i % 5;

            // anything greater than 0 will evaluate to true
            if (!notDivisibleBy3)
            {
                element = element + "Fizz";
            }

            // if divisible by 5, concat "Buzz" to element at current index
            if (!notDivisibleBy5)
            {
                element = element + "Buzz";
            }

            // else concat iterator value (i) to element at current index
            if (notDivisibleBy3 && notDivisibleBy5)
            {
                element = to_string(i);
            }

            // insert element into vector
            ret_vector.at(i - 1) = element;
        }

        return ret_vector;
    }
};
