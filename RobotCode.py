# Program for Sprint Week #2, Robot Obstacle Course

# Written by: Kara Balsom, Glen May, Ian Collins, and Mark Hannem
# Date Written: April 15, 2022

# Import Time Library
import time

# Set Up marker_found and room_type:

marker_found = False
room_type = 0


# Scan for Marker Function:
def scan_for_marker():
    global marker_found

    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    marker_found = False

    while marker_found == False:
        gimbal_ctrl.yaw_ctrl(-90)
        gimbal_ctrl.yaw_ctrl(90)


# Recognize Marker 1 Function:

def vision_recognized_marker_number_one(msg):
    global marker_found
    global room_type

    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    marker_found = True
    room_type = 1
    print(room_type)


# Recognize Marker 2 Function:

def vision_recognized_marker_number_two(msg):
    global marker_found
    global room_type

    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    marker_found = True
    room_type = 2
    print(room_type)


# Recognize Marker 3 Function:

def vision_recognized_marker_number_three(msg):
    global marker_found
    global room_type

    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    marker_found = True
    room_type = 3
    print(room_type)


# Recognize Marker F Function:

def vision_recognized_marker_letter_F(msg):
    global marker_found
    vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_F)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    gun_ctrl.fire_once()
    marker_found = True
    print("F target")


# Recognize Person Function:

def vision_recognized_people(msg):
    global person_found
    vision_ctrl.disable_detection(rm_define.vision_detection_people)
    media_ctrl.play_sound(rm_define.media_sound_attacked)
    person_found = True
    print("Person Found")


# Scan for Person Function:

def scan_for_person_and_play_sound():
    global person_found
    vision_ctrl.enable_detection(rm_define.vision_detection_people)
    person_found = False
    while person_found == False:
        gimbal_ctrl.yaw_ctrl(-90)
        gimbal_ctrl.yaw_ctrl(90)
    print("Rescuing Person!")


# Scan for Fire Function:

def scan_for_fire():
    global marker_found

    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    marker_found = False

    while marker_found == False:
        gimbal_ctrl.yaw_ctrl(-90)
        gimbal_ctrl.yaw_ctrl(90)

    print("Fire Put Out!")


# Poison Room Function:

def poison_room():
    media_ctrl.play_sound(rm_define.media_sound_attacked, wait_complete_flag=True)
    gimbal_ctrl.yaw_ctrl(-90)
    gimbal_ctrl.yaw_ctrl(90)

    print("Bypassing Poison Room!")


# Return To Start of Course Function:

def return_to_start_of_course(room):
    if room == 1:
        # Set Lights to Flashing to Lead Person Back:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 250, 250, 250, rm_define.effect_flash)
        # Leave Room:
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 4.7)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        # Go Back to Start:
        print("Bring Person to Safety!")
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 2.33)
    elif room == 2:
        # Set Lights to Flashing to Lead Person Back:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 250, 250, 250, rm_define.effect_flash)
        # Leave Room:
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 3.95)
        gimbal_ctrl.recenter()
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        # Go Back to Start:
        print("Bring Person to Safety!")
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 0.43)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 45)
        gimbal_ctrl.recenter()
        print("Going to Sleep!")
        time.sleep(5)
        chassis_ctrl.move_with_distance(0, 2.4)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 45)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 2.60)
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 2.33)
    elif room == 3:
        # Set Lights to Flashing to Lead Person Back:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 250, 250, 250, rm_define.effect_flash)
        # Leave Room:
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 1.20)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 4.70)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.move_with_distance(0, 1.50)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.40)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        # Go Back to Start:
        print("Bring Person to Safety!")
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 3.9)
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 0.43)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 45)
        gimbal_ctrl.recenter()
        print("Going to Sleep!")
        time.sleep(5)
        chassis_ctrl.move_with_distance(0, 2.4)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 45)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 2.60)
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 2.33)
    else:
        # Set Lights to Flashing to Return to Start of Course:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 250, 250, 250, rm_define.effect_flash)
        # Leave Room:
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.30)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.60)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        # Go Back to Start:
        print("Going Back to Start!")
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 0.08)
        chassis_ctrl.move_with_distance(0, 3.90)
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 0.43)
        print("Going to Sleep!")
        time.sleep(5)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 45)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.4)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 45)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 2.60)
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 2.33)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        gimbal_ctrl.recenter()
        led_ctrl.turn_off(rm_define.armor_all)


# Move Back to Position from Start Function:

def move_to_room_from_start(room):
    if room == 1:
        print("Going to Sleep!")
        time.sleep(5)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        gimbal_ctrl.recenter()
        # Turn Off Lights:
        led_ctrl.turn_off(rm_define.armor_all)
        # Go Back to Position:
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 2.33)
    elif room == 2:
        print("Going to Sleep!")
        time.sleep(5)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        gimbal_ctrl.recenter()
        # Turn Off Lights:
        led_ctrl.turn_off(rm_define.armor_all)
        # Go Back to Position:
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 2.33)
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 2.60)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 45)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.40)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 45)
        gimbal_ctrl.recenter()
        print("Going to Sleep!")
        time.sleep(5)
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 0.43)
    elif room == 3:
        print("Going to Sleep!")
        time.sleep(5)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        gimbal_ctrl.recenter()
        # Turn Off Lights:
        led_ctrl.turn_off(rm_define.armor_all)
        # Go Back to Position:
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 2.33)
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 2.60)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 45)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.40)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 45)
        gimbal_ctrl.recenter()
        print("Going to Sleep!")
        time.sleep(5)
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 0.43)
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 3.9)


# Start Main Program:

def start():
    # Set Up Room Counter:
    roomcounter = 0

    # Robot Settings:
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    chassis_ctrl.set_trans_speed(0.75)
    chassis_ctrl.set_rotate_speed(30)
    gimbal_ctrl.set_rotate_speed(30)

    # Move from starting point to Room #1 (733 cm):
    chassis_ctrl.move_with_distance(0, 5.0)
    chassis_ctrl.move_with_distance(0, 2.33)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()

    # Scan Room #1 Marker:
    scan_for_marker()
    roomcounter += 1

    # Determine Action Depending on Room Type:
    if (room_type == 1):
        print("This Room is on Fire")
        chassis_ctrl.move_with_distance(0, 4.7)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        # Scan for Fire
        scan_for_fire()
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 4.7)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    elif (room_type == 2):
        print("This Room is Poison!")
        poison_room()
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
    elif (room_type == 3):
        print("Looking for a Person!")
        chassis_ctrl.move_with_distance(0, 4.7)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        # Scan for Person
        scan_for_person_and_play_sound()
        return_to_start_of_course(roomcounter)
        move_to_room_from_start(roomcounter)

    # Move to Turning Point
    chassis_ctrl.move_with_distance(0, 5.0)
    chassis_ctrl.move_with_distance(0, 2.60)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 45)
    gimbal_ctrl.recenter()

    # Move to Reset Point
    chassis_ctrl.move_with_distance(0, 2.40)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 45)
    gimbal_ctrl.recenter()
    print("Going to Sleep!")
    time.sleep(5)

    # Move to Room #2
    chassis_ctrl.move_with_distance(0, 5.0)
    chassis_ctrl.move_with_distance(0, 0.43)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()

    # Scan Room #2 Marker:
    scan_for_marker()
    roomcounter += 1

    # Determine Action Depending on Room Type:
    if (room_type == 1):
        print("This Room is on Fire!")
        chassis_ctrl.move_with_distance(0, 3.95)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 5.0)
        # Scan for Fire
        scan_for_fire()
        time.sleep(5)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 3.95)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
    elif (room_type == 2):
        print("This Room is Poison!")
        poison_room()
        # Turn and Continue on with Course
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
    elif (room_type == 3):
        print("Looking for a Person!")
        chassis_ctrl.move_with_distance(0, 3.95)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        chassis_ctrl.move_with_distance(0, 5.0)
        # Scan for Person
        scan_for_person_and_play_sound()
        return_to_start_of_course(roomcounter)
        move_to_room_from_start(roomcounter)

    # Move to Room # 3
    chassis_ctrl.move_with_distance(0, 5.0)
    chassis_ctrl.move_with_distance(0, 3.90)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()
    # Scan Room #3 Marker:
    scan_for_marker()
    roomcounter += 1

    # Determine Action Depending on Room Type:
    if (room_type == 1):
        print("This Room is on Fire!")
        chassis_ctrl.move_with_distance(0, 2.40)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 1.50)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 4.70)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 1.20)
        # Scan for Fire
        scan_for_fire()
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 1.20)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 4.70)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 1.50)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.40)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
    elif (room_type == 2):
        print("This Room is Poison!")
        poison_room()
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
    elif (room_type == 3):
        print("Looking For a Person!")
        chassis_ctrl.move_with_distance(0, 2.40)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 1.50)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 4.70)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 1.20)
        # Scan for Person
        scan_for_person_and_play_sound()
        return_to_start_of_course(roomcounter)
        move_to_room_from_start(roomcounter)

    # Move to Room # 4
    chassis_ctrl.move_with_distance(0, 5.0)
    chassis_ctrl.move_with_distance(0, 5.0)
    chassis_ctrl.move_with_distance(0, 0.08)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()

    # Scan Room #4 Marker:
    scan_for_marker()
    roomcounter += 1

    # Determine Action Depending on Room Type:
    if (room_type == 1):
        print("This Room is on Fire!")
        chassis_ctrl.move_with_distance(0, 2.60)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.30)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        scan_for_fire()
        print("Returning to Start of Course!")
        return_to_start_of_course(roomcounter)
    elif (room_type == 2):
        print("This Room is Poison!")
        poison_room()
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        return_to_start_of_course(roomcounter)
    elif (room_type == 3):
        print("Looking For a Person!")
        chassis_ctrl.move_with_distance(0, 2.60)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.30)
        scan_for_person_and_play_sound()
        return_to_start_of_course(roomcounter)
        move_to_room_from_start(roomcounter)

# End of Program