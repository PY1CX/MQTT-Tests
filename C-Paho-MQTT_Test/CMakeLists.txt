cmake_minimum_required(VERSION 2.8)

project(helloworld)

#get_filename_component(PAHO_MQTT_C_DEV_LIB_DIR ${CMAKE_CURRENT_SOURCE_DIR}/paho.mqtt.c/build/output ABSOLUTE)
#find_package (PAHO_MQTT_C_DEV_LIB)
#SET(CMAKE_SCRIPTS "${CMAKE_SOURCE_DIR}/paho.mqtt.c/cmake")
#SET(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/paho.mqtt.c/cmake/modules")


add_executable(server server_paho.c)


TARGET_LINK_LIBRARIES(server paho-mqtt3a)