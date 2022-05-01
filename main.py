import random
def guessExpression():
  num = random.randint(1, 5)
  times = random.randint(1, 5)
  count = 0
  addex = ""
  while count != times:
    count += 1
    if count == times:
      addex += str(num)
    else:
      addex += str(num) + " + " 
  print(addex)
  ans = str(num) + " * " + str(times)
  print("What is the correct multiplication expression? Use \"*\" as the multiplication symbol, and space the symbols apart! ")
  ex = input()
  while ex != ans:
    print("Sorry! That's not correct. Try again! ")
    ex = input()
  print("Correct! Great job! Do you want to play again? \"retry\" or \"playground\" ")
  retryEx = input()
  print(retryEx)
  if retryEx == "retry":
    guessExpression()
  elif retryEx == "playground":
    playground()
def guessFactor():
  factor1 = random.randint(1, 5)
  factor2 = random.randint(1, 5)
  productFac = factor1 * factor2
  print(str(factor1) + " * _ = " + str(productFac))
  print("What is the correct factor? ")
  factorInput = input()
  while int(factorInput) != factor2:
    print("Sorry! That's not correct. One more time!")
    factorInput = input()
  print("Congratulations! You got it! Do you want to do it again? \"retry\" or \"playground\" ")
  retryFac = input()
  if retryFac == "retry":
    guessFactor()
  elif retryFac == "playground":
    playground()
def guessProduct():
  num1 = random.randint(1, 5)
  num2 = random.randint(1, 5)
  product = str(num1) + " * " + str(num2) + " = _ "
  print(product)
  print("What is the product? ")
  productCorrect = num1 * num2
  productInput = input()
  while int(productInput) != productCorrect:
      print("Sorry! That's not correct. You'll get it, though! ")
      productInput = input()
  print("Hooray! You\'re right! Do you want to try again? \"retry\" or \"playground\" ")
  retryPro = input()
  if retryPro == "retry":
    guessProduct()
  elif retryPro == "playground":
    playground()
def playground():
  print("What do you want to play? \"Expression\" \"Factor\" \"Product\" \"menu\" ")
  game = input()
  if game == "Expression":
    guessExpression()
  elif game == "Factor":
    guessFactor()
  elif game == "Product":
    guessProduct()
  elif game == "menu":
    print("Thank you for playing in the playground with me! See you around!")
    mainMenu()
def mainMenu():
  print("Buddy Boy Teaches Multiplication")
  print("Type in \"start\" or \"quit\" ")
  menu = input()
  if menu == "start":
    print("Hi! I'm Buddy Boy! What's your name? ")
    name = input()
    print("Hello, " + str(name) + "!")
    print("Do you want to do the tutorial? \"yes\" or \"no\" ")
    tutor = input()
    if tutor == "yes":
      print("Good choice! We'll spend most of our time in the playground, so let's check it out!")
      print("In the playground, you can play one of three fun games. There's \"Guess the Expression\", where you have to rewrite an addition expression, where the addends are the same, as a multiplication expression; \"Guess the Factor\", where you are given the first factor and the product, and have to guess the second factor; and finally, \"Guess the Product\", where you are given a multiplication equation, and have to find the product.")
      print("I hope you have fun in the playground! Bye!")
      playground()
    elif tutor == "no":
      playground()
  elif menu == "quit":
    print("Thank you for playing \"Buddy Boy Teaches Multiplication\" See you next time!")
mainMenu()