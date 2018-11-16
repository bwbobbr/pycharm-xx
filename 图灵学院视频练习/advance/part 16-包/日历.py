import calendar
cal = calendar.calendar(2018)

# cal = calendar.calendar(2018,w = XX,l = XX , c = XX)
# w = 每个日期之间的间隔字符数
# l = 每周所占用的行数
# c = 每个月之间的间隔字符数
print(type(cal))
print(cal)
# isleap 判断某一年是否闰年
a = calendar.isleap(2000)
print(a)
# leapdays: 获取指定年份之间的闰年的个数
print(calendar.leapdays(2000,2018))
