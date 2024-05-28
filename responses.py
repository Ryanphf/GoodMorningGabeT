from random import choice, randint



def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '/gabebio':
        return ('Gabriel Toumani is a 18 year old male standing at a stout 5 feet 5.5 inches. He is employed at Ohoo '
                'Boba in La Crescenta California, while also owning his own detailing business @Gtautodetailing! I '
                '*love* Gabe Toumani!'
                '\nHere is where you can reach him; \n**Email:** gabrieltoumani06@gmail.com \n**Phone:** 818-636-6615 \n'
                '**Instagram:** @gabriel_toumani\n'
                '**Website:** https://sites.google.com/view/gt-auto-detailing/home\n' 
                '**Discord:** <@724424331211309127> ')

    elif '/gabehelp' in lowered:
        return ('Hello there! Here are some commands you can use: \n **/gabebio;** short biography of the young man '
                'Gabriel Toumani \n -rolldice; im sure you can guess what this does \n **/gabeheight;** Gabriel\'s height '
                'in inches \n If you would like responses privately dm\'d to you, add a **"?"** before a command.')


    elif '/gabeheight' in lowered:
        return ('Gabriel Toumani stands at a height of 5 feet 5.5 inches! \n**This makes Gabe shorter than the average '
                'woman '
                'in these countries/regions:** Bosnia, Dinaric Alps(5\'7.5), Netherlands(5\'7), Montenegro, Latvia(5\'6.5)'
                ', Belgium, Iceland, Germany, Lithuania, Slovenia, Czech Republic, Denmark, Finland, Norway(5\'6).\n'
                '**Gabe is the same height as the average women in the following countries/regions:** Tonga, Albania, Kosovo-Pristina,'
                ' Serbia, Sweden, Samoa, Croatia, Senegal-Urban, Austria, Israel (5\'5.5).')

    elif 'bye' in lowered:
        return 'See ya!'

    elif '-rolldice' in lowered:
        return f'You rolled: {randint(1,6)}'

    else:
        return choice('')

