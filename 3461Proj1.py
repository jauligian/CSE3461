import configparser
import logging

#removes any leading/trailing white space and tokenizes the input
def tokenize(str):
    str = str.strip()
    tokens = str.split()
    return tokens

#combines the tokens back together with a space separating and the first token all capitalized
def combine (str):
    str[0] = str[0].upper()
    combined = ' '.join(str) 
    return combined

#Set up the config parser
config = configparser.ConfigParser()
config.read('config.ini')

#print all configuration options
for section in config.sections():
    print("[" + section + "]")
    for key, value in config.items(section):
        print(key + " = " + value)
    print()

#clear the log file
with open('log.log', 'w'):
    pass

#setup the logger 
logging.basicConfig(filename='log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('3461 Project 1 starting')

#loop through input until getting 'quit' as first token
while True:
    #get input and tokenize it
    print('Enter an input string:')
    inp = input()
    tokens = tokenize(inp)
    
    #if the input was empty or only spaces starts loop over
    if len(tokens) == 0:
        continue
    
    #prints initial input
    logging.info(inp)
    
    #checks if first token was quit and stops loop
    if (tokens[0] == 'quit'):
        break
    
    #combines the tokens back together and prints the new string
    combined = combine(tokens)
    print(combined)
    logging.info(combined)

#Shut down program
print('Shutting down...')
logging.info('Shutting down...')
