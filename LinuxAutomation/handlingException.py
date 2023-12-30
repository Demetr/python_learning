thinkers = ['Plato', 'Playdough', 'Gumby']
while True:
    try:
        thinker = thinkers.pop()
        print(thinker)
    except IndexError as e:
        print('Exception: We tried to pop too many thinkers.')
        print(e)
        break
    except Exception as e:
        print(e)
        break
    finally:
        print('We are done with the try-except block.')
    
