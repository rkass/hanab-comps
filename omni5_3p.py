from rank_teams import mps, pretty_print

seed_scores = {
    '1': [
        {
            'team': 'hakha3,padi,scharkbite',
            'turns': 32,
            'score': 13
        },
        {
            'team': 'kimbifille,Valetta6789,micerang',
            'turns': 58,
            'score': 25
        },    
        {
            'team': 'florrat2,sjrdrodge,libster',
            'turns': 52,
            'score': 25
        },
        {
            'team': 'dobi,wump,rz',
            'turns': 54,
            'score': 25
        },
        {
            'team': 'avanderwalde,JerryYang,rkass',
            'turns': 50,
            'score': 25
        },
        {
            'team': 'antitelharsic,Pablo-,nitawa',
            'turns': 55,
            'score': 25
        },
        {
            'team': 'BradyBot,KimG,RogueGal',
            'turns': 54,
            'score': 22
        }
    ],
    '2': [
        {
            'team': 'hakha3,padi,scharkbite',
            'turns': 48,
            'score': 20
        },
        {
            'team': 'kimbifille,Valetta6789,micerang',
            'turns': 54,
            'score': 25
        },    
        {
            'team': 'florrat2,sjrdrodge,libster',
            'turns': 52,
            'score': 25
        },
        {
            'team': 'dobi,wump,rz',
            'turns': 52,
            'score': 25
        },
        {
            'team': 'avanderwalde,JerryYang,rkass',
            'turns': 55,
            'score': 25
        },
        {
            'team': 'antitelharsic,Pablo-,nitawa',
            'turns': 55,
            'score': 24
        },
        {
            'team': 'BradyBot,KimG,RogueGal',
            'turns': None,
            'score': None
        }
    ],
    '3': [       
        {
            'team': 'hakha3,padi,scharkbite',
            'turns': 53,
            'score': 25
        },
        {
            'team': 'kimbifille,Valetta6789,micerang',
            'turns': 58,
            'score': 25
        },    
        {
            'team': 'florrat2,sjrdrodge,libster',
            'turns': 52,
            'score': 25
        },
        {
            'team': 'dobi,wump,rz',
            'turns': 54,
            'score': 25
        },
        {
            'team': 'avanderwalde,JerryYang,rkass',
            'turns': 51,
            'score': 25
        },
        {
            'team': 'antitelharsic,Pablo-,nitawa',
            'turns': 55,
            'score': 25
        },
        {
            'team': 'BradyBot,KimG,RogueGal',
            'turns': None,
            'score': None
        }
    ],
    '4': [
        {
            'team': 'hakha3,padi,scharkbite',
            'turns': 55,
            'score': 24
        },
        {
            'team': 'florrat2,sjrdrodge,libster',
            'turns': None,
            'score': None
        },
        {
            'team': 'dobi,wump,rz',
            'turns': 53,
            'score': 23
        },
        {
            'team': 'kimbifille,Valetta6789,micerang',
            'turns': 54,
            'score': 25
        },            
        {
            'team': 'avanderwalde,JerryYang,rkass',
            'turns': 55,
            'score': 25
        },
        {
            'team': 'antitelharsic,Pablo-,nitawa',
            'turns': 51,
            'score': 25
        },
        {
            'team': 'BradyBot,KimG,RogueGal',
            'turns': None,
            'score': None
        }
    ]
}
pretty_print(mps(seed_scores))