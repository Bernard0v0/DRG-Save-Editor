from enum import Enum, StrEnum, auto


class Dwarf(StrEnum):
    DRILLER = "钻机手"
    GUNNER = "枪手"
    SCOUT = "侦察兵"
    ENGINEER = "工程师"


class Resource(Enum):
    BISMOR = auto()
    ENOR = auto()
    JADIZ = auto()
    CROPPA = auto()
    MAGNITE = auto()
    UMANITE = auto()
    YEAST = auto()
    MALT = auto()
    STARCH = auto()
    BARLEY = auto()
    ERROR = auto()
    CORES = auto()
    DATA = auto()
    PHAZ = auto()


class Category(StrEnum):
    """Type of overclock"""
    COSMETIC_BEARD = "时装 - 下颚胡须"
    COSMETIC_HEADWEAR = "时装 - 头饰"
    COSMETIC_MUSTACHE = "时装 - 上唇胡须"
    COSMETIC_SIDEBURNS = "时装 - 鬓角"
    VICTORY_MOVES = "胜利姿势"
    WEAPONS = "武器"
    WEAPON_SKINS = "武器涂装"
    UNKNOWN = "未知"


class Status(StrEnum):
    """Status of an overclock"""
    UNACQUIRED = "未获取"
    UNFORGED = "未锻造"
    FORGED = "已锻造"
