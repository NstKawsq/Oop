import cont


temp = cont.Cont()
flag = temp.input()
temp.multi()
if flag[1] == 0:
    temp.out()
    temp.mark_count()
    temp.sort()
    temp.out()
    temp.filtered_output_by_quotation()
    temp.filtered_output_by_aforizm()
    temp.clear()
    temp.out()
