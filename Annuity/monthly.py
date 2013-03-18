if(__name__=='__main__'):
    principle = raw_input('Enter a principle amount: ')
    years = raw_input('Enter the number of years of the debt: ')
    tempInterest = raw_input('Enter an APR (ie: 3.4%): ')

    try:
#I'm assuming you're given an APR, not a purely monthly rate
        rate = float(tempInterest) / 1200.0
    except ValueError:
        print "Enter a valid number for the principle"
        exit(1)
    
    try:
        periods = float(years)*12.0
    except ValueError:
        print "Enter a valid number for the number of years"
        exit(1)
        
    exponent = (1.0+rate)**periods

    answer = float(principle) * (rate + (rate/(exponent - 1)))

    print "The monthly payment is: " + str(answer)
