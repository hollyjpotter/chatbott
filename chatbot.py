# says hello and their name
def hello():
    name = input(" What is your name? ")
    print(' Hello ' + name)
    print(' My name is Chatbot! Nice to meet you! ')
# processes how they respond to 'how are you'
def hru():
    hrur = input(' How are you? ')
    if (hrur.lower() == 'good'):
        print (" Great I'm glad! ")
    elif (hrur.lower() == 'fine'):
        print (" Same, I could be better. ")
    else:
        print (' Me too. ')
# age
def age():
    tage = input(' How old are you? ')
    print (' I remember when I was ' + tage )
    print (' I was so naive!')
#where are you
def wherelive():
    location = input(' Where are you located right now ')
    if (location.lower() == 'home'):
        print ('oh me too')
    elif (location.lower() == 'school'):
        print ('that is fun')
    else:
        print (' thats cool ')
#else
def shopping():
    print (' Oh you want to get down to bussiness. ')
    shoppingresponse = input (' What can I help you with? (dress, pants, shirts?) ')
    if (shoppingresponse.lower() = 'pants' ):
        pants()
    if (shoppingresponse.lower() = 'dress' ):
        dress()
    if (shoppingresponse.lower() = 'shirts' ):
        shirts()
    else:
        print (' I am sorry I do no understand. ')

# idk
def main():
  while True:
    answer1 = input(" (What will you say?) ")
    if (answer1.lower() == 'hi' or 'hello' or 'hey' or 'whats up'):
        hello()
    answer2 = input(' (What will you say?) ')
    if (answer2.lower() == 'how are you' or 'nice to meet you too' or +
        'nice to meet you to' or 'you too'):
            hru()


    # check what the user inputs
# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
