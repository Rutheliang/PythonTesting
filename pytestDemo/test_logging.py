import logging


def test_loggingDemo(): # move to baseclass.py

    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log') # what to print / where to print
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s") # what format
    fileHandler.setFormatter(formatter) # connecting the formatter and filehandler
    logger.addHandler(fileHandler)  # filehandler object / what format or what file should be send

    logger.setLevel(logging.CRITICAL) # hierarchy / order / level
    # if you set "info" then debug will not be displayed
    # if you set "debug" then all will be displayed
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("A major has happened")
    logger.critical("Critical issue")
