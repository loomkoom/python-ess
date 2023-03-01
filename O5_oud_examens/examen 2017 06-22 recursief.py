'''
        TIJD:    15 min
        geschat: 45 min

'''


def legal_path(path, connection_matrix):
    ''' nagaan of het pad volledig gevolgd kan worden
        connection_matrix[I][J] = True  is een geldige verbinding van I naar J (en neit per se omgekeerd)
        met path een sequentie van opeenvolgende locaties
    '''
    if len(path) == 1:
        return []

    else:
        connection = legal_path(path[1:], connection_matrix)
        if not connection_matrix[path[0]][path[1]]:
            connection.insert(0, (path[0], path[1]))

    return connection


the_matrix = \
 [ [True, False, True, True] ,
 [True, True, False, True] ,
 [False, False, True, True] ,
 [True, False, False, True] ]
assert legal_path([0,2,3,3,0,3],the_matrix) == []
assert not legal_path((1,3,2,2,3,1,2),the_matrix) == \
 [(3,2),(3,1),(3,2)]