import os
import re
import json
from collections import defaultdict

text_files = [
    './names_3110.txt', './names_707.txt', './names_322.txt', './names_7775.txt', './names_13633.txt',
    './names_1036.txt', './names_140.txt', './names_2973.txt', './names_4679.txt', './names_163.txt',
    './names_80.txt', './popular_python_repos.txt', './names_16364.txt', './names_4402.txt', './names_1073.txt',
    './names_4357.txt', './names_156.txt', './names_550.txt', './names_929.txt', './names_5489.txt',
    './names_770.txt', './names_161.txt', './names_430.txt', './names_3302.txt', './names_4284.txt',
    './names_548.txt', './names_1387.txt', './names_17272.txt', './names_4.txt', './names_261.txt',
    './names_55.txt', './names_1672.txt', './names_705.txt', './names_5670.txt', './names_6198.txt',
    './names_756.txt', './directory_size_report.txt', './names_11644.txt', './names_1512.txt', './names_118.txt',
    './names_1991.txt', './names_297.txt', './names_1363.txt', './names_2885.txt', './names_13404.txt',
    './names_1044.txt', './names_130.txt', './names_2286.txt', './names_275.txt', './names_10617.txt',
    './names_735.txt', './names_199.txt', './names_19.txt', './names_213.txt', './names_334.txt', './names_13.txt',
    './names_314.txt', './names_5981.txt', './names_9105.txt', './names_728.txt', './names_97.txt', './names_321.txt',
    './names_1413.txt', './names_96.txt', './names_3197.txt', './names_43.txt', './names_404.txt', './names_1276.txt',
    './names_332.txt', './names_10144.txt', './names_160.txt', './names_2419.txt', './names_8.txt', './names_2543.txt',
    './names_89.txt', './names_8374.txt', './names_60777.txt', './names_192.txt', './names_1658.txt', './names_1491.txt',
    './names_2557.txt', './names_467.txt', './names_797.txt', './names_868.txt', './names_1974.txt', './names_4065.txt',
    './names_1759.txt', './names_5982.txt', './names_478.txt', './names_235.txt', './names_2122.txt', './names_233.txt',
    './names_5507.txt', './names_4985.txt', './names_273.txt', './names_336.txt', './names_5923.txt', './names_5462.txt',
    './names_1480.txt', './names_214.txt', './names_185.txt', './names_1463.txt', './date_report.txt', './names_34252.txt',
    './names_1116.txt', './names_1809.txt', './names_13686.txt', './names_1325.txt', './names_2770.txt', './names_6.txt',
    './names_25607.txt', './names_1723.txt', './names_670.txt', './names_781.txt', './names_572.txt', './names_1101.txt',
    './names