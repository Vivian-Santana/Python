#from code import Background
from code.Background import Background
from code.Const import WIN_WIDTH


class EntityFactory:
    
    @staticmethod
    def get_entity(entity_name: str, position = (0, 0)):
        # match-case é funcionalmente equivalente ao switch-case encontrado em outras linguagens
        # aplicado dessa forma genérica evita que fique grande e repetitivo.
        match entity_name:
            case 'Level1Bg':
                list_bg = [] # carrega tds os backgrouds dentro de uma lista um por um e guarda na list_bg
                for i in range(7): # level1Bg numero de imgs
                    list_bg.append(Background(name= f'Level1Bg{i}', position = (0,0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
