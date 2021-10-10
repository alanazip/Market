secret = "alana"
digitations = []

while True:
    letter = input('Digite uma letra:\n')

    if len(letter) > 1:
        print("Digite apenas uma letra.")
        continue

    digitations.append(letter)

    if letter in secret:
        print(f'A letra que você digitou contem na palavra secreta!')
    else:
        print(f'A letra que você digitou não contem na palavra secreta :(')
        digitations.pop()
    
    temporarySecret = ''
    for secretLetter in secret:
        if secretLetter in digitations:
            temporarySecret += secretLetter
        else:
            temporarySecret += '*'
    
    if temporarySecret == secret:
        print(f"Você ganhou!!! A palavra era {temporarySecret}.")
        break
    else:
        print(f'A palavra secreta está assim: {temporarySecret}')
