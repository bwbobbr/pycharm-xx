time_leave = 6*60*60 + 52*60
time_gone = 8*60 + 15 +(7*60 + 12)*3 + 8*60 +15
time_home = time_leave + time_gone
time_h = time_home//(60*60)
time_min = (time_home - time_h*60*60)//60
time_s = time_home - time_h*60*60 - time_min*60
print(time_h,":",time_min,":",time_s)
