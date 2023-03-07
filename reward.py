import math
import numpy as np



def get_racing_line_waypoints():
    return [[ 6.87774944,  3.66178751,  6.8198638 ,  3.13153791,  6.93563509,
         4.19203711,  6.78572867,  3.55837579],
       [ 6.62793398,  3.68915915,  6.56963015,  3.1589551 ,  6.68623781,
         4.21936321,  6.57618268,  3.62802675],
       [ 6.37814403,  3.71672738,  6.31942797,  3.18656898,  6.43686008,
         4.24688578,  6.35225069,  3.68473194],
       [ 6.12837696,  3.74448586,  6.06939793,  3.2143569 ,  6.187356  ,
         4.27461481,  6.11750611,  3.73049912],
       [ 5.87861609,  3.77230203,  5.81957102,  3.24218011,  5.93766117,
         4.30242395,  5.87537452,  3.76798065],
       [ 5.62885404,  3.80012298,  5.56979895,  3.27000189,  5.68790913,
         4.33024406,  5.62842761,  3.7995473 ],
       [ 5.37909055,  3.82794845,  5.32002497,  3.29782891,  5.43815613,
         4.35806799,  5.37909055,  3.82794845],
       [ 5.12932611,  3.85578048,  5.07025003,  3.3256619 ,  5.18840218,
         4.38589907,  5.12932611,  3.85578048],
       [ 4.87955999,  3.88361645,  4.82047415,  3.35349894,  4.93864584,
         4.41373396,  4.87955999,  3.88361645],
       [ 4.62979293,  3.91145754,  4.57069588,  3.38134098,  4.68888998,
         4.4415741 ,  4.62979293,  3.91145754],
       [ 4.38002443,  3.93930352,  4.32099295,  3.40917993,  4.43905592,
         4.46942711,  4.38002443,  3.93930352],
       [ 4.13024998,  3.96708345,  4.07152414,  3.43692589,  4.18897581,
         4.49724102,  4.13024998,  3.96708345],
       [ 3.88045847,  3.99464095,  3.82220793,  3.46443105,  3.93870902,
         4.52485085,  3.88045847,  3.99464095],
       [ 3.63065052,  4.02197158,  3.57288098,  3.49170899,  3.68842006,
         4.55223417,  3.63067603,  4.02190951],
       [ 3.38082492,  4.04907358,  3.32353592,  3.51875901,  3.43811393,
         4.57938814,  3.38120608,  4.04839112],
       [ 3.13098192,  4.07594955,  3.07417393,  3.54558301,  3.18778992,
         4.60631609,  3.13219221,  4.07358487],
       [ 2.88112247,  4.10259759,  2.82479596,  3.57218003,  2.93744898,
         4.63301516,  2.88379301,  4.09695573],
       [ 2.63124597,  4.12901807,  2.57532692,  3.598557  ,  2.68716502,
         4.65947914,  2.63617723,  4.11795792],
       [ 2.38135707,  4.15528047,  2.32468009,  3.6249001 ,  2.43803406,
         4.68566084,  2.38952529,  4.13603376],
       [ 2.13153148,  4.18241739,  2.07264304,  3.65227795,  2.19041991,
         4.71255684,  2.14403028,  4.15061211],
       [ 1.88179404,  4.21077311,  1.82033205,  3.68092608,  1.94325602,
         4.74062014,  1.89989825,  4.16110806],
       [ 1.63214499,  4.24034643,  1.56811297,  3.71080399,  1.69617701,
         4.76988888,  1.65739908,  4.1667745 ],
       [ 1.38258398,  4.27113748,  1.31598401,  3.74191189,  1.44918394,
         4.80036306,  1.41664143,  4.16735974],
       [ 1.133111  ,  4.30314708,  1.06394601,  3.77425003,  1.20227599,
         4.83204412,  1.17785161,  4.16227984],
       [ 0.88372681,  4.33637452,  0.8119998 ,  3.80781889,  0.95545381,
         4.86493015,  0.94111688,  4.15136037],
       [ 0.6344305 ,  4.37081993,  0.56318319,  3.84220004,  0.70567781,
         4.89943981,  0.70642503,  4.13470535],
       [ 0.38501321,  4.40359104,  0.32287341,  3.87382293,  0.447153  ,
         4.93335915,  0.47395314,  4.11189143],
       [ 0.13509189,  4.42939508,  0.08781327,  3.89809394,  0.1823705 ,
         4.96069622,  0.24391083,  4.08242203],
       [-0.11534167,  4.44811809, -0.1474071 ,  3.91568303, -0.08327625,
         4.98055315,  0.01659118,  4.04559304],
       [-0.366291  ,  4.459589  , -0.3531768 ,  3.92635012, -0.3794052 ,
         4.99282789, -0.20758038,  4.00037427],
       [-0.61609459,  4.43582249, -0.52198499,  3.91078997, -0.71020418,
         4.96085501, -0.42800383,  3.94531852],
       [-0.85872012,  4.37131357, -0.67983222,  3.86880493, -1.03760803,
         4.87382221, -0.64382567,  3.87838911],
       [-1.08748657,  4.2680161 , -0.82756817,  3.80222797, -1.34740496,
         4.73380423, -0.85363836,  3.79623896],
       [-1.29553831,  4.12755847, -0.96023059,  3.71272802, -1.63084602,
         4.54238892, -1.05941664,  3.70391965],
       [-1.4764775 ,  3.95359647, -1.07625699,  3.60097909, -1.87669802,
         4.30621386, -1.26217904,  3.60386937],
       [-1.62629896,  3.75213802, -1.17623794,  3.46585011, -2.07635999,
         4.03842592, -1.46278915,  3.49812711],
       [-1.74530452,  3.53097343, -1.27520096,  3.27894592, -2.21540809,
         3.78300095, -1.66205214,  3.38871123],
       [-1.863675  ,  3.3093636 , -1.40357304,  3.0395081 , -2.32377696,
         3.5792191 , -1.86068168,  3.27753553],
       [-1.99931949,  3.09787905, -1.56211102,  2.79232311, -2.43652797,
         3.40343499, -2.06259528,  3.16673366],
       [-2.15129894,  2.89781249, -1.73928297,  2.55905294, -2.56331491,
         3.23657203, -2.26569781,  3.05857582],
       [-2.31820899,  2.71002948, -1.93516505,  2.33882499, -2.70125294,
         3.08123398, -2.47039961,  2.95409144],
       [-2.50065804,  2.53731   , -2.15103006,  2.13447499, -2.85028601,
         2.94014502, -2.67717492,  2.85455236],
       [-2.69733202,  2.3809815 , -2.38415408,  1.94920003, -3.01050997,
         2.81276298, -2.88625335,  2.76072923],
       [-2.90699553,  2.24258655, -2.63612103,  1.78308403, -3.17787004,
         2.70208907, -3.09797576,  2.67374074],
       [-3.12959254,  2.12616503, -2.90749907,  1.64120102, -3.351686  ,
         2.61112905, -3.31250024,  2.5943056 ],
       [-3.36315   ,  2.03368706, -3.19365811,  1.52793205, -3.53264189,
         2.53944206, -3.52988894,  2.52291118],
       [-3.60525799,  1.96675599, -3.492975  ,  1.44530797, -3.71754098,
         2.488204  , -3.75012875,  2.45983694],
       [-3.85344756,  1.92811102, -3.80181408,  1.39721596, -3.90508103,
         2.45900607, -3.97313748,  2.40515076],
       [-4.10443401,  1.91820806, -4.11399698,  1.38489401, -4.09487104,
         2.45152211, -4.19876635,  2.35869904],
       [-4.35490561,  1.9371025 , -4.41835308,  1.40748894, -4.29145813,
         2.46671605, -4.42680331,  2.32009901],
       [-4.60286546,  1.97792453, -4.69294596,  1.45218599, -4.51278496,
         2.50366306, -4.65697866,  2.28874128],
       [-4.85028148,  2.02198094, -4.94602919,  1.49724495, -4.75453377,
         2.54671693, -4.88897099,  2.26381544],
       [-5.09731197,  2.06814551, -5.19756079,  1.54425097, -4.99706316,
         2.59204006, -5.12240375,  2.244373  ],
       [-5.34393406,  2.11644298, -5.44771719,  1.59323704, -5.24015093,
         2.63964891, -5.35681241,  2.22943886],
       [-5.59031916,  2.16593796, -5.69715118,  1.64334595, -5.48348713,
         2.68852997, -5.5915752 ,  2.21813722],
       [-5.83636189,  2.21710896, -5.94643497,  1.69518995, -5.7262888 ,
         2.73902798, -5.82589718,  2.20960073],
       [-6.08211422,  2.26965845, -6.19508123,  1.74835801, -5.96914721,
         2.79095888, -6.05917006,  2.20297269],
       [-6.32757401,  2.32355553, -6.44404984,  1.80302799, -6.21109819,
         2.84408307, -6.28812516,  2.19529209],
       [-6.5725956 ,  2.37941146, -6.69334602,  1.85985899, -6.45184517,
         2.89896393, -6.51558948,  2.18429223],
       [-6.81713653,  2.43733543, -6.93876505,  1.91798794, -6.695508  ,
         2.95668292, -6.74058897,  2.16782124],
       [-7.06185555,  2.49399352, -7.1513629 ,  1.96815705, -6.97234821,
         3.01982999, -6.96207763,  2.14361704],
       [-7.31148577,  2.52148652, -7.33490276,  1.98860097, -7.28806877,
         3.05437207, -7.17885135,  2.10920735],
       [-7.56253552,  2.51599753, -7.51023912,  1.98516703, -7.61483192,
         3.04682803, -7.3894437 ,  2.06187904],
       [-7.809762  ,  2.47240299, -7.67105722,  1.957353  , -7.94846678,
         2.98745298, -7.59226769,  1.99923235],
       [-8.04535317,  2.38598198, -7.81246614,  1.90610802, -8.2782402 ,
         2.86585593, -7.78391445,  1.91659967],
       [-8.25895953,  2.25441056, -7.93386507,  1.83152902, -8.58405399,
         2.67729211, -7.95993416,  1.81035357],
       [-8.44103956,  2.08179098, -8.03409004,  1.73696101, -8.84798908,
         2.42662096, -8.12348805,  1.68834029],
       [-8.58100986,  1.87447143, -8.1133604 ,  1.61791897, -9.04865932,
         2.13102388, -8.27464616,  1.55264888],
       [-8.68110943,  1.64396501, -8.19201565,  1.43112004, -9.17020321,
         1.85680997, -8.41300953,  1.40472513],
       [-8.78156805,  1.41360903, -8.29277039,  1.200086  , -9.27036572,
         1.62713206, -8.53813564,  1.24604976],
       [-8.88230896,  1.18337667, -8.39353657,  0.96979439, -9.37108135,
         1.39695895, -8.6488722 ,  1.07775772],
       [-8.98282433,  0.95304602, -8.49402237,  0.73953199, -9.47162628,
         1.16656005, -8.74399429,  0.90126874],
       [-9.08350039,  0.7227852 , -8.59494305,  0.50871319, -9.57205772,
         0.93685722, -8.8211088 ,  0.71794461],
       [-9.1845417 ,  0.49268435, -8.69591713,  0.27876499, -9.67316628,
         0.70660371, -8.87760251,  0.5299036 ],
       [-9.28507423,  0.26236094, -8.78365421,  0.08044477, -9.78649426,
         0.44427711, -8.91096633,  0.34002071],
       [-9.35542011,  0.02181458, -8.82917976, -0.06528754, -9.88166046,
         0.1089167 , -8.91707388,  0.15219196],
       [-9.36633444, -0.22863965, -8.83608532, -0.17075481, -9.89658356,
        -0.2865245 , -8.8915326 , -0.0277633 ],
       [-9.30180359, -0.47022745, -8.81856537, -0.24440449, -9.78504181,
        -0.69605041, -8.83113617, -0.19237123],
       [-9.15792656, -0.67464657, -8.77735901, -0.30090311, -9.53849411,
        -1.04839003, -8.73274824, -0.33157096],
       [-8.95570517, -0.82251926, -8.69300938, -0.35829249, -9.21840096,
        -1.28674603, -8.60354853, -0.44206714],
       [-8.72442436, -0.91989914, -8.55857372, -0.4129383 , -8.890275  ,
        -1.42685997, -8.45186428, -0.52595599],
       [-8.48013544, -0.97808473, -8.39081955, -0.4522154 , -8.56945133,
        -1.50395405, -8.28337881, -0.58589423],
       [-8.23030901, -1.00381944, -8.20906162, -0.4708429 , -8.2515564 ,
        -1.53679597, -8.10171121, -0.62362504],
       [-7.9792285 , -0.99805316, -8.02746296, -0.4668383 , -7.93099403,
        -1.52926803, -7.90988138, -0.64132171],
       [-7.73126054, -0.95850855, -7.85278702, -0.4391371 , -7.60973406,
        -1.47788   , -7.71047954, -0.64181404],
       [-7.49149394, -0.88392955, -7.68769884, -0.3879261 , -7.29528904,
        -1.379933  , -7.50570168, -0.62855186],
       [-7.2656095 , -0.77431226, -7.53297186, -0.31275749, -6.99824715,
        -1.23586702, -7.29746133, -0.60562119],
       [-7.0581224 , -0.63289025, -7.3888278 , -0.2143815 , -6.72741699,
        -1.05139899, -7.08751233, -0.57766438],
       [-6.87253547, -0.4637025 , -7.23864985, -0.07579029, -6.50642109,
        -0.85161471, -6.87799197, -0.55299237],
       [-6.69282389, -0.28811619, -7.04089785,  0.1160621 , -6.34474993,
        -0.69229448, -6.66927967, -0.53355228],
       [-6.49272513, -0.13659297, -6.76485014,  0.32216999, -6.22060013,
        -0.59535593, -6.46177486, -0.5217348 ],
       [-6.26415205, -0.03379184, -6.40882921,  0.47961271, -6.11947489,
        -0.54719639, -6.25590223, -0.51988631],
       [-6.01591778, -0.00217026, -6.01932478,  0.53121889, -6.01251078,
        -0.53555942, -6.05218562, -0.53065282],
       [-5.76637745, -0.03072414, -5.67760801,  0.49523741, -5.85514688,
        -0.55668569, -5.85134486, -0.55730478],
       [-5.52128148, -0.08565295, -5.36165285,  0.4233011 , -5.68091011,
        -0.594607  , -5.65458995, -0.60468625],
       [-5.28893495, -0.18044885, -5.03372288,  0.2879338 , -5.54414701,
        -0.64883149, -5.46293469, -0.67528298],
       [-5.0834651 , -0.32418685, -4.73316717,  0.0780653 , -5.43376303,
        -0.726439  , -5.27558974, -0.76389572],
       [-4.9126749 , -0.5081492 , -4.48715591, -0.1865146 , -5.33819389,
        -0.8297838 , -5.09165527, -0.8661037 ],
       [-4.7823844 , -0.72248076, -4.31926394, -0.45784011, -5.24550486,
        -0.9871214 , -4.90998118, -0.97709391],
       [-4.66365051, -0.94396794, -4.19713497, -0.68535793, -5.13016605,
        -1.20257795, -4.72944853, -1.09246738],
       [-4.53873181, -1.16201344, -4.08163786, -0.88709491, -4.99582577,
        -1.43693197, -4.53660621, -1.21365137],
       [-4.40467489, -1.37455451, -3.96093297, -1.07856703, -4.84841681,
        -1.670542  , -4.34179776, -1.33334021],
       [-4.25994658, -1.5799675 , -3.83343601, -1.25964797, -4.68645716,
        -1.90028703, -4.14467311, -1.45096316],
       [-4.10302508, -1.77620757, -3.69878602, -1.42820406, -4.50726414,
        -2.12421107, -3.94479167, -1.56571645],
       [-3.93230987, -1.96054947, -3.55704689, -1.58148098, -4.30757284,
        -2.33961797, -3.74204294, -1.677038  ],
       [-3.74627292, -2.12937945, -3.40884995, -1.71626794, -4.08369589,
        -2.54249096, -3.53617877, -1.78415518],
       [-3.54372954, -2.27793902, -3.25512099, -1.82936299, -3.83233809,
        -2.72651505, -3.32702164, -1.88633768],
       [-3.32461846, -2.40066952, -3.09731388, -1.91812599, -3.55192304,
        -2.88321304, -3.11451807, -1.98306158],
       [-3.09050047, -2.49143797, -2.93682003, -1.98065603, -3.24418092,
        -3.00221992, -2.89867681, -2.07397933],
       [-2.84519207, -2.54491901, -2.76752305, -2.01720405, -2.9228611 ,
        -3.07263398, -2.679557  , -2.1589159 ],
       [-2.59469652, -2.56439805, -2.55814505, -2.03225207, -2.631248  ,
        -3.09654403, -2.45727304, -2.23787042],
       [-2.34383357, -2.579355  , -2.31225204, -2.04689097, -2.37541509,
        -3.11181903, -2.23199858, -2.31101257],
       [-2.0929625 , -2.59415698, -2.06156611, -2.06168199, -2.12435889,
        -3.12663198, -2.00396494, -2.37867084],
       [-1.84208947, -2.60893905, -1.81082499, -2.07645607, -1.87335396,
        -3.14142203, -1.77345279, -2.44131059],
       [-1.59121054, -2.62361658, -1.56036603, -2.09110904, -1.62205505,
        -3.15612411, -1.54077886, -2.49950341],
       [-1.34031498, -2.63800406, -1.30998194, -2.10546708, -1.37064803,
        -3.17054105, -1.30628597, -2.55390397],
       [-1.08940798, -2.65219891, -1.059394  , -2.11964393, -1.11942196,
        -3.18475389, -1.07034767, -2.60525769],
       [-0.83849525, -2.66628551, -0.80863672, -2.13372207, -0.86835378,
        -3.19884896, -0.83337633, -2.65441511],
       [-0.58758029, -2.68033397, -0.5577628 , -2.14776802, -0.61739779,
        -3.21289992, -0.59574061, -2.70215126],
       [-0.3366653 , -2.69438255, -0.30693221, -2.16181207, -0.36639839,
        -3.22695303, -0.35794139, -2.75080463],
       [-0.08574594, -2.70835149, -0.05611788, -2.17577505, -0.115374  ,
        -3.24092793, -0.12063643, -2.80074088],
       [ 0.16517455, -2.72230053,  0.1948701 , -2.18972802,  0.135479  ,
        -3.25487304,  0.11604397, -2.85230116],
       [ 0.4160904 , -2.73633289,  0.4461506 , -2.20378089,  0.3860302 ,
        -3.2688849 ,  0.35192794, -2.90593761],
       [ 0.66699153, -2.75062609,  0.69734329, -2.21809006,  0.63663977,
        -3.28316212,  0.5868972 , -2.96196716],
       [ 0.91789174, -2.76493299,  0.94743598, -2.23235202,  0.88834751,
        -3.29751396,  0.8208824 , -3.02058402],
       [ 1.16883498, -2.77846491,  1.21771801, -2.24730992,  1.11995196,
        -3.3096199 ,  1.05386759, -3.08184791],
       [ 1.41712099, -2.81084299,  1.55353296, -2.29518104,  1.28070903,
        -3.32650495,  1.28589402, -3.14567389],
       [ 1.64935303, -2.90563941,  1.89728701, -2.43336391,  1.40141904,
        -3.37791491,  1.51706244, -3.21182446],
       [ 1.85937703, -3.04303241,  2.184026  , -2.61980891,  1.53472805,
        -3.4662559 ,  1.74749009, -3.28002599],
       [ 2.04661405, -3.21038699,  2.42535305, -2.83479095,  1.66787505,
        -3.58598304,  1.97727462, -3.35007459],
       [ 2.21245456, -3.39907098,  2.61209512, -3.04579592,  1.812814  ,
        -3.75234604,  2.20649523, -3.42185558],
       [ 2.37939799, -3.58684754,  2.761621  , -3.21479702,  1.99717498,
        -3.95889807,  2.43554031, -3.49558876],
       [ 2.56254244, -3.75873601,  2.89476299, -3.341429  ,  2.23032188,
        -4.17604303,  2.66562489, -3.56754086],
       [ 2.77089906, -3.89855039,  3.02086401, -3.42734694,  2.5209341 ,
        -4.36975384,  2.89669361, -3.6374319 ],
       [ 3.00348246, -3.99264956,  3.16282296, -3.48360491,  2.84414196,
        -4.5016942 ,  3.1287314 , -3.70510368],
       [ 3.24847603, -4.04801798,  3.35082102, -3.52452898,  3.14613104,
        -4.57150698,  3.36181886, -3.77024811],
       [ 3.49641442, -4.08901656,  3.57386088, -3.56126904,  3.41896796,
        -4.61676407,  3.59601936, -3.83260703],
       [ 3.745646  , -4.12097812,  3.805794  , -3.59098005,  3.685498  ,
        -4.65097618,  3.83143721, -3.89180318],
       [ 3.99573493, -4.14568245,  4.04570389, -3.61462808,  3.94576597,
        -4.67673683,  4.06812582, -3.94755117],
       [ 4.24604392, -4.16806257,  4.29225492, -3.63666797,  4.19983292,
        -4.69945717,  4.30609628, -3.99962431],
       [ 4.49645901, -4.18922698,  4.54044485, -3.65764403,  4.45247316,
        -4.72080994,  4.54531177, -4.04785458],
       [ 4.74694681, -4.20950961,  4.7892828 , -3.67779207,  4.70461082,
        -4.74122715,  4.78568468, -4.0921243 ],
       [ 4.9974885 , -4.22912002,  5.03859997, -3.69730711,  4.95637703,
        -4.76093292,  5.02707697, -4.13234655],
       [ 5.24806738, -4.24824798,  5.28829479, -3.71636701,  5.20783997,
        -4.78012896,  5.2693018 , -4.16843904],
       [ 5.49867296, -4.26702499,  5.53826094, -3.73509598,  5.45908499,
        -4.79895401,  5.51212428, -4.20031284],
       [ 5.74929714, -4.28555143,  5.78843307, -3.75358891,  5.71016121,
        -4.81751394,  5.75526217, -4.22788482],
       [ 5.99993396, -4.30390239,  6.03857183, -3.77190399,  5.96129608,
        -4.83590078,  5.99838787, -4.25086083],
       [ 6.25059247, -4.32195938,  6.28855801, -3.78991199,  6.21262693,
        -4.85400677,  6.24108803, -4.26882987],
       [ 6.50127482, -4.33967638,  6.53857088, -3.8075819 ,  6.46397877,
        -4.87177086,  6.48283762, -4.28125951],
       [ 6.75197792, -4.35710299,  6.78870392, -3.82496905,  6.71525192,
        -4.88923693,  6.72303824, -4.28767426],
       [ 7.00269794, -4.37428248,  7.03895378, -3.84211612,  6.96644211,
        -4.90644884,  6.96079153, -4.28697008],
       [ 7.25343156, -4.39126658,  7.28934622, -3.85907698,  7.2175169 ,
        -4.92345619,  7.1949787 , -4.27798437],
       [ 7.50417352, -4.40812504,  7.53987312, -3.87592101,  7.46847391,
        -4.94032907,  7.42423263, -4.25939653],
       [ 7.75492001, -4.42490542,  7.79574203, -3.89306998,  7.71409798,
        -4.95674086,  7.64693764, -4.22974638],
       [ 8.00510788, -4.44657302,  8.04101562, -3.91438293,  7.96920013,
        -4.9787631 ,  7.86120756, -4.18742675],
       [ 8.25582838, -4.45870495,  8.23602676, -3.92567301,  8.27563   ,
        -4.99173689,  8.06481975, -4.13068868],
       [ 8.50494766, -4.42800546,  8.3891716 , -3.90732193,  8.62072372,
        -4.94868898,  8.25506873, -4.05766494],
       [ 8.74339581, -4.35031354,  8.51855564, -3.86661696,  8.96823597,
        -4.83401012,  8.42783264, -3.96579635],
       [ 8.956388  , -4.21817756,  8.61896515, -3.80506611,  9.29381084,
        -4.63128901,  8.57802248, -3.85323117],
       [ 9.12837839, -4.03586841,  8.69855785, -3.72000504,  9.55819893,
        -4.35173178,  8.69903212, -3.71944042],
       [ 9.25107765, -3.81713498,  8.7619772 , -3.60430598,  9.74017811,
        -4.02996397,  8.77852755, -3.56556009],
       [ 9.32756472, -3.57806849,  8.80831337, -3.45602798,  9.84681606,
        -3.700109  ,  8.82340732, -3.40235632],
       [ 9.36559153, -3.32988203,  8.83370495, -3.28973007,  9.8974781 ,
        -3.37003398,  8.83859379, -3.23540285],
       [ 9.3652544 , -3.07880855,  8.83344555, -3.1199851 ,  9.89706326,
        -3.03763199,  8.82797041, -3.06812444],
       [ 9.32693958, -2.83067894,  8.80688572, -2.94925499,  9.84699345,
        -2.71210289,  8.79398648, -2.90280445],
       [ 9.25389338, -2.59041548,  8.75502396, -2.77921391,  9.75276279,
        -2.40161705,  8.73848688, -2.74114653],
       [ 9.14956093, -2.36198699,  8.68282223, -2.620193  ,  9.61629963,
        -2.10378098,  8.66049874, -2.58532148],
       [ 9.01148415, -2.15223104,  8.59062767, -2.47994304,  9.43234062,
        -1.82451904,  8.55459469, -2.44022432],
       [ 8.84194565, -1.96694207,  8.47815228, -2.35703111,  9.20573902,
        -1.57685304,  8.42409196, -2.30814019],
       [ 8.64530134, -1.81073099,  8.34752369, -2.25327396,  8.94307899,
        -1.36818802,  8.27321626, -2.18943017],
       [ 8.42654276, -1.68742448,  8.20211887, -2.171314  ,  8.65096664,
        -1.20353496,  8.10508703, -2.08401297],
       [ 8.19108295, -1.60007   ,  8.04563332, -2.11325598,  8.33653259,
        -1.08688402,  7.92253383, -1.99121879],
       [ 7.94479012, -1.55088502,  7.88035822, -2.08037901,  8.00922203,
        -1.02139103,  7.72813498, -1.90988985],
       [ 7.69385695, -1.53956753,  7.68056393, -2.07280207,  7.70714998,
        -1.00633299,  7.52389381, -1.83888018],
       [ 7.44255185, -1.53836745,  7.44000387, -2.07176089,  7.44509983,
        -1.00497401,  7.31143452, -1.7770729 ],
       [ 7.19124699, -1.53716695,  7.18869877, -2.07056093,  7.1937952 ,
        -1.00377297,  7.09241388, -1.72301596],
       [ 6.93994141, -1.53596604,  6.93818903, -2.06936312,  6.94169378,
        -1.00256896,  6.86825508, -1.67529102],
       [ 6.68868709, -1.53551543,  6.68924809, -2.06891489,  6.68812609,
        -1.00211596,  6.64026398, -1.63244839],
       [ 6.43752694, -1.53649497,  6.43614578, -2.06989288,  6.4389081 ,
        -1.00309706,  6.40952921, -1.59319166],
       [ 6.18615007, -1.53421295,  6.17592192, -2.0675149 ,  6.19637823,
        -1.000911  ,  6.17647859, -1.55680927],
       [ 5.93443346, -1.52684164,  5.91345787, -2.059829  ,  5.95540905,
        -0.99385428,  5.94108459, -1.51647782],
       [ 5.68237901, -1.51438144,  5.666471  , -2.047544  ,  5.69828701,
        -0.98121887,  5.70734026, -1.47258524],
       [ 5.43098187, -1.51180145,  5.45522594, -2.04465008,  5.4067378 ,
        -0.97895283,  5.47561872, -1.42464096],
       [ 5.18142414, -1.53714299,  5.23351812, -2.06799293,  5.12933016,
        -1.00629306,  5.24623671, -1.37219654],
       [ 4.93126917, -1.56083852,  4.96529913, -2.09315205,  4.89723921,
        -1.02852499,  5.0196125 , -1.31463319],
       [ 4.68013501, -1.56918997,  4.67912579, -2.10258889,  4.68114424,
        -1.03579104,  4.79620628, -1.25131515],
       [ 4.42904854, -1.55988848,  4.38586903, -2.09153795,  4.47222805,
        -1.02823901,  4.57650257, -1.18163657],
       [ 4.17978311, -1.52855301,  4.08351517, -2.05319405,  4.27605104,
        -1.00391197,  4.36092111, -1.10517625],
       [ 3.93567443, -1.46936032,  3.78358889, -1.98061895,  4.08775997,
        -0.95810169,  4.15002511, -1.02136515],
       [ 3.69886899, -1.38549241,  3.49268508, -1.87743104,  3.9050529 ,
        -0.89355379,  3.9442346 , -0.929959  ],
       [ 3.47307956, -1.27547878,  3.21092606, -1.74001205,  3.73523307,
        -0.81094551,  3.74382986, -0.83099708],
       [ 3.26220596, -1.13906837,  2.94071603, -1.56469703,  3.58369589,
        -0.7134397 ,  3.54896728, -0.72474877],
       [ 3.0733974 , -0.9735949 ,  2.68878889, -1.34317803,  3.45800591,
        -0.60401177,  3.35989945, -0.61140442],
       [ 2.91563749, -0.77842142,  2.48896289, -1.09852195,  3.3423121 ,
        -0.45832089,  3.17740969, -0.49063399],
       [ 2.77219403, -0.57208894,  2.339118  , -0.88347417,  3.20527005,
        -0.26070371,  3.00245153, -0.36214197],
       [ 2.6222719 , -0.37040795,  2.19770288, -0.69329649,  3.04684091,
        -0.0475194 ,  2.83643849, -0.22546487],
       [ 2.46796501, -0.1720558 ,  2.04846001, -0.50149661,  2.88747001,
         0.15738501,  2.68145572, -0.0800054 ],
       [ 2.31184947,  0.02487935,  1.89098096, -0.3028174 ,  2.73271799,
         0.35257611,  2.54052   ,  0.07480235],
       [ 2.15919852,  0.22450002,  1.73035002, -0.09268197,  2.58804703,
         0.541682  ,  2.41677808,  0.23866991],
       [ 2.01302546,  0.4289065 ,  1.566975  ,  0.1364094 ,  2.45907593,
         0.7214036 ,  2.31659362,  0.41122113],
       [ 1.88388151,  0.64434345,  1.41624796,  0.38776121,  2.35151505,
         0.9009257 ,  2.24596967,  0.58935645],
       [ 1.77153999,  0.86902773,  1.265607  ,  0.70006847,  2.27747297,
         1.03798699,  2.21065525,  0.76761121],
       [ 1.72672904,  1.11392498,  1.19395399,  1.13973796,  2.25950408,
         1.088112  ,  2.21485851,  0.93900046],
       [ 1.79517955,  1.35395449,  1.32003701,  1.596349  ,  2.27032208,
         1.11155999,  2.26295319,  1.09574795],
       [ 1.94950753,  1.550493  ,  1.61094701,  1.96267295,  2.28806806,
         1.13831306,  2.361418  ,  1.22744479],
       [ 2.17099655,  1.66304898,  2.0108521 ,  2.17184091,  2.331141  ,
         1.15425706,  2.48913893,  1.3406005 ],
       [ 2.41962242,  1.69801056,  2.37302089,  2.22937107,  2.46622396,
         1.16665006,  2.64247211,  1.43533918],
       [ 2.67070401,  1.70686597,  2.67363095,  2.24025798,  2.66777706,
         1.17347395,  2.81832168,  1.51196254],
       [ 2.92169857,  1.69525397,  2.94982409,  2.22791195,  2.89357305,
         1.16259599,  3.01401032,  1.5708422 ],
       [ 3.17253089,  1.68036902,  3.1932869 ,  2.21336508,  3.15177488,
         1.14737296,  3.22620747,  1.61342696],
       [ 3.42379546,  1.67570251,  3.43305898,  2.20902205,  3.41453195,
         1.14238298,  3.45168466,  1.64171616],
       [ 3.675071  ,  1.67164004,  3.68292809,  2.20498204,  3.66721392,
         1.13829803,  3.68735744,  1.65821107],
       [ 3.92635643,  1.66829902,  3.93265295,  2.20166206,  3.92005992,
         1.13493598,  3.93039854,  1.66572189],
       [ 4.17765093,  1.66570699,  4.18287897,  2.19908094,  4.17242289,
         1.13233304,  4.17834074,  1.66713258],
       [ 4.42894793,  1.66337252,  4.43357182,  2.19675207,  4.42432404,
         1.12999296,  4.42898042,  1.66536727],
       [ 4.68024755,  1.66134995,  4.68394423,  2.19473696,  4.67655087,
         1.12796295,  4.67865369,  1.66699941],
       [ 4.93155146,  1.65988952,  4.93403292,  2.19328403,  4.92907   ,
         1.126495  ,  4.92615987,  1.67292679],
       [ 5.18285751,  1.65901202,  5.18459702,  2.19240904,  5.18111801,
         1.125615  ,  5.17068813,  1.68417775],
       [ 5.43416452,  1.65825045,  5.43551922,  2.19164896,  5.43280983,
         1.12485194,  5.41129812,  1.70182912],
       [ 5.68547153,  1.65773547,  5.68607903,  2.19113493,  5.68486404,
         1.124336  ,  5.64694396,  1.72692594],
       [ 5.93677998,  1.65767795,  5.93639612,  2.19107795,  5.93716383,
         1.12427795,  5.87650597,  1.76041435],
       [ 6.18808699,  1.65809697,  6.18712807,  2.1914959 ,  6.18904591,
         1.12469804,  6.09885355,  1.80305544],
       [ 6.43939447,  1.65858251,  6.42995596,  2.19189906,  6.44883299,
         1.12526596,  6.31282767,  1.85546631],
       [ 6.69045353,  1.66698647,  6.63230896,  2.19720793,  6.7485981 ,
         1.136765  ,  6.5167066 ,  1.91864062],
       [ 6.93728399,  1.713175  ,  6.79717207,  2.227844  ,  7.07739592,
         1.198506  ,  6.70885894,  1.99312805],
       [ 7.17345738,  1.79847747,  6.95232582,  2.28388095,  7.39458895,
         1.31307399,  6.88744404,  2.0793498 ],
       [ 7.39281297,  1.9206965 ,  7.09635592,  2.36412501,  7.68927002,
         1.47726798,  7.05031946,  2.17759987],
       [ 7.58959055,  2.07668501,  7.22542715,  2.466429  ,  7.95375395,
         1.68694103,  7.19424137,  2.28839883],
       [ 7.75855827,  2.26243705,  7.33604908,  2.58801603,  8.18106747,
         1.93685806,  7.315914  ,  2.41148839],
       [ 7.89506769,  2.47309756,  7.41998482,  2.71560907,  8.37015057,
         2.23058605,  7.41149392,  2.54599436],
       [ 7.98552775,  2.70702553,  7.46905279,  2.84032607,  8.50200272,
         2.57372499,  7.47637009,  2.69017999],
       [ 8.01955462,  2.95534456,  7.48620605,  2.94794106,  8.55290318,
         2.96274805,  7.50440952,  2.84105346],
       [ 7.97878647,  3.20179057,  7.48575306,  2.99823904,  8.47181988,
         3.4053421 ,  7.4861029 ,  2.99320919],
       [ 7.83435941,  3.40446353,  7.47579622,  3.00956106,  8.19292259,
         3.799366  ,  7.40446756,  3.13342695],
       [ 7.61761189,  3.52936006,  7.4103179 ,  3.03788805,  7.82490587,
         4.02083206,  7.28990746,  3.26125288],
       [ 7.37607908,  3.59764493,  7.2640481 ,  3.07614303,  7.48811007,
         4.11914682,  7.14643848,  3.37528876],
       [ 7.12758899,  3.63461351,  7.05949211,  3.10557795,  7.19568586,
         4.16364908,  6.97710792,  3.47436505],
       [ 6.87774944,  3.66178751,  6.8198638 ,  3.13153791,  6.93563509,
         4.19203711,  6.78572867,  3.55837579]]





def dist(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5



# thanks for https://github.com/cdthompson/deepracer-k1999-race-lines for the good racing line calculator which I forked to add new tracks https://github.com/fmacrae/deepracer-k1999-race-lines.  The output of that project is inputed to the reward funtion code as get_racing_line_waypoints fucntion contents.

# thanks to https://stackoverflow.com/questions/20924085/python-conversion-between-coordinates
def rect(r, theta):
    """
    theta in degrees
    returns tuple; (float, float); (x,y)
    """

    x = r * math.cos(math.radians(theta))
    y = r * math.sin(math.radians(theta))
    return x, y


# thanks to https://stackoverflow.com/questions/20924085/python-conversion-between-coordinates
def polar(x, y):
    """
    returns r, theta(degrees)
    """

    r = (x ** 2 + y ** 2) ** .5
    theta = math.degrees(math.atan2(y,x))
    return r, theta


def angle_mod_360(angle):
    """
    Maps an angle to the interval -180, +180.
    Examples:
    angle_mod_360(362) == 2
    angle_mod_360(270) == -90
    :param angle: angle in degree
    :return: angle in degree. Between -180 and +180
    """

    n = math.floor(angle/360.0)

    angle_between_0_and_360 = angle - n*360.0

    if angle_between_0_and_360 <= 180.0:
        return angle_between_0_and_360
    else:
        return angle_between_0_and_360 - 360


def get_waypoints_ordered_in_driving_direction(params):
    # waypoints are always provided in counter clock wise order
    if params['is_reversed']: # driving clock wise.
        return list(reversed(params['waypoints']))
    else: # driving counter clock wise.
        return params['waypoints']

def get_racingline_waypoints_ordered_in_driving_direction(racingline_waypoints, params):
    # waypoints are always provided in counter clock wise order
    if params['is_reversed']: # driving clock wise.
        return list(reversed(racingline_waypoints))
    else: # driving counter clock wise.
        return racingline_waypoints


def up_sample(waypoints, factor):
    """
    Adds extra waypoints in between provided waypoints
    :param waypoints:
    :param factor: integer. E.g. 3 means that the resulting list has 3 times as many points.
    :return:
    """
    p = waypoints
    n = len(p)

    return [[i / factor * p[(j+1) % n][0] + (1 - i / factor) * p[j][0],
             i / factor * p[(j+1) % n][1] + (1 - i / factor) * p[j][1]] for j in range(n) for i in range(factor)]


# taken from https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
# A Python3 program to find if 2 given line segments intersect or not

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

# Given three collinear points p, q, r, the function checks if
# point q lies on line segment 'pr'
def onSegment(p, q, r):
	if ( (q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and
		(q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
		return True
	return False

def orientation(p, q, r):
	# to find the orientation of an ordered triplet (p,q,r)
	# function returns the following values:
	# 0 : Collinear points
	# 1 : Clockwise points
	# 2 : Counterclockwise
	
	# See https://www.geeksforgeeks.org/orientation-3-ordered-points/amp/
	# for details of below formula.
	
	val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
	if (val > 0):
		
		# Clockwise orientation
		return 1
	elif (val < 0):
		
		# Counterclockwise orientation
		return 2
	else:
		
		# Collinear orientation
		return 0

# The main function that returns true if
# the line segment 'p1q1' and 'p2q2' intersect.
def doIntersect(p1,q1,p2,q2):
	
	# Find the 4 orientations required for
	# the general and special cases
	o1 = orientation(p1, q1, p2)
	o2 = orientation(p1, q1, q2)
	o3 = orientation(p2, q2, p1)
	o4 = orientation(p2, q2, q1)

	# General case
	if ((o1 != o2) and (o3 != o4)):
		return True

	# Special Cases

	# p1 , q1 and p2 are collinear and p2 lies on segment p1q1
	if ((o1 == 0) and onSegment(p1, p2, q1)):
		return True

	# p1 , q1 and q2 are collinear and q2 lies on segment p1q1
	if ((o2 == 0) and onSegment(p1, q2, q1)):
		return True

	# p2 , q2 and p1 are collinear and p1 lies on segment p2q2
	if ((o3 == 0) and onSegment(p2, p1, q2)):
		return True

	# p2 , q2 and q1 are collinear and q1 lies on segment p2q2
	if ((o4 == 0) and onSegment(p2, q1, q2)):
		return True

	# If none of the cases
	return False



def not_collided(params, i, racingline_waypoints, inner_waypoints, outer_waypoints):
    car_x = params['x']
    car_y = params['y']

    #define the line the car is trying to get to
    p1 = Point(car_x, car_y)
    q1 = Point(racingline_waypoints[i][0],racingline_waypoints[i][1])
        
    #now loop through the intervening boundary lines to see if it crosses any boundaries
    for iLoop in range(i):
        #check inner
        p2 = Point(inner_waypoints[i][0], inner_waypoints[i][1])
        q2 = Point(inner_waypoints[i+1][0], inner_waypoints[i+1][1])
        if doIntersect(p1, q1, p2, q2):
            #we've a collision
            return False
        #check outer
        p2 = Point(outer_waypoints[i][0], outer_waypoints[i][1])
        q2 = Point(outer_waypoints[i+1][0], outer_waypoints[i+1][1])
        if doIntersect(p1, q1, p2, q2):
            #we've a collision
            return False
    return True



def get_target_point(params):
    RATIO_UPSAMPLE = 2
    #waypoints = up_sample(get_waypoints_ordered_in_driving_direction(params), RATIO_UPSAMPLE)
    waypoints_input = np.array(get_racing_line_waypoints())

    center_line = waypoints_input[:,0:2]
    inner_border = waypoints_input[:,2:4]
    outer_border = waypoints_input[:,4:6]
    racing_line = waypoints_input[:,6:8]

    racingline_waypoints= up_sample(get_racingline_waypoints_ordered_in_driving_direction(racing_line, params), RATIO_UPSAMPLE)
    inner_waypoints= up_sample(get_racingline_waypoints_ordered_in_driving_direction(inner_border, params), RATIO_UPSAMPLE)
    outer_waypoints= up_sample(get_racingline_waypoints_ordered_in_driving_direction(outer_border, params), RATIO_UPSAMPLE)
    waypoints= up_sample(get_racingline_waypoints_ordered_in_driving_direction(center_line, params), RATIO_UPSAMPLE)

    car = [params['x'], params['y']]

    distances = [dist(p, car) for p in waypoints]
    min_dist = min(distances)
    i_closest = distances.index(min_dist)

    n = len(waypoints)

    #waypoints_starting_with_closest = [waypoints[(i+i_closest) % n] for i in range(n)]
    racingline_waypoints_starting_with_closest = [racingline_waypoints[(i+i_closest) % n] for i in range(n)]
    inner_waypoints_starting_with_closest = [inner_waypoints[(i+i_closest) % n] for i in range(n)]
    outer_waypoints_starting_with_closest = [outer_waypoints[(i+i_closest) % n] for i in range(n)]
    
    #skip forward till you find a path that collided with a boundary
    i_first_outside = 0
    while not_collided(params, i_first_outside, racingline_waypoints_starting_with_closest, inner_waypoints_starting_with_closest, outer_waypoints_starting_with_closest):
      i_first_outside+=1
      if i_first_outside >= (n - 1) : break

    #r = params['track_width'] * 0.9
    #is_inside = [dist(p, car) < r for p in waypoints_starting_with_closest]
    #i_first_outside = is_inside.index(False)

    #if i_first_outside < 0:  # this can only happen if we choose r as big as the entire track
    #    return waypoints[i_closest]
    #work back to the closest one that doesn't go outside the bounds of the track.
    #return waypoints_starting_with_closest[i_first_outside]


    return racingline_waypoints_starting_with_closest[i_first_outside]
      

def get_target_steering_degree(params):
    tx, ty = get_target_point(params)
    car_x = params['x']
    car_y = params['y']
    dx = tx-car_x
    dy = ty-car_y
    heading = params['heading']

    _, target_angle = polar(dx, dy)

    steering_angle = target_angle - heading

    return angle_mod_360(steering_angle)


def score_steer_to_point_ahead(params):
    best_stearing_angle = get_target_steering_degree(params)
    steering_angle = params['steering_angle']

    error = (steering_angle - best_stearing_angle) / 60.0  # 60 degree is already really bad

    score = 1.0 - abs(error)

    return max(score, 0.01)  # optimizer is rumored to struggle with negative numbers and numbers too close to zero


#There is one row per waypoint.
#There are 8 columns.

#1. x coordinate of centre lane at waypoint
#2. y coordinate of centre lane at waypoint
#3. x coordinate of left lane beside waypoint
#4. y coordinate of left lane beside waypoint
#5. x coordinate of right lane
#6. y coordinate of right lane
#7. x coordinate of racingline
#8. y coordinate of racingline

def test_funct():
    return 2
    
def reward_function(params):
    # straightsector = list(range(0,50))
    # straightsector.extend(range(306,355))


    reward_score = float(score_steer_to_point_ahead(params))
    #if params["closest_waypoints"][1] in straightsector:
    #    reward_score = reward_score + (2 * params['speed']) #give a wee nudge for going faster
    return reward_score





def get_test_params():
    return {
        'x': 0.7,
        'y': 1.05,
        'heading': 160.0,
        'track_width': 0.45,
        'is_reversed': False,
        'steering_angle': 0.0,
        'waypoints': [
            [0.75, -0.7],
            [1.0, 0.0],
            [0.7, 0.52],
            [0.58, 0.7],
            [0.48, 0.8],
            [0.15, 0.95],
            [-0.1, 1.0],
            [-0.7, 0.75],
            [-0.9, 0.25],
            [-0.9, -0.55],
        ]
    }


def test_reward():
    params = get_test_params()

    reward = reward_function(params)

    print("test_reward: {}".format(reward))

    assert reward > 0.0
def run_tests():
    test_reward()

    print("All tests successful")


#run_tests()