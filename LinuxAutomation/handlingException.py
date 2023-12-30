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
        print('Exception: Any other exception except IndexError.')
        print(e)
        break
    finally:
        print('We are done with the try-except block.')
    

    # trying other exceptions
    try:
        # Generate an IOError
        raise IOError('This is an IOError')

        # Generate a KeyError
        dictionary = {}
        print(dictionary['non_existent_key'])

        # Generate an ImportError
        import non_existent_module
    except IOError as e:
        print('Caught an IOError:', e)
    except KeyError as e:
        print('Caught a KeyError:', e)
    except ImportError as e:
        print('Caught an ImportError:', e)  
    except IndexError as e:
        print(e)
        break
    except Exception as e:
        print('Exception: Any other exception except IndexError, IOError, KeyError, ImportError.')
        print(e)
        break
    finally:
        print('We are done with the try-except block.')


