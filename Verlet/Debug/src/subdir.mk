################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CPP_SRCS += \
../src/Functions.cpp \
../src/Point.cpp \
../src/Screen.cpp \
../src/Stick.cpp \
../src/Verlet.cpp 

CPP_DEPS += \
./src/Functions.d \
./src/Point.d \
./src/Screen.d \
./src/Stick.d \
./src/Verlet.d 

OBJS += \
./src/Functions.o \
./src/Point.o \
./src/Screen.o \
./src/Stick.o \
./src/Verlet.o 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.cpp src/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C++ Compiler'
	g++ -I/Library/Frameworks/Headers -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


clean: clean-src

clean-src:
	-$(RM) ./src/Functions.d ./src/Functions.o ./src/Point.d ./src/Point.o ./src/Screen.d ./src/Screen.o ./src/Stick.d ./src/Stick.o ./src/Verlet.d ./src/Verlet.o

.PHONY: clean-src

