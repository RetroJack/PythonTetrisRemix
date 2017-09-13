import random

class selectPiece:

    #random.seed(954852142466813512254936128452465584689795469648)
    
    Mi_SHAPE_TEMPLATE = [['.....',
                          '.....',
                          '.....',
                          '.OO..',
                          '.....'],
                         ['.....',
                          '..O..',
                          '..O..',
                          '.....',
                          '.....']]

    i_SHAPE_TEMPLATE = [['.....',
                         '..O..',
                         '..O..',
                         '..O..',
                         '.....'],
                        ['.....',
                         '.....',
                         '.OOO.',
                         '.....',
                         '.....']]

    BO_SHAPE_TEMPLATE = [['.....',
                          '.O.O.',
                          '..O..',
                          '.....',
                          '.....'],
                         ['.....',
                          '..O..',
                          '.O...',
                          '..O..',
                          '.....']]

    FO_SHAPE_TEMPLATE = [['.....',
                          '.....',
                          '.....',
                          '.....',
                          '.....'],
                         ['.....',
                          '.....',
                          '.....',
                          '.....',
                          '.....']]

    I_SHAPE_TEMPLATE =  [['.....',
                          '.....',
                          'OOOOO',
                          '.....',
                          '.....'],
                         ['..O..',
                          '..O..',
                          '..O..',
                          '..O..',
                          '..O..']]

    S_SHAPE_TEMPLATE = [['.....',
                         '.....',
                         '..OO.',
                         '.OO..',
                         '.....'],
                        ['.....',
                         '..O..',
                         '..OO.',
                         '...O.',
                         '.....']]

    Z_SHAPE_TEMPLATE = [['.....',
                         '.....',
                         '.OO..',
                         '..OO.',
                         '.....'],
                        ['.....',
                         '..O..',
                         '.OO..',
                         '.O...',
                         '.....']]

    BLOCK_SHAPE_TEMPLATE = [['OOOOO',
                             'OOOOO',
                             'OOOOO',
                             'OOOOO',
                             'OOOOO']]

    FUK_SHAPE_TEMPLATE = [['OO.OO',
                           'O.O.O',
                           '.O.O.',
                           'O.O.O',
                           'OO.OO']]

    O_SHAPE_TEMPLATE = [['.....',
                         '.....',
                         '.OO..',
                         '.OO..',
                         '.....']]

    P_SHAPE_TEMPLATE = [['.....',
                         '..O..',
                         '.O.O.',
                         '..O..',
                         '.....']]

    D_SHAPE_TEMPLATE = [['.....',
                         '.....',
                         '..O..',
                         '.....',
                         '.....']]

    J_SHAPE_TEMPLATE = [['.....',
                         '.O...',
                         '.OOO.',
                         '.....',
                         '.....'],
                        ['.....',
                         '..OO.',
                         '..O..',
                         '..O..',
                         '.....'],
                        ['.....',
                         '.....',
                         '.OOO.',
                         '...O.',
                         '.....'],
                        ['.....',
                         '..O..',
                         '..O..',
                         '.OO..',
                         '.....']]

    L_SHAPE_TEMPLATE = [['.....',
                         '...O.',
                         '.OOO.',
                         '.....',
                         '.....'],
                        ['.....',
                         '..O..',
                         '..O..',
                         '..OO.',
                         '.....'],
                        ['.....',
                         '.....',
                         '.OOO.',
                         '.O...',
                         '.....'],
                        ['.....',
                         '.OO..',
                         '..O..',
                         '..O..',
                         '.....']]

    T_SHAPE_TEMPLATE = [['.....',
                         '..O..',
                         '.OOO.',
                         '.....',
                         '.....'],
                        ['.....',
                         '..O..',
                         '..OO.',
                         '..O..',
                         '.....'],
                        ['.....',
                         '.....',
                         '.OOO.',
                         '..O..',
                         '.....'],
                        ['.....',
                         '..O..',
                         '.OO..',
                         '..O..',
                         '.....']]
    
    NORMAL_PIECES = {'S': S_SHAPE_TEMPLATE,
                     'Z': Z_SHAPE_TEMPLATE,
                     'J': J_SHAPE_TEMPLATE,
                     'L': L_SHAPE_TEMPLATE,
                     'O': O_SHAPE_TEMPLATE,
                     'T': T_SHAPE_TEMPLATE}
    
    SUPER_PIECES ={'B': BLOCK_SHAPE_TEMPLATE,
                   '!': FUK_SHAPE_TEMPLATE,
                   'D'  : D_SHAPE_TEMPLATE,
                   'I'  : I_SHAPE_TEMPLATE,
                   'i'  : i_SHAPE_TEMPLATE,
                   'Mi' : Mi_SHAPE_TEMPLATE,
                   'P'  : P_SHAPE_TEMPLATE}
    recent = []
    pos    = 0
        
    def PieceSelection():
        pieceSelect=random.randint(1,50)
        if pieceSelect<=10:
            pieceName=random.choice(list(selectPiece.SUPER_PIECES))
            Template=selectPiece.SUPER_PIECES[pieceName]
        else:
            pieceName=random.choice(list(selectPiece.NORMAL_PIECES))
            Template=selectPiece.NORMAL_PIECES[pieceName]
        return Template

    def ColorSelection():
        #                R    G    B
        COLORS = {'1' :(255, 255, 255),#White
                  '2' :(185, 185, 185),#Gray
                  '3' :(  0,   0,   0),#Black
                  '4' :(155,   0,   0),#Red
                  '5' :(  0, 155,   0),#Green
                  '6' :(  0,   0, 155),#Blue
                  '7' :(155, 155,   0),#Yellow
                  '8' :(175,  20,  20),#LightRed
                  '9' :( 20, 175,  20),#LightGreen
                  '10':( 20,  20, 175),#LightBlue
                  '11':(175, 175,  20)}#LightYellow
        colorSelect=random.randint(1,12)
        color=(0,0,0)
        if colorSelect==12:
            color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        else:
            color=COLORS[str(colorSelect)]
        return color

    def checkPiece(pieceName):
        if pieceName in selectPiece.recent:
            return 0
        else:
            if len(selectPiece.recent)<3:
                selectPiece.recent.append(pieceName)
                selectPiece.pos+=1
            else:
                selectPiece.recent.pop(0)
                selectPiece.recent.append(pieceName)
            return 1
        
    def getPiece():
        color=selectPiece.ColorSelection()
        pieceList=selectPiece.PieceSelection()
        piece=pieceList[0]
        while selectPiece.checkPiece(piece) != 1:
            pieceList=selectPiece.PieceSelection()
            piece=pieceList[0]
        return (piece,color)
    
    

b=selectPiece
x=0
while x<100:
    print(b.getPiece())
    x+=1
