from pprint import pprint
from config import *
import cogs.db_funcs as func

# # creating database and adding tables
# func.create_database(DB_NAME)
# func.use_database(DB_NAME)
# func.create_coop_table("1B")
# func.create_course_table("courses")

# coop_dates = {    
#     '1': ['Cycle 1 Round 1', 50, 'May 9 - 16', 'May 17 @ 9 am', 'May 24 - June 8', 'June 9 @ 2 pm', 'June 10 @ 2 pm', 'June 10 end of day'],
#     '2': ['Cycle 1 Round 2', 100, 'May 18 - 24', 'May 25 @ 9 am', 'May 24 - June 8', 'June 9 @ 2 pm', 'June 10 @ 2 pm', 'June 10 end of day'],
#     '3': ['Cycle 2 Round 1', 150, 'June 13 - 20', 'June 21 @ 9 am', 'June 27 - July 8', 'July 11 @ 2 pm', 'July 12 @ 2 pm', 'June 12 end of day'],
#     '4': ['Cycle 2 Round 2', 200, 'June 22 - 27', 'June 28 @ 9 am', 'June 27 - July 8', 'July 11 @ 2 pm', 'July 12 @ 2 pm', 'June 12 end of day'],
#     '5': ['Cycle 3 Round 1', 500, 'July 13', 'Every 2 days', 'July 19 - July 21', 'July 21 @ 8 pm', 'July 22 @ 11 am', 'July 22 end of day'],
#     '6': ['Cycle 4 Round 1', 500, 'July 13', 'Every 2 days', 'July 26 - 28', 'July 28 @ 8 pm', 'July 29 @ 11 am', 'July 29 end of day'],
#     '7': ['Cycle 5 Round 1', 500, 'July 13', 'Every 2 days', 'Aug 2 - 4', 'Aug 4 @ 8 pm', 'Aug 5 @ 11 am', 'Aug 5 end of day']
# }

# # Adds in coop dates 
# for i in coop_dates:
#     values = []
#     for j in coop_dates[i]:
#         values.append(j)
#     func.add_onto_coop_table(values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7])

# # pprint(func.get_specific_course_values('1b_coop'))

# filler_course = {
#     '1': ['Rnadom1', '2022-05-01 @ 11 pm', 1, '108'],
#     '2': ['Rnadom2', '2022-05-02 @ 11 pm', 1, '108'],
#     '3': ['Rnadom3', '2022-05-03 @ 11 pm', 1, '106'],
#     '4': ['Rnadom4', '2022-05-11 @ 11 pm', 1, '106'],
#     '5': ['Rnadom5', '2022-05-15 @ 11 pm', 1, '119'],
#     '6': ['Rnadom6', '2022-05-02 @ 11 pm', 1, '119'],
#     '7': ['Rnadom7', '2022-05-22 @ 11 pm', 1, '192'],
#     '8': ['Rnadom8', '2022-05-17 @ 11 pm', 1, '192'],
#     '9': ['Rnadom9', '2022-05-19 @ 11 pm', 1, '140'],
#     '10': ['Rnadom10', '2022-05-25 @ 11 pm', 1, '140'],
#     '11': ['Rnadom11', '2022-05-23 @ 11 pm', 1, '124'],
#     '12': ['Rnadom12', '2022-05-30 @ 11 pm', 1, '124'],
# }

# # Adds in course dates 
# for i in filler_course:
#     values = []
#     for j in filler_course[i]:
#         values.append(j)
#     func.add_onto_course_table(values[0], values[1], values[2], values[3])
        
pprint(func.get_specific_course_values('106'))