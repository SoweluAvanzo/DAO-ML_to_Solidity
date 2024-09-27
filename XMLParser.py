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
        4,1,47,577,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,1,0,3,0,80,
        8,0,1,0,5,0,83,8,0,10,0,12,0,86,9,0,1,0,1,0,5,0,90,8,0,10,0,12,0,
        93,9,0,1,0,1,0,1,1,1,1,5,1,99,8,1,10,1,12,1,102,9,1,1,1,1,1,1,2,
        3,2,107,8,2,1,2,1,2,1,2,1,2,1,2,3,2,114,8,2,1,2,3,2,117,8,2,5,2,
        119,8,2,10,2,12,2,122,9,2,1,3,1,3,1,3,5,3,127,8,3,10,3,12,3,130,
        9,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,142,8,3,10,3,12,
        3,145,9,3,1,3,3,3,148,8,3,1,4,1,4,1,4,5,4,153,8,4,10,4,12,4,156,
        9,4,1,4,5,4,159,8,4,10,4,12,4,162,9,4,1,4,5,4,165,8,4,10,4,12,4,
        168,9,4,1,4,1,4,3,4,172,8,4,1,4,1,4,1,4,1,4,1,4,3,4,179,8,4,1,4,
        3,4,182,8,4,5,4,184,8,4,10,4,12,4,187,9,4,1,4,1,4,1,4,1,4,1,4,1,
        5,1,5,1,5,5,5,197,8,5,10,5,12,5,200,9,5,1,5,1,5,5,5,204,8,5,10,5,
        12,5,207,9,5,1,5,1,5,5,5,211,8,5,10,5,12,5,214,9,5,1,5,1,5,5,5,218,
        8,5,10,5,12,5,221,9,5,1,5,1,5,5,5,225,8,5,10,5,12,5,228,9,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,5,6,240,8,6,10,6,12,6,243,9,
        6,1,6,1,6,5,6,247,8,6,10,6,12,6,250,9,6,1,6,1,6,5,6,254,8,6,10,6,
        12,6,257,9,6,1,6,1,6,5,6,261,8,6,10,6,12,6,264,9,6,1,6,3,6,267,8,
        6,1,6,5,6,270,8,6,10,6,12,6,273,9,6,1,6,3,6,276,8,6,1,6,5,6,279,
        8,6,10,6,12,6,282,9,6,1,6,1,6,5,6,286,8,6,10,6,12,6,289,9,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,5,7,302,8,7,10,7,12,7,305,
        9,7,1,7,1,7,5,7,309,8,7,10,7,12,7,312,9,7,1,7,3,7,315,8,7,1,7,5,
        7,318,8,7,10,7,12,7,321,9,7,1,7,3,7,324,8,7,1,7,5,7,327,8,7,10,7,
        12,7,330,9,7,1,7,3,7,333,8,7,1,7,5,7,336,8,7,10,7,12,7,339,9,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,5,8,352,8,8,10,8,12,8,
        355,9,8,1,8,1,8,5,8,359,8,8,10,8,12,8,362,9,8,1,8,1,8,5,8,366,8,
        8,10,8,12,8,369,9,8,1,8,3,8,372,8,8,1,8,5,8,375,8,8,10,8,12,8,378,
        9,8,1,8,1,8,1,9,1,9,1,9,5,9,385,8,9,10,9,12,9,388,9,9,1,9,1,9,1,
        10,3,10,393,8,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,403,
        8,10,1,10,3,10,406,8,10,5,10,408,8,10,10,10,12,10,411,9,10,1,11,
        3,11,414,8,11,1,11,1,11,1,11,1,11,1,11,3,11,421,8,11,1,11,3,11,424,
        8,11,5,11,426,8,11,10,11,12,11,429,9,11,1,12,1,12,1,12,5,12,434,
        8,12,10,12,12,12,437,9,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,13,
        1,13,1,13,5,13,449,8,13,10,13,12,13,452,9,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,14,1,14,1,14,5,14,464,8,14,10,14,12,14,467,9,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,5,15,479,8,15,
        10,15,12,15,482,9,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,
        1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,20,
        1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,23,1,23,
        1,23,1,23,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,
        1,26,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,
        1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,33,
        1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,36,1,36,
        1,36,1,36,1,37,1,37,1,38,1,38,1,38,0,0,39,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,
        62,64,66,68,70,72,74,76,0,3,1,0,4,5,2,0,6,6,9,9,3,0,1,1,6,6,47,47,
        610,0,79,1,0,0,0,2,96,1,0,0,0,4,106,1,0,0,0,6,147,1,0,0,0,8,149,
        1,0,0,0,10,193,1,0,0,0,12,236,1,0,0,0,14,297,1,0,0,0,16,347,1,0,
        0,0,18,381,1,0,0,0,20,392,1,0,0,0,22,413,1,0,0,0,24,430,1,0,0,0,
        26,445,1,0,0,0,28,460,1,0,0,0,30,475,1,0,0,0,32,490,1,0,0,0,34,492,
        1,0,0,0,36,496,1,0,0,0,38,500,1,0,0,0,40,504,1,0,0,0,42,508,1,0,
        0,0,44,512,1,0,0,0,46,516,1,0,0,0,48,520,1,0,0,0,50,524,1,0,0,0,
        52,528,1,0,0,0,54,532,1,0,0,0,56,536,1,0,0,0,58,540,1,0,0,0,60,544,
        1,0,0,0,62,548,1,0,0,0,64,552,1,0,0,0,66,556,1,0,0,0,68,560,1,0,
        0,0,70,564,1,0,0,0,72,568,1,0,0,0,74,572,1,0,0,0,76,574,1,0,0,0,
        78,80,3,2,1,0,79,78,1,0,0,0,79,80,1,0,0,0,80,84,1,0,0,0,81,83,3,
        76,38,0,82,81,1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,
        85,87,1,0,0,0,86,84,1,0,0,0,87,91,3,8,4,0,88,90,3,76,38,0,89,88,
        1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,94,1,0,0,0,
        93,91,1,0,0,0,94,95,5,0,0,1,95,1,1,0,0,0,96,100,5,8,0,0,97,99,3,
        72,36,0,98,97,1,0,0,0,99,102,1,0,0,0,100,98,1,0,0,0,100,101,1,0,
        0,0,101,103,1,0,0,0,102,100,1,0,0,0,103,104,5,40,0,0,104,3,1,0,0,
        0,105,107,3,74,37,0,106,105,1,0,0,0,106,107,1,0,0,0,107,120,1,0,
        0,0,108,114,3,6,3,0,109,114,3,32,16,0,110,114,5,2,0,0,111,114,5,
        47,0,0,112,114,5,1,0,0,113,108,1,0,0,0,113,109,1,0,0,0,113,110,1,
        0,0,0,113,111,1,0,0,0,113,112,1,0,0,0,114,116,1,0,0,0,115,117,3,
        74,37,0,116,115,1,0,0,0,116,117,1,0,0,0,117,119,1,0,0,0,118,113,
        1,0,0,0,119,122,1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,5,1,
        0,0,0,122,120,1,0,0,0,123,124,5,7,0,0,124,128,5,45,0,0,125,127,3,
        72,36,0,126,125,1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,128,129,
        1,0,0,0,129,131,1,0,0,0,130,128,1,0,0,0,131,132,5,39,0,0,132,133,
        3,4,2,0,133,134,5,7,0,0,134,135,5,42,0,0,135,136,5,45,0,0,136,137,
        5,39,0,0,137,148,1,0,0,0,138,139,5,7,0,0,139,143,5,45,0,0,140,142,
        3,72,36,0,141,140,1,0,0,0,142,145,1,0,0,0,143,141,1,0,0,0,143,144,
        1,0,0,0,144,146,1,0,0,0,145,143,1,0,0,0,146,148,5,41,0,0,147,123,
        1,0,0,0,147,138,1,0,0,0,148,7,1,0,0,0,149,150,5,7,0,0,150,154,5,
        10,0,0,151,153,3,76,38,0,152,151,1,0,0,0,153,156,1,0,0,0,154,152,
        1,0,0,0,154,155,1,0,0,0,155,160,1,0,0,0,156,154,1,0,0,0,157,159,
        3,72,36,0,158,157,1,0,0,0,159,162,1,0,0,0,160,158,1,0,0,0,160,161,
        1,0,0,0,161,166,1,0,0,0,162,160,1,0,0,0,163,165,3,76,38,0,164,163,
        1,0,0,0,165,168,1,0,0,0,166,164,1,0,0,0,166,167,1,0,0,0,167,169,
        1,0,0,0,168,166,1,0,0,0,169,171,5,39,0,0,170,172,3,74,37,0,171,170,
        1,0,0,0,171,172,1,0,0,0,172,185,1,0,0,0,173,179,3,10,5,0,174,179,
        3,32,16,0,175,179,5,2,0,0,176,179,5,47,0,0,177,179,5,1,0,0,178,173,
        1,0,0,0,178,174,1,0,0,0,178,175,1,0,0,0,178,176,1,0,0,0,178,177,
        1,0,0,0,179,181,1,0,0,0,180,182,3,74,37,0,181,180,1,0,0,0,181,182,
        1,0,0,0,182,184,1,0,0,0,183,178,1,0,0,0,184,187,1,0,0,0,185,183,
        1,0,0,0,185,186,1,0,0,0,186,188,1,0,0,0,187,185,1,0,0,0,188,189,
        5,7,0,0,189,190,5,42,0,0,190,191,5,10,0,0,191,192,5,39,0,0,192,9,
        1,0,0,0,193,194,5,7,0,0,194,198,5,11,0,0,195,197,3,76,38,0,196,195,
        1,0,0,0,197,200,1,0,0,0,198,196,1,0,0,0,198,199,1,0,0,0,199,201,
        1,0,0,0,200,198,1,0,0,0,201,205,3,34,17,0,202,204,3,76,38,0,203,
        202,1,0,0,0,204,207,1,0,0,0,205,203,1,0,0,0,205,206,1,0,0,0,206,
        208,1,0,0,0,207,205,1,0,0,0,208,212,3,36,18,0,209,211,3,76,38,0,
        210,209,1,0,0,0,211,214,1,0,0,0,212,210,1,0,0,0,212,213,1,0,0,0,
        213,215,1,0,0,0,214,212,1,0,0,0,215,219,3,38,19,0,216,218,3,76,38,
        0,217,216,1,0,0,0,218,221,1,0,0,0,219,217,1,0,0,0,219,220,1,0,0,
        0,220,222,1,0,0,0,221,219,1,0,0,0,222,226,3,40,20,0,223,225,3,76,
        38,0,224,223,1,0,0,0,225,228,1,0,0,0,226,224,1,0,0,0,226,227,1,0,
        0,0,227,229,1,0,0,0,228,226,1,0,0,0,229,230,5,39,0,0,230,231,3,20,
        10,0,231,232,5,7,0,0,232,233,5,42,0,0,233,234,5,11,0,0,234,235,5,
        39,0,0,235,11,1,0,0,0,236,237,5,7,0,0,237,241,5,12,0,0,238,240,3,
        76,38,0,239,238,1,0,0,0,240,243,1,0,0,0,241,239,1,0,0,0,241,242,
        1,0,0,0,242,244,1,0,0,0,243,241,1,0,0,0,244,248,3,42,21,0,245,247,
        3,76,38,0,246,245,1,0,0,0,247,250,1,0,0,0,248,246,1,0,0,0,248,249,
        1,0,0,0,249,251,1,0,0,0,250,248,1,0,0,0,251,255,3,44,22,0,252,254,
        3,76,38,0,253,252,1,0,0,0,254,257,1,0,0,0,255,253,1,0,0,0,255,256,
        1,0,0,0,256,258,1,0,0,0,257,255,1,0,0,0,258,262,3,46,23,0,259,261,
        3,76,38,0,260,259,1,0,0,0,261,264,1,0,0,0,262,260,1,0,0,0,262,263,
        1,0,0,0,263,266,1,0,0,0,264,262,1,0,0,0,265,267,3,48,24,0,266,265,
        1,0,0,0,266,267,1,0,0,0,267,271,1,0,0,0,268,270,3,76,38,0,269,268,
        1,0,0,0,270,273,1,0,0,0,271,269,1,0,0,0,271,272,1,0,0,0,272,275,
        1,0,0,0,273,271,1,0,0,0,274,276,3,50,25,0,275,274,1,0,0,0,275,276,
        1,0,0,0,276,280,1,0,0,0,277,279,3,76,38,0,278,277,1,0,0,0,279,282,
        1,0,0,0,280,278,1,0,0,0,280,281,1,0,0,0,281,283,1,0,0,0,282,280,
        1,0,0,0,283,287,3,52,26,0,284,286,3,76,38,0,285,284,1,0,0,0,286,
        289,1,0,0,0,287,285,1,0,0,0,287,288,1,0,0,0,288,290,1,0,0,0,289,
        287,1,0,0,0,290,291,5,39,0,0,291,292,3,22,11,0,292,293,5,7,0,0,293,
        294,5,42,0,0,294,295,5,12,0,0,295,296,5,39,0,0,296,13,1,0,0,0,297,
        298,5,7,0,0,298,299,5,13,0,0,299,303,3,54,27,0,300,302,3,76,38,0,
        301,300,1,0,0,0,302,305,1,0,0,0,303,301,1,0,0,0,303,304,1,0,0,0,
        304,306,1,0,0,0,305,303,1,0,0,0,306,310,3,56,28,0,307,309,3,76,38,
        0,308,307,1,0,0,0,309,312,1,0,0,0,310,308,1,0,0,0,310,311,1,0,0,
        0,311,314,1,0,0,0,312,310,1,0,0,0,313,315,3,58,29,0,314,313,1,0,
        0,0,314,315,1,0,0,0,315,319,1,0,0,0,316,318,3,76,38,0,317,316,1,
        0,0,0,318,321,1,0,0,0,319,317,1,0,0,0,319,320,1,0,0,0,320,323,1,
        0,0,0,321,319,1,0,0,0,322,324,3,60,30,0,323,322,1,0,0,0,323,324,
        1,0,0,0,324,328,1,0,0,0,325,327,3,76,38,0,326,325,1,0,0,0,327,330,
        1,0,0,0,328,326,1,0,0,0,328,329,1,0,0,0,329,332,1,0,0,0,330,328,
        1,0,0,0,331,333,3,62,31,0,332,331,1,0,0,0,332,333,1,0,0,0,333,337,
        1,0,0,0,334,336,3,76,38,0,335,334,1,0,0,0,336,339,1,0,0,0,337,335,
        1,0,0,0,337,338,1,0,0,0,338,340,1,0,0,0,339,337,1,0,0,0,340,341,
        5,39,0,0,341,342,3,22,11,0,342,343,5,7,0,0,343,344,5,42,0,0,344,
        345,5,13,0,0,345,346,5,39,0,0,346,15,1,0,0,0,347,348,5,7,0,0,348,
        349,5,14,0,0,349,353,3,64,32,0,350,352,3,76,38,0,351,350,1,0,0,0,
        352,355,1,0,0,0,353,351,1,0,0,0,353,354,1,0,0,0,354,356,1,0,0,0,
        355,353,1,0,0,0,356,360,3,66,33,0,357,359,3,76,38,0,358,357,1,0,
        0,0,359,362,1,0,0,0,360,358,1,0,0,0,360,361,1,0,0,0,361,363,1,0,
        0,0,362,360,1,0,0,0,363,367,3,68,34,0,364,366,3,76,38,0,365,364,
        1,0,0,0,366,369,1,0,0,0,367,365,1,0,0,0,367,368,1,0,0,0,368,371,
        1,0,0,0,369,367,1,0,0,0,370,372,3,70,35,0,371,370,1,0,0,0,371,372,
        1,0,0,0,372,376,1,0,0,0,373,375,3,76,38,0,374,373,1,0,0,0,375,378,
        1,0,0,0,376,374,1,0,0,0,376,377,1,0,0,0,377,379,1,0,0,0,378,376,
        1,0,0,0,379,380,5,41,0,0,380,17,1,0,0,0,381,382,5,7,0,0,382,386,
        5,15,0,0,383,385,3,72,36,0,384,383,1,0,0,0,385,388,1,0,0,0,386,384,
        1,0,0,0,386,387,1,0,0,0,387,389,1,0,0,0,388,386,1,0,0,0,389,390,
        5,41,0,0,390,19,1,0,0,0,391,393,3,74,37,0,392,391,1,0,0,0,392,393,
        1,0,0,0,393,409,1,0,0,0,394,403,3,12,6,0,395,403,3,14,7,0,396,403,
        3,16,8,0,397,403,3,18,9,0,398,403,3,32,16,0,399,403,5,2,0,0,400,
        403,5,47,0,0,401,403,5,1,0,0,402,394,1,0,0,0,402,395,1,0,0,0,402,
        396,1,0,0,0,402,397,1,0,0,0,402,398,1,0,0,0,402,399,1,0,0,0,402,
        400,1,0,0,0,402,401,1,0,0,0,403,405,1,0,0,0,404,406,3,74,37,0,405,
        404,1,0,0,0,405,406,1,0,0,0,406,408,1,0,0,0,407,402,1,0,0,0,408,
        411,1,0,0,0,409,407,1,0,0,0,409,410,1,0,0,0,410,21,1,0,0,0,411,409,
        1,0,0,0,412,414,3,74,37,0,413,412,1,0,0,0,413,414,1,0,0,0,414,427,
        1,0,0,0,415,421,3,24,12,0,416,421,3,26,13,0,417,421,3,28,14,0,418,
        421,3,30,15,0,419,421,5,1,0,0,420,415,1,0,0,0,420,416,1,0,0,0,420,
        417,1,0,0,0,420,418,1,0,0,0,420,419,1,0,0,0,421,423,1,0,0,0,422,
        424,3,74,37,0,423,422,1,0,0,0,423,424,1,0,0,0,424,426,1,0,0,0,425,
        420,1,0,0,0,426,429,1,0,0,0,427,425,1,0,0,0,427,428,1,0,0,0,428,
        23,1,0,0,0,429,427,1,0,0,0,430,431,5,7,0,0,431,435,5,16,0,0,432,
        434,3,72,36,0,433,432,1,0,0,0,434,437,1,0,0,0,435,433,1,0,0,0,435,
        436,1,0,0,0,436,438,1,0,0,0,437,435,1,0,0,0,438,439,5,39,0,0,439,
        440,3,4,2,0,440,441,5,7,0,0,441,442,5,42,0,0,442,443,5,16,0,0,443,
        444,5,39,0,0,444,25,1,0,0,0,445,446,5,7,0,0,446,450,5,17,0,0,447,
        449,3,72,36,0,448,447,1,0,0,0,449,452,1,0,0,0,450,448,1,0,0,0,450,
        451,1,0,0,0,451,453,1,0,0,0,452,450,1,0,0,0,453,454,5,39,0,0,454,
        455,3,4,2,0,455,456,5,7,0,0,456,457,5,42,0,0,457,458,5,17,0,0,458,
        459,5,39,0,0,459,27,1,0,0,0,460,461,5,7,0,0,461,465,5,18,0,0,462,
        464,3,72,36,0,463,462,1,0,0,0,464,467,1,0,0,0,465,463,1,0,0,0,465,
        466,1,0,0,0,466,468,1,0,0,0,467,465,1,0,0,0,468,469,5,39,0,0,469,
        470,3,4,2,0,470,471,5,7,0,0,471,472,5,42,0,0,472,473,5,18,0,0,473,
        474,5,39,0,0,474,29,1,0,0,0,475,476,5,7,0,0,476,480,5,19,0,0,477,
        479,3,72,36,0,478,477,1,0,0,0,479,482,1,0,0,0,480,478,1,0,0,0,480,
        481,1,0,0,0,481,483,1,0,0,0,482,480,1,0,0,0,483,484,5,39,0,0,484,
        485,3,4,2,0,485,486,5,7,0,0,486,487,5,42,0,0,487,488,5,19,0,0,488,
        489,5,39,0,0,489,31,1,0,0,0,490,491,7,0,0,0,491,33,1,0,0,0,492,493,
        5,20,0,0,493,494,5,43,0,0,494,495,5,44,0,0,495,35,1,0,0,0,496,497,
        5,21,0,0,497,498,5,43,0,0,498,499,5,44,0,0,499,37,1,0,0,0,500,501,
        5,22,0,0,501,502,5,43,0,0,502,503,5,44,0,0,503,39,1,0,0,0,504,505,
        5,23,0,0,505,506,5,43,0,0,506,507,5,44,0,0,507,41,1,0,0,0,508,509,
        5,24,0,0,509,510,5,43,0,0,510,511,5,44,0,0,511,43,1,0,0,0,512,513,
        5,25,0,0,513,514,5,43,0,0,514,515,5,44,0,0,515,45,1,0,0,0,516,517,
        5,26,0,0,517,518,5,43,0,0,518,519,5,44,0,0,519,47,1,0,0,0,520,521,
        5,29,0,0,521,522,5,43,0,0,522,523,5,44,0,0,523,49,1,0,0,0,524,525,
        5,30,0,0,525,526,5,43,0,0,526,527,5,44,0,0,527,51,1,0,0,0,528,529,
        5,37,0,0,529,530,5,43,0,0,530,531,5,44,0,0,531,53,1,0,0,0,532,533,
        5,27,0,0,533,534,5,43,0,0,534,535,5,44,0,0,535,55,1,0,0,0,536,537,
        5,28,0,0,537,538,5,43,0,0,538,539,5,44,0,0,539,57,1,0,0,0,540,541,
        5,32,0,0,541,542,5,43,0,0,542,543,5,44,0,0,543,59,1,0,0,0,544,545,
        5,33,0,0,545,546,5,43,0,0,546,547,5,44,0,0,547,61,1,0,0,0,548,549,
        5,31,0,0,549,550,5,43,0,0,550,551,5,44,0,0,551,63,1,0,0,0,552,553,
        5,34,0,0,553,554,5,43,0,0,554,555,5,44,0,0,555,65,1,0,0,0,556,557,
        5,36,0,0,557,558,5,43,0,0,558,559,5,44,0,0,559,67,1,0,0,0,560,561,
        5,38,0,0,561,562,5,43,0,0,562,563,5,44,0,0,563,69,1,0,0,0,564,565,
        5,35,0,0,565,566,5,43,0,0,566,567,5,44,0,0,567,71,1,0,0,0,568,569,
        5,45,0,0,569,570,5,43,0,0,570,571,5,44,0,0,571,73,1,0,0,0,572,573,
        7,1,0,0,573,75,1,0,0,0,574,575,7,2,0,0,575,77,1,0,0,0,58,79,84,91,
        100,106,113,116,120,128,143,147,154,160,166,171,178,181,185,198,
        205,212,219,226,241,248,255,262,266,271,275,280,287,303,310,314,
        319,323,328,332,337,353,360,367,371,376,386,392,402,405,409,413,
        420,423,427,435,450,465,480
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
                     "'permission_type'", "'>'", "<INVALID>", "'/>'", "'/'", 
                     "'='" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "CDATA", "DTD", "EntityRef", 
                      "CharRef", "SEA_WS", "OPEN", "XMLDeclOpen", "TEXT", 
                      "DIAGRAM", "DAO", "ROLE", "COMMITTEE", "PERMISSION", 
                      "GOV", "ASSOCIATION", "CONTROL", "AGGREGATES", "FEDERATES", 
                      "DAOID", "DAONAME", "MISSIONSTATEMENT", "HIERARCHICALINHERITANCE", 
                      "ROLEID", "ROLENAME", "ROLEASSIGNMENTMETHOD", "COMMITTEEID", 
                      "COMMITTEEDESCRIPTION", "NAGENTMIN", "NAGENTMAX", 
                      "DMMETHOD", "VOTINGCONDITION", "PROPOSALCONDITION", 
                      "PERMISSIONID", "REF_GOV_AREA", "ALLOWEDACTION", "AGENTTYPE", 
                      "PERMISSIONTYPE", "CLOSE", "SPECIAL_CLOSE", "SLASH_CLOSE", 
                      "SLASH", "EQUALS", "STRING", "Name", "S", "PI" ]

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
    RULE_permission_id = 32
    RULE_allowed_action = 33
    RULE_permission_type = 34
    RULE_ref_gov_area = 35
    RULE_attribute = 36
    RULE_chardata = 37
    RULE_misc = 38

    ruleNames =  [ "document", "prolog", "content", "element", "diagram", 
                   "dao", "role", "committee", "permission", "gov", "daocontent", 
                   "relations", "associated_to", "controlled_by", "aggregates", 
                   "federates_into", "reference", "dao_id", "dao_name", 
                   "mission_statement", "hierarchical_inheritance", "role_id", 
                   "role_name", "role_assignment_method", "n_agent_min", 
                   "n_agent_max", "agent_type", "committee_id", "committee_description", 
                   "voting_condition", "proposal_condition", "decision_making_method", 
                   "permission_id", "allowed_action", "permission_type", 
                   "ref_gov_area", "attribute", "chardata", "misc" ]

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
    CLOSE=39
    SPECIAL_CLOSE=40
    SLASH_CLOSE=41
    SLASH=42
    EQUALS=43
    STRING=44
    Name=45
    S=46
    PI=47

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
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 78
                self.prolog()


            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488355394) != 0):
                self.state = 81
                self.misc()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 87
            self.diagram()
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488355394) != 0):
                self.state = 88
                self.misc()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 94
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
            self.state = 96
            self.match(XMLParser.XMLDeclOpen)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 97
                self.attribute()
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 103
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
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6 or _la==9:
                self.state = 105
                self.chardata()


            self.state = 120
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 113
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [7]:
                        self.state = 108
                        self.element()
                        pass
                    elif token in [4, 5]:
                        self.state = 109
                        self.reference()
                        pass
                    elif token in [2]:
                        self.state = 110
                        self.match(XMLParser.CDATA)
                        pass
                    elif token in [47]:
                        self.state = 111
                        self.match(XMLParser.PI)
                        pass
                    elif token in [1]:
                        self.state = 112
                        self.match(XMLParser.COMMENT)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 116
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==6 or _la==9:
                        self.state = 115
                        self.chardata()

             
                self.state = 122
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
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.match(XMLParser.OPEN)
                self.state = 124
                self.match(XMLParser.Name)
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==45:
                    self.state = 125
                    self.attribute()
                    self.state = 130
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 131
                self.match(XMLParser.CLOSE)
                self.state = 132
                self.content()
                self.state = 133
                self.match(XMLParser.OPEN)
                self.state = 134
                self.match(XMLParser.SLASH)
                self.state = 135
                self.match(XMLParser.Name)
                self.state = 136
                self.match(XMLParser.CLOSE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.match(XMLParser.OPEN)
                self.state = 139
                self.match(XMLParser.Name)
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==45:
                    self.state = 140
                    self.attribute()
                    self.state = 145
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 146
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
            self.state = 149
            self.match(XMLParser.OPEN)
            self.state = 150
            self.match(XMLParser.DIAGRAM)
            self.state = 154
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 151
                    self.misc() 
                self.state = 156
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 157
                self.attribute()
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488355394) != 0):
                self.state = 163
                self.misc()
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 169
            self.match(XMLParser.CLOSE)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6 or _la==9:
                self.state = 170
                self.chardata()


            self.state = 185
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 178
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [7]:
                        self.state = 173
                        self.dao()
                        pass
                    elif token in [4, 5]:
                        self.state = 174
                        self.reference()
                        pass
                    elif token in [2]:
                        self.state = 175
                        self.match(XMLParser.CDATA)
                        pass
                    elif token in [47]:
                        self.state = 176
                        self.match(XMLParser.PI)
                        pass
                    elif token in [1]:
                        self.state = 177
                        self.match(XMLParser.COMMENT)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 181
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==6 or _la==9:
                        self.state = 180
                        self.chardata()

             
                self.state = 187
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

            self.state = 188
            self.match(XMLParser.OPEN)
            self.state = 189
            self.match(XMLParser.SLASH)
            self.state = 190
            self.match(XMLParser.DIAGRAM)
            self.state = 191
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
            self.state = 193
            self.match(XMLParser.OPEN)
            self.state = 194
            self.match(XMLParser.DAO)
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488355394) != 0):
                self.state = 195
                self.misc()
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 201
            self.dao_id()
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488355394) != 0):
                self.state = 202
                self.misc()
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 208
            self.dao_name()
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488355394) != 0):
                self.state = 209
                self.misc()
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 215
            self.mission_statement()
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488355394) != 0):
                self.state = 216
                self.misc()
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 222
            self.hierarchical_inheritance()
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488355394) != 0):
                self.state = 223
                self.misc()
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 229
            self.match(XMLParser.CLOSE)
            self.state = 230
            self.daocontent()
            self.state = 231
            self.match(XMLParser.OPEN)
            self.state = 232
            self.match(XMLParser.SLASH)
            self.state = 233
            self.match(XMLParser.DAO)
            self.state = 234
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
            self.state = 236
            self.match(XMLParser.OPEN)
            self.state = 237
            self.match(XMLParser.ROLE)
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488355394) != 0):
                self.state = 238
                self.misc()
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 244
            self.role_id()
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488355394) != 0):
                self.state = 245
                self.misc()
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 251
            self.role_name()
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488355394) != 0):
                self.state = 252
                self.misc()
                self.state = 257
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 258
            self.role_assignment_method()
            self.state = 262
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 259
                    self.misc() 
                self.state = 264
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 265
                self.n_agent_min()


            self.state = 271
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 268
                    self.misc() 
                self.state = 273
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 274
                self.n_agent_max()


            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488355394) != 0):
                self.state = 277
                self.misc()
                self.state = 282
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 283
            self.agent_type()
            self.state = 287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488355394) != 0):
                self.state = 284
                self.misc()
                self.state = 289
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 290
            self.match(XMLParser.CLOSE)
            self.state = 291
            self.relations()
            self.state = 292
            self.match(XMLParser.OPEN)
            self.state = 293
            self.match(XMLParser.SLASH)
            self.state = 294
            self.match(XMLParser.ROLE)
            self.state = 295
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
            self.state = 297
            self.match(XMLParser.OPEN)
            self.state = 298
            self.match(XMLParser.COMMITTEE)
            self.state = 299
            self.committee_id()
            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488355394) != 0):
                self.state = 300
                self.misc()
                self.state = 305
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 306
            self.committee_description()
            self.state = 310
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 307
                    self.misc() 
                self.state = 312
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 313
                self.voting_condition()


            self.state = 319
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 316
                    self.misc() 
                self.state = 321
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

            self.state = 323
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 322
                self.proposal_condition()


            self.state = 328
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 325
                    self.misc() 
                self.state = 330
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 331
                self.decision_making_method()


            self.state = 337
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488355394) != 0):
                self.state = 334
                self.misc()
                self.state = 339
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 340
            self.match(XMLParser.CLOSE)
            self.state = 341
            self.relations()
            self.state = 342
            self.match(XMLParser.OPEN)
            self.state = 343
            self.match(XMLParser.SLASH)
            self.state = 344
            self.match(XMLParser.COMMITTEE)
            self.state = 345
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
            self.state = 347
            self.match(XMLParser.OPEN)
            self.state = 348
            self.match(XMLParser.PERMISSION)
            self.state = 349
            self.permission_id()
            self.state = 353
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488355394) != 0):
                self.state = 350
                self.misc()
                self.state = 355
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 356
            self.allowed_action()
            self.state = 360
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488355394) != 0):
                self.state = 357
                self.misc()
                self.state = 362
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 363
            self.permission_type()
            self.state = 367
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 364
                    self.misc() 
                self.state = 369
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

            self.state = 371
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 370
                self.ref_gov_area()


            self.state = 376
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488355394) != 0):
                self.state = 373
                self.misc()
                self.state = 378
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 379
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
            self.state = 381
            self.match(XMLParser.OPEN)
            self.state = 382
            self.match(XMLParser.GOV)
            self.state = 386
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 383
                self.attribute()
                self.state = 388
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 389
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
            self.state = 392
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6 or _la==9:
                self.state = 391
                self.chardata()


            self.state = 409
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,49,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 402
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                    if la_ == 1:
                        self.state = 394
                        self.role()
                        pass

                    elif la_ == 2:
                        self.state = 395
                        self.committee()
                        pass

                    elif la_ == 3:
                        self.state = 396
                        self.permission()
                        pass

                    elif la_ == 4:
                        self.state = 397
                        self.gov()
                        pass

                    elif la_ == 5:
                        self.state = 398
                        self.reference()
                        pass

                    elif la_ == 6:
                        self.state = 399
                        self.match(XMLParser.CDATA)
                        pass

                    elif la_ == 7:
                        self.state = 400
                        self.match(XMLParser.PI)
                        pass

                    elif la_ == 8:
                        self.state = 401
                        self.match(XMLParser.COMMENT)
                        pass


                    self.state = 405
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==6 or _la==9:
                        self.state = 404
                        self.chardata()

             
                self.state = 411
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,49,self._ctx)

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
            self.state = 413
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6 or _la==9:
                self.state = 412
                self.chardata()


            self.state = 427
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,53,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 420
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                    if la_ == 1:
                        self.state = 415
                        self.associated_to()
                        pass

                    elif la_ == 2:
                        self.state = 416
                        self.controlled_by()
                        pass

                    elif la_ == 3:
                        self.state = 417
                        self.aggregates()
                        pass

                    elif la_ == 4:
                        self.state = 418
                        self.federates_into()
                        pass

                    elif la_ == 5:
                        self.state = 419
                        self.match(XMLParser.COMMENT)
                        pass


                    self.state = 423
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==6 or _la==9:
                        self.state = 422
                        self.chardata()

             
                self.state = 429
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,53,self._ctx)

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
            self.state = 430
            self.match(XMLParser.OPEN)
            self.state = 431
            self.match(XMLParser.ASSOCIATION)
            self.state = 435
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 432
                self.attribute()
                self.state = 437
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 438
            self.match(XMLParser.CLOSE)
            self.state = 439
            self.content()
            self.state = 440
            self.match(XMLParser.OPEN)
            self.state = 441
            self.match(XMLParser.SLASH)
            self.state = 442
            self.match(XMLParser.ASSOCIATION)
            self.state = 443
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
            self.state = 445
            self.match(XMLParser.OPEN)
            self.state = 446
            self.match(XMLParser.CONTROL)
            self.state = 450
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 447
                self.attribute()
                self.state = 452
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 453
            self.match(XMLParser.CLOSE)
            self.state = 454
            self.content()
            self.state = 455
            self.match(XMLParser.OPEN)
            self.state = 456
            self.match(XMLParser.SLASH)
            self.state = 457
            self.match(XMLParser.CONTROL)
            self.state = 458
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
            self.state = 460
            self.match(XMLParser.OPEN)
            self.state = 461
            self.match(XMLParser.AGGREGATES)
            self.state = 465
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 462
                self.attribute()
                self.state = 467
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 468
            self.match(XMLParser.CLOSE)
            self.state = 469
            self.content()
            self.state = 470
            self.match(XMLParser.OPEN)
            self.state = 471
            self.match(XMLParser.SLASH)
            self.state = 472
            self.match(XMLParser.AGGREGATES)
            self.state = 473
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
            self.state = 475
            self.match(XMLParser.OPEN)
            self.state = 476
            self.match(XMLParser.FEDERATES)
            self.state = 480
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 477
                self.attribute()
                self.state = 482
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 483
            self.match(XMLParser.CLOSE)
            self.state = 484
            self.content()
            self.state = 485
            self.match(XMLParser.OPEN)
            self.state = 486
            self.match(XMLParser.SLASH)
            self.state = 487
            self.match(XMLParser.FEDERATES)
            self.state = 488
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
            self.state = 490
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
            self.state = 492
            self.match(XMLParser.DAOID)
            self.state = 493
            self.match(XMLParser.EQUALS)
            self.state = 494
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
            self.state = 496
            self.match(XMLParser.DAONAME)
            self.state = 497
            self.match(XMLParser.EQUALS)
            self.state = 498
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
            self.state = 500
            self.match(XMLParser.MISSIONSTATEMENT)
            self.state = 501
            self.match(XMLParser.EQUALS)
            self.state = 502
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
            self.state = 504
            self.match(XMLParser.HIERARCHICALINHERITANCE)
            self.state = 505
            self.match(XMLParser.EQUALS)
            self.state = 506
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
            self.state = 508
            self.match(XMLParser.ROLEID)
            self.state = 509
            self.match(XMLParser.EQUALS)
            self.state = 510
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
            self.state = 512
            self.match(XMLParser.ROLENAME)
            self.state = 513
            self.match(XMLParser.EQUALS)
            self.state = 514
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
            self.state = 516
            self.match(XMLParser.ROLEASSIGNMENTMETHOD)
            self.state = 517
            self.match(XMLParser.EQUALS)
            self.state = 518
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
            self.state = 520
            self.match(XMLParser.NAGENTMIN)
            self.state = 521
            self.match(XMLParser.EQUALS)
            self.state = 522
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
            self.state = 524
            self.match(XMLParser.NAGENTMAX)
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
            self.state = 528
            self.match(XMLParser.AGENTTYPE)
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
            self.state = 532
            self.match(XMLParser.COMMITTEEID)
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
            self.state = 536
            self.match(XMLParser.COMMITTEEDESCRIPTION)
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
            self.state = 540
            self.match(XMLParser.VOTINGCONDITION)
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
            self.state = 544
            self.match(XMLParser.PROPOSALCONDITION)
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
            self.state = 548
            self.match(XMLParser.DMMETHOD)
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
        self.enterRule(localctx, 64, self.RULE_permission_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 552
            self.match(XMLParser.PERMISSIONID)
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
        self.enterRule(localctx, 66, self.RULE_allowed_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 556
            self.match(XMLParser.ALLOWEDACTION)
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
        self.enterRule(localctx, 68, self.RULE_permission_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 560
            self.match(XMLParser.PERMISSIONTYPE)
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
        self.enterRule(localctx, 70, self.RULE_ref_gov_area)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 564
            self.match(XMLParser.REF_GOV_AREA)
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
        self.enterRule(localctx, 72, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568
            self.match(XMLParser.Name)
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
        self.enterRule(localctx, 74, self.RULE_chardata)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 572
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
        self.enterRule(localctx, 76, self.RULE_misc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488355394) != 0)):
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





