# try, catch
# code will fail but you don't want test case to stop then you can wrap that specific code in try block
# python use the key word except instead of catch


try:
    with open('filelog.txt', 'r') as reader: # randon file filelog.text / file doesn't exist
        reader.read()

except:
    print("Somehow I reached this block because there is failure in try block")  # customize failure message

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except Exception as e: # python error not your specific msg or customize msg
    print(e)

# use this keyword if you use try catch mechanism / always use this after try catch
# What is  purpose of finally keyword - delete cookies or any records like data / clean up records
finally:
    print("Cleaning up records")






