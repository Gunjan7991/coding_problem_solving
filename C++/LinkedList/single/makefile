CC = g++
CFLAGS = -Wall -g

linked: main.o sll.o
	$(CC) $(CFLAGS) -o linked main.o sll.o

main.o: main.cpp
	$(CC) $(CFLAGS) -c main.cpp

sll.o: sll.cpp sll.h
	$(CC) $(CFLAGS) -c sll.cpp

clean:
	$(RM) linked *.o *~
