#!/usr/bin/env ruby
###
#
#  This script sorts the integer arguments in ascending order.
#
###

# Initialize an empty array to store the results.
result = []

# Loop through each argument given in the command line.
ARGV.each do |arg|
    # Skip the current iteration if the argument is not an integer.
    # This is done by matching the argument with a regular expression that checks for integer values.
    next if arg !~ /^-?[0-9]+$/

    # Convert the argument to an integer.
    i_arg = arg.to_i

    # Initialize a flag to track whether the integer has been inserted into the results array.
    is_inserted = false
    i = 0
    l = result.size
    # Loop through the results array to find the correct position for the integer argument.
    while !is_inserted && i < l do
        # If the current result is less than the integer argument, increment the counter and continue to the next iteration.
        if result[i] < i_arg
            i += 1
        # If the current result is greater than or equal to the integer argument, insert the integer at the current position in the results array.
        # Then set the flag to true to end the loop.
        else
            result.insert(i, i_arg)
            is_inserted = true
            break
        end
    end
    # If the integer argument is larger than all the numbers in the results array, it hasn't been inserted yet.
    # Therefore, append it to the end of the results array.
    result << i_arg if !is_inserted
end

# Print the sorted results.
puts result
