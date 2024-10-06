# Generated from XMLParser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,49,617,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,1,0,3,0,84,8,0,1,0,5,0,87,8,0,10,0,12,0,90,9,0,1,0,1,0,
        5,0,94,8,0,10,0,12,0,97,9,0,1,0,1,0,1,1,1,1,5,1,103,8,1,10,1,12,
        1,106,9,1,1,1,1,1,1,2,3,2,111,8,2,1,2,1,2,1,2,1,2,1,2,3,2,118,8,
        2,1,2,3,2,121,8,2,5,2,123,8,2,10,2,12,2,126,9,2,1,3,1,3,1,3,5,3,
        131,8,3,10,3,12,3,134,9,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,5,3,146,8,3,10,3,12,3,149,9,3,1,3,3,3,152,8,3,1,4,1,4,1,4,5,4,
        157,8,4,10,4,12,4,160,9,4,1,4,5,4,163,8,4,10,4,12,4,166,9,4,1,4,
        5,4,169,8,4,10,4,12,4,172,9,4,1,4,1,4,3,4,176,8,4,1,4,1,4,1,4,1,
        4,1,4,3,4,183,8,4,1,4,3,4,186,8,4,5,4,188,8,4,10,4,12,4,191,9,4,
        1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,5,5,201,8,5,10,5,12,5,204,9,5,1,
        5,1,5,5,5,208,8,5,10,5,12,5,211,9,5,1,5,1,5,5,5,215,8,5,10,5,12,
        5,218,9,5,1,5,1,5,5,5,222,8,5,10,5,12,5,225,9,5,1,5,1,5,5,5,229,
        8,5,10,5,12,5,232,9,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,5,
        6,244,8,6,10,6,12,6,247,9,6,1,6,1,6,5,6,251,8,6,10,6,12,6,254,9,
        6,1,6,1,6,5,6,258,8,6,10,6,12,6,261,9,6,1,6,1,6,5,6,265,8,6,10,6,
        12,6,268,9,6,1,6,3,6,271,8,6,1,6,5,6,274,8,6,10,6,12,6,277,9,6,1,
        6,3,6,280,8,6,1,6,5,6,283,8,6,10,6,12,6,286,9,6,1,6,1,6,5,6,290,
        8,6,10,6,12,6,293,9,6,1,6,1,6,5,6,297,8,6,10,6,12,6,300,9,6,1,6,
        1,6,5,6,304,8,6,10,6,12,6,307,9,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        7,1,7,1,7,1,7,5,7,320,8,7,10,7,12,7,323,9,7,1,7,1,7,5,7,327,8,7,
        10,7,12,7,330,9,7,1,7,3,7,333,8,7,1,7,5,7,336,8,7,10,7,12,7,339,
        9,7,1,7,3,7,342,8,7,1,7,5,7,345,8,7,10,7,12,7,348,9,7,1,7,3,7,351,
        8,7,1,7,5,7,354,8,7,10,7,12,7,357,9,7,1,7,1,7,5,7,361,8,7,10,7,12,
        7,364,9,7,1,7,1,7,5,7,368,8,7,10,7,12,7,371,9,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,8,1,8,1,8,1,8,5,8,384,8,8,10,8,12,8,387,9,8,1,8,1,
        8,5,8,391,8,8,10,8,12,8,394,9,8,1,8,1,8,5,8,398,8,8,10,8,12,8,401,
        9,8,1,8,3,8,404,8,8,1,8,5,8,407,8,8,10,8,12,8,410,9,8,1,8,1,8,1,
        9,1,9,1,9,5,9,417,8,9,10,9,12,9,420,9,9,1,9,1,9,1,10,3,10,425,8,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,435,8,10,1,10,3,
        10,438,8,10,5,10,440,8,10,10,10,12,10,443,9,10,1,11,3,11,446,8,11,
        1,11,1,11,1,11,1,11,1,11,3,11,453,8,11,1,11,3,11,456,8,11,5,11,458,
        8,11,10,11,12,11,461,9,11,1,12,1,12,1,12,5,12,466,8,12,10,12,12,
        12,469,9,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,5,
        13,481,8,13,10,13,12,13,484,9,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,14,1,14,1,14,5,14,496,8,14,10,14,12,14,499,9,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,5,15,511,8,15,10,15,12,15,
        514,9,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,17,1,17,
        1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,20,1,20,1,20,
        1,20,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,
        1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,27,
        1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,30,1,30,
        1,30,1,30,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,33,1,33,1,33,
        1,33,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,36,
        1,37,1,37,1,37,1,37,1,38,1,38,1,38,1,38,1,39,1,39,1,40,1,40,1,40,
        0,0,41,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,0,3,
        1,0,4,5,2,0,6,6,9,9,3,0,1,1,6,6,49,49,652,0,83,1,0,0,0,2,100,1,0,
        0,0,4,110,1,0,0,0,6,151,1,0,0,0,8,153,1,0,0,0,10,197,1,0,0,0,12,
        240,1,0,0,0,14,315,1,0,0,0,16,379,1,0,0,0,18,413,1,0,0,0,20,424,
        1,0,0,0,22,445,1,0,0,0,24,462,1,0,0,0,26,477,1,0,0,0,28,492,1,0,
        0,0,30,507,1,0,0,0,32,522,1,0,0,0,34,524,1,0,0,0,36,528,1,0,0,0,
        38,532,1,0,0,0,40,536,1,0,0,0,42,540,1,0,0,0,44,544,1,0,0,0,46,548,
        1,0,0,0,48,552,1,0,0,0,50,556,1,0,0,0,52,560,1,0,0,0,54,564,1,0,
        0,0,56,568,1,0,0,0,58,572,1,0,0,0,60,576,1,0,0,0,62,580,1,0,0,0,
        64,584,1,0,0,0,66,588,1,0,0,0,68,592,1,0,0,0,70,596,1,0,0,0,72,600,
        1,0,0,0,74,604,1,0,0,0,76,608,1,0,0,0,78,612,1,0,0,0,80,614,1,0,
        0,0,82,84,3,2,1,0,83,82,1,0,0,0,83,84,1,0,0,0,84,88,1,0,0,0,85,87,
        3,80,40,0,86,85,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,
        0,89,91,1,0,0,0,90,88,1,0,0,0,91,95,3,8,4,0,92,94,3,80,40,0,93,92,
        1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,98,1,0,0,0,
        97,95,1,0,0,0,98,99,5,0,0,1,99,1,1,0,0,0,100,104,5,8,0,0,101,103,
        3,76,38,0,102,101,1,0,0,0,103,106,1,0,0,0,104,102,1,0,0,0,104,105,
        1,0,0,0,105,107,1,0,0,0,106,104,1,0,0,0,107,108,5,42,0,0,108,3,1,
        0,0,0,109,111,3,78,39,0,110,109,1,0,0,0,110,111,1,0,0,0,111,124,
        1,0,0,0,112,118,3,6,3,0,113,118,3,32,16,0,114,118,5,2,0,0,115,118,
        5,49,0,0,116,118,5,1,0,0,117,112,1,0,0,0,117,113,1,0,0,0,117,114,
        1,0,0,0,117,115,1,0,0,0,117,116,1,0,0,0,118,120,1,0,0,0,119,121,
        3,78,39,0,120,119,1,0,0,0,120,121,1,0,0,0,121,123,1,0,0,0,122,117,
        1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,125,5,1,
        0,0,0,126,124,1,0,0,0,127,128,5,7,0,0,128,132,5,47,0,0,129,131,3,
        76,38,0,130,129,1,0,0,0,131,134,1,0,0,0,132,130,1,0,0,0,132,133,
        1,0,0,0,133,135,1,0,0,0,134,132,1,0,0,0,135,136,5,41,0,0,136,137,
        3,4,2,0,137,138,5,7,0,0,138,139,5,44,0,0,139,140,5,47,0,0,140,141,
        5,41,0,0,141,152,1,0,0,0,142,143,5,7,0,0,143,147,5,47,0,0,144,146,
        3,76,38,0,145,144,1,0,0,0,146,149,1,0,0,0,147,145,1,0,0,0,147,148,
        1,0,0,0,148,150,1,0,0,0,149,147,1,0,0,0,150,152,5,43,0,0,151,127,
        1,0,0,0,151,142,1,0,0,0,152,7,1,0,0,0,153,154,5,7,0,0,154,158,5,
        10,0,0,155,157,3,80,40,0,156,155,1,0,0,0,157,160,1,0,0,0,158,156,
        1,0,0,0,158,159,1,0,0,0,159,164,1,0,0,0,160,158,1,0,0,0,161,163,
        3,76,38,0,162,161,1,0,0,0,163,166,1,0,0,0,164,162,1,0,0,0,164,165,
        1,0,0,0,165,170,1,0,0,0,166,164,1,0,0,0,167,169,3,80,40,0,168,167,
        1,0,0,0,169,172,1,0,0,0,170,168,1,0,0,0,170,171,1,0,0,0,171,173,
        1,0,0,0,172,170,1,0,0,0,173,175,5,41,0,0,174,176,3,78,39,0,175,174,
        1,0,0,0,175,176,1,0,0,0,176,189,1,0,0,0,177,183,3,10,5,0,178,183,
        3,32,16,0,179,183,5,2,0,0,180,183,5,49,0,0,181,183,5,1,0,0,182,177,
        1,0,0,0,182,178,1,0,0,0,182,179,1,0,0,0,182,180,1,0,0,0,182,181,
        1,0,0,0,183,185,1,0,0,0,184,186,3,78,39,0,185,184,1,0,0,0,185,186,
        1,0,0,0,186,188,1,0,0,0,187,182,1,0,0,0,188,191,1,0,0,0,189,187,
        1,0,0,0,189,190,1,0,0,0,190,192,1,0,0,0,191,189,1,0,0,0,192,193,
        5,7,0,0,193,194,5,44,0,0,194,195,5,10,0,0,195,196,5,41,0,0,196,9,
        1,0,0,0,197,198,5,7,0,0,198,202,5,11,0,0,199,201,3,80,40,0,200,199,
        1,0,0,0,201,204,1,0,0,0,202,200,1,0,0,0,202,203,1,0,0,0,203,205,
        1,0,0,0,204,202,1,0,0,0,205,209,3,34,17,0,206,208,3,80,40,0,207,
        206,1,0,0,0,208,211,1,0,0,0,209,207,1,0,0,0,209,210,1,0,0,0,210,
        212,1,0,0,0,211,209,1,0,0,0,212,216,3,36,18,0,213,215,3,80,40,0,
        214,213,1,0,0,0,215,218,1,0,0,0,216,214,1,0,0,0,216,217,1,0,0,0,
        217,219,1,0,0,0,218,216,1,0,0,0,219,223,3,38,19,0,220,222,3,80,40,
        0,221,220,1,0,0,0,222,225,1,0,0,0,223,221,1,0,0,0,223,224,1,0,0,
        0,224,226,1,0,0,0,225,223,1,0,0,0,226,230,3,40,20,0,227,229,3,80,
        40,0,228,227,1,0,0,0,229,232,1,0,0,0,230,228,1,0,0,0,230,231,1,0,
        0,0,231,233,1,0,0,0,232,230,1,0,0,0,233,234,5,41,0,0,234,235,3,20,
        10,0,235,236,5,7,0,0,236,237,5,44,0,0,237,238,5,11,0,0,238,239,5,
        41,0,0,239,11,1,0,0,0,240,241,5,7,0,0,241,245,5,12,0,0,242,244,3,
        80,40,0,243,242,1,0,0,0,244,247,1,0,0,0,245,243,1,0,0,0,245,246,
        1,0,0,0,246,248,1,0,0,0,247,245,1,0,0,0,248,252,3,42,21,0,249,251,
        3,80,40,0,250,249,1,0,0,0,251,254,1,0,0,0,252,250,1,0,0,0,252,253,
        1,0,0,0,253,255,1,0,0,0,254,252,1,0,0,0,255,259,3,44,22,0,256,258,
        3,80,40,0,257,256,1,0,0,0,258,261,1,0,0,0,259,257,1,0,0,0,259,260,
        1,0,0,0,260,262,1,0,0,0,261,259,1,0,0,0,262,266,3,46,23,0,263,265,
        3,80,40,0,264,263,1,0,0,0,265,268,1,0,0,0,266,264,1,0,0,0,266,267,
        1,0,0,0,267,270,1,0,0,0,268,266,1,0,0,0,269,271,3,48,24,0,270,269,
        1,0,0,0,270,271,1,0,0,0,271,275,1,0,0,0,272,274,3,80,40,0,273,272,
        1,0,0,0,274,277,1,0,0,0,275,273,1,0,0,0,275,276,1,0,0,0,276,279,
        1,0,0,0,277,275,1,0,0,0,278,280,3,50,25,0,279,278,1,0,0,0,279,280,
        1,0,0,0,280,284,1,0,0,0,281,283,3,80,40,0,282,281,1,0,0,0,283,286,
        1,0,0,0,284,282,1,0,0,0,284,285,1,0,0,0,285,287,1,0,0,0,286,284,
        1,0,0,0,287,291,3,52,26,0,288,290,3,80,40,0,289,288,1,0,0,0,290,
        293,1,0,0,0,291,289,1,0,0,0,291,292,1,0,0,0,292,294,1,0,0,0,293,
        291,1,0,0,0,294,298,3,64,32,0,295,297,3,80,40,0,296,295,1,0,0,0,
        297,300,1,0,0,0,298,296,1,0,0,0,298,299,1,0,0,0,299,301,1,0,0,0,
        300,298,1,0,0,0,301,305,3,66,33,0,302,304,3,80,40,0,303,302,1,0,
        0,0,304,307,1,0,0,0,305,303,1,0,0,0,305,306,1,0,0,0,306,308,1,0,
        0,0,307,305,1,0,0,0,308,309,5,41,0,0,309,310,3,22,11,0,310,311,5,
        7,0,0,311,312,5,44,0,0,312,313,5,12,0,0,313,314,5,41,0,0,314,13,
        1,0,0,0,315,316,5,7,0,0,316,317,5,13,0,0,317,321,3,54,27,0,318,320,
        3,80,40,0,319,318,1,0,0,0,320,323,1,0,0,0,321,319,1,0,0,0,321,322,
        1,0,0,0,322,324,1,0,0,0,323,321,1,0,0,0,324,328,3,56,28,0,325,327,
        3,80,40,0,326,325,1,0,0,0,327,330,1,0,0,0,328,326,1,0,0,0,328,329,
        1,0,0,0,329,332,1,0,0,0,330,328,1,0,0,0,331,333,3,58,29,0,332,331,
        1,0,0,0,332,333,1,0,0,0,333,337,1,0,0,0,334,336,3,80,40,0,335,334,
        1,0,0,0,336,339,1,0,0,0,337,335,1,0,0,0,337,338,1,0,0,0,338,341,
        1,0,0,0,339,337,1,0,0,0,340,342,3,60,30,0,341,340,1,0,0,0,341,342,
        1,0,0,0,342,346,1,0,0,0,343,345,3,80,40,0,344,343,1,0,0,0,345,348,
        1,0,0,0,346,344,1,0,0,0,346,347,1,0,0,0,347,350,1,0,0,0,348,346,
        1,0,0,0,349,351,3,62,31,0,350,349,1,0,0,0,350,351,1,0,0,0,351,355,
        1,0,0,0,352,354,3,80,40,0,353,352,1,0,0,0,354,357,1,0,0,0,355,353,
        1,0,0,0,355,356,1,0,0,0,356,358,1,0,0,0,357,355,1,0,0,0,358,362,
        3,64,32,0,359,361,3,80,40,0,360,359,1,0,0,0,361,364,1,0,0,0,362,
        360,1,0,0,0,362,363,1,0,0,0,363,365,1,0,0,0,364,362,1,0,0,0,365,
        369,3,66,33,0,366,368,3,80,40,0,367,366,1,0,0,0,368,371,1,0,0,0,
        369,367,1,0,0,0,369,370,1,0,0,0,370,372,1,0,0,0,371,369,1,0,0,0,
        372,373,5,41,0,0,373,374,3,22,11,0,374,375,5,7,0,0,375,376,5,44,
        0,0,376,377,5,13,0,0,377,378,5,41,0,0,378,15,1,0,0,0,379,380,5,7,
        0,0,380,381,5,14,0,0,381,385,3,68,34,0,382,384,3,80,40,0,383,382,
        1,0,0,0,384,387,1,0,0,0,385,383,1,0,0,0,385,386,1,0,0,0,386,388,
        1,0,0,0,387,385,1,0,0,0,388,392,3,70,35,0,389,391,3,80,40,0,390,
        389,1,0,0,0,391,394,1,0,0,0,392,390,1,0,0,0,392,393,1,0,0,0,393,
        395,1,0,0,0,394,392,1,0,0,0,395,399,3,72,36,0,396,398,3,80,40,0,
        397,396,1,0,0,0,398,401,1,0,0,0,399,397,1,0,0,0,399,400,1,0,0,0,
        400,403,1,0,0,0,401,399,1,0,0,0,402,404,3,74,37,0,403,402,1,0,0,
        0,403,404,1,0,0,0,404,408,1,0,0,0,405,407,3,80,40,0,406,405,1,0,
        0,0,407,410,1,0,0,0,408,406,1,0,0,0,408,409,1,0,0,0,409,411,1,0,
        0,0,410,408,1,0,0,0,411,412,5,43,0,0,412,17,1,0,0,0,413,414,5,7,
        0,0,414,418,5,15,0,0,415,417,3,76,38,0,416,415,1,0,0,0,417,420,1,
        0,0,0,418,416,1,0,0,0,418,419,1,0,0,0,419,421,1,0,0,0,420,418,1,
        0,0,0,421,422,5,43,0,0,422,19,1,0,0,0,423,425,3,78,39,0,424,423,
        1,0,0,0,424,425,1,0,0,0,425,441,1,0,0,0,426,435,3,12,6,0,427,435,
        3,14,7,0,428,435,3,16,8,0,429,435,3,18,9,0,430,435,3,32,16,0,431,
        435,5,2,0,0,432,435,5,49,0,0,433,435,5,1,0,0,434,426,1,0,0,0,434,
        427,1,0,0,0,434,428,1,0,0,0,434,429,1,0,0,0,434,430,1,0,0,0,434,
        431,1,0,0,0,434,432,1,0,0,0,434,433,1,0,0,0,435,437,1,0,0,0,436,
        438,3,78,39,0,437,436,1,0,0,0,437,438,1,0,0,0,438,440,1,0,0,0,439,
        434,1,0,0,0,440,443,1,0,0,0,441,439,1,0,0,0,441,442,1,0,0,0,442,
        21,1,0,0,0,443,441,1,0,0,0,444,446,3,78,39,0,445,444,1,0,0,0,445,
        446,1,0,0,0,446,459,1,0,0,0,447,453,3,24,12,0,448,453,3,26,13,0,
        449,453,3,28,14,0,450,453,3,30,15,0,451,453,5,1,0,0,452,447,1,0,
        0,0,452,448,1,0,0,0,452,449,1,0,0,0,452,450,1,0,0,0,452,451,1,0,
        0,0,453,455,1,0,0,0,454,456,3,78,39,0,455,454,1,0,0,0,455,456,1,
        0,0,0,456,458,1,0,0,0,457,452,1,0,0,0,458,461,1,0,0,0,459,457,1,
        0,0,0,459,460,1,0,0,0,460,23,1,0,0,0,461,459,1,0,0,0,462,463,5,7,
        0,0,463,467,5,16,0,0,464,466,3,76,38,0,465,464,1,0,0,0,466,469,1,
        0,0,0,467,465,1,0,0,0,467,468,1,0,0,0,468,470,1,0,0,0,469,467,1,
        0,0,0,470,471,5,41,0,0,471,472,3,4,2,0,472,473,5,7,0,0,473,474,5,
        44,0,0,474,475,5,16,0,0,475,476,5,41,0,0,476,25,1,0,0,0,477,478,
        5,7,0,0,478,482,5,17,0,0,479,481,3,76,38,0,480,479,1,0,0,0,481,484,
        1,0,0,0,482,480,1,0,0,0,482,483,1,0,0,0,483,485,1,0,0,0,484,482,
        1,0,0,0,485,486,5,41,0,0,486,487,3,4,2,0,487,488,5,7,0,0,488,489,
        5,44,0,0,489,490,5,17,0,0,490,491,5,41,0,0,491,27,1,0,0,0,492,493,
        5,7,0,0,493,497,5,18,0,0,494,496,3,76,38,0,495,494,1,0,0,0,496,499,
        1,0,0,0,497,495,1,0,0,0,497,498,1,0,0,0,498,500,1,0,0,0,499,497,
        1,0,0,0,500,501,5,41,0,0,501,502,3,4,2,0,502,503,5,7,0,0,503,504,
        5,44,0,0,504,505,5,18,0,0,505,506,5,41,0,0,506,29,1,0,0,0,507,508,
        5,7,0,0,508,512,5,19,0,0,509,511,3,76,38,0,510,509,1,0,0,0,511,514,
        1,0,0,0,512,510,1,0,0,0,512,513,1,0,0,0,513,515,1,0,0,0,514,512,
        1,0,0,0,515,516,5,41,0,0,516,517,3,4,2,0,517,518,5,7,0,0,518,519,
        5,44,0,0,519,520,5,19,0,0,520,521,5,41,0,0,521,31,1,0,0,0,522,523,
        7,0,0,0,523,33,1,0,0,0,524,525,5,20,0,0,525,526,5,45,0,0,526,527,
        5,46,0,0,527,35,1,0,0,0,528,529,5,21,0,0,529,530,5,45,0,0,530,531,
        5,46,0,0,531,37,1,0,0,0,532,533,5,22,0,0,533,534,5,45,0,0,534,535,
        5,46,0,0,535,39,1,0,0,0,536,537,5,23,0,0,537,538,5,45,0,0,538,539,
        5,46,0,0,539,41,1,0,0,0,540,541,5,24,0,0,541,542,5,45,0,0,542,543,
        5,46,0,0,543,43,1,0,0,0,544,545,5,25,0,0,545,546,5,45,0,0,546,547,
        5,46,0,0,547,45,1,0,0,0,548,549,5,26,0,0,549,550,5,45,0,0,550,551,
        5,46,0,0,551,47,1,0,0,0,552,553,5,29,0,0,553,554,5,45,0,0,554,555,
        5,46,0,0,555,49,1,0,0,0,556,557,5,30,0,0,557,558,5,45,0,0,558,559,
        5,46,0,0,559,51,1,0,0,0,560,561,5,37,0,0,561,562,5,45,0,0,562,563,
        5,46,0,0,563,53,1,0,0,0,564,565,5,27,0,0,565,566,5,45,0,0,566,567,
        5,46,0,0,567,55,1,0,0,0,568,569,5,28,0,0,569,570,5,45,0,0,570,571,
        5,46,0,0,571,57,1,0,0,0,572,573,5,32,0,0,573,574,5,45,0,0,574,575,
        5,46,0,0,575,59,1,0,0,0,576,577,5,33,0,0,577,578,5,45,0,0,578,579,
        5,46,0,0,579,61,1,0,0,0,580,581,5,31,0,0,581,582,5,45,0,0,582,583,
        5,46,0,0,583,63,1,0,0,0,584,585,5,40,0,0,585,586,5,45,0,0,586,587,
        5,46,0,0,587,65,1,0,0,0,588,589,5,39,0,0,589,590,5,45,0,0,590,591,
        5,46,0,0,591,67,1,0,0,0,592,593,5,34,0,0,593,594,5,45,0,0,594,595,
        5,46,0,0,595,69,1,0,0,0,596,597,5,36,0,0,597,598,5,45,0,0,598,599,
        5,46,0,0,599,71,1,0,0,0,600,601,5,38,0,0,601,602,5,45,0,0,602,603,
        5,46,0,0,603,73,1,0,0,0,604,605,5,35,0,0,605,606,5,45,0,0,606,607,
        5,46,0,0,607,75,1,0,0,0,608,609,5,47,0,0,609,610,5,45,0,0,610,611,
        5,46,0,0,611,77,1,0,0,0,612,613,7,1,0,0,613,79,1,0,0,0,614,615,7,
        2,0,0,615,81,1,0,0,0,62,83,88,95,104,110,117,120,124,132,147,151,
        158,164,170,175,182,185,189,202,209,216,223,230,245,252,259,266,
        270,275,279,284,291,298,305,321,328,332,337,341,346,350,355,362,
        369,385,392,399,403,408,418,424,434,437,441,445,452,455,459,467,
        482,497,512
    ]

class XMLParser ( Parser ):

    grammarFileName = "XMLParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'<'", "<INVALID>", 
                     "<INVALID>", "'DAO-ML_diagram'", "'DAO'", "'Role'", 
                     "'Committee'", "'Permission'", "'GovernanceArea'", 
                     "'associated_to'", "'is_controlled_by'", "'aggregates'", 
                     "'federates_into'", "'DAO_ID'", "'DAO_name'", "'mission_statement'", 
                     "'hierarchical_inheritance'", "'role_ID'", "'role_name'", 
                     "'role_assignment_method'", "'committee_ID'", "'committee_description'", 
                     "'n_agent_min'", "'n_agent_max'", "'decision_making_method'", 
                     "'voting_condition'", "'proposal_condition'", "'permission_ID'", 
                     "'ref_gov_area'", "'allowed_action'", "'agent_type'", 
                     "'permission_type'", "'federation_level'", "'aggregation_level'", 
                     "'>'", "<INVALID>", "'/>'", "'/'", "'='" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "CDATA", "DTD", "EntityRef", 
                      "CharRef", "SEA_WS", "OPEN", "XMLDeclOpen", "TEXT", 
                      "DIAGRAM", "DAO", "ROLE", "COMMITTEE", "PERMISSION", 
                      "GOV", "ASSOCIATION", "CONTROL", "AGGREGATES", "FEDERATES", 
                      "DAOID", "DAONAME", "MISSIONSTATEMENT", "HIERARCHICALINHERITANCE", 
                      "ROLEID", "ROLENAME", "ROLEASSIGNMENTMETHOD", "COMMITTEEID", 
                      "COMMITTEEDESCRIPTION", "NAGENTMIN", "NAGENTMAX", 
                      "DMMETHOD", "VOTINGCONDITION", "PROPOSALCONDITION", 
                      "PERMISSIONID", "REF_GOV_AREA", "ALLOWEDACTION", "AGENTTYPE", 
                      "PERMISSIONTYPE", "FEDERATIONLEVEL", "AGGREGATIONLEVEL", 
                      "CLOSE", "SPECIAL_CLOSE", "SLASH_CLOSE", "SLASH", 
                      "EQUALS", "STRING", "Name", "S", "PI" ]

    RULE_document = 0
    RULE_prolog = 1
    RULE_content = 2
    RULE_element = 3
    RULE_diagram = 4
    RULE_dao = 5
    RULE_role = 6
    RULE_committee = 7
    RULE_permission = 8
    RULE_gov = 9
    RULE_daocontent = 10
    RULE_relations = 11
    RULE_associated_to = 12
    RULE_controlled_by = 13
    RULE_aggregates = 14
    RULE_federates_into = 15
    RULE_reference = 16
    RULE_dao_id = 17
    RULE_dao_name = 18
    RULE_mission_statement = 19
    RULE_hierarchical_inheritance = 20
    RULE_role_id = 21
    RULE_role_name = 22
    RULE_role_assignment_method = 23
    RULE_n_agent_min = 24
    RULE_n_agent_max = 25
    RULE_agent_type = 26
    RULE_committee_id = 27
    RULE_committee_description = 28
    RULE_voting_condition = 29
    RULE_proposal_condition = 30
    RULE_decision_making_method = 31
    RULE_aggregation_level = 32
    RULE_federation_level = 33
    RULE_permission_id = 34
    RULE_allowed_action = 35
    RULE_permission_type = 36
    RULE_ref_gov_area = 37
    RULE_attribute = 38
    RULE_chardata = 39
    RULE_misc = 40

    ruleNames =  [ "document", "prolog", "content", "element", "diagram", 
                   "dao", "role", "committee", "permission", "gov", "daocontent", 
                   "relations", "associated_to", "controlled_by", "aggregates", 
                   "federates_into", "reference", "dao_id", "dao_name", 
                   "mission_statement", "hierarchical_inheritance", "role_id", 
                   "role_name", "role_assignment_method", "n_agent_min", 
                   "n_agent_max", "agent_type", "committee_id", "committee_description", 
                   "voting_condition", "proposal_condition", "decision_making_method", 
                   "aggregation_level", "federation_level", "permission_id", 
                   "allowed_action", "permission_type", "ref_gov_area", 
                   "attribute", "chardata", "misc" ]

    EOF = Token.EOF
    COMMENT=1
    CDATA=2
    DTD=3
    EntityRef=4
    CharRef=5
    SEA_WS=6
    OPEN=7
    XMLDeclOpen=8
    TEXT=9
    DIAGRAM=10
    DAO=11
    ROLE=12
    COMMITTEE=13
    PERMISSION=14
    GOV=15
    ASSOCIATION=16
    CONTROL=17
    AGGREGATES=18
    FEDERATES=19
    DAOID=20
    DAONAME=21
    MISSIONSTATEMENT=22
    HIERARCHICALINHERITANCE=23
    ROLEID=24
    ROLENAME=25
    ROLEASSIGNMENTMETHOD=26
    COMMITTEEID=27
    COMMITTEEDESCRIPTION=28
    NAGENTMIN=29
    NAGENTMAX=30
    DMMETHOD=31
    VOTINGCONDITION=32
    PROPOSALCONDITION=33
    PERMISSIONID=34
    REF_GOV_AREA=35
    ALLOWEDACTION=36
    AGENTTYPE=37
    PERMISSIONTYPE=38
    FEDERATIONLEVEL=39
    AGGREGATIONLEVEL=40
    CLOSE=41
    SPECIAL_CLOSE=42
    SLASH_CLOSE=43
    SLASH=44
    EQUALS=45
    STRING=46
    Name=47
    S=48
    PI=49

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DocumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def diagram(self):
            return self.getTypedRuleContext(XMLParser.DiagramContext,0)


        def EOF(self):
            return self.getToken(XMLParser.EOF, 0)

        def prolog(self):
            return self.getTypedRuleContext(XMLParser.PrologContext,0)


        def misc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.MiscContext)
            else:
                return self.getTypedRuleContext(XMLParser.MiscContext,i)


        def getRuleIndex(self):
            return XMLParser.RULE_document

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDocument" ):
                return visitor.visitDocument(self)
            else:
                return visitor.visitChildren(self)




    def document(self):

        localctx = XMLParser.DocumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_document)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 82
                self.prolog()


            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562949953421378) != 0):
                self.state = 85
                self.misc()
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 91
            self.diagram()
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562949953421378) != 0):
                self.state = 92
                self.misc()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 98
            self.match(XMLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrologContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def XMLDeclOpen(self):
            return self.getToken(XMLParser.XMLDeclOpen, 0)

        def SPECIAL_CLOSE(self):
            return self.getToken(XMLParser.SPECIAL_CLOSE, 0)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(XMLParser.AttributeContext,i)


        def getRuleIndex(self):
            return XMLParser.RULE_prolog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProlog" ):
                return visitor.visitProlog(self)
            else:
                return visitor.visitChildren(self)




    def prolog(self):

        localctx = XMLParser.PrologContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_prolog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(XMLParser.XMLDeclOpen)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==47:
                self.state = 101
                self.attribute()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 107
            self.match(XMLParser.SPECIAL_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def chardata(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.ChardataContext)
            else:
                return self.getTypedRuleContext(XMLParser.ChardataContext,i)


        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.ElementContext)
            else:
                return self.getTypedRuleContext(XMLParser.ElementContext,i)


        def reference(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.ReferenceContext)
            else:
                return self.getTypedRuleContext(XMLParser.ReferenceContext,i)


        def CDATA(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.CDATA)
            else:
                return self.getToken(XMLParser.CDATA, i)

        def PI(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.PI)
            else:
                return self.getToken(XMLParser.PI, i)

        def COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.COMMENT)
            else:
                return self.getToken(XMLParser.COMMENT, i)

        def getRuleIndex(self):
            return XMLParser.RULE_content

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContent" ):
                return visitor.visitContent(self)
            else:
                return visitor.visitChildren(self)




    def content(self):

        localctx = XMLParser.ContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6 or _la==9:
                self.state = 109
                self.chardata()


            self.state = 124
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 117
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [7]:
                        self.state = 112
                        self.element()
                        pass
                    elif token in [4, 5]:
                        self.state = 113
                        self.reference()
                        pass
                    elif token in [2]:
                        self.state = 114
                        self.match(XMLParser.CDATA)
                        pass
                    elif token in [49]:
                        self.state = 115
                        self.match(XMLParser.PI)
                        pass
                    elif token in [1]:
                        self.state = 116
                        self.match(XMLParser.COMMENT)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 120
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==6 or _la==9:
                        self.state = 119
                        self.chardata()

             
                self.state = 126
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.OPEN)
            else:
                return self.getToken(XMLParser.OPEN, i)

        def Name(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.Name)
            else:
                return self.getToken(XMLParser.Name, i)

        def CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.CLOSE)
            else:
                return self.getToken(XMLParser.CLOSE, i)

        def content(self):
            return self.getTypedRuleContext(XMLParser.ContentContext,0)


        def SLASH(self):
            return self.getToken(XMLParser.SLASH, 0)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(XMLParser.AttributeContext,i)


        def SLASH_CLOSE(self):
            return self.getToken(XMLParser.SLASH_CLOSE, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = XMLParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_element)
        self._la = 0 # Token type
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.match(XMLParser.OPEN)
                self.state = 128
                self.match(XMLParser.Name)
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==47:
                    self.state = 129
                    self.attribute()
                    self.state = 134
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 135
                self.match(XMLParser.CLOSE)
                self.state = 136
                self.content()
                self.state = 137
                self.match(XMLParser.OPEN)
                self.state = 138
                self.match(XMLParser.SLASH)
                self.state = 139
                self.match(XMLParser.Name)
                self.state = 140
                self.match(XMLParser.CLOSE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.match(XMLParser.OPEN)
                self.state = 143
                self.match(XMLParser.Name)
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==47:
                    self.state = 144
                    self.attribute()
                    self.state = 149
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 150
                self.match(XMLParser.SLASH_CLOSE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DiagramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.OPEN)
            else:
                return self.getToken(XMLParser.OPEN, i)

        def DIAGRAM(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.DIAGRAM)
            else:
                return self.getToken(XMLParser.DIAGRAM, i)

        def CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.CLOSE)
            else:
                return self.getToken(XMLParser.CLOSE, i)

        def SLASH(self):
            return self.getToken(XMLParser.SLASH, 0)

        def misc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.MiscContext)
            else:
                return self.getTypedRuleContext(XMLParser.MiscContext,i)


        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(XMLParser.AttributeContext,i)


        def chardata(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.ChardataContext)
            else:
                return self.getTypedRuleContext(XMLParser.ChardataContext,i)


        def dao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.DaoContext)
            else:
                return self.getTypedRuleContext(XMLParser.DaoContext,i)


        def reference(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.ReferenceContext)
            else:
                return self.getTypedRuleContext(XMLParser.ReferenceContext,i)


        def CDATA(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.CDATA)
            else:
                return self.getToken(XMLParser.CDATA, i)

        def PI(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.PI)
            else:
                return self.getToken(XMLParser.PI, i)

        def COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.COMMENT)
            else:
                return self.getToken(XMLParser.COMMENT, i)

        def getRuleIndex(self):
            return XMLParser.RULE_diagram

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiagram" ):
                return visitor.visitDiagram(self)
            else:
                return visitor.visitChildren(self)




    def diagram(self):

        localctx = XMLParser.DiagramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_diagram)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(XMLParser.OPEN)
            self.state = 154
            self.match(XMLParser.DIAGRAM)
            self.state = 158
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 155
                    self.misc() 
                self.state = 160
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==47:
                self.state = 161
                self.attribute()
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562949953421378) != 0):
                self.state = 167
                self.misc()
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 173
            self.match(XMLParser.CLOSE)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6 or _la==9:
                self.state = 174
                self.chardata()


            self.state = 189
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 182
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [7]:
                        self.state = 177
                        self.dao()
                        pass
                    elif token in [4, 5]:
                        self.state = 178
                        self.reference()
                        pass
                    elif token in [2]:
                        self.state = 179
                        self.match(XMLParser.CDATA)
                        pass
                    elif token in [49]:
                        self.state = 180
                        self.match(XMLParser.PI)
                        pass
                    elif token in [1]:
                        self.state = 181
                        self.match(XMLParser.COMMENT)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 185
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==6 or _la==9:
                        self.state = 184
                        self.chardata()

             
                self.state = 191
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

            self.state = 192
            self.match(XMLParser.OPEN)
            self.state = 193
            self.match(XMLParser.SLASH)
            self.state = 194
            self.match(XMLParser.DIAGRAM)
            self.state = 195
            self.match(XMLParser.CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.OPEN)
            else:
                return self.getToken(XMLParser.OPEN, i)

        def DAO(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.DAO)
            else:
                return self.getToken(XMLParser.DAO, i)

        def dao_id(self):
            return self.getTypedRuleContext(XMLParser.Dao_idContext,0)


        def dao_name(self):
            return self.getTypedRuleContext(XMLParser.Dao_nameContext,0)


        def mission_statement(self):
            return self.getTypedRuleContext(XMLParser.Mission_statementContext,0)


        def hierarchical_inheritance(self):
            return self.getTypedRuleContext(XMLParser.Hierarchical_inheritanceContext,0)


        def CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.CLOSE)
            else:
                return self.getToken(XMLParser.CLOSE, i)

        def daocontent(self):
            return self.getTypedRuleContext(XMLParser.DaocontentContext,0)


        def SLASH(self):
            return self.getToken(XMLParser.SLASH, 0)

        def misc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.MiscContext)
            else:
                return self.getTypedRuleContext(XMLParser.MiscContext,i)


        def getRuleIndex(self):
            return XMLParser.RULE_dao

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDao" ):
                return visitor.visitDao(self)
            else:
                return visitor.visitChildren(self)




    def dao(self):

        localctx = XMLParser.DaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_dao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(XMLParser.OPEN)
            self.state = 198
            self.match(XMLParser.DAO)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562949953421378) != 0):
                self.state = 199
                self.misc()
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 205
            self.dao_id()
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562949953421378) != 0):
                self.state = 206
                self.misc()
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 212
            self.dao_name()
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562949953421378) != 0):
                self.state = 213
                self.misc()
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 219
            self.mission_statement()
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562949953421378) != 0):
                self.state = 220
                self.misc()
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 226
            self.hierarchical_inheritance()
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562949953421378) != 0):
                self.state = 227
                self.misc()
                self.state = 232
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 233
            self.match(XMLParser.CLOSE)
            self.state = 234
            self.daocontent()
            self.state = 235
            self.match(XMLParser.OPEN)
            self.state = 236
            self.match(XMLParser.SLASH)
            self.state = 237
            self.match(XMLParser.DAO)
            self.state = 238
            self.match(XMLParser.CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RoleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.OPEN)
            else:
                return self.getToken(XMLParser.OPEN, i)

        def ROLE(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.ROLE)
            else:
                return self.getToken(XMLParser.ROLE, i)

        def role_id(self):
            return self.getTypedRuleContext(XMLParser.Role_idContext,0)


        def role_name(self):
            return self.getTypedRuleContext(XMLParser.Role_nameContext,0)


        def role_assignment_method(self):
            return self.getTypedRuleContext(XMLParser.Role_assignment_methodContext,0)


        def agent_type(self):
            return self.getTypedRuleContext(XMLParser.Agent_typeContext,0)


        def aggregation_level(self):
            return self.getTypedRuleContext(XMLParser.Aggregation_levelContext,0)


        def federation_level(self):
            return self.getTypedRuleContext(XMLParser.Federation_levelContext,0)


        def CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.CLOSE)
            else:
                return self.getToken(XMLParser.CLOSE, i)

        def relations(self):
            return self.getTypedRuleContext(XMLParser.RelationsContext,0)


        def SLASH(self):
            return self.getToken(XMLParser.SLASH, 0)

        def misc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.MiscContext)
            else:
                return self.getTypedRuleContext(XMLParser.MiscContext,i)


        def n_agent_min(self):
            return self.getTypedRuleContext(XMLParser.N_agent_minContext,0)


        def n_agent_max(self):
            return self.getTypedRuleContext(XMLParser.N_agent_maxContext,0)


        def getRuleIndex(self):
            return XMLParser.RULE_role

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRole" ):
                return visitor.visitRole(self)
            else:
                return visitor.visitChildren(self)




    def role(self):

        localctx = XMLParser.RoleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_role)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(XMLParser.OPEN)
            self.state = 241
            self.match(XMLParser.ROLE)
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562949953421378) != 0):
                self.state = 242
                self.misc()
                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 248
            self.role_id()
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562949953421378) != 0):
                self.state = 249
                self.misc()
                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 255
            self.role_name()
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562949953421378) != 0):
                self.state = 256
                self.misc()
                self.state = 261
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 262
            self.role_assignment_method()
            self.state = 266
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 263
                    self.misc() 
                self.state = 268
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 269
                self.n_agent_min()


            self.state = 275
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 272
                    self.misc() 
                self.state = 277
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 278
                self.n_agent_max()


            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562949953421378) != 0):
                self.state = 281
                self.misc()
                self.state = 286
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 287
            self.agent_type()
            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562949953421378) != 0):
                self.state = 288
                self.misc()
                self.state = 293
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 294
            self.aggregation_level()
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562949953421378) != 0):
                self.state = 295
                self.misc()
                self.state = 300
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 301
            self.federation_level()
            self.state = 305
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562949953421378) != 0):
                self.state = 302
                self.misc()
                self.state = 307
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 308
            self.match(XMLParser.CLOSE)
            self.state = 309
            self.relations()
            self.state = 310
            self.match(XMLParser.OPEN)
            self.state = 311
            self.match(XMLParser.SLASH)
            self.state = 312
            self.match(XMLParser.ROLE)
            self.state = 313
            self.match(XMLParser.CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommitteeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.OPEN)
            else:
                return self.getToken(XMLParser.OPEN, i)

        def COMMITTEE(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.COMMITTEE)
            else:
                return self.getToken(XMLParser.COMMITTEE, i)

        def committee_id(self):
            return self.getTypedRuleContext(XMLParser.Committee_idContext,0)


        def committee_description(self):
            return self.getTypedRuleContext(XMLParser.Committee_descriptionContext,0)


        def aggregation_level(self):
            return self.getTypedRuleContext(XMLParser.Aggregation_levelContext,0)


        def federation_level(self):
            return self.getTypedRuleContext(XMLParser.Federation_levelContext,0)


        def CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.CLOSE)
            else:
                return self.getToken(XMLParser.CLOSE, i)

        def relations(self):
            return self.getTypedRuleContext(XMLParser.RelationsContext,0)


        def SLASH(self):
            return self.getToken(XMLParser.SLASH, 0)

        def misc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.MiscContext)
            else:
                return self.getTypedRuleContext(XMLParser.MiscContext,i)


        def voting_condition(self):
            return self.getTypedRuleContext(XMLParser.Voting_conditionContext,0)


        def proposal_condition(self):
            return self.getTypedRuleContext(XMLParser.Proposal_conditionContext,0)


        def decision_making_method(self):
            return self.getTypedRuleContext(XMLParser.Decision_making_methodContext,0)


        def getRuleIndex(self):
            return XMLParser.RULE_committee

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommittee" ):
                return visitor.visitCommittee(self)
            else:
                return visitor.visitChildren(self)




    def committee(self):

        localctx = XMLParser.CommitteeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_committee)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(XMLParser.OPEN)
            self.state = 316
            self.match(XMLParser.COMMITTEE)
            self.state = 317
            self.committee_id()
            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562949953421378) != 0):
                self.state = 318
                self.misc()
                self.state = 323
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 324
            self.committee_description()
            self.state = 328
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 325
                    self.misc() 
                self.state = 330
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 331
                self.voting_condition()


            self.state = 337
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 334
                    self.misc() 
                self.state = 339
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 340
                self.proposal_condition()


            self.state = 346
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 343
                    self.misc() 
                self.state = 348
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

            self.state = 350
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 349
                self.decision_making_method()


            self.state = 355
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562949953421378) != 0):
                self.state = 352
                self.misc()
                self.state = 357
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 358
            self.aggregation_level()
            self.state = 362
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562949953421378) != 0):
                self.state = 359
                self.misc()
                self.state = 364
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 365
            self.federation_level()
            self.state = 369
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562949953421378) != 0):
                self.state = 366
                self.misc()
                self.state = 371
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 372
            self.match(XMLParser.CLOSE)
            self.state = 373
            self.relations()
            self.state = 374
            self.match(XMLParser.OPEN)
            self.state = 375
            self.match(XMLParser.SLASH)
            self.state = 376
            self.match(XMLParser.COMMITTEE)
            self.state = 377
            self.match(XMLParser.CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PermissionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self):
            return self.getToken(XMLParser.OPEN, 0)

        def PERMISSION(self):
            return self.getToken(XMLParser.PERMISSION, 0)

        def permission_id(self):
            return self.getTypedRuleContext(XMLParser.Permission_idContext,0)


        def allowed_action(self):
            return self.getTypedRuleContext(XMLParser.Allowed_actionContext,0)


        def permission_type(self):
            return self.getTypedRuleContext(XMLParser.Permission_typeContext,0)


        def SLASH_CLOSE(self):
            return self.getToken(XMLParser.SLASH_CLOSE, 0)

        def misc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.MiscContext)
            else:
                return self.getTypedRuleContext(XMLParser.MiscContext,i)


        def ref_gov_area(self):
            return self.getTypedRuleContext(XMLParser.Ref_gov_areaContext,0)


        def getRuleIndex(self):
            return XMLParser.RULE_permission

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPermission" ):
                return visitor.visitPermission(self)
            else:
                return visitor.visitChildren(self)




    def permission(self):

        localctx = XMLParser.PermissionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_permission)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(XMLParser.OPEN)
            self.state = 380
            self.match(XMLParser.PERMISSION)
            self.state = 381
            self.permission_id()
            self.state = 385
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562949953421378) != 0):
                self.state = 382
                self.misc()
                self.state = 387
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 388
            self.allowed_action()
            self.state = 392
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562949953421378) != 0):
                self.state = 389
                self.misc()
                self.state = 394
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 395
            self.permission_type()
            self.state = 399
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 396
                    self.misc() 
                self.state = 401
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

            self.state = 403
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 402
                self.ref_gov_area()


            self.state = 408
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562949953421378) != 0):
                self.state = 405
                self.misc()
                self.state = 410
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 411
            self.match(XMLParser.SLASH_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GovContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self):
            return self.getToken(XMLParser.OPEN, 0)

        def GOV(self):
            return self.getToken(XMLParser.GOV, 0)

        def SLASH_CLOSE(self):
            return self.getToken(XMLParser.SLASH_CLOSE, 0)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(XMLParser.AttributeContext,i)


        def getRuleIndex(self):
            return XMLParser.RULE_gov

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGov" ):
                return visitor.visitGov(self)
            else:
                return visitor.visitChildren(self)




    def gov(self):

        localctx = XMLParser.GovContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_gov)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.match(XMLParser.OPEN)
            self.state = 414
            self.match(XMLParser.GOV)
            self.state = 418
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==47:
                self.state = 415
                self.attribute()
                self.state = 420
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 421
            self.match(XMLParser.SLASH_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DaocontentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def chardata(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.ChardataContext)
            else:
                return self.getTypedRuleContext(XMLParser.ChardataContext,i)


        def role(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.RoleContext)
            else:
                return self.getTypedRuleContext(XMLParser.RoleContext,i)


        def committee(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.CommitteeContext)
            else:
                return self.getTypedRuleContext(XMLParser.CommitteeContext,i)


        def permission(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.PermissionContext)
            else:
                return self.getTypedRuleContext(XMLParser.PermissionContext,i)


        def gov(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.GovContext)
            else:
                return self.getTypedRuleContext(XMLParser.GovContext,i)


        def reference(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.ReferenceContext)
            else:
                return self.getTypedRuleContext(XMLParser.ReferenceContext,i)


        def CDATA(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.CDATA)
            else:
                return self.getToken(XMLParser.CDATA, i)

        def PI(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.PI)
            else:
                return self.getToken(XMLParser.PI, i)

        def COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.COMMENT)
            else:
                return self.getToken(XMLParser.COMMENT, i)

        def getRuleIndex(self):
            return XMLParser.RULE_daocontent

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDaocontent" ):
                return visitor.visitDaocontent(self)
            else:
                return visitor.visitChildren(self)




    def daocontent(self):

        localctx = XMLParser.DaocontentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_daocontent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6 or _la==9:
                self.state = 423
                self.chardata()


            self.state = 441
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,53,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 434
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                    if la_ == 1:
                        self.state = 426
                        self.role()
                        pass

                    elif la_ == 2:
                        self.state = 427
                        self.committee()
                        pass

                    elif la_ == 3:
                        self.state = 428
                        self.permission()
                        pass

                    elif la_ == 4:
                        self.state = 429
                        self.gov()
                        pass

                    elif la_ == 5:
                        self.state = 430
                        self.reference()
                        pass

                    elif la_ == 6:
                        self.state = 431
                        self.match(XMLParser.CDATA)
                        pass

                    elif la_ == 7:
                        self.state = 432
                        self.match(XMLParser.PI)
                        pass

                    elif la_ == 8:
                        self.state = 433
                        self.match(XMLParser.COMMENT)
                        pass


                    self.state = 437
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==6 or _la==9:
                        self.state = 436
                        self.chardata()

             
                self.state = 443
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,53,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def chardata(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.ChardataContext)
            else:
                return self.getTypedRuleContext(XMLParser.ChardataContext,i)


        def associated_to(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Associated_toContext)
            else:
                return self.getTypedRuleContext(XMLParser.Associated_toContext,i)


        def controlled_by(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Controlled_byContext)
            else:
                return self.getTypedRuleContext(XMLParser.Controlled_byContext,i)


        def aggregates(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.AggregatesContext)
            else:
                return self.getTypedRuleContext(XMLParser.AggregatesContext,i)


        def federates_into(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Federates_intoContext)
            else:
                return self.getTypedRuleContext(XMLParser.Federates_intoContext,i)


        def COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.COMMENT)
            else:
                return self.getToken(XMLParser.COMMENT, i)

        def getRuleIndex(self):
            return XMLParser.RULE_relations

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelations" ):
                return visitor.visitRelations(self)
            else:
                return visitor.visitChildren(self)




    def relations(self):

        localctx = XMLParser.RelationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_relations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6 or _la==9:
                self.state = 444
                self.chardata()


            self.state = 459
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,57,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 452
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
                    if la_ == 1:
                        self.state = 447
                        self.associated_to()
                        pass

                    elif la_ == 2:
                        self.state = 448
                        self.controlled_by()
                        pass

                    elif la_ == 3:
                        self.state = 449
                        self.aggregates()
                        pass

                    elif la_ == 4:
                        self.state = 450
                        self.federates_into()
                        pass

                    elif la_ == 5:
                        self.state = 451
                        self.match(XMLParser.COMMENT)
                        pass


                    self.state = 455
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==6 or _la==9:
                        self.state = 454
                        self.chardata()

             
                self.state = 461
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,57,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Associated_toContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.OPEN)
            else:
                return self.getToken(XMLParser.OPEN, i)

        def ASSOCIATION(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.ASSOCIATION)
            else:
                return self.getToken(XMLParser.ASSOCIATION, i)

        def CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.CLOSE)
            else:
                return self.getToken(XMLParser.CLOSE, i)

        def content(self):
            return self.getTypedRuleContext(XMLParser.ContentContext,0)


        def SLASH(self):
            return self.getToken(XMLParser.SLASH, 0)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(XMLParser.AttributeContext,i)


        def getRuleIndex(self):
            return XMLParser.RULE_associated_to

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssociated_to" ):
                return visitor.visitAssociated_to(self)
            else:
                return visitor.visitChildren(self)




    def associated_to(self):

        localctx = XMLParser.Associated_toContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_associated_to)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.match(XMLParser.OPEN)
            self.state = 463
            self.match(XMLParser.ASSOCIATION)
            self.state = 467
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==47:
                self.state = 464
                self.attribute()
                self.state = 469
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 470
            self.match(XMLParser.CLOSE)
            self.state = 471
            self.content()
            self.state = 472
            self.match(XMLParser.OPEN)
            self.state = 473
            self.match(XMLParser.SLASH)
            self.state = 474
            self.match(XMLParser.ASSOCIATION)
            self.state = 475
            self.match(XMLParser.CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Controlled_byContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.OPEN)
            else:
                return self.getToken(XMLParser.OPEN, i)

        def CONTROL(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.CONTROL)
            else:
                return self.getToken(XMLParser.CONTROL, i)

        def CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.CLOSE)
            else:
                return self.getToken(XMLParser.CLOSE, i)

        def content(self):
            return self.getTypedRuleContext(XMLParser.ContentContext,0)


        def SLASH(self):
            return self.getToken(XMLParser.SLASH, 0)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(XMLParser.AttributeContext,i)


        def getRuleIndex(self):
            return XMLParser.RULE_controlled_by

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitControlled_by" ):
                return visitor.visitControlled_by(self)
            else:
                return visitor.visitChildren(self)




    def controlled_by(self):

        localctx = XMLParser.Controlled_byContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_controlled_by)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self.match(XMLParser.OPEN)
            self.state = 478
            self.match(XMLParser.CONTROL)
            self.state = 482
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==47:
                self.state = 479
                self.attribute()
                self.state = 484
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 485
            self.match(XMLParser.CLOSE)
            self.state = 486
            self.content()
            self.state = 487
            self.match(XMLParser.OPEN)
            self.state = 488
            self.match(XMLParser.SLASH)
            self.state = 489
            self.match(XMLParser.CONTROL)
            self.state = 490
            self.match(XMLParser.CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggregatesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.OPEN)
            else:
                return self.getToken(XMLParser.OPEN, i)

        def AGGREGATES(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.AGGREGATES)
            else:
                return self.getToken(XMLParser.AGGREGATES, i)

        def CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.CLOSE)
            else:
                return self.getToken(XMLParser.CLOSE, i)

        def content(self):
            return self.getTypedRuleContext(XMLParser.ContentContext,0)


        def SLASH(self):
            return self.getToken(XMLParser.SLASH, 0)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(XMLParser.AttributeContext,i)


        def getRuleIndex(self):
            return XMLParser.RULE_aggregates

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregates" ):
                return visitor.visitAggregates(self)
            else:
                return visitor.visitChildren(self)




    def aggregates(self):

        localctx = XMLParser.AggregatesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_aggregates)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            self.match(XMLParser.OPEN)
            self.state = 493
            self.match(XMLParser.AGGREGATES)
            self.state = 497
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==47:
                self.state = 494
                self.attribute()
                self.state = 499
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 500
            self.match(XMLParser.CLOSE)
            self.state = 501
            self.content()
            self.state = 502
            self.match(XMLParser.OPEN)
            self.state = 503
            self.match(XMLParser.SLASH)
            self.state = 504
            self.match(XMLParser.AGGREGATES)
            self.state = 505
            self.match(XMLParser.CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Federates_intoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.OPEN)
            else:
                return self.getToken(XMLParser.OPEN, i)

        def FEDERATES(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.FEDERATES)
            else:
                return self.getToken(XMLParser.FEDERATES, i)

        def CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.CLOSE)
            else:
                return self.getToken(XMLParser.CLOSE, i)

        def content(self):
            return self.getTypedRuleContext(XMLParser.ContentContext,0)


        def SLASH(self):
            return self.getToken(XMLParser.SLASH, 0)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(XMLParser.AttributeContext,i)


        def getRuleIndex(self):
            return XMLParser.RULE_federates_into

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFederates_into" ):
                return visitor.visitFederates_into(self)
            else:
                return visitor.visitChildren(self)




    def federates_into(self):

        localctx = XMLParser.Federates_intoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_federates_into)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.match(XMLParser.OPEN)
            self.state = 508
            self.match(XMLParser.FEDERATES)
            self.state = 512
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==47:
                self.state = 509
                self.attribute()
                self.state = 514
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 515
            self.match(XMLParser.CLOSE)
            self.state = 516
            self.content()
            self.state = 517
            self.match(XMLParser.OPEN)
            self.state = 518
            self.match(XMLParser.SLASH)
            self.state = 519
            self.match(XMLParser.FEDERATES)
            self.state = 520
            self.match(XMLParser.CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReferenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EntityRef(self):
            return self.getToken(XMLParser.EntityRef, 0)

        def CharRef(self):
            return self.getToken(XMLParser.CharRef, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_reference

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReference" ):
                return visitor.visitReference(self)
            else:
                return visitor.visitChildren(self)




    def reference(self):

        localctx = XMLParser.ReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_reference)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dao_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DAOID(self):
            return self.getToken(XMLParser.DAOID, 0)

        def EQUALS(self):
            return self.getToken(XMLParser.EQUALS, 0)

        def STRING(self):
            return self.getToken(XMLParser.STRING, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_dao_id

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDao_id" ):
                return visitor.visitDao_id(self)
            else:
                return visitor.visitChildren(self)




    def dao_id(self):

        localctx = XMLParser.Dao_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_dao_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
            self.match(XMLParser.DAOID)
            self.state = 525
            self.match(XMLParser.EQUALS)
            self.state = 526
            self.match(XMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dao_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DAONAME(self):
            return self.getToken(XMLParser.DAONAME, 0)

        def EQUALS(self):
            return self.getToken(XMLParser.EQUALS, 0)

        def STRING(self):
            return self.getToken(XMLParser.STRING, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_dao_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDao_name" ):
                return visitor.visitDao_name(self)
            else:
                return visitor.visitChildren(self)




    def dao_name(self):

        localctx = XMLParser.Dao_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_dao_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 528
            self.match(XMLParser.DAONAME)
            self.state = 529
            self.match(XMLParser.EQUALS)
            self.state = 530
            self.match(XMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mission_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MISSIONSTATEMENT(self):
            return self.getToken(XMLParser.MISSIONSTATEMENT, 0)

        def EQUALS(self):
            return self.getToken(XMLParser.EQUALS, 0)

        def STRING(self):
            return self.getToken(XMLParser.STRING, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_mission_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMission_statement" ):
                return visitor.visitMission_statement(self)
            else:
                return visitor.visitChildren(self)




    def mission_statement(self):

        localctx = XMLParser.Mission_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_mission_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
            self.match(XMLParser.MISSIONSTATEMENT)
            self.state = 533
            self.match(XMLParser.EQUALS)
            self.state = 534
            self.match(XMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Hierarchical_inheritanceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HIERARCHICALINHERITANCE(self):
            return self.getToken(XMLParser.HIERARCHICALINHERITANCE, 0)

        def EQUALS(self):
            return self.getToken(XMLParser.EQUALS, 0)

        def STRING(self):
            return self.getToken(XMLParser.STRING, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_hierarchical_inheritance

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHierarchical_inheritance" ):
                return visitor.visitHierarchical_inheritance(self)
            else:
                return visitor.visitChildren(self)




    def hierarchical_inheritance(self):

        localctx = XMLParser.Hierarchical_inheritanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_hierarchical_inheritance)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self.match(XMLParser.HIERARCHICALINHERITANCE)
            self.state = 537
            self.match(XMLParser.EQUALS)
            self.state = 538
            self.match(XMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Role_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ROLEID(self):
            return self.getToken(XMLParser.ROLEID, 0)

        def EQUALS(self):
            return self.getToken(XMLParser.EQUALS, 0)

        def STRING(self):
            return self.getToken(XMLParser.STRING, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_role_id

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRole_id" ):
                return visitor.visitRole_id(self)
            else:
                return visitor.visitChildren(self)




    def role_id(self):

        localctx = XMLParser.Role_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_role_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 540
            self.match(XMLParser.ROLEID)
            self.state = 541
            self.match(XMLParser.EQUALS)
            self.state = 542
            self.match(XMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Role_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ROLENAME(self):
            return self.getToken(XMLParser.ROLENAME, 0)

        def EQUALS(self):
            return self.getToken(XMLParser.EQUALS, 0)

        def STRING(self):
            return self.getToken(XMLParser.STRING, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_role_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRole_name" ):
                return visitor.visitRole_name(self)
            else:
                return visitor.visitChildren(self)




    def role_name(self):

        localctx = XMLParser.Role_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_role_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
            self.match(XMLParser.ROLENAME)
            self.state = 545
            self.match(XMLParser.EQUALS)
            self.state = 546
            self.match(XMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Role_assignment_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ROLEASSIGNMENTMETHOD(self):
            return self.getToken(XMLParser.ROLEASSIGNMENTMETHOD, 0)

        def EQUALS(self):
            return self.getToken(XMLParser.EQUALS, 0)

        def STRING(self):
            return self.getToken(XMLParser.STRING, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_role_assignment_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRole_assignment_method" ):
                return visitor.visitRole_assignment_method(self)
            else:
                return visitor.visitChildren(self)




    def role_assignment_method(self):

        localctx = XMLParser.Role_assignment_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_role_assignment_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 548
            self.match(XMLParser.ROLEASSIGNMENTMETHOD)
            self.state = 549
            self.match(XMLParser.EQUALS)
            self.state = 550
            self.match(XMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class N_agent_minContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAGENTMIN(self):
            return self.getToken(XMLParser.NAGENTMIN, 0)

        def EQUALS(self):
            return self.getToken(XMLParser.EQUALS, 0)

        def STRING(self):
            return self.getToken(XMLParser.STRING, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_n_agent_min

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitN_agent_min" ):
                return visitor.visitN_agent_min(self)
            else:
                return visitor.visitChildren(self)




    def n_agent_min(self):

        localctx = XMLParser.N_agent_minContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_n_agent_min)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 552
            self.match(XMLParser.NAGENTMIN)
            self.state = 553
            self.match(XMLParser.EQUALS)
            self.state = 554
            self.match(XMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class N_agent_maxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAGENTMAX(self):
            return self.getToken(XMLParser.NAGENTMAX, 0)

        def EQUALS(self):
            return self.getToken(XMLParser.EQUALS, 0)

        def STRING(self):
            return self.getToken(XMLParser.STRING, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_n_agent_max

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitN_agent_max" ):
                return visitor.visitN_agent_max(self)
            else:
                return visitor.visitChildren(self)




    def n_agent_max(self):

        localctx = XMLParser.N_agent_maxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_n_agent_max)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 556
            self.match(XMLParser.NAGENTMAX)
            self.state = 557
            self.match(XMLParser.EQUALS)
            self.state = 558
            self.match(XMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Agent_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AGENTTYPE(self):
            return self.getToken(XMLParser.AGENTTYPE, 0)

        def EQUALS(self):
            return self.getToken(XMLParser.EQUALS, 0)

        def STRING(self):
            return self.getToken(XMLParser.STRING, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_agent_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgent_type" ):
                return visitor.visitAgent_type(self)
            else:
                return visitor.visitChildren(self)




    def agent_type(self):

        localctx = XMLParser.Agent_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_agent_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 560
            self.match(XMLParser.AGENTTYPE)
            self.state = 561
            self.match(XMLParser.EQUALS)
            self.state = 562
            self.match(XMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Committee_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMITTEEID(self):
            return self.getToken(XMLParser.COMMITTEEID, 0)

        def EQUALS(self):
            return self.getToken(XMLParser.EQUALS, 0)

        def STRING(self):
            return self.getToken(XMLParser.STRING, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_committee_id

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommittee_id" ):
                return visitor.visitCommittee_id(self)
            else:
                return visitor.visitChildren(self)




    def committee_id(self):

        localctx = XMLParser.Committee_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_committee_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 564
            self.match(XMLParser.COMMITTEEID)
            self.state = 565
            self.match(XMLParser.EQUALS)
            self.state = 566
            self.match(XMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Committee_descriptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMITTEEDESCRIPTION(self):
            return self.getToken(XMLParser.COMMITTEEDESCRIPTION, 0)

        def EQUALS(self):
            return self.getToken(XMLParser.EQUALS, 0)

        def STRING(self):
            return self.getToken(XMLParser.STRING, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_committee_description

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommittee_description" ):
                return visitor.visitCommittee_description(self)
            else:
                return visitor.visitChildren(self)




    def committee_description(self):

        localctx = XMLParser.Committee_descriptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_committee_description)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568
            self.match(XMLParser.COMMITTEEDESCRIPTION)
            self.state = 569
            self.match(XMLParser.EQUALS)
            self.state = 570
            self.match(XMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Voting_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOTINGCONDITION(self):
            return self.getToken(XMLParser.VOTINGCONDITION, 0)

        def EQUALS(self):
            return self.getToken(XMLParser.EQUALS, 0)

        def STRING(self):
            return self.getToken(XMLParser.STRING, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_voting_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVoting_condition" ):
                return visitor.visitVoting_condition(self)
            else:
                return visitor.visitChildren(self)




    def voting_condition(self):

        localctx = XMLParser.Voting_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_voting_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 572
            self.match(XMLParser.VOTINGCONDITION)
            self.state = 573
            self.match(XMLParser.EQUALS)
            self.state = 574
            self.match(XMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Proposal_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROPOSALCONDITION(self):
            return self.getToken(XMLParser.PROPOSALCONDITION, 0)

        def EQUALS(self):
            return self.getToken(XMLParser.EQUALS, 0)

        def STRING(self):
            return self.getToken(XMLParser.STRING, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_proposal_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProposal_condition" ):
                return visitor.visitProposal_condition(self)
            else:
                return visitor.visitChildren(self)




    def proposal_condition(self):

        localctx = XMLParser.Proposal_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_proposal_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
            self.match(XMLParser.PROPOSALCONDITION)
            self.state = 577
            self.match(XMLParser.EQUALS)
            self.state = 578
            self.match(XMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decision_making_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DMMETHOD(self):
            return self.getToken(XMLParser.DMMETHOD, 0)

        def EQUALS(self):
            return self.getToken(XMLParser.EQUALS, 0)

        def STRING(self):
            return self.getToken(XMLParser.STRING, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_decision_making_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecision_making_method" ):
                return visitor.visitDecision_making_method(self)
            else:
                return visitor.visitChildren(self)




    def decision_making_method(self):

        localctx = XMLParser.Decision_making_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_decision_making_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 580
            self.match(XMLParser.DMMETHOD)
            self.state = 581
            self.match(XMLParser.EQUALS)
            self.state = 582
            self.match(XMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Aggregation_levelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AGGREGATIONLEVEL(self):
            return self.getToken(XMLParser.AGGREGATIONLEVEL, 0)

        def EQUALS(self):
            return self.getToken(XMLParser.EQUALS, 0)

        def STRING(self):
            return self.getToken(XMLParser.STRING, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_aggregation_level

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregation_level" ):
                return visitor.visitAggregation_level(self)
            else:
                return visitor.visitChildren(self)




    def aggregation_level(self):

        localctx = XMLParser.Aggregation_levelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_aggregation_level)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 584
            self.match(XMLParser.AGGREGATIONLEVEL)
            self.state = 585
            self.match(XMLParser.EQUALS)
            self.state = 586
            self.match(XMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Federation_levelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FEDERATIONLEVEL(self):
            return self.getToken(XMLParser.FEDERATIONLEVEL, 0)

        def EQUALS(self):
            return self.getToken(XMLParser.EQUALS, 0)

        def STRING(self):
            return self.getToken(XMLParser.STRING, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_federation_level

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFederation_level" ):
                return visitor.visitFederation_level(self)
            else:
                return visitor.visitChildren(self)




    def federation_level(self):

        localctx = XMLParser.Federation_levelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_federation_level)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 588
            self.match(XMLParser.FEDERATIONLEVEL)
            self.state = 589
            self.match(XMLParser.EQUALS)
            self.state = 590
            self.match(XMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Permission_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PERMISSIONID(self):
            return self.getToken(XMLParser.PERMISSIONID, 0)

        def EQUALS(self):
            return self.getToken(XMLParser.EQUALS, 0)

        def STRING(self):
            return self.getToken(XMLParser.STRING, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_permission_id

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPermission_id" ):
                return visitor.visitPermission_id(self)
            else:
                return visitor.visitChildren(self)




    def permission_id(self):

        localctx = XMLParser.Permission_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_permission_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592
            self.match(XMLParser.PERMISSIONID)
            self.state = 593
            self.match(XMLParser.EQUALS)
            self.state = 594
            self.match(XMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Allowed_actionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ALLOWEDACTION(self):
            return self.getToken(XMLParser.ALLOWEDACTION, 0)

        def EQUALS(self):
            return self.getToken(XMLParser.EQUALS, 0)

        def STRING(self):
            return self.getToken(XMLParser.STRING, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_allowed_action

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAllowed_action" ):
                return visitor.visitAllowed_action(self)
            else:
                return visitor.visitChildren(self)




    def allowed_action(self):

        localctx = XMLParser.Allowed_actionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_allowed_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 596
            self.match(XMLParser.ALLOWEDACTION)
            self.state = 597
            self.match(XMLParser.EQUALS)
            self.state = 598
            self.match(XMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Permission_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PERMISSIONTYPE(self):
            return self.getToken(XMLParser.PERMISSIONTYPE, 0)

        def EQUALS(self):
            return self.getToken(XMLParser.EQUALS, 0)

        def STRING(self):
            return self.getToken(XMLParser.STRING, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_permission_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPermission_type" ):
                return visitor.visitPermission_type(self)
            else:
                return visitor.visitChildren(self)




    def permission_type(self):

        localctx = XMLParser.Permission_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_permission_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 600
            self.match(XMLParser.PERMISSIONTYPE)
            self.state = 601
            self.match(XMLParser.EQUALS)
            self.state = 602
            self.match(XMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ref_gov_areaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REF_GOV_AREA(self):
            return self.getToken(XMLParser.REF_GOV_AREA, 0)

        def EQUALS(self):
            return self.getToken(XMLParser.EQUALS, 0)

        def STRING(self):
            return self.getToken(XMLParser.STRING, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_ref_gov_area

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRef_gov_area" ):
                return visitor.visitRef_gov_area(self)
            else:
                return visitor.visitChildren(self)




    def ref_gov_area(self):

        localctx = XMLParser.Ref_gov_areaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_ref_gov_area)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            self.match(XMLParser.REF_GOV_AREA)
            self.state = 605
            self.match(XMLParser.EQUALS)
            self.state = 606
            self.match(XMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Name(self):
            return self.getToken(XMLParser.Name, 0)

        def EQUALS(self):
            return self.getToken(XMLParser.EQUALS, 0)

        def STRING(self):
            return self.getToken(XMLParser.STRING, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = XMLParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 608
            self.match(XMLParser.Name)
            self.state = 609
            self.match(XMLParser.EQUALS)
            self.state = 610
            self.match(XMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChardataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(XMLParser.TEXT, 0)

        def SEA_WS(self):
            return self.getToken(XMLParser.SEA_WS, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_chardata

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChardata" ):
                return visitor.visitChardata(self)
            else:
                return visitor.visitChildren(self)




    def chardata(self):

        localctx = XMLParser.ChardataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_chardata)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 612
            _la = self._input.LA(1)
            if not(_la==6 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MiscContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(XMLParser.COMMENT, 0)

        def PI(self):
            return self.getToken(XMLParser.PI, 0)

        def SEA_WS(self):
            return self.getToken(XMLParser.SEA_WS, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_misc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMisc" ):
                return visitor.visitMisc(self)
            else:
                return visitor.visitChildren(self)




    def misc(self):

        localctx = XMLParser.MiscContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_misc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 614
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 562949953421378) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





