# Generated from ./src/parsers/xml/XMLParser.g4 by ANTLR 4.13.1
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
        4,1,54,563,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,1,0,3,0,90,8,0,1,0,5,0,93,
        8,0,10,0,12,0,96,9,0,1,0,1,0,5,0,100,8,0,10,0,12,0,103,9,0,1,0,1,
        0,1,1,1,1,5,1,109,8,1,10,1,12,1,112,9,1,1,1,1,1,1,2,3,2,117,8,2,
        1,2,1,2,1,2,3,2,122,8,2,1,2,3,2,125,8,2,5,2,127,8,2,10,2,12,2,130,
        9,2,1,3,1,3,1,3,5,3,135,8,3,10,3,12,3,138,9,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,5,3,150,8,3,10,3,12,3,153,9,3,1,3,3,3,156,
        8,3,1,4,1,4,1,4,5,4,161,8,4,10,4,12,4,164,9,4,1,4,5,4,167,8,4,10,
        4,12,4,170,9,4,1,4,3,4,173,8,4,1,4,5,4,176,8,4,10,4,12,4,179,9,4,
        1,4,5,4,182,8,4,10,4,12,4,185,9,4,1,4,1,4,3,4,189,8,4,1,4,1,4,1,
        4,1,4,3,4,195,8,4,1,4,5,4,198,8,4,10,4,12,4,201,9,4,1,4,3,4,204,
        8,4,5,4,206,8,4,10,4,12,4,209,9,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,
        5,5,5,219,8,5,10,5,12,5,222,9,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,230,
        8,5,1,5,5,5,233,8,5,10,5,12,5,236,9,5,5,5,238,8,5,10,5,12,5,241,
        9,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,5,6,253,8,6,10,6,12,
        6,256,9,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,268,8,6,1,
        6,5,6,271,8,6,10,6,12,6,274,9,6,5,6,276,8,6,10,6,12,6,279,9,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,5,7,291,8,7,10,7,12,7,294,
        9,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,305,8,7,1,7,5,7,308,
        8,7,10,7,12,7,311,9,7,5,7,313,8,7,10,7,12,7,316,9,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,8,1,8,1,8,5,8,328,8,8,10,8,12,8,331,9,8,1,8,1,
        8,1,8,1,8,1,8,1,8,3,8,339,8,8,1,8,5,8,342,8,8,10,8,12,8,345,9,8,
        5,8,347,8,8,10,8,12,8,350,9,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,3,
        10,360,8,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,368,8,10,1,10,3,10,
        371,8,10,5,10,373,8,10,10,10,12,10,376,9,10,1,11,3,11,379,8,11,1,
        11,1,11,1,11,1,11,1,11,3,11,386,8,11,1,11,3,11,389,8,11,5,11,391,
        8,11,10,11,12,11,394,9,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,17,1,17,1,18,5,18,441,
        8,18,10,18,12,18,444,9,18,1,18,1,18,3,18,448,8,18,1,18,5,18,451,
        8,18,10,18,12,18,454,9,18,5,18,456,8,18,10,18,12,18,459,9,18,1,19,
        1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,22,1,22,
        1,22,1,22,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,25,1,25,1,25,
        1,25,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,
        1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,32,
        1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,35,1,35,
        1,35,1,35,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,38,1,38,1,38,
        1,38,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,41,1,41,1,41,1,41,
        1,41,1,41,1,41,1,41,3,41,557,8,41,1,42,1,42,1,43,1,43,1,43,0,0,44,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,
        46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,0,
        4,1,0,4,5,2,0,1,2,54,54,2,0,6,6,9,9,3,0,1,1,6,6,54,54,601,0,89,1,
        0,0,0,2,106,1,0,0,0,4,116,1,0,0,0,6,155,1,0,0,0,8,157,1,0,0,0,10,
        215,1,0,0,0,12,249,1,0,0,0,14,287,1,0,0,0,16,324,1,0,0,0,18,353,
        1,0,0,0,20,359,1,0,0,0,22,378,1,0,0,0,24,395,1,0,0,0,26,405,1,0,
        0,0,28,415,1,0,0,0,30,425,1,0,0,0,32,435,1,0,0,0,34,437,1,0,0,0,
        36,442,1,0,0,0,38,460,1,0,0,0,40,464,1,0,0,0,42,468,1,0,0,0,44,472,
        1,0,0,0,46,476,1,0,0,0,48,480,1,0,0,0,50,484,1,0,0,0,52,488,1,0,
        0,0,54,492,1,0,0,0,56,496,1,0,0,0,58,500,1,0,0,0,60,504,1,0,0,0,
        62,508,1,0,0,0,64,512,1,0,0,0,66,516,1,0,0,0,68,520,1,0,0,0,70,524,
        1,0,0,0,72,528,1,0,0,0,74,532,1,0,0,0,76,536,1,0,0,0,78,540,1,0,
        0,0,80,544,1,0,0,0,82,556,1,0,0,0,84,558,1,0,0,0,86,560,1,0,0,0,
        88,90,3,2,1,0,89,88,1,0,0,0,89,90,1,0,0,0,90,94,1,0,0,0,91,93,3,
        86,43,0,92,91,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,
        95,97,1,0,0,0,96,94,1,0,0,0,97,101,3,8,4,0,98,100,3,86,43,0,99,98,
        1,0,0,0,100,103,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,104,1,
        0,0,0,103,101,1,0,0,0,104,105,5,0,0,1,105,1,1,0,0,0,106,110,5,8,
        0,0,107,109,3,80,40,0,108,107,1,0,0,0,109,112,1,0,0,0,110,108,1,
        0,0,0,110,111,1,0,0,0,111,113,1,0,0,0,112,110,1,0,0,0,113,114,5,
        42,0,0,114,3,1,0,0,0,115,117,3,84,42,0,116,115,1,0,0,0,116,117,1,
        0,0,0,117,128,1,0,0,0,118,122,3,6,3,0,119,122,3,32,16,0,120,122,
        3,34,17,0,121,118,1,0,0,0,121,119,1,0,0,0,121,120,1,0,0,0,122,124,
        1,0,0,0,123,125,3,84,42,0,124,123,1,0,0,0,124,125,1,0,0,0,125,127,
        1,0,0,0,126,121,1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,128,129,
        1,0,0,0,129,5,1,0,0,0,130,128,1,0,0,0,131,132,5,7,0,0,132,136,5,
        47,0,0,133,135,3,80,40,0,134,133,1,0,0,0,135,138,1,0,0,0,136,134,
        1,0,0,0,136,137,1,0,0,0,137,139,1,0,0,0,138,136,1,0,0,0,139,140,
        5,41,0,0,140,141,3,4,2,0,141,142,5,7,0,0,142,143,5,44,0,0,143,144,
        5,47,0,0,144,145,5,41,0,0,145,156,1,0,0,0,146,147,5,7,0,0,147,151,
        5,47,0,0,148,150,3,80,40,0,149,148,1,0,0,0,150,153,1,0,0,0,151,149,
        1,0,0,0,151,152,1,0,0,0,152,154,1,0,0,0,153,151,1,0,0,0,154,156,
        5,43,0,0,155,131,1,0,0,0,155,146,1,0,0,0,156,7,1,0,0,0,157,158,5,
        7,0,0,158,162,5,10,0,0,159,161,3,86,43,0,160,159,1,0,0,0,161,164,
        1,0,0,0,162,160,1,0,0,0,162,163,1,0,0,0,163,172,1,0,0,0,164,162,
        1,0,0,0,165,167,3,80,40,0,166,165,1,0,0,0,167,170,1,0,0,0,168,166,
        1,0,0,0,168,169,1,0,0,0,169,171,1,0,0,0,170,168,1,0,0,0,171,173,
        3,82,41,0,172,168,1,0,0,0,172,173,1,0,0,0,173,177,1,0,0,0,174,176,
        3,80,40,0,175,174,1,0,0,0,176,179,1,0,0,0,177,175,1,0,0,0,177,178,
        1,0,0,0,178,183,1,0,0,0,179,177,1,0,0,0,180,182,3,86,43,0,181,180,
        1,0,0,0,182,185,1,0,0,0,183,181,1,0,0,0,183,184,1,0,0,0,184,186,
        1,0,0,0,185,183,1,0,0,0,186,188,5,41,0,0,187,189,3,84,42,0,188,187,
        1,0,0,0,188,189,1,0,0,0,189,207,1,0,0,0,190,195,3,10,5,0,191,195,
        3,32,16,0,192,195,3,34,17,0,193,195,3,80,40,0,194,190,1,0,0,0,194,
        191,1,0,0,0,194,192,1,0,0,0,194,193,1,0,0,0,195,199,1,0,0,0,196,
        198,3,86,43,0,197,196,1,0,0,0,198,201,1,0,0,0,199,197,1,0,0,0,199,
        200,1,0,0,0,200,203,1,0,0,0,201,199,1,0,0,0,202,204,3,84,42,0,203,
        202,1,0,0,0,203,204,1,0,0,0,204,206,1,0,0,0,205,194,1,0,0,0,206,
        209,1,0,0,0,207,205,1,0,0,0,207,208,1,0,0,0,208,210,1,0,0,0,209,
        207,1,0,0,0,210,211,5,7,0,0,211,212,5,44,0,0,212,213,5,10,0,0,213,
        214,5,41,0,0,214,9,1,0,0,0,215,216,5,7,0,0,216,220,5,11,0,0,217,
        219,3,86,43,0,218,217,1,0,0,0,219,222,1,0,0,0,220,218,1,0,0,0,220,
        221,1,0,0,0,221,239,1,0,0,0,222,220,1,0,0,0,223,230,3,38,19,0,224,
        230,3,40,20,0,225,230,3,42,21,0,226,230,3,44,22,0,227,230,3,34,17,
        0,228,230,3,80,40,0,229,223,1,0,0,0,229,224,1,0,0,0,229,225,1,0,
        0,0,229,226,1,0,0,0,229,227,1,0,0,0,229,228,1,0,0,0,230,234,1,0,
        0,0,231,233,3,86,43,0,232,231,1,0,0,0,233,236,1,0,0,0,234,232,1,
        0,0,0,234,235,1,0,0,0,235,238,1,0,0,0,236,234,1,0,0,0,237,229,1,
        0,0,0,238,241,1,0,0,0,239,237,1,0,0,0,239,240,1,0,0,0,240,242,1,
        0,0,0,241,239,1,0,0,0,242,243,5,41,0,0,243,244,3,20,10,0,244,245,
        5,7,0,0,245,246,5,44,0,0,246,247,5,11,0,0,247,248,5,41,0,0,248,11,
        1,0,0,0,249,250,5,7,0,0,250,254,5,12,0,0,251,253,3,86,43,0,252,251,
        1,0,0,0,253,256,1,0,0,0,254,252,1,0,0,0,254,255,1,0,0,0,255,277,
        1,0,0,0,256,254,1,0,0,0,257,268,3,46,23,0,258,268,3,48,24,0,259,
        268,3,50,25,0,260,268,3,52,26,0,261,268,3,54,27,0,262,268,3,56,28,
        0,263,268,3,68,34,0,264,268,3,70,35,0,265,268,3,34,17,0,266,268,
        3,80,40,0,267,257,1,0,0,0,267,258,1,0,0,0,267,259,1,0,0,0,267,260,
        1,0,0,0,267,261,1,0,0,0,267,262,1,0,0,0,267,263,1,0,0,0,267,264,
        1,0,0,0,267,265,1,0,0,0,267,266,1,0,0,0,268,272,1,0,0,0,269,271,
        3,86,43,0,270,269,1,0,0,0,271,274,1,0,0,0,272,270,1,0,0,0,272,273,
        1,0,0,0,273,276,1,0,0,0,274,272,1,0,0,0,275,267,1,0,0,0,276,279,
        1,0,0,0,277,275,1,0,0,0,277,278,1,0,0,0,278,280,1,0,0,0,279,277,
        1,0,0,0,280,281,5,41,0,0,281,282,3,22,11,0,282,283,5,7,0,0,283,284,
        5,44,0,0,284,285,5,12,0,0,285,286,5,41,0,0,286,13,1,0,0,0,287,288,
        5,7,0,0,288,292,5,13,0,0,289,291,3,86,43,0,290,289,1,0,0,0,291,294,
        1,0,0,0,292,290,1,0,0,0,292,293,1,0,0,0,293,314,1,0,0,0,294,292,
        1,0,0,0,295,305,3,58,29,0,296,305,3,60,30,0,297,305,3,62,31,0,298,
        305,3,64,32,0,299,305,3,66,33,0,300,305,3,68,34,0,301,305,3,70,35,
        0,302,305,3,34,17,0,303,305,3,80,40,0,304,295,1,0,0,0,304,296,1,
        0,0,0,304,297,1,0,0,0,304,298,1,0,0,0,304,299,1,0,0,0,304,300,1,
        0,0,0,304,301,1,0,0,0,304,302,1,0,0,0,304,303,1,0,0,0,305,309,1,
        0,0,0,306,308,3,86,43,0,307,306,1,0,0,0,308,311,1,0,0,0,309,307,
        1,0,0,0,309,310,1,0,0,0,310,313,1,0,0,0,311,309,1,0,0,0,312,304,
        1,0,0,0,313,316,1,0,0,0,314,312,1,0,0,0,314,315,1,0,0,0,315,317,
        1,0,0,0,316,314,1,0,0,0,317,318,5,41,0,0,318,319,3,22,11,0,319,320,
        5,7,0,0,320,321,5,44,0,0,321,322,5,13,0,0,322,323,5,41,0,0,323,15,
        1,0,0,0,324,325,5,7,0,0,325,329,5,14,0,0,326,328,3,86,43,0,327,326,
        1,0,0,0,328,331,1,0,0,0,329,327,1,0,0,0,329,330,1,0,0,0,330,348,
        1,0,0,0,331,329,1,0,0,0,332,339,3,72,36,0,333,339,3,74,37,0,334,
        339,3,76,38,0,335,339,3,78,39,0,336,339,3,34,17,0,337,339,3,80,40,
        0,338,332,1,0,0,0,338,333,1,0,0,0,338,334,1,0,0,0,338,335,1,0,0,
        0,338,336,1,0,0,0,338,337,1,0,0,0,339,343,1,0,0,0,340,342,3,86,43,
        0,341,340,1,0,0,0,342,345,1,0,0,0,343,341,1,0,0,0,343,344,1,0,0,
        0,344,347,1,0,0,0,345,343,1,0,0,0,346,338,1,0,0,0,347,350,1,0,0,
        0,348,346,1,0,0,0,348,349,1,0,0,0,349,351,1,0,0,0,350,348,1,0,0,
        0,351,352,5,43,0,0,352,17,1,0,0,0,353,354,5,7,0,0,354,355,5,15,0,
        0,355,356,3,36,18,0,356,357,5,43,0,0,357,19,1,0,0,0,358,360,3,84,
        42,0,359,358,1,0,0,0,359,360,1,0,0,0,360,374,1,0,0,0,361,368,3,12,
        6,0,362,368,3,14,7,0,363,368,3,16,8,0,364,368,3,18,9,0,365,368,3,
        32,16,0,366,368,3,34,17,0,367,361,1,0,0,0,367,362,1,0,0,0,367,363,
        1,0,0,0,367,364,1,0,0,0,367,365,1,0,0,0,367,366,1,0,0,0,368,370,
        1,0,0,0,369,371,3,84,42,0,370,369,1,0,0,0,370,371,1,0,0,0,371,373,
        1,0,0,0,372,367,1,0,0,0,373,376,1,0,0,0,374,372,1,0,0,0,374,375,
        1,0,0,0,375,21,1,0,0,0,376,374,1,0,0,0,377,379,3,84,42,0,378,377,
        1,0,0,0,378,379,1,0,0,0,379,392,1,0,0,0,380,386,3,24,12,0,381,386,
        3,26,13,0,382,386,3,28,14,0,383,386,3,30,15,0,384,386,5,1,0,0,385,
        380,1,0,0,0,385,381,1,0,0,0,385,382,1,0,0,0,385,383,1,0,0,0,385,
        384,1,0,0,0,386,388,1,0,0,0,387,389,3,84,42,0,388,387,1,0,0,0,388,
        389,1,0,0,0,389,391,1,0,0,0,390,385,1,0,0,0,391,394,1,0,0,0,392,
        390,1,0,0,0,392,393,1,0,0,0,393,23,1,0,0,0,394,392,1,0,0,0,395,396,
        5,7,0,0,396,397,5,16,0,0,397,398,3,36,18,0,398,399,5,41,0,0,399,
        400,3,4,2,0,400,401,5,7,0,0,401,402,5,44,0,0,402,403,5,16,0,0,403,
        404,5,41,0,0,404,25,1,0,0,0,405,406,5,7,0,0,406,407,5,17,0,0,407,
        408,3,36,18,0,408,409,5,41,0,0,409,410,3,4,2,0,410,411,5,7,0,0,411,
        412,5,44,0,0,412,413,5,17,0,0,413,414,5,41,0,0,414,27,1,0,0,0,415,
        416,5,7,0,0,416,417,5,18,0,0,417,418,3,36,18,0,418,419,5,41,0,0,
        419,420,3,4,2,0,420,421,5,7,0,0,421,422,5,44,0,0,422,423,5,18,0,
        0,423,424,5,41,0,0,424,29,1,0,0,0,425,426,5,7,0,0,426,427,5,19,0,
        0,427,428,3,36,18,0,428,429,5,41,0,0,429,430,3,4,2,0,430,431,5,7,
        0,0,431,432,5,44,0,0,432,433,5,19,0,0,433,434,5,41,0,0,434,31,1,
        0,0,0,435,436,7,0,0,0,436,33,1,0,0,0,437,438,7,1,0,0,438,35,1,0,
        0,0,439,441,3,86,43,0,440,439,1,0,0,0,441,444,1,0,0,0,442,440,1,
        0,0,0,442,443,1,0,0,0,443,457,1,0,0,0,444,442,1,0,0,0,445,448,3,
        34,17,0,446,448,3,80,40,0,447,445,1,0,0,0,447,446,1,0,0,0,448,452,
        1,0,0,0,449,451,3,86,43,0,450,449,1,0,0,0,451,454,1,0,0,0,452,450,
        1,0,0,0,452,453,1,0,0,0,453,456,1,0,0,0,454,452,1,0,0,0,455,447,
        1,0,0,0,456,459,1,0,0,0,457,455,1,0,0,0,457,458,1,0,0,0,458,37,1,
        0,0,0,459,457,1,0,0,0,460,461,5,20,0,0,461,462,5,45,0,0,462,463,
        5,46,0,0,463,39,1,0,0,0,464,465,5,21,0,0,465,466,5,45,0,0,466,467,
        5,46,0,0,467,41,1,0,0,0,468,469,5,22,0,0,469,470,5,45,0,0,470,471,
        5,46,0,0,471,43,1,0,0,0,472,473,5,23,0,0,473,474,5,45,0,0,474,475,
        5,46,0,0,475,45,1,0,0,0,476,477,5,24,0,0,477,478,5,45,0,0,478,479,
        5,46,0,0,479,47,1,0,0,0,480,481,5,25,0,0,481,482,5,45,0,0,482,483,
        5,46,0,0,483,49,1,0,0,0,484,485,5,26,0,0,485,486,5,45,0,0,486,487,
        5,46,0,0,487,51,1,0,0,0,488,489,5,29,0,0,489,490,5,45,0,0,490,491,
        5,46,0,0,491,53,1,0,0,0,492,493,5,30,0,0,493,494,5,45,0,0,494,495,
        5,46,0,0,495,55,1,0,0,0,496,497,5,37,0,0,497,498,5,45,0,0,498,499,
        5,46,0,0,499,57,1,0,0,0,500,501,5,27,0,0,501,502,5,45,0,0,502,503,
        5,46,0,0,503,59,1,0,0,0,504,505,5,28,0,0,505,506,5,45,0,0,506,507,
        5,46,0,0,507,61,1,0,0,0,508,509,5,32,0,0,509,510,5,45,0,0,510,511,
        5,46,0,0,511,63,1,0,0,0,512,513,5,33,0,0,513,514,5,45,0,0,514,515,
        5,46,0,0,515,65,1,0,0,0,516,517,5,31,0,0,517,518,5,45,0,0,518,519,
        5,46,0,0,519,67,1,0,0,0,520,521,5,40,0,0,521,522,5,45,0,0,522,523,
        5,46,0,0,523,69,1,0,0,0,524,525,5,39,0,0,525,526,5,45,0,0,526,527,
        5,46,0,0,527,71,1,0,0,0,528,529,5,34,0,0,529,530,5,45,0,0,530,531,
        5,46,0,0,531,73,1,0,0,0,532,533,5,36,0,0,533,534,5,45,0,0,534,535,
        5,46,0,0,535,75,1,0,0,0,536,537,5,38,0,0,537,538,5,45,0,0,538,539,
        5,46,0,0,539,77,1,0,0,0,540,541,5,35,0,0,541,542,5,45,0,0,542,543,
        5,46,0,0,543,79,1,0,0,0,544,545,5,47,0,0,545,546,5,45,0,0,546,547,
        5,46,0,0,547,81,1,0,0,0,548,549,5,50,0,0,549,550,5,45,0,0,550,551,
        5,49,0,0,551,552,5,53,0,0,552,557,5,49,0,0,553,554,5,50,0,0,554,
        555,5,45,0,0,555,557,5,46,0,0,556,548,1,0,0,0,556,553,1,0,0,0,557,
        83,1,0,0,0,558,559,7,2,0,0,559,85,1,0,0,0,560,561,7,3,0,0,561,87,
        1,0,0,0,50,89,94,101,110,116,121,124,128,136,151,155,162,168,172,
        177,183,188,194,199,203,207,220,229,234,239,254,267,272,277,292,
        304,309,314,329,338,343,348,359,367,370,374,378,385,388,392,442,
        447,452,457,556
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
                     "'>'", "<INVALID>", "'/>'", "'/'", "'='", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'\"'", "'uniqueID'", "'dao'" ]

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
                      "EQUALS", "STRING", "Name", "S", "DOUBLE_TICK", "UNIQUEID_LITERAL", 
                      "UNIQUEID_PREFIX", "UUIDV4", "UNIQUEID", "PI" ]

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
    RULE_comments_and_stuff = 17
    RULE_set_of_attributes = 18
    RULE_dao_id = 19
    RULE_dao_name = 20
    RULE_mission_statement = 21
    RULE_hierarchical_inheritance = 22
    RULE_role_id = 23
    RULE_role_name = 24
    RULE_role_assignment_method = 25
    RULE_n_agent_min = 26
    RULE_n_agent_max = 27
    RULE_agent_type = 28
    RULE_committee_id = 29
    RULE_committee_description = 30
    RULE_voting_condition = 31
    RULE_proposal_condition = 32
    RULE_decision_making_method = 33
    RULE_aggregation_level = 34
    RULE_federation_level = 35
    RULE_permission_id = 36
    RULE_allowed_action = 37
    RULE_permission_type = 38
    RULE_ref_gov_area = 39
    RULE_attribute = 40
    RULE_unique_id = 41
    RULE_chardata = 42
    RULE_misc = 43

    ruleNames =  [ "document", "prolog", "content", "element", "diagram", 
                   "dao", "role", "committee", "permission", "gov", "daocontent", 
                   "relations", "associated_to", "controlled_by", "aggregates", 
                   "federates_into", "reference", "comments_and_stuff", 
                   "set_of_attributes", "dao_id", "dao_name", "mission_statement", 
                   "hierarchical_inheritance", "role_id", "role_name", "role_assignment_method", 
                   "n_agent_min", "n_agent_max", "agent_type", "committee_id", 
                   "committee_description", "voting_condition", "proposal_condition", 
                   "decision_making_method", "aggregation_level", "federation_level", 
                   "permission_id", "allowed_action", "permission_type", 
                   "ref_gov_area", "attribute", "unique_id", "chardata", 
                   "misc" ]

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
    DOUBLE_TICK=49
    UNIQUEID_LITERAL=50
    UNIQUEID_PREFIX=51
    UUIDV4=52
    UNIQUEID=53
    PI=54

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDocument" ):
                listener.enterDocument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDocument" ):
                listener.exitDocument(self)

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
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 88
                self.prolog()


            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 18014398509482050) != 0):
                self.state = 91
                self.misc()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
            self.diagram()
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 18014398509482050) != 0):
                self.state = 98
                self.misc()
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 104
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProlog" ):
                listener.enterProlog(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProlog" ):
                listener.exitProlog(self)

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
            self.state = 106
            self.match(XMLParser.XMLDeclOpen)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==47:
                self.state = 107
                self.attribute()
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 113
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


        def comments_and_stuff(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Comments_and_stuffContext)
            else:
                return self.getTypedRuleContext(XMLParser.Comments_and_stuffContext,i)


        def getRuleIndex(self):
            return XMLParser.RULE_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContent" ):
                listener.enterContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContent" ):
                listener.exitContent(self)

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
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6 or _la==9:
                self.state = 115
                self.chardata()


            self.state = 128
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 121
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [7]:
                        self.state = 118
                        self.element()
                        pass
                    elif token in [4, 5]:
                        self.state = 119
                        self.reference()
                        pass
                    elif token in [1, 2, 54]:
                        self.state = 120
                        self.comments_and_stuff()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 124
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==6 or _la==9:
                        self.state = 123
                        self.chardata()

             
                self.state = 130
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)

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
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.match(XMLParser.OPEN)
                self.state = 132
                self.match(XMLParser.Name)
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==47:
                    self.state = 133
                    self.attribute()
                    self.state = 138
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 139
                self.match(XMLParser.CLOSE)
                self.state = 140
                self.content()
                self.state = 141
                self.match(XMLParser.OPEN)
                self.state = 142
                self.match(XMLParser.SLASH)
                self.state = 143
                self.match(XMLParser.Name)
                self.state = 144
                self.match(XMLParser.CLOSE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.match(XMLParser.OPEN)
                self.state = 147
                self.match(XMLParser.Name)
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==47:
                    self.state = 148
                    self.attribute()
                    self.state = 153
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 154
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


        def unique_id(self):
            return self.getTypedRuleContext(XMLParser.Unique_idContext,0)


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


        def comments_and_stuff(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Comments_and_stuffContext)
            else:
                return self.getTypedRuleContext(XMLParser.Comments_and_stuffContext,i)


        def getRuleIndex(self):
            return XMLParser.RULE_diagram

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiagram" ):
                listener.enterDiagram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiagram" ):
                listener.exitDiagram(self)

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
            self.state = 157
            self.match(XMLParser.OPEN)
            self.state = 158
            self.match(XMLParser.DIAGRAM)
            self.state = 162
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 159
                    self.misc() 
                self.state = 164
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==47:
                    self.state = 165
                    self.attribute()
                    self.state = 170
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 171
                self.unique_id()


            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==47:
                self.state = 174
                self.attribute()
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 18014398509482050) != 0):
                self.state = 180
                self.misc()
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 186
            self.match(XMLParser.CLOSE)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6 or _la==9:
                self.state = 187
                self.chardata()


            self.state = 207
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 194
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [7]:
                        self.state = 190
                        self.dao()
                        pass
                    elif token in [4, 5]:
                        self.state = 191
                        self.reference()
                        pass
                    elif token in [1, 2, 54]:
                        self.state = 192
                        self.comments_and_stuff()
                        pass
                    elif token in [47]:
                        self.state = 193
                        self.attribute()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 199
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 196
                            self.misc() 
                        self.state = 201
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

                    self.state = 203
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==6 or _la==9:
                        self.state = 202
                        self.chardata()

             
                self.state = 209
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

            self.state = 210
            self.match(XMLParser.OPEN)
            self.state = 211
            self.match(XMLParser.SLASH)
            self.state = 212
            self.match(XMLParser.DIAGRAM)
            self.state = 213
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


        def dao_id(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Dao_idContext)
            else:
                return self.getTypedRuleContext(XMLParser.Dao_idContext,i)


        def dao_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Dao_nameContext)
            else:
                return self.getTypedRuleContext(XMLParser.Dao_nameContext,i)


        def mission_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Mission_statementContext)
            else:
                return self.getTypedRuleContext(XMLParser.Mission_statementContext,i)


        def hierarchical_inheritance(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Hierarchical_inheritanceContext)
            else:
                return self.getTypedRuleContext(XMLParser.Hierarchical_inheritanceContext,i)


        def comments_and_stuff(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Comments_and_stuffContext)
            else:
                return self.getTypedRuleContext(XMLParser.Comments_and_stuffContext,i)


        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(XMLParser.AttributeContext,i)


        def getRuleIndex(self):
            return XMLParser.RULE_dao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDao" ):
                listener.enterDao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDao" ):
                listener.exitDao(self)

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
            self.state = 215
            self.match(XMLParser.OPEN)
            self.state = 216
            self.match(XMLParser.DAO)
            self.state = 220
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 217
                    self.misc() 
                self.state = 222
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 18155136013565958) != 0):
                self.state = 229
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [20]:
                    self.state = 223
                    self.dao_id()
                    pass
                elif token in [21]:
                    self.state = 224
                    self.dao_name()
                    pass
                elif token in [22]:
                    self.state = 225
                    self.mission_statement()
                    pass
                elif token in [23]:
                    self.state = 226
                    self.hierarchical_inheritance()
                    pass
                elif token in [1, 2, 54]:
                    self.state = 227
                    self.comments_and_stuff()
                    pass
                elif token in [47]:
                    self.state = 228
                    self.attribute()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 234
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 231
                        self.misc() 
                    self.state = 236
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

                self.state = 241
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 242
            self.match(XMLParser.CLOSE)
            self.state = 243
            self.daocontent()
            self.state = 244
            self.match(XMLParser.OPEN)
            self.state = 245
            self.match(XMLParser.SLASH)
            self.state = 246
            self.match(XMLParser.DAO)
            self.state = 247
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


        def role_id(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Role_idContext)
            else:
                return self.getTypedRuleContext(XMLParser.Role_idContext,i)


        def role_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Role_nameContext)
            else:
                return self.getTypedRuleContext(XMLParser.Role_nameContext,i)


        def role_assignment_method(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Role_assignment_methodContext)
            else:
                return self.getTypedRuleContext(XMLParser.Role_assignment_methodContext,i)


        def n_agent_min(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.N_agent_minContext)
            else:
                return self.getTypedRuleContext(XMLParser.N_agent_minContext,i)


        def n_agent_max(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.N_agent_maxContext)
            else:
                return self.getTypedRuleContext(XMLParser.N_agent_maxContext,i)


        def agent_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Agent_typeContext)
            else:
                return self.getTypedRuleContext(XMLParser.Agent_typeContext,i)


        def aggregation_level(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Aggregation_levelContext)
            else:
                return self.getTypedRuleContext(XMLParser.Aggregation_levelContext,i)


        def federation_level(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Federation_levelContext)
            else:
                return self.getTypedRuleContext(XMLParser.Federation_levelContext,i)


        def comments_and_stuff(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Comments_and_stuffContext)
            else:
                return self.getTypedRuleContext(XMLParser.Comments_and_stuffContext,i)


        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(XMLParser.AttributeContext,i)


        def getRuleIndex(self):
            return XMLParser.RULE_role

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRole" ):
                listener.enterRole(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRole" ):
                listener.exitRole(self)

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
            self.state = 249
            self.match(XMLParser.OPEN)
            self.state = 250
            self.match(XMLParser.ROLE)
            self.state = 254
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 251
                    self.misc() 
                self.state = 256
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 18156924432285702) != 0):
                self.state = 267
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [24]:
                    self.state = 257
                    self.role_id()
                    pass
                elif token in [25]:
                    self.state = 258
                    self.role_name()
                    pass
                elif token in [26]:
                    self.state = 259
                    self.role_assignment_method()
                    pass
                elif token in [29]:
                    self.state = 260
                    self.n_agent_min()
                    pass
                elif token in [30]:
                    self.state = 261
                    self.n_agent_max()
                    pass
                elif token in [37]:
                    self.state = 262
                    self.agent_type()
                    pass
                elif token in [40]:
                    self.state = 263
                    self.aggregation_level()
                    pass
                elif token in [39]:
                    self.state = 264
                    self.federation_level()
                    pass
                elif token in [1, 2, 54]:
                    self.state = 265
                    self.comments_and_stuff()
                    pass
                elif token in [47]:
                    self.state = 266
                    self.attribute()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 272
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 269
                        self.misc() 
                    self.state = 274
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

                self.state = 279
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 280
            self.match(XMLParser.CLOSE)
            self.state = 281
            self.relations()
            self.state = 282
            self.match(XMLParser.OPEN)
            self.state = 283
            self.match(XMLParser.SLASH)
            self.state = 284
            self.match(XMLParser.ROLE)
            self.state = 285
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


        def committee_id(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Committee_idContext)
            else:
                return self.getTypedRuleContext(XMLParser.Committee_idContext,i)


        def committee_description(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Committee_descriptionContext)
            else:
                return self.getTypedRuleContext(XMLParser.Committee_descriptionContext,i)


        def voting_condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Voting_conditionContext)
            else:
                return self.getTypedRuleContext(XMLParser.Voting_conditionContext,i)


        def proposal_condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Proposal_conditionContext)
            else:
                return self.getTypedRuleContext(XMLParser.Proposal_conditionContext,i)


        def decision_making_method(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Decision_making_methodContext)
            else:
                return self.getTypedRuleContext(XMLParser.Decision_making_methodContext,i)


        def aggregation_level(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Aggregation_levelContext)
            else:
                return self.getTypedRuleContext(XMLParser.Aggregation_levelContext,i)


        def federation_level(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Federation_levelContext)
            else:
                return self.getTypedRuleContext(XMLParser.Federation_levelContext,i)


        def comments_and_stuff(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Comments_and_stuffContext)
            else:
                return self.getTypedRuleContext(XMLParser.Comments_and_stuffContext,i)


        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(XMLParser.AttributeContext,i)


        def getRuleIndex(self):
            return XMLParser.RULE_committee

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommittee" ):
                listener.enterCommittee(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommittee" ):
                listener.exitCommittee(self)

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
            self.state = 287
            self.match(XMLParser.OPEN)
            self.state = 288
            self.match(XMLParser.COMMITTEE)
            self.state = 292
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 289
                    self.misc() 
                self.state = 294
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 18156800700317702) != 0):
                self.state = 304
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [27]:
                    self.state = 295
                    self.committee_id()
                    pass
                elif token in [28]:
                    self.state = 296
                    self.committee_description()
                    pass
                elif token in [32]:
                    self.state = 297
                    self.voting_condition()
                    pass
                elif token in [33]:
                    self.state = 298
                    self.proposal_condition()
                    pass
                elif token in [31]:
                    self.state = 299
                    self.decision_making_method()
                    pass
                elif token in [40]:
                    self.state = 300
                    self.aggregation_level()
                    pass
                elif token in [39]:
                    self.state = 301
                    self.federation_level()
                    pass
                elif token in [1, 2, 54]:
                    self.state = 302
                    self.comments_and_stuff()
                    pass
                elif token in [47]:
                    self.state = 303
                    self.attribute()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 309
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 306
                        self.misc() 
                    self.state = 311
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

                self.state = 316
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 317
            self.match(XMLParser.CLOSE)
            self.state = 318
            self.relations()
            self.state = 319
            self.match(XMLParser.OPEN)
            self.state = 320
            self.match(XMLParser.SLASH)
            self.state = 321
            self.match(XMLParser.COMMITTEE)
            self.state = 322
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

        def SLASH_CLOSE(self):
            return self.getToken(XMLParser.SLASH_CLOSE, 0)

        def misc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.MiscContext)
            else:
                return self.getTypedRuleContext(XMLParser.MiscContext,i)


        def permission_id(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Permission_idContext)
            else:
                return self.getTypedRuleContext(XMLParser.Permission_idContext,i)


        def allowed_action(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Allowed_actionContext)
            else:
                return self.getTypedRuleContext(XMLParser.Allowed_actionContext,i)


        def permission_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Permission_typeContext)
            else:
                return self.getTypedRuleContext(XMLParser.Permission_typeContext,i)


        def ref_gov_area(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Ref_gov_areaContext)
            else:
                return self.getTypedRuleContext(XMLParser.Ref_gov_areaContext,i)


        def comments_and_stuff(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Comments_and_stuffContext)
            else:
                return self.getTypedRuleContext(XMLParser.Comments_and_stuffContext,i)


        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(XMLParser.AttributeContext,i)


        def getRuleIndex(self):
            return XMLParser.RULE_permission

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPermission" ):
                listener.enterPermission(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPermission" ):
                listener.exitPermission(self)

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
            self.state = 324
            self.match(XMLParser.OPEN)
            self.state = 325
            self.match(XMLParser.PERMISSION)
            self.state = 329
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 326
                    self.misc() 
                self.state = 331
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

            self.state = 348
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 18155531134828550) != 0):
                self.state = 338
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [34]:
                    self.state = 332
                    self.permission_id()
                    pass
                elif token in [36]:
                    self.state = 333
                    self.allowed_action()
                    pass
                elif token in [38]:
                    self.state = 334
                    self.permission_type()
                    pass
                elif token in [35]:
                    self.state = 335
                    self.ref_gov_area()
                    pass
                elif token in [1, 2, 54]:
                    self.state = 336
                    self.comments_and_stuff()
                    pass
                elif token in [47]:
                    self.state = 337
                    self.attribute()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 343
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 340
                        self.misc() 
                    self.state = 345
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

                self.state = 350
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 351
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

        def set_of_attributes(self):
            return self.getTypedRuleContext(XMLParser.Set_of_attributesContext,0)


        def SLASH_CLOSE(self):
            return self.getToken(XMLParser.SLASH_CLOSE, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_gov

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGov" ):
                listener.enterGov(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGov" ):
                listener.exitGov(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGov" ):
                return visitor.visitGov(self)
            else:
                return visitor.visitChildren(self)




    def gov(self):

        localctx = XMLParser.GovContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_gov)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(XMLParser.OPEN)
            self.state = 354
            self.match(XMLParser.GOV)
            self.state = 355
            self.set_of_attributes()
            self.state = 356
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


        def comments_and_stuff(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Comments_and_stuffContext)
            else:
                return self.getTypedRuleContext(XMLParser.Comments_and_stuffContext,i)


        def getRuleIndex(self):
            return XMLParser.RULE_daocontent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDaocontent" ):
                listener.enterDaocontent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDaocontent" ):
                listener.exitDaocontent(self)

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
            self.state = 359
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6 or _la==9:
                self.state = 358
                self.chardata()


            self.state = 374
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 367
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                    if la_ == 1:
                        self.state = 361
                        self.role()
                        pass

                    elif la_ == 2:
                        self.state = 362
                        self.committee()
                        pass

                    elif la_ == 3:
                        self.state = 363
                        self.permission()
                        pass

                    elif la_ == 4:
                        self.state = 364
                        self.gov()
                        pass

                    elif la_ == 5:
                        self.state = 365
                        self.reference()
                        pass

                    elif la_ == 6:
                        self.state = 366
                        self.comments_and_stuff()
                        pass


                    self.state = 370
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==6 or _la==9:
                        self.state = 369
                        self.chardata()

             
                self.state = 376
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelations" ):
                listener.enterRelations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelations" ):
                listener.exitRelations(self)

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
            self.state = 378
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6 or _la==9:
                self.state = 377
                self.chardata()


            self.state = 392
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 385
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                    if la_ == 1:
                        self.state = 380
                        self.associated_to()
                        pass

                    elif la_ == 2:
                        self.state = 381
                        self.controlled_by()
                        pass

                    elif la_ == 3:
                        self.state = 382
                        self.aggregates()
                        pass

                    elif la_ == 4:
                        self.state = 383
                        self.federates_into()
                        pass

                    elif la_ == 5:
                        self.state = 384
                        self.match(XMLParser.COMMENT)
                        pass


                    self.state = 388
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==6 or _la==9:
                        self.state = 387
                        self.chardata()

             
                self.state = 394
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

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

        def set_of_attributes(self):
            return self.getTypedRuleContext(XMLParser.Set_of_attributesContext,0)


        def CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.CLOSE)
            else:
                return self.getToken(XMLParser.CLOSE, i)

        def content(self):
            return self.getTypedRuleContext(XMLParser.ContentContext,0)


        def SLASH(self):
            return self.getToken(XMLParser.SLASH, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_associated_to

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssociated_to" ):
                listener.enterAssociated_to(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssociated_to" ):
                listener.exitAssociated_to(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssociated_to" ):
                return visitor.visitAssociated_to(self)
            else:
                return visitor.visitChildren(self)




    def associated_to(self):

        localctx = XMLParser.Associated_toContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_associated_to)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.match(XMLParser.OPEN)
            self.state = 396
            self.match(XMLParser.ASSOCIATION)
            self.state = 397
            self.set_of_attributes()
            self.state = 398
            self.match(XMLParser.CLOSE)
            self.state = 399
            self.content()
            self.state = 400
            self.match(XMLParser.OPEN)
            self.state = 401
            self.match(XMLParser.SLASH)
            self.state = 402
            self.match(XMLParser.ASSOCIATION)
            self.state = 403
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

        def set_of_attributes(self):
            return self.getTypedRuleContext(XMLParser.Set_of_attributesContext,0)


        def CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.CLOSE)
            else:
                return self.getToken(XMLParser.CLOSE, i)

        def content(self):
            return self.getTypedRuleContext(XMLParser.ContentContext,0)


        def SLASH(self):
            return self.getToken(XMLParser.SLASH, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_controlled_by

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterControlled_by" ):
                listener.enterControlled_by(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitControlled_by" ):
                listener.exitControlled_by(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitControlled_by" ):
                return visitor.visitControlled_by(self)
            else:
                return visitor.visitChildren(self)




    def controlled_by(self):

        localctx = XMLParser.Controlled_byContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_controlled_by)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(XMLParser.OPEN)
            self.state = 406
            self.match(XMLParser.CONTROL)
            self.state = 407
            self.set_of_attributes()
            self.state = 408
            self.match(XMLParser.CLOSE)
            self.state = 409
            self.content()
            self.state = 410
            self.match(XMLParser.OPEN)
            self.state = 411
            self.match(XMLParser.SLASH)
            self.state = 412
            self.match(XMLParser.CONTROL)
            self.state = 413
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

        def set_of_attributes(self):
            return self.getTypedRuleContext(XMLParser.Set_of_attributesContext,0)


        def CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.CLOSE)
            else:
                return self.getToken(XMLParser.CLOSE, i)

        def content(self):
            return self.getTypedRuleContext(XMLParser.ContentContext,0)


        def SLASH(self):
            return self.getToken(XMLParser.SLASH, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_aggregates

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregates" ):
                listener.enterAggregates(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregates" ):
                listener.exitAggregates(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregates" ):
                return visitor.visitAggregates(self)
            else:
                return visitor.visitChildren(self)




    def aggregates(self):

        localctx = XMLParser.AggregatesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_aggregates)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(XMLParser.OPEN)
            self.state = 416
            self.match(XMLParser.AGGREGATES)
            self.state = 417
            self.set_of_attributes()
            self.state = 418
            self.match(XMLParser.CLOSE)
            self.state = 419
            self.content()
            self.state = 420
            self.match(XMLParser.OPEN)
            self.state = 421
            self.match(XMLParser.SLASH)
            self.state = 422
            self.match(XMLParser.AGGREGATES)
            self.state = 423
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

        def set_of_attributes(self):
            return self.getTypedRuleContext(XMLParser.Set_of_attributesContext,0)


        def CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.CLOSE)
            else:
                return self.getToken(XMLParser.CLOSE, i)

        def content(self):
            return self.getTypedRuleContext(XMLParser.ContentContext,0)


        def SLASH(self):
            return self.getToken(XMLParser.SLASH, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_federates_into

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFederates_into" ):
                listener.enterFederates_into(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFederates_into" ):
                listener.exitFederates_into(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFederates_into" ):
                return visitor.visitFederates_into(self)
            else:
                return visitor.visitChildren(self)




    def federates_into(self):

        localctx = XMLParser.Federates_intoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_federates_into)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.match(XMLParser.OPEN)
            self.state = 426
            self.match(XMLParser.FEDERATES)
            self.state = 427
            self.set_of_attributes()
            self.state = 428
            self.match(XMLParser.CLOSE)
            self.state = 429
            self.content()
            self.state = 430
            self.match(XMLParser.OPEN)
            self.state = 431
            self.match(XMLParser.SLASH)
            self.state = 432
            self.match(XMLParser.FEDERATES)
            self.state = 433
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReference" ):
                listener.enterReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReference" ):
                listener.exitReference(self)

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
            self.state = 435
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


    class Comments_and_stuffContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CDATA(self):
            return self.getToken(XMLParser.CDATA, 0)

        def PI(self):
            return self.getToken(XMLParser.PI, 0)

        def COMMENT(self):
            return self.getToken(XMLParser.COMMENT, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_comments_and_stuff

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComments_and_stuff" ):
                listener.enterComments_and_stuff(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComments_and_stuff" ):
                listener.exitComments_and_stuff(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComments_and_stuff" ):
                return visitor.visitComments_and_stuff(self)
            else:
                return visitor.visitChildren(self)




    def comments_and_stuff(self):

        localctx = XMLParser.Comments_and_stuffContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_comments_and_stuff)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 18014398509481990) != 0)):
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


    class Set_of_attributesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def misc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.MiscContext)
            else:
                return self.getTypedRuleContext(XMLParser.MiscContext,i)


        def comments_and_stuff(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.Comments_and_stuffContext)
            else:
                return self.getTypedRuleContext(XMLParser.Comments_and_stuffContext,i)


        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(XMLParser.AttributeContext,i)


        def getRuleIndex(self):
            return XMLParser.RULE_set_of_attributes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSet_of_attributes" ):
                listener.enterSet_of_attributes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSet_of_attributes" ):
                listener.exitSet_of_attributes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSet_of_attributes" ):
                return visitor.visitSet_of_attributes(self)
            else:
                return visitor.visitChildren(self)




    def set_of_attributes(self):

        localctx = XMLParser.Set_of_attributesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_set_of_attributes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 439
                    self.misc() 
                self.state = 444
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

            self.state = 457
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 18155135997837318) != 0):
                self.state = 447
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 2, 54]:
                    self.state = 445
                    self.comments_and_stuff()
                    pass
                elif token in [47]:
                    self.state = 446
                    self.attribute()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 452
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 449
                        self.misc() 
                    self.state = 454
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

                self.state = 459
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDao_id" ):
                listener.enterDao_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDao_id" ):
                listener.exitDao_id(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDao_id" ):
                return visitor.visitDao_id(self)
            else:
                return visitor.visitChildren(self)




    def dao_id(self):

        localctx = XMLParser.Dao_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_dao_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.match(XMLParser.DAOID)
            self.state = 461
            self.match(XMLParser.EQUALS)
            self.state = 462
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDao_name" ):
                listener.enterDao_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDao_name" ):
                listener.exitDao_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDao_name" ):
                return visitor.visitDao_name(self)
            else:
                return visitor.visitChildren(self)




    def dao_name(self):

        localctx = XMLParser.Dao_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_dao_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            self.match(XMLParser.DAONAME)
            self.state = 465
            self.match(XMLParser.EQUALS)
            self.state = 466
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMission_statement" ):
                listener.enterMission_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMission_statement" ):
                listener.exitMission_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMission_statement" ):
                return visitor.visitMission_statement(self)
            else:
                return visitor.visitChildren(self)




    def mission_statement(self):

        localctx = XMLParser.Mission_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_mission_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.match(XMLParser.MISSIONSTATEMENT)
            self.state = 469
            self.match(XMLParser.EQUALS)
            self.state = 470
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHierarchical_inheritance" ):
                listener.enterHierarchical_inheritance(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHierarchical_inheritance" ):
                listener.exitHierarchical_inheritance(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHierarchical_inheritance" ):
                return visitor.visitHierarchical_inheritance(self)
            else:
                return visitor.visitChildren(self)




    def hierarchical_inheritance(self):

        localctx = XMLParser.Hierarchical_inheritanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_hierarchical_inheritance)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.match(XMLParser.HIERARCHICALINHERITANCE)
            self.state = 473
            self.match(XMLParser.EQUALS)
            self.state = 474
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRole_id" ):
                listener.enterRole_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRole_id" ):
                listener.exitRole_id(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRole_id" ):
                return visitor.visitRole_id(self)
            else:
                return visitor.visitChildren(self)




    def role_id(self):

        localctx = XMLParser.Role_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_role_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.match(XMLParser.ROLEID)
            self.state = 477
            self.match(XMLParser.EQUALS)
            self.state = 478
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRole_name" ):
                listener.enterRole_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRole_name" ):
                listener.exitRole_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRole_name" ):
                return visitor.visitRole_name(self)
            else:
                return visitor.visitChildren(self)




    def role_name(self):

        localctx = XMLParser.Role_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_role_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.match(XMLParser.ROLENAME)
            self.state = 481
            self.match(XMLParser.EQUALS)
            self.state = 482
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRole_assignment_method" ):
                listener.enterRole_assignment_method(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRole_assignment_method" ):
                listener.exitRole_assignment_method(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRole_assignment_method" ):
                return visitor.visitRole_assignment_method(self)
            else:
                return visitor.visitChildren(self)




    def role_assignment_method(self):

        localctx = XMLParser.Role_assignment_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_role_assignment_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self.match(XMLParser.ROLEASSIGNMENTMETHOD)
            self.state = 485
            self.match(XMLParser.EQUALS)
            self.state = 486
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterN_agent_min" ):
                listener.enterN_agent_min(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitN_agent_min" ):
                listener.exitN_agent_min(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitN_agent_min" ):
                return visitor.visitN_agent_min(self)
            else:
                return visitor.visitChildren(self)




    def n_agent_min(self):

        localctx = XMLParser.N_agent_minContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_n_agent_min)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.match(XMLParser.NAGENTMIN)
            self.state = 489
            self.match(XMLParser.EQUALS)
            self.state = 490
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterN_agent_max" ):
                listener.enterN_agent_max(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitN_agent_max" ):
                listener.exitN_agent_max(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitN_agent_max" ):
                return visitor.visitN_agent_max(self)
            else:
                return visitor.visitChildren(self)




    def n_agent_max(self):

        localctx = XMLParser.N_agent_maxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_n_agent_max)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            self.match(XMLParser.NAGENTMAX)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgent_type" ):
                listener.enterAgent_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgent_type" ):
                listener.exitAgent_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgent_type" ):
                return visitor.visitAgent_type(self)
            else:
                return visitor.visitChildren(self)




    def agent_type(self):

        localctx = XMLParser.Agent_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_agent_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
            self.match(XMLParser.AGENTTYPE)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommittee_id" ):
                listener.enterCommittee_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommittee_id" ):
                listener.exitCommittee_id(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommittee_id" ):
                return visitor.visitCommittee_id(self)
            else:
                return visitor.visitChildren(self)




    def committee_id(self):

        localctx = XMLParser.Committee_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_committee_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            self.match(XMLParser.COMMITTEEID)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommittee_description" ):
                listener.enterCommittee_description(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommittee_description" ):
                listener.exitCommittee_description(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommittee_description" ):
                return visitor.visitCommittee_description(self)
            else:
                return visitor.visitChildren(self)




    def committee_description(self):

        localctx = XMLParser.Committee_descriptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_committee_description)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.match(XMLParser.COMMITTEEDESCRIPTION)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVoting_condition" ):
                listener.enterVoting_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVoting_condition" ):
                listener.exitVoting_condition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVoting_condition" ):
                return visitor.visitVoting_condition(self)
            else:
                return visitor.visitChildren(self)




    def voting_condition(self):

        localctx = XMLParser.Voting_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_voting_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            self.match(XMLParser.VOTINGCONDITION)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProposal_condition" ):
                listener.enterProposal_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProposal_condition" ):
                listener.exitProposal_condition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProposal_condition" ):
                return visitor.visitProposal_condition(self)
            else:
                return visitor.visitChildren(self)




    def proposal_condition(self):

        localctx = XMLParser.Proposal_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_proposal_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
            self.match(XMLParser.PROPOSALCONDITION)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecision_making_method" ):
                listener.enterDecision_making_method(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecision_making_method" ):
                listener.exitDecision_making_method(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecision_making_method" ):
                return visitor.visitDecision_making_method(self)
            else:
                return visitor.visitChildren(self)




    def decision_making_method(self):

        localctx = XMLParser.Decision_making_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_decision_making_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            self.match(XMLParser.DMMETHOD)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregation_level" ):
                listener.enterAggregation_level(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregation_level" ):
                listener.exitAggregation_level(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregation_level" ):
                return visitor.visitAggregation_level(self)
            else:
                return visitor.visitChildren(self)




    def aggregation_level(self):

        localctx = XMLParser.Aggregation_levelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_aggregation_level)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self.match(XMLParser.AGGREGATIONLEVEL)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFederation_level" ):
                listener.enterFederation_level(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFederation_level" ):
                listener.exitFederation_level(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFederation_level" ):
                return visitor.visitFederation_level(self)
            else:
                return visitor.visitChildren(self)




    def federation_level(self):

        localctx = XMLParser.Federation_levelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_federation_level)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
            self.match(XMLParser.FEDERATIONLEVEL)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPermission_id" ):
                listener.enterPermission_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPermission_id" ):
                listener.exitPermission_id(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPermission_id" ):
                return visitor.visitPermission_id(self)
            else:
                return visitor.visitChildren(self)




    def permission_id(self):

        localctx = XMLParser.Permission_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_permission_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 528
            self.match(XMLParser.PERMISSIONID)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAllowed_action" ):
                listener.enterAllowed_action(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAllowed_action" ):
                listener.exitAllowed_action(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAllowed_action" ):
                return visitor.visitAllowed_action(self)
            else:
                return visitor.visitChildren(self)




    def allowed_action(self):

        localctx = XMLParser.Allowed_actionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_allowed_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
            self.match(XMLParser.ALLOWEDACTION)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPermission_type" ):
                listener.enterPermission_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPermission_type" ):
                listener.exitPermission_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPermission_type" ):
                return visitor.visitPermission_type(self)
            else:
                return visitor.visitChildren(self)




    def permission_type(self):

        localctx = XMLParser.Permission_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_permission_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self.match(XMLParser.PERMISSIONTYPE)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRef_gov_area" ):
                listener.enterRef_gov_area(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRef_gov_area" ):
                listener.exitRef_gov_area(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRef_gov_area" ):
                return visitor.visitRef_gov_area(self)
            else:
                return visitor.visitChildren(self)




    def ref_gov_area(self):

        localctx = XMLParser.Ref_gov_areaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_ref_gov_area)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 540
            self.match(XMLParser.REF_GOV_AREA)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = XMLParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
            self.match(XMLParser.Name)
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


    class Unique_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNIQUEID_LITERAL(self):
            return self.getToken(XMLParser.UNIQUEID_LITERAL, 0)

        def EQUALS(self):
            return self.getToken(XMLParser.EQUALS, 0)

        def DOUBLE_TICK(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.DOUBLE_TICK)
            else:
                return self.getToken(XMLParser.DOUBLE_TICK, i)

        def UNIQUEID(self):
            return self.getToken(XMLParser.UNIQUEID, 0)

        def STRING(self):
            return self.getToken(XMLParser.STRING, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_unique_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnique_id" ):
                listener.enterUnique_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnique_id" ):
                listener.exitUnique_id(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnique_id" ):
                return visitor.visitUnique_id(self)
            else:
                return visitor.visitChildren(self)




    def unique_id(self):

        localctx = XMLParser.Unique_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_unique_id)
        try:
            self.state = 556
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 548
                self.match(XMLParser.UNIQUEID_LITERAL)
                self.state = 549
                self.match(XMLParser.EQUALS)
                self.state = 550
                self.match(XMLParser.DOUBLE_TICK)
                self.state = 551
                self.match(XMLParser.UNIQUEID)
                self.state = 552
                self.match(XMLParser.DOUBLE_TICK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 553
                self.match(XMLParser.UNIQUEID_LITERAL)
                self.state = 554
                self.match(XMLParser.EQUALS)
                self.state = 555
                self.match(XMLParser.STRING)
                pass


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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChardata" ):
                listener.enterChardata(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChardata" ):
                listener.exitChardata(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChardata" ):
                return visitor.visitChardata(self)
            else:
                return visitor.visitChildren(self)




    def chardata(self):

        localctx = XMLParser.ChardataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_chardata)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 558
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMisc" ):
                listener.enterMisc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMisc" ):
                listener.exitMisc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMisc" ):
                return visitor.visitMisc(self)
            else:
                return visitor.visitChildren(self)




    def misc(self):

        localctx = XMLParser.MiscContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_misc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 560
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 18014398509482050) != 0)):
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





