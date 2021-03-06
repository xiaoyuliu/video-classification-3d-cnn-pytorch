import json

trainVideos = ['APOCALYPTO_fall_floor_f_nm_np1_ba_med_5.avi', 'American_History_X_fall_floor_f_cm_np1_ba_med_3.avi',
               'American_History_X_fall_floor_f_cm_np1_le_bad_1.avi',
               'American_History_X_fall_floor_f_nm_np1_ba_bad_10.avi', 'BATMAN_BEGINS_fall_floor_f_cm_np1_ba_med_3.avi',
               'BATMAN_BEGINS_fall_floor_f_cm_np1_ba_med_5.avi', 'BATMAN_BEGINS_fall_floor_h_cm_np1_fr_bad_2.avi',
               'BIG_FISH_fall_floor_f_cm_np1_fr_med_24.avi', 'BIG_FISH_fall_floor_f_nm_np1_fr_bad_21.avi',
               'CasinoRoyale_fall_floor_f_cm_np1_fr_med_7.avi', 'Catch_Me_If_You_Can_fall_floor_f_cm_np1_fr_med_0.avi',
               'Crash_fall_floor_u_cm_np1_fr_med_1.avi', 'EVOLUTION_fall_floor_f_cm_np1_fr_med_21.avi',
               'EVOLUTION_fall_floor_f_nm_np1_ba_med_5.avi', 'Fellowship_4_fall_floor_u_cm_np1_fr_med_5.avi',
               'Fellowship_5_fall_floor_u_cm_np1_fr_med_8.avi', 'Fellowship_7_fall_floor_f_cm_np1_ba_med_2.avi',
               'Fellowship_7_fall_floor_f_cm_np1_ba_med_3.avi', 'Finding_Forrester_3_fall_floor_f_cm_np2_ri_med_1.avi',
               'HP_PRISONER_OF_AZKABAN_fall_floor_f_cm_np1_ri_med_5.avi',
               'HP_PRISONER_OF_AZKABAN_fall_floor_u_cm_np1_fr_med_14.avi',
               'KUNG_FU_HUSTLE_fall_floor_f_cm_np1_ba_bad_21.avi', 'KUNG_FU_HUSTLE_fall_floor_f_cm_np1_ba_bad_49.avi',
               'KUNG_FU_HUSTLE_fall_floor_f_cm_np1_ba_med_35.avi', 'KUNG_FU_HUSTLE_fall_floor_f_cm_np1_fr_bad_22.avi',
               'KUNG_FU_HUSTLE_fall_floor_f_cm_np1_fr_bad_47.avi', 'KUNG_FU_HUSTLE_fall_floor_f_cm_np1_fr_med_40.avi',
               'KUNG_FU_HUSTLE_fall_floor_f_cm_np1_le_med_3.avi', 'KUNG_FU_HUSTLE_fall_floor_f_cm_np1_le_med_41.avi',
               'KUNG_FU_HUSTLE_fall_floor_f_cm_np1_ri_med_19.avi', 'KUNG_FU_HUSTLE_fall_floor_f_nm_np1_ba_bad_54.avi',
               'KUNG_FU_HUSTLE_fall_floor_f_nm_np1_le_bad_0.avi', 'KUNG_FU_HUSTLE_fall_floor_f_nm_np1_le_med_13.avi',
               'KUNG_FU_HUSTLE_fall_floor_u_nm_np1_le_med_4.avi', 'MeettheFockers_fall_floor_f_nm_np1_fr_med_11.avi',
               'MeettheFockers_fall_floor_f_nm_np1_fr_med_5.avi', 'OldSchool_fall_floor_f_cm_np1_ri_med_17.avi',
               'Pirates_6_fall_floor_f_cm_np1_fr_bad_5.avi', 'Prelinger_ActYourA1949_fall_floor_f_cm_np1_ri_med_11.avi',
               'Prelinger_ActYourA1949_fall_floor_f_nm_np1_ri_med_9.avi',
               'Return_of_the_King_1_fall_floor_u_nm_np1_le_med_8.avi',
               'Return_of_the_King_8_fall_floor_f_cm_np1_ba_med_2.avi', 'RushHour2_fall_floor_f_cm_np1_fr_bad_3.avi',
               'SweeneyTodd_fall_floor_u_nm_np1_fr_bad_12.avi', 'THE_PROTECTOR_fall_floor_f_cm_np1_ba_bad_87.avi',
               'THE_PROTECTOR_fall_floor_f_cm_np1_ba_med_6.avi', 'THE_PROTECTOR_fall_floor_f_cm_np1_ba_med_85.avi',
               'THE_PROTECTOR_fall_floor_f_cm_np1_fr_bad_41.avi', 'THE_PROTECTOR_fall_floor_f_cm_np1_fr_med_33.avi',
               'THE_PROTECTOR_fall_floor_f_cm_np1_fr_med_36.avi', 'THE_PROTECTOR_fall_floor_f_cm_np1_fr_med_55.avi',
               'THE_PROTECTOR_fall_floor_f_cm_np1_fr_med_89.avi', 'THE_PROTECTOR_fall_floor_f_cm_np1_le_med_75.avi',
               'THE_PROTECTOR_fall_floor_f_cm_np1_le_med_98.avi', 'THE_PROTECTOR_fall_floor_f_cm_np1_ri_bad_73.avi',
               'THE_PROTECTOR_fall_floor_f_nm_np1_ba_bad_20.avi', 'THE_PROTECTOR_fall_floor_f_nm_np1_ba_bad_65.avi',
               'THE_PROTECTOR_fall_floor_f_nm_np1_fr_bad_100.avi', 'THE_PROTECTOR_fall_floor_f_nm_np1_fr_bad_93.avi',
               'THE_PROTECTOR_fall_floor_f_nm_np1_fr_goo_10.avi', 'THE_PROTECTOR_fall_floor_f_nm_np1_fr_med_18.avi',
               'THE_PROTECTOR_fall_floor_f_nm_np1_fr_med_61.avi', 'THE_PROTECTOR_fall_floor_f_nm_np1_fr_med_84.avi',
               'THE_PROTECTOR_fall_floor_f_nm_np1_le_bad_2.avi', 'THE_PROTECTOR_fall_floor_f_nm_np1_ri_bad_92.avi',
               'THE_PROTECTOR_fall_floor_u_cm_np1_ba_med_86.avi', 'THE_PROTECTOR_fall_floor_u_cm_np1_fr_med_56.avi',
               'TheLastManOnearth_fall_floor_f_cm_np1_fr_med_58.avi', 'The_Matrix_5_fall_floor_f_nm_np1_fr_bad_10.avi',
               'Two_Towers_3_fall_floor_u_cm_np1_fr_med_6.avi']


def run():
    with open('output.json') as json_file:
        data = json.load(json_file)

    count = 0
    for i in range(len(data)):
        if data[i]['video'] in trainVideos:
            continue
        d = data[i]['clips']
        for j in range(len(d)):
            # print(d[j]['label'])
            if d[j]['label'] in ['fall floor']:
                count += 1
                break

    print(float(count) / len(data))


if __name__ == '__main__':
    run()
