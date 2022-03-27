def isnum(num):
    try:
        int(num)
        return True
    except ValueError:
        try:
            float(num)
            return True
        except:
            return False


    


