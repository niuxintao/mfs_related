import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as co

#assign, missing, checking, wrong, interface, extranous
out_printtokens = [[0.012345679012345678,0.012345679012345678,0.012345679012345678,0.012345679012345678,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.012345679012345678,0.012345679012345678,0.012658227848101266,0.012658227848101266,0.012345679012345678,0.012658227848101266,0.012345679012345678,0.012345679012345678,0.012345679012345678,0.012658227848101266,0.012345679012345678,0.012345679012345678,0.012345679012345678,0.012345679012345678,0.012345679012345678,0.012345679012345678,0.0136986301369863,0.0136986301369863,0.014084507042253521,0.014084507042253521,0.0136986301369863,0.014084507042253521,0.0136986301369863,0.0136986301369863,0.0136986301369863,0.014084507042253521,0.0136986301369863,0.0136986301369863,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.011235955056179775,0.008928571428571428,0.008928571428571428,0.014184397163120567,0.014184397163120567,0.007246376811594203,0.0072992700729927005,0.01282051282051282,0.01282051282051282,],[0.021739130434782608,0.02127659574468085,0.021739130434782608,0.021739130434782608,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.021739130434782608,0.014925373134328358,0.021739130434782608,0.021739130434782608,0.021739130434782608,0.014925373134328358,0.021739130434782608,0.014705882352941176,0.02127659574468085,0.014925373134328358,0.021739130434782608,0.021739130434782608,0.021739130434782608,0.02127659574468085,0.021739130434782608,0.021739130434782608,0.02631578947368421,0.01694915254237288,0.02631578947368421,0.02631578947368421,0.02631578947368421,0.01694915254237288,0.02631578947368421,0.016666666666666666,0.02564102564102564,0.01694915254237288,0.02631578947368421,0.02631578947368421,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.3333333333333333,0.3333333333333333,0.0,0.0,0.0,0.0,]]

out_printtokens2 = [[0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.014925373134328358,0.014492753623188406,0.025,0.023255813953488372,0.014492753623188406,0.014925373134328358,0.02702702702702703,0.023255813953488372,0.030303030303030304,0.030303030303030304,0.030303030303030304,0.030303030303030304,0.023255813953488372,0.014925373134328358,0.023255813953488372,0.014925373134328358,0.02702702702702703,0.02702702702702703,0.025,0.025,0.014492753623188406,0.014492753623188406,0.02702702702702703,0.025,0.0,0.0,0.0,0.0,0.007042253521126761,0.00684931506849315,0.006622516556291391,0.005555555555555556,0.005681818181818182,0.005494505494505495,0.005649717514124294,0.00510204081632653,0.005649717514124294,0.005555555555555556,0.005681818181818182,0.005649717514124294,0.005649717514124294,0.005649717514124294,0.005681818181818182,0.005494505494505495,0.005681818181818182,0.005263157894736842,0.005128205128205128,0.005494505494505495,0.005649717514124294,0.0056179775280898875,0.005681818181818182,0.00510204081632653,0.005747126436781609,0.00558659217877095,0.00558659217877095,0.00558659217877095,0.004975124378109453,0.005128205128205128,0.005128205128205128,0.004975124378109453,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,],[0.25,0.25,0.25,0.03571428571428571,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.2,0.034482758620689655,0.25,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,]]

out_replace = [[0.038461538461538464,0.038461538461538464,0.011111111111111112,0.038461538461538464,0.011111111111111112,0.038461538461538464,0.0136986301369863,0.0136986301369863,0.014084507042253521,0.014084507042253521,0.0136986301369863,0.014084507042253521,0.0136986301369863,0.0136986301369863,0.0136986301369863,0.014084507042253521,0.0136986301369863,0.0136986301369863,0.027777777777777776,0.027777777777777776,0.027777777777777776,0.027777777777777776,0.030303030303030304,0.027777777777777776,0.027777777777777776,0.027777777777777776,0.030303030303030304,0.027777777777777776,0.027777777777777776,0.02857142857142857,0.02702702702702703,0.02702702702702703,0.027777777777777776,0.027777777777777776,0.02857142857142857,0.027777777777777776,0.02857142857142857,0.02702702702702703,0.027777777777777776,0.02702702702702703,0.027777777777777776,0.027777777777777776,0.02857142857142857,0.027777777777777776,0.027777777777777776,0.027777777777777776,0.027777777777777776,0.027777777777777776,0.030303030303030304,0.030303030303030304,0.014925373134328358,0.014492753623188406,0.025,0.023255813953488372,0.014492753623188406,0.014925373134328358,0.02702702702702703,0.023255813953488372,0.030303030303030304,0.030303030303030304,0.030303030303030304,0.030303030303030304,0.023255813953488372,0.014925373134328358,0.023255813953488372,0.014925373134328358,0.02702702702702703,0.02702702702702703,0.025,0.025,0.014492753623188406,0.014492753623188406,0.02702702702702703,0.025,0.0,0.0,0.0,0.0,0.007042253521126761,0.007042253521126761,0.007042253521126761,0.00684931506849315,0.006622516556291391,0.014184397163120567,0.014184397163120567,0.005555555555555556,0.005681818181818182,0.005494505494505495,0.005649717514124294,0.00510204081632653,0.005649717514124294,0.005555555555555556,0.005681818181818182,0.005649717514124294,0.005649717514124294,0.005649717514124294,0.005681818181818182,0.005494505494505495,0.005681818181818182,0.005263157894736842,0.005128205128205128,0.005494505494505495,0.005649717514124294,0.0056179775280898875,0.005681818181818182,0.00510204081632653,0.005747126436781609,0.00558659217877095,0.00558659217877095,0.00558659217877095,0.004975124378109453,0.005128205128205128,0.005128205128205128,0.004975124378109453,0.007142857142857143,0.00546448087431694,0.005405405405405406,0.0056179775280898875,0.00546448087431694,0.0056179775280898875,0.005376344086021506,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,],[0.0,0.0,0.0,0.0,0.0,0.0,0.02631578947368421,0.01694915254237288,0.02631578947368421,0.02631578947368421,0.02631578947368421,0.01694915254237288,0.02631578947368421,0.016666666666666666,0.02564102564102564,0.01694915254237288,0.02631578947368421,0.02631578947368421,0.045454545454545456,0.045454545454545456,0.045454545454545456,0.045454545454545456,0.045454545454545456,0.045454545454545456,0.045454545454545456,0.045454545454545456,0.045454545454545456,0.045454545454545456,0.045454545454545456,0.041666666666666664,0.043478260869565216,0.043478260869565216,0.045454545454545456,0.045454545454545456,0.041666666666666664,0.045454545454545456,0.041666666666666664,0.043478260869565216,0.045454545454545456,0.043478260869565216,0.045454545454545456,0.045454545454545456,0.041666666666666664,0.045454545454545456,0.045454545454545456,0.045454545454545456,0.045454545454545456,0.045454545454545456,0.045454545454545456,0.045454545454545456,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.3333333333333333,0.3333333333333333,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,]]

out_schedule = [[0.038461538461538464,0.038461538461538464,0.011111111111111112,0.038461538461538464,0.011111111111111112,0.038461538461538464,0.012345679012345678,0.012345679012345678,0.012345679012345678,0.012345679012345678,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.012345679012345678,0.012345679012345678,0.012658227848101266,0.012658227848101266,0.012345679012345678,0.012658227848101266,0.012345679012345678,0.012345679012345678,0.012345679012345678,0.012658227848101266,0.012345679012345678,0.012345679012345678,0.012345679012345678,0.012345679012345678,0.012345679012345678,0.012345679012345678,0.0136986301369863,0.0136986301369863,0.014084507042253521,0.014084507042253521,0.0136986301369863,0.014084507042253521,0.0136986301369863,0.0136986301369863,0.0136986301369863,0.014084507042253521,0.0136986301369863,0.0136986301369863,0.0136986301369863,0.0136986301369863,0.014084507042253521,0.014084507042253521,0.0136986301369863,0.014084507042253521,0.0136986301369863,0.0136986301369863,0.0136986301369863,0.014084507042253521,0.0136986301369863,0.0136986301369863,0.027777777777777776,0.027777777777777776,0.027777777777777776,0.027777777777777776,0.030303030303030304,0.027777777777777776,0.027777777777777776,0.027777777777777776,0.030303030303030304,0.027777777777777776,0.027777777777777776,0.02857142857142857,0.02702702702702703,0.02702702702702703,0.027777777777777776,0.027777777777777776,0.02857142857142857,0.027777777777777776,0.02857142857142857,0.02702702702702703,0.027777777777777776,0.02702702702702703,0.027777777777777776,0.027777777777777776,0.02857142857142857,0.027777777777777776,0.027777777777777776,0.027777777777777776,0.027777777777777776,0.027777777777777776,0.030303030303030304,0.030303030303030304,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.011235955056179775,0.008928571428571428,0.008928571428571428,0.0,0.007042253521126761,0.007042253521126761,0.007246376811594203,0.0072992700729927005,0.007142857142857143,0.005263157894736842,0.005405405405405406,0.005405405405405406,0.005405405405405406,0.005376344086021506,0.01282051282051282,0.01282051282051282,0.00546448087431694,0.005405405405405406,0.0056179775280898875,0.00546448087431694,0.0056179775280898875,0.005376344086021506,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,],[0.0,0.0,0.0,0.0,0.0,0.0,0.021739130434782608,0.02127659574468085,0.021739130434782608,0.021739130434782608,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.021739130434782608,0.014925373134328358,0.021739130434782608,0.021739130434782608,0.021739130434782608,0.014925373134328358,0.021739130434782608,0.014705882352941176,0.02127659574468085,0.014925373134328358,0.021739130434782608,0.021739130434782608,0.021739130434782608,0.02127659574468085,0.021739130434782608,0.021739130434782608,0.02631578947368421,0.01694915254237288,0.02631578947368421,0.02631578947368421,0.02631578947368421,0.01694915254237288,0.02631578947368421,0.016666666666666666,0.02564102564102564,0.01694915254237288,0.02631578947368421,0.02631578947368421,0.02631578947368421,0.01694915254237288,0.02631578947368421,0.02631578947368421,0.02631578947368421,0.01694915254237288,0.02631578947368421,0.016666666666666666,0.02564102564102564,0.01694915254237288,0.02631578947368421,0.02631578947368421,0.045454545454545456,0.045454545454545456,0.045454545454545456,0.045454545454545456,0.045454545454545456,0.045454545454545456,0.045454545454545456,0.045454545454545456,0.045454545454545456,0.045454545454545456,0.045454545454545456,0.041666666666666664,0.043478260869565216,0.043478260869565216,0.045454545454545456,0.045454545454545456,0.041666666666666664,0.045454545454545456,0.041666666666666664,0.043478260869565216,0.045454545454545456,0.043478260869565216,0.045454545454545456,0.045454545454545456,0.041666666666666664,0.045454545454545456,0.045454545454545456,0.045454545454545456,0.045454545454545456,0.045454545454545456,0.045454545454545456,0.045454545454545456,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,]]

out_schedule2 = [[0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.022727272727272728,0.0,0.0,0.0,0.005263157894736842,0.005405405405405406,0.005405405405405406,0.005405405405405406,0.005376344086021506,],[0.25,0.25,0.25,0.03571428571428571,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.2,0.034482758620689655,0.25,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,]]

out_tcas = [[0.0,0.0,0.014184397163120567,0.014184397163120567,0.0,0.0,0.0,0.0,],[0.0,0.0,0.3333333333333333,0.3333333333333333,0.0,0.0,0.0,0.0,]]


#define figure and figure size figsize=(width, height)
fig = plt.figure(figsize=(15, 8))
#plt.axvline(x=0.48,color='black',linestyle="--")
#define subplots 3x6
# 1        2    3 
# 4        5    6
# 7        8    9
# 10    11    12
# 13    14    15
# 16    17    18


printtokens = fig.add_subplot(3,2,1) #gas1
printtokensn1 = fig.add_subplot(3,2,1, sharex=printtokens, sharey=printtokens, frameon=False) #gas1 nomeeritud

printtokens2 = fig.add_subplot(3,2,2) #out9
printtokens2n1 = fig.add_subplot(3,2,2, sharex=printtokens2,sharey=printtokens2, frameon=False) #out9

replace = fig.add_subplot(3,2,3) #out8
replacen1 = fig.add_subplot(3,2,3, sharex=replace, sharey=replace, frameon=False) #out8

schedule = fig.add_subplot(3,2,4) #out8
schedulen1 = fig.add_subplot(3,2,4, sharex=schedule, sharey=schedule, frameon=False) #out8

schedule2 = fig.add_subplot(3,2,5) #out8
schedule2n1 = fig.add_subplot(3,2,5, sharex=schedule2, sharey=schedule2, frameon=False) #out8

tcas = fig.add_subplot(3,2,6) #out8
tcasn1 = fig.add_subplot(3,2,6, sharex=tcas, sharey=tcas, frameon=False) #out8



#plot data and normalized data 
line_1, = printtokens.plot(np.arange(len(out_printtokens[0])), out_printtokens[0],   ls=":", marker="o", mfc="None",   color="k")
line_2, = printtokensn1.plot(np.arange(len(out_printtokens[0])), out_printtokens[1], ls="--", marker="d",   color="k")


printtokens2.plot(np.arange(len(out_printtokens2[0])), out_printtokens2[0],   ls=":", marker="o", mfc="None",   color="k")
printtokens2n1.plot(np.arange(len(out_printtokens2[0])), out_printtokens2[1], ls="--", marker="d",   color="k")


replace.plot(np.arange(len(out_replace[0])), out_replace[0],   ls=":", marker="o", mfc="None",   color="k")
replacen1.plot(np.arange(len(out_replace[0])), out_replace[1], ls="--",marker="d",  color="k")



schedule.plot(np.arange(len(out_schedule[0])), out_schedule[0],   ls=":", marker="o", mfc="None",   color="k")
schedulen1.plot(np.arange(len(out_schedule[0])), out_schedule[1], ls="--",marker="d",  color="k")


schedule2.plot(np.arange(len(out_schedule2[0])), out_schedule2[0],   ls=":", marker="o", mfc="None",   color="k")
schedule2n1.plot(np.arange(len(out_schedule2[0])), out_schedule2[1], ls="--",marker="d", color="k")


tcas.plot(np.arange(len(out_tcas[0])), out_tcas[0],   ls=":", marker="o", mfc="None",   color="k")
tcasn1.plot(np.arange(len(out_tcas[0])), out_tcas[1], ls="--",marker="d",color="k")




#configure legend
fig.legend([line_1, line_2], ['weak', 'strong'],'upper left',
           ncol=2,prop={'size':10})


printtokens.yaxis.tick_left()
replace.yaxis.tick_left()
tcas.yaxis.tick_left()


#set X labels
#printtokens.set_xlabel(r"$(a)\ Result\ of\ the\ number\ of\ accurately\ identified\ MFS$")
#printtokens2.set_xlabel(r"$(f)\ The\ aggregative\ result\ for\ the\ five\ metrics$")
#replace.set_xlabel(r"$(g)\ Needed\ test\ cases$")
#schedule.set_xlabel(r"$(c)\ Result\ of\ the\ number\ of\ identified\ super-schemas\ of\ the\ MFS$")
#schedule2.set_xlabel(r"$(b)\ Result\ of\ the\ number\ of\ identified\ sub-schemas\ of\ the\ MFS$")
#tcas.set_xlabel(r"$(d)\ Result\ of\ the\ number\ of\ ignored\ MFS$")
#totinfo.set_xlabel(r"$(e)\ Result\ of\ the\ number\ of\ identified\ irrelevant\ schemas\ of\ the\ MFS$")
#grep.set_xlabel(r"$(e)\ Result\ of\ the\ number\ of\ identified\ irrelevant\ schemas\ of\ the\ MFS$")


fig.text(0.5, 0.02, 'The MFS of corresponding faulty types', ha='center')
fig.text(0.01, 0.5, 'The correlation between guaranteed code and real faulty code', va='center', rotation='vertical')

fig.text(0.25, 0.98, 'ODC class', ha='center')

fig.text(0.75, 0.98, 'Fault types', ha='center')


#set Y labels
printtokens.set_ylabel(r"$Assignment$")
printtokens2.set_ylabel(r"$Missing Code$")
replace.set_ylabel(r"$Checking$")
schedule.set_ylabel(r"$Wrong Code$")
schedule2.set_ylabel(r"$Interface$")
tcas.set_ylabel(r"$Extraneous Code$")

#adjust plot spacing
plt.subplots_adjust(left=0.07, bottom=0.08, right=0.97, top=0.96, wspace=0.20, hspace=0.25)

#finally draw the plot
plt.show()
