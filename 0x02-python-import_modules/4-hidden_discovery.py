#!/usr/bin/python3

if __name__ == "__main__":
    '''print names defined by compiled module hidden_4.pyc'''
    import hidden_4

    hidden = dir(hidden_4)
    for i in hidden:
        if (i[:1] != '_') and (i[:2] != '__'):
            print(hidden)
