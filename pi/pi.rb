=begin

Question 1 / 1

The first 12 digits of pi are 314159265358. We can make these digits into an expression evaluating to 27182 (first 5 digits of e) as follows:

3141 * 5 / 9 * 26 / 5 * 3 - 5 * 8 = 27182
or
3 + 1 - 415 * 92 + 65358 = 27182

Notice that the order of the input digits is not changed. Operators (+,-,/, or *) are simply inserted to create the expression.

Write a function to take a list of numbers and a target, and return all the ways that those numbers can be formed into expressions evaluating to the target. Do not use the eval function in Python, Ruby or JavaScript

For example:
f("314159265358", 27182) should print:

3 + 1 - 415 * 92 + 65358 = 27182
3 * 1 + 4 * 159 + 26535 + 8 = 27182
3 / 1 + 4 * 159 + 26535 + 8 = 27182
3 * 14 * 15 + 9 + 26535 + 8 = 27182
3141 * 5 / 9 * 26 / 5 * 3 - 5 * 8 = 27182
=end

=begin
at a high level, I'm going to test every combination of operators on an array
of numbers that is possible from the list given. For example if the list is
31415 and the target is 60000, I would try 3141 + 5, 3141 - 5, 3141 * 5, 3141 / 5 and see
if those possibilities == 60000. If not, I would move onto 314 + 15, 314 - 15, 314 * 15, 314 / 15,
314 + 1 + 5, 314 + 1 - 5, 314 + 1 * 5, 314 + 1 / 5, 314 - 1 + 1, 314 - 1 - 5, 314 - 1 * 5, 314 - 1 / 5,
etc. But the problem seems to lend well to recursion but I'm unsure how to implement
it. As the first number gets smaller and smaller, the possibilities seem to grow,
but I am unsure how to recursively implement a solution.

I think Ruby's public send might be useful here.
arg1.public_send(op, arg2)

where op is the operator and arg 2 is an array of remaining numbers in the list
that isn't the first number.
=end

def calculate(list, target)
  possible_numbers_array = generate_number_sequence(list)
  correct_numbers_array = check(possible_numbers_array, target)
end

def operators
  ["+", "-", "*", "/"]
end

def generate_number_sequence(list)
  final_possibilities = []
  end_of_base_number_index = list.size - 1
  while end_of_base_number_index > 0
    starting_base = take_starting_number(list, end_of_base_number_index)
    final_possibilities.push(generate_possibilities_with(starting_base))

    end_of_base_number_index++
end

private

def take_starting_number(list, end_of_base_number_index)
  list.chars.first(list.size - end_of_base_number_index).join.to_i
end
