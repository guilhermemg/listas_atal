project(lista2)

add_executable(lista2 CD.cpp)

install(TARGETS lista2 RUNTIME DESTINATION bin)

#set_source_files_properties( CD.out PROPERTIES GENERATED true)
#add_custom_command ( OUTPUT CD.out
    #COMMAND lista2 < CD.in 
    #WORKING_DIRECTORY ${CMAKE_SOURCE_DIR} )
#add_executable ( lista2 CD.out )