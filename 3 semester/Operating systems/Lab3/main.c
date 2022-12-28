#include <locale.h>
#include <stdio.h>
#include <windows.h>
#include <winerror.h>

int main() {
    char buffer[100] = "";
    DWORD len, actlen, dwFileSize;
    HANDLE hstdout, fhandle;
    char fname[] = "text.txt";
    BOOL rc, open;
    COORD cd_1;
    cd_1.X = 50;
    cd_1.Y = 0;
    const DWORD size = 100 + 1;
    WCHAR lpszBuffer[size];
    len = strlen(buffer);
    hstdout = GetStdHandle(STD_OUTPUT_HANDLE);
    if (hstdout == INVALID_HANDLE_VALUE)
        return 0;

    do {
        fhandle = CreateFile(fname, GENERIC_READ, 0, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
        if (fhandle == INVALID_HANDLE_VALUE) {
            setlocale(LC_ALL, "Rus");
            system("cls");
            DWORD Err = GetLastError();
            SetConsoleCursorPosition(hstdout, cd_1);
            SetConsoleTextAttribute(hstdout, FOREGROUND_INTENSITY | FOREGROUND_RED);
            FormatMessage(FORMAT_MESSAGE_FROM_SYSTEM, NULL, Err, MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT), (LPTSTR)&lpszBuffer, size, NULL);
            printf("Error code: %d\nError name: %s\n", Err, lpszBuffer);
            Sleep(2000);
            open = FALSE;
        } else {
            open = TRUE;
        }
    } while (open == FALSE);

    system("cls");
    SetConsoleCursorPosition(hstdout, cd_1);
    SetConsoleTextAttribute(hstdout, FOREGROUND_INTENSITY | FOREGROUND_BLUE);
    rc = ReadFile(fhandle, buffer + len, 80, &actlen, NULL);

    if (!rc)
        return 0;

    WriteFile(hstdout, buffer, len + actlen, &actlen, NULL);
    getchar();
    CloseHandle(fhandle);
}
