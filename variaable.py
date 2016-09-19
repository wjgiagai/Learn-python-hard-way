cars = 100#车辆一共100辆
space_in_a_car = 4.0#每辆车能放下四个人
drivers = 20#司机共有20人
passengers = 90#乘客共有90人
cars_not_driven =cars - drivers#空闲车辆=车辆总数-司机人数
cars_driven = drivers#使用车辆=司机人数
carpool_capacity = cars_driven * space_in_a_car#可接送乘客人数=使用车辆×每辆车的容量
average_passengers_per_car = passengers/cars_driven每辆车的乘客数量=乘客人数/使用车辆数

print "There are",cars,"cars available."共有车辆100台
print "There are only",drivers,"drivers available."每辆车能放下4个乘客
print "There will be",cars_not_driven,"empty cars today"剩余80辆车空闲
print "We can transport",carpool_capacity,"people today"可运送人数80人
print "We have",passengers,"to carpool today"我们有90人要运送
print "We need to put about",average_passengers_per_car,"in each car"每辆车要坐4个乘客
