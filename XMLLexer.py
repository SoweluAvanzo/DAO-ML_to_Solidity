# Generated from XMLLexer.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,46,674,6,-1,6,-1,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,
        4,2,5,7,5,2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,
        12,7,12,2,13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,
        18,2,19,7,19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,
        25,7,25,2,26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,
        31,2,32,7,32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,
        38,7,38,2,39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,
        44,2,45,7,45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,
        51,7,51,1,0,1,0,1,0,1,0,1,0,1,0,5,0,114,8,0,10,0,12,0,117,9,0,1,
        0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,134,
        8,1,10,1,12,1,137,9,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,5,2,147,8,
        2,10,2,12,2,150,9,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,
        1,4,4,4,164,8,4,11,4,12,4,165,1,4,1,4,1,4,1,4,1,4,1,4,1,4,4,4,175,
        8,4,11,4,12,4,176,1,4,1,4,3,4,181,8,4,1,5,1,5,3,5,185,8,5,1,5,4,
        5,188,8,5,11,5,12,5,189,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,4,9,215,8,9,
        11,9,12,9,216,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,
        1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,
        1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,
        1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,
        1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,27,
        1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,
        1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,32,
        1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,
        1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,
        1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,34,1,34,1,34,
        1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,35,
        1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,36,
        1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,
        1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,
        1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,
        1,40,1,41,1,41,1,42,1,42,1,43,1,43,5,43,626,8,43,10,43,12,43,629,
        9,43,1,43,1,43,1,43,5,43,634,8,43,10,43,12,43,637,9,43,1,43,3,43,
        640,8,43,1,44,1,44,5,44,644,8,44,10,44,12,44,647,9,44,1,45,1,45,
        1,45,1,45,1,46,1,46,1,47,1,47,1,48,1,48,1,48,1,48,3,48,661,8,48,
        1,49,3,49,664,8,49,1,50,1,50,1,50,1,50,1,50,1,51,1,51,1,51,1,51,
        3,115,135,148,0,52,3,1,5,2,7,3,9,4,11,5,13,6,15,7,17,8,19,0,21,9,
        23,10,25,11,27,12,29,13,31,14,33,15,35,16,37,17,39,18,41,19,43,20,
        45,21,47,22,49,23,51,24,53,25,55,26,57,27,59,28,61,29,63,30,65,31,
        67,32,69,33,71,34,73,35,75,36,77,37,79,38,81,39,83,40,85,41,87,42,
        89,43,91,44,93,45,95,0,97,0,99,0,101,0,103,46,105,0,3,0,1,2,9,2,
        0,9,9,32,32,2,0,38,38,60,60,2,0,34,34,60,60,2,0,39,39,60,60,3,0,
        9,10,13,13,32,32,3,0,48,57,65,70,97,102,1,0,48,57,3,0,183,183,768,
        879,8255,8256,9,0,58,58,65,90,95,95,97,122,8304,8591,11264,12271,
        12289,55295,63744,64975,65008,65533,684,0,3,1,0,0,0,0,5,1,0,0,0,
        0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,
        17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,1,23,1,0,0,0,1,25,1,0,0,0,1,
        27,1,0,0,0,1,29,1,0,0,0,1,31,1,0,0,0,1,33,1,0,0,0,1,35,1,0,0,0,1,
        37,1,0,0,0,1,39,1,0,0,0,1,41,1,0,0,0,1,43,1,0,0,0,1,45,1,0,0,0,1,
        47,1,0,0,0,1,49,1,0,0,0,1,51,1,0,0,0,1,53,1,0,0,0,1,55,1,0,0,0,1,
        57,1,0,0,0,1,59,1,0,0,0,1,61,1,0,0,0,1,63,1,0,0,0,1,65,1,0,0,0,1,
        67,1,0,0,0,1,69,1,0,0,0,1,71,1,0,0,0,1,73,1,0,0,0,1,75,1,0,0,0,1,
        77,1,0,0,0,1,79,1,0,0,0,1,81,1,0,0,0,1,83,1,0,0,0,1,85,1,0,0,0,1,
        87,1,0,0,0,1,89,1,0,0,0,1,91,1,0,0,0,1,93,1,0,0,0,2,103,1,0,0,0,
        2,105,1,0,0,0,3,107,1,0,0,0,5,122,1,0,0,0,7,142,1,0,0,0,9,155,1,
        0,0,0,11,180,1,0,0,0,13,187,1,0,0,0,15,191,1,0,0,0,17,195,1,0,0,
        0,19,205,1,0,0,0,21,214,1,0,0,0,23,218,1,0,0,0,25,233,1,0,0,0,27,
        237,1,0,0,0,29,242,1,0,0,0,31,252,1,0,0,0,33,263,1,0,0,0,35,278,
        1,0,0,0,37,292,1,0,0,0,39,309,1,0,0,0,41,320,1,0,0,0,43,335,1,0,
        0,0,45,342,1,0,0,0,47,351,1,0,0,0,49,369,1,0,0,0,51,394,1,0,0,0,
        53,402,1,0,0,0,55,412,1,0,0,0,57,435,1,0,0,0,59,448,1,0,0,0,61,470,
        1,0,0,0,63,482,1,0,0,0,65,494,1,0,0,0,67,513,1,0,0,0,69,536,1,0,
        0,0,71,550,1,0,0,0,73,563,1,0,0,0,75,578,1,0,0,0,77,589,1,0,0,0,
        79,605,1,0,0,0,81,609,1,0,0,0,83,614,1,0,0,0,85,619,1,0,0,0,87,621,
        1,0,0,0,89,639,1,0,0,0,91,641,1,0,0,0,93,648,1,0,0,0,95,652,1,0,
        0,0,97,654,1,0,0,0,99,660,1,0,0,0,101,663,1,0,0,0,103,665,1,0,0,
        0,105,670,1,0,0,0,107,108,5,60,0,0,108,109,5,33,0,0,109,110,5,45,
        0,0,110,111,5,45,0,0,111,115,1,0,0,0,112,114,9,0,0,0,113,112,1,0,
        0,0,114,117,1,0,0,0,115,116,1,0,0,0,115,113,1,0,0,0,116,118,1,0,
        0,0,117,115,1,0,0,0,118,119,5,45,0,0,119,120,5,45,0,0,120,121,5,
        62,0,0,121,4,1,0,0,0,122,123,5,60,0,0,123,124,5,33,0,0,124,125,5,
        91,0,0,125,126,5,67,0,0,126,127,5,68,0,0,127,128,5,65,0,0,128,129,
        5,84,0,0,129,130,5,65,0,0,130,131,5,91,0,0,131,135,1,0,0,0,132,134,
        9,0,0,0,133,132,1,0,0,0,134,137,1,0,0,0,135,136,1,0,0,0,135,133,
        1,0,0,0,136,138,1,0,0,0,137,135,1,0,0,0,138,139,5,93,0,0,139,140,
        5,93,0,0,140,141,5,62,0,0,141,6,1,0,0,0,142,143,5,60,0,0,143,144,
        5,33,0,0,144,148,1,0,0,0,145,147,9,0,0,0,146,145,1,0,0,0,147,150,
        1,0,0,0,148,149,1,0,0,0,148,146,1,0,0,0,149,151,1,0,0,0,150,148,
        1,0,0,0,151,152,5,62,0,0,152,153,1,0,0,0,153,154,6,2,0,0,154,8,1,
        0,0,0,155,156,5,38,0,0,156,157,3,91,44,0,157,158,5,59,0,0,158,10,
        1,0,0,0,159,160,5,38,0,0,160,161,5,35,0,0,161,163,1,0,0,0,162,164,
        3,97,47,0,163,162,1,0,0,0,164,165,1,0,0,0,165,163,1,0,0,0,165,166,
        1,0,0,0,166,167,1,0,0,0,167,168,5,59,0,0,168,181,1,0,0,0,169,170,
        5,38,0,0,170,171,5,35,0,0,171,172,5,120,0,0,172,174,1,0,0,0,173,
        175,3,95,46,0,174,173,1,0,0,0,175,176,1,0,0,0,176,174,1,0,0,0,176,
        177,1,0,0,0,177,178,1,0,0,0,178,179,5,59,0,0,179,181,1,0,0,0,180,
        159,1,0,0,0,180,169,1,0,0,0,181,12,1,0,0,0,182,188,7,0,0,0,183,185,
        5,13,0,0,184,183,1,0,0,0,184,185,1,0,0,0,185,186,1,0,0,0,186,188,
        5,10,0,0,187,182,1,0,0,0,187,184,1,0,0,0,188,189,1,0,0,0,189,187,
        1,0,0,0,189,190,1,0,0,0,190,14,1,0,0,0,191,192,5,60,0,0,192,193,
        1,0,0,0,193,194,6,6,1,0,194,16,1,0,0,0,195,196,5,60,0,0,196,197,
        5,63,0,0,197,198,5,120,0,0,198,199,5,109,0,0,199,200,5,108,0,0,200,
        201,1,0,0,0,201,202,3,93,45,0,202,203,1,0,0,0,203,204,6,7,1,0,204,
        18,1,0,0,0,205,206,5,60,0,0,206,207,5,63,0,0,207,208,1,0,0,0,208,
        209,3,91,44,0,209,210,1,0,0,0,210,211,6,8,2,0,211,212,6,8,3,0,212,
        20,1,0,0,0,213,215,8,1,0,0,214,213,1,0,0,0,215,216,1,0,0,0,216,214,
        1,0,0,0,216,217,1,0,0,0,217,22,1,0,0,0,218,219,5,68,0,0,219,220,
        5,65,0,0,220,221,5,79,0,0,221,222,5,45,0,0,222,223,5,77,0,0,223,
        224,5,76,0,0,224,225,5,95,0,0,225,226,5,100,0,0,226,227,5,105,0,
        0,227,228,5,97,0,0,228,229,5,103,0,0,229,230,5,114,0,0,230,231,5,
        97,0,0,231,232,5,109,0,0,232,24,1,0,0,0,233,234,5,68,0,0,234,235,
        5,65,0,0,235,236,5,79,0,0,236,26,1,0,0,0,237,238,5,82,0,0,238,239,
        5,111,0,0,239,240,5,108,0,0,240,241,5,101,0,0,241,28,1,0,0,0,242,
        243,5,67,0,0,243,244,5,111,0,0,244,245,5,109,0,0,245,246,5,109,0,
        0,246,247,5,105,0,0,247,248,5,116,0,0,248,249,5,116,0,0,249,250,
        5,101,0,0,250,251,5,101,0,0,251,30,1,0,0,0,252,253,5,80,0,0,253,
        254,5,101,0,0,254,255,5,114,0,0,255,256,5,109,0,0,256,257,5,105,
        0,0,257,258,5,115,0,0,258,259,5,115,0,0,259,260,5,105,0,0,260,261,
        5,111,0,0,261,262,5,110,0,0,262,32,1,0,0,0,263,264,5,71,0,0,264,
        265,5,111,0,0,265,266,5,118,0,0,266,267,5,101,0,0,267,268,5,114,
        0,0,268,269,5,110,0,0,269,270,5,97,0,0,270,271,5,110,0,0,271,272,
        5,99,0,0,272,273,5,101,0,0,273,274,5,65,0,0,274,275,5,114,0,0,275,
        276,5,101,0,0,276,277,5,97,0,0,277,34,1,0,0,0,278,279,5,97,0,0,279,
        280,5,115,0,0,280,281,5,115,0,0,281,282,5,111,0,0,282,283,5,99,0,
        0,283,284,5,105,0,0,284,285,5,97,0,0,285,286,5,116,0,0,286,287,5,
        101,0,0,287,288,5,100,0,0,288,289,5,95,0,0,289,290,5,116,0,0,290,
        291,5,111,0,0,291,36,1,0,0,0,292,293,5,105,0,0,293,294,5,115,0,0,
        294,295,5,95,0,0,295,296,5,99,0,0,296,297,5,111,0,0,297,298,5,110,
        0,0,298,299,5,116,0,0,299,300,5,114,0,0,300,301,5,111,0,0,301,302,
        5,108,0,0,302,303,5,108,0,0,303,304,5,101,0,0,304,305,5,100,0,0,
        305,306,5,95,0,0,306,307,5,98,0,0,307,308,5,121,0,0,308,38,1,0,0,
        0,309,310,5,97,0,0,310,311,5,103,0,0,311,312,5,103,0,0,312,313,5,
        114,0,0,313,314,5,101,0,0,314,315,5,103,0,0,315,316,5,97,0,0,316,
        317,5,116,0,0,317,318,5,101,0,0,318,319,5,115,0,0,319,40,1,0,0,0,
        320,321,5,102,0,0,321,322,5,101,0,0,322,323,5,100,0,0,323,324,5,
        101,0,0,324,325,5,114,0,0,325,326,5,97,0,0,326,327,5,116,0,0,327,
        328,5,101,0,0,328,329,5,115,0,0,329,330,5,95,0,0,330,331,5,105,0,
        0,331,332,5,110,0,0,332,333,5,116,0,0,333,334,5,111,0,0,334,42,1,
        0,0,0,335,336,5,68,0,0,336,337,5,65,0,0,337,338,5,79,0,0,338,339,
        5,95,0,0,339,340,5,73,0,0,340,341,5,68,0,0,341,44,1,0,0,0,342,343,
        5,68,0,0,343,344,5,65,0,0,344,345,5,79,0,0,345,346,5,95,0,0,346,
        347,5,110,0,0,347,348,5,97,0,0,348,349,5,109,0,0,349,350,5,101,0,
        0,350,46,1,0,0,0,351,352,5,109,0,0,352,353,5,105,0,0,353,354,5,115,
        0,0,354,355,5,115,0,0,355,356,5,105,0,0,356,357,5,111,0,0,357,358,
        5,110,0,0,358,359,5,95,0,0,359,360,5,115,0,0,360,361,5,116,0,0,361,
        362,5,97,0,0,362,363,5,116,0,0,363,364,5,101,0,0,364,365,5,109,0,
        0,365,366,5,101,0,0,366,367,5,110,0,0,367,368,5,116,0,0,368,48,1,
        0,0,0,369,370,5,104,0,0,370,371,5,105,0,0,371,372,5,101,0,0,372,
        373,5,114,0,0,373,374,5,97,0,0,374,375,5,114,0,0,375,376,5,99,0,
        0,376,377,5,104,0,0,377,378,5,105,0,0,378,379,5,99,0,0,379,380,5,
        97,0,0,380,381,5,108,0,0,381,382,5,95,0,0,382,383,5,105,0,0,383,
        384,5,110,0,0,384,385,5,104,0,0,385,386,5,101,0,0,386,387,5,114,
        0,0,387,388,5,105,0,0,388,389,5,116,0,0,389,390,5,97,0,0,390,391,
        5,110,0,0,391,392,5,99,0,0,392,393,5,101,0,0,393,50,1,0,0,0,394,
        395,5,114,0,0,395,396,5,111,0,0,396,397,5,108,0,0,397,398,5,101,
        0,0,398,399,5,95,0,0,399,400,5,73,0,0,400,401,5,68,0,0,401,52,1,
        0,0,0,402,403,5,114,0,0,403,404,5,111,0,0,404,405,5,108,0,0,405,
        406,5,101,0,0,406,407,5,95,0,0,407,408,5,110,0,0,408,409,5,97,0,
        0,409,410,5,109,0,0,410,411,5,101,0,0,411,54,1,0,0,0,412,413,5,114,
        0,0,413,414,5,111,0,0,414,415,5,108,0,0,415,416,5,101,0,0,416,417,
        5,95,0,0,417,418,5,97,0,0,418,419,5,115,0,0,419,420,5,115,0,0,420,
        421,5,105,0,0,421,422,5,103,0,0,422,423,5,110,0,0,423,424,5,109,
        0,0,424,425,5,101,0,0,425,426,5,110,0,0,426,427,5,116,0,0,427,428,
        5,95,0,0,428,429,5,109,0,0,429,430,5,101,0,0,430,431,5,116,0,0,431,
        432,5,104,0,0,432,433,5,111,0,0,433,434,5,100,0,0,434,56,1,0,0,0,
        435,436,5,99,0,0,436,437,5,111,0,0,437,438,5,109,0,0,438,439,5,109,
        0,0,439,440,5,105,0,0,440,441,5,116,0,0,441,442,5,116,0,0,442,443,
        5,101,0,0,443,444,5,101,0,0,444,445,5,95,0,0,445,446,5,73,0,0,446,
        447,5,68,0,0,447,58,1,0,0,0,448,449,5,99,0,0,449,450,5,111,0,0,450,
        451,5,109,0,0,451,452,5,109,0,0,452,453,5,105,0,0,453,454,5,116,
        0,0,454,455,5,116,0,0,455,456,5,101,0,0,456,457,5,101,0,0,457,458,
        5,95,0,0,458,459,5,100,0,0,459,460,5,101,0,0,460,461,5,115,0,0,461,
        462,5,99,0,0,462,463,5,114,0,0,463,464,5,105,0,0,464,465,5,112,0,
        0,465,466,5,116,0,0,466,467,5,105,0,0,467,468,5,111,0,0,468,469,
        5,110,0,0,469,60,1,0,0,0,470,471,5,110,0,0,471,472,5,95,0,0,472,
        473,5,97,0,0,473,474,5,103,0,0,474,475,5,101,0,0,475,476,5,110,0,
        0,476,477,5,116,0,0,477,478,5,95,0,0,478,479,5,109,0,0,479,480,5,
        105,0,0,480,481,5,110,0,0,481,62,1,0,0,0,482,483,5,110,0,0,483,484,
        5,95,0,0,484,485,5,97,0,0,485,486,5,103,0,0,486,487,5,101,0,0,487,
        488,5,110,0,0,488,489,5,116,0,0,489,490,5,95,0,0,490,491,5,109,0,
        0,491,492,5,97,0,0,492,493,5,120,0,0,493,64,1,0,0,0,494,495,5,97,
        0,0,495,496,5,112,0,0,496,497,5,112,0,0,497,498,5,111,0,0,498,499,
        5,105,0,0,499,500,5,110,0,0,500,501,5,116,0,0,501,502,5,109,0,0,
        502,503,5,101,0,0,503,504,5,110,0,0,504,505,5,116,0,0,505,506,5,
        95,0,0,506,507,5,109,0,0,507,508,5,101,0,0,508,509,5,116,0,0,509,
        510,5,104,0,0,510,511,5,111,0,0,511,512,5,100,0,0,512,66,1,0,0,0,
        513,514,5,100,0,0,514,515,5,101,0,0,515,516,5,99,0,0,516,517,5,105,
        0,0,517,518,5,115,0,0,518,519,5,105,0,0,519,520,5,111,0,0,520,521,
        5,110,0,0,521,522,5,95,0,0,522,523,5,109,0,0,523,524,5,97,0,0,524,
        525,5,107,0,0,525,526,5,105,0,0,526,527,5,110,0,0,527,528,5,103,
        0,0,528,529,5,95,0,0,529,530,5,109,0,0,530,531,5,101,0,0,531,532,
        5,116,0,0,532,533,5,104,0,0,533,534,5,111,0,0,534,535,5,100,0,0,
        535,68,1,0,0,0,536,537,5,112,0,0,537,538,5,101,0,0,538,539,5,114,
        0,0,539,540,5,109,0,0,540,541,5,105,0,0,541,542,5,115,0,0,542,543,
        5,115,0,0,543,544,5,105,0,0,544,545,5,111,0,0,545,546,5,110,0,0,
        546,547,5,95,0,0,547,548,5,73,0,0,548,549,5,68,0,0,549,70,1,0,0,
        0,550,551,5,114,0,0,551,552,5,101,0,0,552,553,5,102,0,0,553,554,
        5,95,0,0,554,555,5,103,0,0,555,556,5,111,0,0,556,557,5,118,0,0,557,
        558,5,95,0,0,558,559,5,97,0,0,559,560,5,114,0,0,560,561,5,101,0,
        0,561,562,5,97,0,0,562,72,1,0,0,0,563,564,5,97,0,0,564,565,5,108,
        0,0,565,566,5,108,0,0,566,567,5,111,0,0,567,568,5,119,0,0,568,569,
        5,101,0,0,569,570,5,100,0,0,570,571,5,95,0,0,571,572,5,97,0,0,572,
        573,5,99,0,0,573,574,5,116,0,0,574,575,5,105,0,0,575,576,5,111,0,
        0,576,577,5,110,0,0,577,74,1,0,0,0,578,579,5,97,0,0,579,580,5,103,
        0,0,580,581,5,101,0,0,581,582,5,110,0,0,582,583,5,116,0,0,583,584,
        5,95,0,0,584,585,5,116,0,0,585,586,5,121,0,0,586,587,5,112,0,0,587,
        588,5,101,0,0,588,76,1,0,0,0,589,590,5,112,0,0,590,591,5,101,0,0,
        591,592,5,114,0,0,592,593,5,109,0,0,593,594,5,105,0,0,594,595,5,
        115,0,0,595,596,5,115,0,0,596,597,5,105,0,0,597,598,5,111,0,0,598,
        599,5,110,0,0,599,600,5,95,0,0,600,601,5,116,0,0,601,602,5,121,0,
        0,602,603,5,112,0,0,603,604,5,101,0,0,604,78,1,0,0,0,605,606,5,62,
        0,0,606,607,1,0,0,0,607,608,6,38,4,0,608,80,1,0,0,0,609,610,5,63,
        0,0,610,611,5,62,0,0,611,612,1,0,0,0,612,613,6,39,4,0,613,82,1,0,
        0,0,614,615,5,47,0,0,615,616,5,62,0,0,616,617,1,0,0,0,617,618,6,
        40,4,0,618,84,1,0,0,0,619,620,5,47,0,0,620,86,1,0,0,0,621,622,5,
        61,0,0,622,88,1,0,0,0,623,627,5,34,0,0,624,626,8,2,0,0,625,624,1,
        0,0,0,626,629,1,0,0,0,627,625,1,0,0,0,627,628,1,0,0,0,628,630,1,
        0,0,0,629,627,1,0,0,0,630,640,5,34,0,0,631,635,5,39,0,0,632,634,
        8,3,0,0,633,632,1,0,0,0,634,637,1,0,0,0,635,633,1,0,0,0,635,636,
        1,0,0,0,636,638,1,0,0,0,637,635,1,0,0,0,638,640,5,39,0,0,639,623,
        1,0,0,0,639,631,1,0,0,0,640,90,1,0,0,0,641,645,3,101,49,0,642,644,
        3,99,48,0,643,642,1,0,0,0,644,647,1,0,0,0,645,643,1,0,0,0,645,646,
        1,0,0,0,646,92,1,0,0,0,647,645,1,0,0,0,648,649,7,4,0,0,649,650,1,
        0,0,0,650,651,6,45,0,0,651,94,1,0,0,0,652,653,7,5,0,0,653,96,1,0,
        0,0,654,655,7,6,0,0,655,98,1,0,0,0,656,661,3,101,49,0,657,661,2,
        45,46,0,658,661,3,97,47,0,659,661,7,7,0,0,660,656,1,0,0,0,660,657,
        1,0,0,0,660,658,1,0,0,0,660,659,1,0,0,0,661,100,1,0,0,0,662,664,
        7,8,0,0,663,662,1,0,0,0,664,102,1,0,0,0,665,666,5,63,0,0,666,667,
        5,62,0,0,667,668,1,0,0,0,668,669,6,50,4,0,669,104,1,0,0,0,670,671,
        9,0,0,0,671,672,1,0,0,0,672,673,6,51,2,0,673,106,1,0,0,0,19,0,1,
        2,115,135,148,165,176,180,184,187,189,216,627,635,639,645,660,663,
        5,6,0,0,5,1,0,3,0,0,5,2,0,4,0,0
    ]

class XMLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INSIDE = 1
    PROC_INSTR = 2

    COMMENT = 1
    CDATA = 2
    DTD = 3
    EntityRef = 4
    CharRef = 5
    SEA_WS = 6
    OPEN = 7
    XMLDeclOpen = 8
    TEXT = 9
    DIAGRAM = 10
    DAO = 11
    ROLE = 12
    COMMITTEE = 13
    PERMISSION = 14
    GOV = 15
    ASSOCIATION = 16
    CONTROL = 17
    AGGREGATES = 18
    FEDERATES = 19
    DAOID = 20
    DAONAME = 21
    MISSIONSTATEMENT = 22
    HIERARCHICALINHERITANCE = 23
    ROLEID = 24
    ROLENAME = 25
    ROLEASSIGNMENTMETHOD = 26
    COMMITTEEID = 27
    COMMITTEEDESCRIPTION = 28
    NAGENTMIN = 29
    NAGENTMAX = 30
    APPOINTMENTMETHOD = 31
    DMMETHOD = 32
    PERMISSIONID = 33
    REF_GOV_AREA = 34
    ALLOWEDACTION = 35
    AGENTTYPE = 36
    PERMISSIONTYPE = 37
    CLOSE = 38
    SPECIAL_CLOSE = 39
    SLASH_CLOSE = 40
    SLASH = 41
    EQUALS = 42
    STRING = 43
    Name = 44
    S = 45
    PI = 46

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE", "INSIDE", "PROC_INSTR" ]

    literalNames = [ "<INVALID>",
            "'<'", "'DAO-ML_diagram'", "'DAO'", "'Role'", "'Committee'", 
            "'Permission'", "'GovernanceArea'", "'associated_to'", "'is_controlled_by'", 
            "'aggregates'", "'federates_into'", "'DAO_ID'", "'DAO_name'", 
            "'mission_statement'", "'hierarchical_inheritance'", "'role_ID'", 
            "'role_name'", "'role_assignment_method'", "'committee_ID'", 
            "'committee_description'", "'n_agent_min'", "'n_agent_max'", 
            "'appointment_method'", "'decision_making_method'", "'permission_ID'", 
            "'ref_gov_area'", "'allowed_action'", "'agent_type'", "'permission_type'", 
            "'>'", "'/>'", "'/'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "CDATA", "DTD", "EntityRef", "CharRef", "SEA_WS", 
            "OPEN", "XMLDeclOpen", "TEXT", "DIAGRAM", "DAO", "ROLE", "COMMITTEE", 
            "PERMISSION", "GOV", "ASSOCIATION", "CONTROL", "AGGREGATES", 
            "FEDERATES", "DAOID", "DAONAME", "MISSIONSTATEMENT", "HIERARCHICALINHERITANCE", 
            "ROLEID", "ROLENAME", "ROLEASSIGNMENTMETHOD", "COMMITTEEID", 
            "COMMITTEEDESCRIPTION", "NAGENTMIN", "NAGENTMAX", "APPOINTMENTMETHOD", 
            "DMMETHOD", "PERMISSIONID", "REF_GOV_AREA", "ALLOWEDACTION", 
            "AGENTTYPE", "PERMISSIONTYPE", "CLOSE", "SPECIAL_CLOSE", "SLASH_CLOSE", 
            "SLASH", "EQUALS", "STRING", "Name", "S", "PI" ]

    ruleNames = [ "COMMENT", "CDATA", "DTD", "EntityRef", "CharRef", "SEA_WS", 
                  "OPEN", "XMLDeclOpen", "SPECIAL_OPEN", "TEXT", "DIAGRAM", 
                  "DAO", "ROLE", "COMMITTEE", "PERMISSION", "GOV", "ASSOCIATION", 
                  "CONTROL", "AGGREGATES", "FEDERATES", "DAOID", "DAONAME", 
                  "MISSIONSTATEMENT", "HIERARCHICALINHERITANCE", "ROLEID", 
                  "ROLENAME", "ROLEASSIGNMENTMETHOD", "COMMITTEEID", "COMMITTEEDESCRIPTION", 
                  "NAGENTMIN", "NAGENTMAX", "APPOINTMENTMETHOD", "DMMETHOD", 
                  "PERMISSIONID", "REF_GOV_AREA", "ALLOWEDACTION", "AGENTTYPE", 
                  "PERMISSIONTYPE", "CLOSE", "SPECIAL_CLOSE", "SLASH_CLOSE", 
                  "SLASH", "EQUALS", "STRING", "Name", "S", "HEXDIGIT", 
                  "DIGIT", "NameChar", "NameStartChar", "PI", "IGNORE" ]

    grammarFileName = "XMLLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


