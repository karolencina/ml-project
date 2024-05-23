from src.app.utils.logger import logging

def main():
    logging.info('Inside the main function')
    return "Test this function"

if __name__ == '__main__':
    logging.info('Start of the code') 
    main()
    logging.info('End of the code')
    