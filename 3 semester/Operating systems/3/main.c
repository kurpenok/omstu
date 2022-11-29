#include <conio.h>
#include <stdio.h>
#include <strsafe.h>
#include <tchar.h>
#include <windows.h>

#define BUFFERSIZE 255 

int main(int argc, TCHAR *argv[]) {
	HANDLE file;
	Sleep(2000);
	
    char buffer[BUFFERSIZE];

	DWORD bytesWasRead = 0;
	HANDLE hStdOut = GetStdHandle(STD_OUTPUT_HANDLE);
	SetConsoleTextAttribute(hStdOut, FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_INTENSITY);
	
    printf("[+] Start:\n");
	do {
		file = CreateFile("file",                // name of the write
		                   GENERIC_READ,          // open for writing
		                   0,                      // do not share
		                   NULL,                   // default security
		                   OPEN_ALWAYS,             // create new file only
		                   FILE_ATTRIBUTE_NORMAL,  // normal file
		                   NULL); 

		if (file == INVALID_HANDLE_VALUE && GetLastError() == ERROR_SHARING_VIOLATION) {
			SetConsoleTextAttribute(hStdOut, FOREGROUND_RED);
			printf("file error sharing violation \n");
		}
		Sleep(1000);
	} while (file == INVALID_HANDLE_VALUE);

	SetConsoleTextAttribute(hStdOut, FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_INTENSITY);
	
    printf("[+] I begin reading:\n");

	BOOL flag = ReadFile(file, buffer, BUFFERSIZE, &bytesWasRead, NULL);
	
    if (flag == FALSE) {
		printf("[-] Can`t read %d\n", file);
		printf("[-] Error is %d\n", GetLastError());
		CloseHandle(file);
		getch();
		return 1;
	}
	
    Sleep(10000);
	
    printf("[+] Finished read: %s\n", buffer);
	
    CloseHandle(file);
	
    getch();
	
    return 0;
}
