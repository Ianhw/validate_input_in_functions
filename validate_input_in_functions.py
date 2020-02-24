



def multiply_string(test_name, test_score, invalid_message):

    test_score = int(test_score)
    if test_score >= 0 and test_score < 100:
        out = test_name,test_score
        return out
    elif test_score < 0 or test_score > 100:
        out = test_name,invalid_message
        return out



if __name__ == '__main__':
    print('Name of test:')
    test_name = input()

    print('test score:')
    one = input()
    test_score = int(one)

    invalid_message = 'Invalid test score, try again!'

    print(multiply_string(test_name, test_score, invalid_message))