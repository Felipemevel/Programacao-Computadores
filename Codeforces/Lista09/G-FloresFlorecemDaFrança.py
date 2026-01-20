while True:
    try:
        line = input().strip()
        if line == '*':
            break
            
        words = line.split()
        if not words:
            continue
            
        first = words[0][0].lower()
        is_tautogram = True
        
        for word in words[1:]:
            if word[0].lower() != first:
                is_tautogram = False
                break
        
        if is_tautogram:
            print('Y')
        else:
            print('N')

    except EOFError:
        break