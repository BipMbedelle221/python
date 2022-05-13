EXPECTED_BAKE_TIME = 40
prep = 2
def bake_time_remaining(elapsed_bake_time ):
    '''
    :param elapsed_bake_time: int baking time already elapsed
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'
 
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    '''
        
    return EXPECTED_BAKE_TIME - elapsed_bake_time
def preparation_time_in_minutes(number_of_layers ):
    """
    :param layers: int total of layers of lasagna
    :return: int total time of preparation of layers derived from         
    'PREPARATION_TIME'
 
    Function that takes the number of layers that will be prepared to lasagna     and returns how many minutes it will take to get done
    """
      
    return  number_of_layers  * prep
def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time ):
    """
    Return elapsed cooking time.
 
    This function takes two numbers representing the number of layers & the       time already spent 
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    
    return elapsed_bake_time + (number_of_layers * prep )
