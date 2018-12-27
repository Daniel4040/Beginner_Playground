"""Welcome to the Palindrome Checker, created by Daniel in December 2018. This function checks for palindromes
   in a case & space-insensitive manner. Have fun with it!"""


def palindromechecker():
    """To be, or not to be a palindrome, that is the question. Let's check below ;)"""

    # First we create our forward string from an input phrase
    # We strip all spaces out of the input phrase to check phrases like "nurses run" as well as a single word
    forward_string = str(input("Input word here: "))
    forward_string = forward_string.replace(" ", "")

    # Create our reversed stack and reversed string
    stack_creator = []
    reversed_stack = []
    reversed_string = ""

    # Create our check variable, either 1 or 0 (True or False respectively)
    palindrome_check = 0

    # Step 1 - Push the contents of the input phrase on a stack, which is just an array in our case
    for i in range(len(forward_string)):
        stack_creator.append(forward_string[i])

    # Step 2 - Pop the end contents off stack and place them into a new array in sequential order (now reverse order)
    # This step is not required. It is possible to create the reversed phrase directly from the stack if desired.
    for i in range(len(stack_creator) - 1, -1, -1):
        reversed_stack.append(stack_creator[i])

    # Step 3 - Create a string out of the contents of the reversed array. Now we have the reversed phrase.
    # As mentioned above, steps 2 and 3 can be consolidated if desired.
    for i in range(len(reversed_stack)):
        reversed_string += reversed_stack[i]

    # Step 4 - Check our result against the original phrase to see if it is a palindrome, then we're finished.
    if str.casefold(forward_string) == str.casefold(reversed_string):
        palindrome_check = 1  # Binary is more fun, right? So is making things more complex than necessary.

    return bool(palindrome_check)


# Run the function and print the result in our case since we want to see the answer in the console
print(palindromechecker())
