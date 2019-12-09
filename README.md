# Polling

Polling is a one of the technologies to communicate data in real-time operation. 
In the real-time communication of data, it has to be achieved sending data in the smallest delay.

## In general speaking, 
it takes a time to sensing an environment and sending the obtained data.
For example, in the case of human beging, time delay between sensing and movement
is about 0.2 second.
Shorter delay-time brings a better responce to realize the real-time movement or other reactions.

In also a robot programing and intelligence, short responce-time brings better real-time performance.
This means that a short sending time is needed to realize the real-time intelligence to move the robot.

## Polling to realize the real-time sending data
It is simple to realize the polling in sending data.
The speed of recieving data should be faster than that of sensing.
For example if it would take 0.1 sec. to sensing environment, the program is able to send data
about 10 time in a second.
This is called 10 Hz or 10 fps to send data.
In this cace, if a program recieves the data 10 time in a second, that is 10 Hz in recieving data,
every data are received in the same timing.

On the other hand, if the speed of receiving program is slower than 10 Hz, for example 5 Hz,
every data can NOT be recieved in a second.
5 data are stucked in a buffer of sending system.
And it takes double time to recieve every data.
This situation brings huge delay time in the sending data.

## Speed of recieving should be faster than that of sending data
This is a simple principle in order to realize the polling that is a real-time property.



See [Wikipedia](https://en.wikipedia.org/wiki/Polling_(computer_science)) as a reference.
