other_courses_min = 2.5
other_courses_max = 7
other_courses_avg = 4
current_course = 1.5

diff_with_min = (current_course / other_courses_min) * 100
diff_with_avg = (current_course /  other_courses_avg) * 100
diff_with_max = (current_course / other_courses_max) *100

min_result = 100 - (diff_with_min) 
avg_result = 100 - (diff_with_avg) 
max_result = 100 -(diff_with_max) 

print(f"el resultado en % con el maximo es: {round(max_result,1)}%; el promedio: {round(avg_result,1)}%; el minimo: {round(min_result,1)}%")
