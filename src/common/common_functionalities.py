from typing import no_type_check


# rounds off the sum of all probabilities in the list to be equal to 1.0
# the input list maybe manipulated to make the sum equal to 1
# an error range of +-0.0000152587890625 in the sum has to be handled at the place of function calling.


@no_type_check
def round_off_list_to_1(input_list: 'list') -> 'manipulates the input list object itself':
    offset = 1 - sum(input_list)
    # Because of floating point precision (.59 + .33 + .08) can be equal to .99999999
    # So we correct the sum only if the absolute difference is more than a tolerance(0.0000152587890625)
    if len(input_list) != 0 and abs(offset) > 1 / 2 ** 16:
        sum_list = sum(input_list)
        # we divide each number in the list by the sum of the list, so that Prob. Distribution is approx. 1
        for i in range(len(input_list)):
            input_list[i] = round(input_list[i] / sum_list, 2)
        new_offset = 1 - sum(input_list)
        # 1 - sum(prob_list) = the difference by which the elements of the list are away from 1.0, could be +'ive /-i've
        # the difference is added/subtracted from the 1st element of the list, which is also rounded to 2 decimal points
        input_list[0] = round(input_list[0] + new_offset, 2)
    # to handle the empty list case
    if len(input_list) == 0:
        input_list.append(1)
    assert abs(1 - sum(input_list)) < 1 / 2 ** 16, "Sum of list not equal to 1.0"
